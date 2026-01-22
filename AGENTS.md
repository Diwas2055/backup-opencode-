# OpenCode Global Rules

This file contains custom instructions for OpenCode that apply globally across all projects.

## Core Principles

- **Concise Communication**: Be direct and to the point. Use minimal text (1-3 sentences).
- **Code Quality**: Write production-ready code with error handling, logging, and tests.
- **Security First**: Never write malicious code. Use environment variables for secrets.
- **No Hallucination**: Never guess - use tools (Grep, Read, WebFetch) to verify information.

## Code Standards

- Follow existing code conventions and patterns in the codebase
- Use the right tool for the job (don't use Bash for file operations)
- Run lint/typecheck when making significant code changes
- Explain non-trivial bash commands before running them

## Project Analysis

When analyzing a project:

1. Use Glob/Read tools to understand structure
2. Use Grep to find specific patterns
3. Check requirements.txt, package.json, or similar for dependencies
4. Look at existing code patterns before making changes

## Task Execution

- Do what's asked without being overly proactive
- Verify solutions with tests when possible
- Ask for clarification when instructions are ambiguous
- Never commit unless explicitly asked

## Memory Management

- Use memory blocks for persistent project information
- Update memory when significant changes occur
- Respect memory scopes (global vs project)

## Prohibited Practices

- No malicious code (even for "educational purposes")
- No hardcoded secrets or credentials
- No debug artifacts (print statements, commented code)
- No mutable default arguments

## OpenCode-Specific

- Use bullet points and structured reports for complex information
- Batch tool calls for efficiency
- Explain bash commands before execution
- Run linting/testing proactively for significant changes
