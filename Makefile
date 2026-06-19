.PHONY: install format format-check validate

install:
	brew install edouard-claude/tap/snip

format:
	npx prettier --write "**/*.md" "**/*.jsonc"

format-check:
	npx prettier --check "**/*.md" "**/*.jsonc"

validate:
	node scripts/validate.js
