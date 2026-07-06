#!/usr/bin/env python3
"""Wrapper for markitdown that configures LLM-powered features via a local vLLM endpoint."""

import argparse
import os
import sys

try:
    from markitdown import MarkItDown
    from openai import OpenAI
except ImportError:
    print("Error: markitdown and openai packages are required.", file=sys.stderr)
    print("Install with: uv tool install markitdown openai", file=sys.stderr)
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Convert files to Markdown with LLM-powered image descriptions.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
EXAMPLES:
  %(prog)s document.pdf
  %(prog)s document.pdf -o output.md
  cat image.jpg | %(prog)s -x .jpg
  %(prog)s presentation.pptx --keep-data-uris

ENVIRONMENT:
  MARKITDOWN_LLM_BASE_URL  Override the vLLM endpoint (default: https://vllm.brain.tdvm.net/v1)
  MARKITDOWN_LLM_MODEL     Override the model name (default: qwen3.6-27b)
  MARKITDOWN_LLM_KEY       API key for the LLM endpoint (optional)
""",
    )

    parser.add_argument(
        "filename", nargs="?", default=None, help="Input file (reads stdin if omitted)"
    )
    parser.add_argument(
        "-o", "--output", help="Output file (writes to stdout if omitted)"
    )
    parser.add_argument("-x", "--extension", help="File extension hint for stdin")
    parser.add_argument("-m", "--mime-type", help="MIME type hint")
    parser.add_argument("-c", "--charset", default="UTF-8", help="Charset hint")
    parser.add_argument(
        "--keep-data-uris", action="store_true", help="Keep base64-encoded images"
    )
    parser.add_argument(
        "-p", "--use-plugins", action="store_true", help="Enable 3rd-party plugins"
    )

    args = parser.parse_args()

    # LLM configuration — defaults to local vLLM endpoint
    base_url = "https://vllm.brain.tdvm.net/v1"
    model = "qwen3.6-27b"
    api_key = None

    # Environment overrides
    if os.environ.get("MARKITDOWN_LLM_BASE_URL"):
        base_url = os.environ["MARKITDOWN_LLM_BASE_URL"]
    if os.environ.get("MARKITDOWN_LLM_MODEL"):
        model = os.environ["MARKITDOWN_LLM_MODEL"]
    if os.environ.get("MARKITDOWN_LLM_KEY"):
        api_key = os.environ["MARKITDOWN_LLM_KEY"]

    # Create LLM client
    llm_client = OpenAI(base_url=base_url, api_key=api_key or "not-needed")

    # Create MarkItDown instance with LLM support
    md = MarkItDown(
        llm_client=llm_client,
        llm_model=model,
        enable_plugins=args.use_plugins,
    )

    # Determine input source
    if args.filename:
        result = md.convert_local(args.filename)
    else:
        # Read from stdin
        import io

        stdin_data = sys.stdin.buffer.read()
        stream_type = args.extension.lstrip(".") if args.extension else None
        if args.mime_type:
            result = md.convert_stream(
                io.BytesIO(stdin_data), stream_type=None, mime_type=args.mime_type
            )
        elif stream_type:
            result = md.convert_stream(io.BytesIO(stdin_data), stream_type=stream_type)
        else:
            result = md.convert_stream(io.BytesIO(stdin_data))

    # Output results
    output_text = result.text_content if result else ""

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(output_text)
    else:
        sys.stdout.write(output_text)


if __name__ == "__main__":
    main()
