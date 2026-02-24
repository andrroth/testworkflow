# AI Code Review Demo

A sample project demonstrating an agentic GitHub Actions workflow that uses Claude to automatically review code changes.

## How It Works

1. **On every push to `main`** or **pull request**, the workflow triggers
2. The workflow extracts the git diff of changed files
3. Claude analyzes the changes and provides feedback on:
   - Code quality and potential bugs
   - Best practices
   - Security concerns
   - Performance implications
   - Improvement suggestions
4. The review is posted as:
   - A **PR comment** (for pull requests)
   - A new **GitHub Issue** (for direct pushes)

## Project Structure

```
.
├── .github/workflows/
│   └── ai-code-reviewer.yml    # The agentic workflow
├── scripts/
│   └── ai_reviewer.py          # Claude integration script
├── src/
│   └── calculator.py           # Sample module
├── tests/
│   └── test_calculator.py      # Sample tests
└── requirements.txt
```

## Try It Out

1. Make changes to `src/calculator.py`
2. Commit and push
3. Check the Actions tab and Issues for the AI review!
