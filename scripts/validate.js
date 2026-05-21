#!/usr/bin/env node
const fs = require('fs');
const path = require('path');

function stripComments(text) {
  let result = '';
  let i = 0;
  while (i < text.length) {
    if (text[i] === '"') {
      result += text[i++];
      while (i < text.length && text[i] !== '"') {
        if (text[i] === '\\') {
          result += text[i++] + (i < text.length ? text[i++] : '');
        } else {
          result += text[i++];
        }
      }
      if (i < text.length) result += text[i++];
    } else if (text[i] === '/' && text[i + 1] === '/') {
      while (i < text.length && text[i] !== '\n') i++;
    } else if (text[i] === '/' && text[i + 1] === '*') {
      i += 2;
      while (i < text.length && !(text[i] === '*' && text[i + 1] === '/')) i++;
      if (i < text.length) i += 2;
    } else {
      result += text[i++];
    }
  }
  return result;
}

const files = ['opencode.json', 'dcp.jsonc'];

for (const file of files) {
  const filePath = path.resolve(file);
  if (!fs.existsSync(filePath)) {
    console.log(`Skipping ${file} (not found)`);
    continue;
  }

  console.log(`Validating ${file}...`);
  let content = fs.readFileSync(filePath, 'utf8');

  if (file.endsWith('.jsonc')) {
    content = stripComments(content);
    content = content.replace(/,(\s*[}\]])/g, '$1');
  }

  try {
    JSON.parse(content);
    console.log('  OK');
  } catch (e) {
    console.error(`  FAIL: ${e.message}`);
    process.exitCode = 1;
  }
}
