.PHONY: install format format-check validate

install:
	brew install edouard-claude/tap/snip

format:
	npx prettier --write "**/*.md" "**/*.json" "**/*.jsonc"

format-check:
	npx prettier --check "**/*.md" "**/*.json" "**/*.jsonc"

validate:
	node scripts/validate.js
