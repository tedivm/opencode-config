---
name: converting-to-markdown
description: Use when converting files to Markdown format for LLM consumption, document analysis, or text extraction. Supports PDF, Office documents, images, audio, HTML, and more via Microsoft's markitdown. Don't use for simple text file reads, existing Markdown files, or when the file is in a usable format.
license: MIT
compatibility: Requires uv installed
metadata:
  source: https://github.com/microsoft/markitdown
  author: Robert Hafner
---

## Quick start

Use the bundled wrapper script — it configures LLM-powered image descriptions automatically:

```bash
SCRIPT_PATH="<skill_path>/scripts/markitdown-llm.py"
uv tool run --with markitdown --with openai python "$SCRIPT_PATH" document.pdf > output.md
```

For basic conversions without LLM features, use markitdown directly:

```bash
uv tool run markitdown document.pdf > output.md
```

## Setup

Install the dependencies once for faster subsequent runs:

```bash
uv tool install markitdown openai
```

After installation, invoke without `--with`:

```bash
SCRIPT_PATH="<skill_path>/scripts/markitdown-llm.py"
uv tool run python "$SCRIPT_PATH" document.pdf -o output.md
```

## Supported formats

- **Documents**: PDF, Word (.docx), PowerPoint (.pptx), Excel (.xlsx, .xls)
- **Images**: JPEG, PNG, GIF, BMP, TIFF (EXIF metadata, LLM-powered descriptions)
- **Audio**: WAV, MP3 (metadata and speech transcription)
- **Web**: HTML, YouTube URLs
- **Archives**: ZIP (iterates over contents)
- **Other**: EPUB, CSV, JSON, XML, Outlook messages

## Workflow

1. **Convert a single file** — Run the wrapper script and capture stdout, or use `-o <output.md>`.
2. **Pipe content** — For stdin input, use `cat file | uv tool run --with markitdown --with openai python <script>` or pipe to the script.
3. **Provide file hints** — When reading from stdin or dealing with extensionless files, add `-x .pdf` to help markitdown choose the right converter.
4. **Verify output** — Check the resulting Markdown for completeness, especially tables and complex layouts.

## CLI reference

| Flag                | Purpose                                         |
| ------------------- | ----------------------------------------------- |
| `-o, --output`      | Write to file instead of stdout                 |
| `-x, --extension`   | File extension hint (stdin/extensionless files) |
| `-m, --mime-type`   | MIME type hint                                  |
| `-c, --charset`     | Charset hint (e.g., UTF-8)                      |
| `--keep-data-uris`  | Preserve base64-encoded images in output        |
| `-p, --use-plugins` | Enable 3rd-party plugins                        |

## LLM configuration

The wrapper uses your local vLLM endpoint for image descriptions and OCR. Override with environment variables:

| Variable                  | Default                          | Purpose            |
| ------------------------- | -------------------------------- | ------------------ |
| `MARKITDOWN_LLM_BASE_URL` | `https://vllm.brain.tdvm.net/v1` | vLLM endpoint      |
| `MARKITDOWN_LLM_MODEL`    | `qwen3.6-27b`                    | Model name         |
| `MARKITDOWN_LLM_KEY`      | _(none)_                         | API key (optional) |

```bash
MARKITDOWN_LLM_BASE_URL=http://localhost:8000/v1 \
  uv tool run --with markitdown --with openai python <script> document.pdf -o output.md
```

## OCR plugin

For enhanced image text extraction in documents:

```bash
uv tool install markitdown-ocr
uv tool run --with markitdown --with openai --with markitdown-ocr python <script> document.pdf -p -o output.md
```

The `-p` flag enables plugins, and the LLM client is automatically configured.

## Python API

For programmatic use without the wrapper:

```python
from markitdown import MarkItDown
from openai import OpenAI

client = OpenAI(base_url="https://vllm.brain.tdvm.net/v1")
md = MarkItDown(
    llm_client=client,
    llm_model="qwen3.6-27b",
    enable_plugins=True,
)
result = md.convert("file.pdf")
print(result.text_content)
```

For local files only (safer — no URL fetching):

```python
result = md.convert_local("file.pdf")
```

For streams:

```python
with open("file.pdf", "rb") as f:
    result = md.convert_stream(f, stream_type="pdf")
```

## Security note

MarkItDown performs I/O with the current process's privileges. Sanitize inputs in untrusted environments. Prefer `convert_local()` or `convert_stream()` over `convert()` when path control is needed.
