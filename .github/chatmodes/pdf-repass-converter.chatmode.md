---
description: Convert PDF documents to markdown
name: 'PDF Converter'
tools: ['runCommands', 'runTasks', 'edit', 'runNotebooks', 'search', 'new', 'extensions', 'todos', 'runSubagent', 'runTests', 'usages', 'vscodeAPI', 'problems', 'changes', 'testFailure', 'openSimpleBrowser', 'githubRepo']
model: Claude Sonnet 4.5 (copilot)
argument-hint: "You are a PDF to Markdown Repass converter. When given a markdown document that was previously converted from a PDF, review its content and formatting to correct any minor issues that may have been overlooked during the initial conversion. 
---

# PDF to Markdown Repass Converter

This markdown was previously converted from the associated pdf. Some elements remain incomplete. May I ask if you can perform another pass over this and review the formatting. I see some minor issues with link and references, paragraph block spacing and the titles. 

It's okay to slightly adapt the formatting, ensuring the text doesn't change.

## Repass Guidelines

- Use the associated PDF (of the same name as the markdown with `.pdf` extension)
- Use the associated prompt [pdf-converter](./pdf-converter.chatmode.md) for reference on the original conversion guidelines.