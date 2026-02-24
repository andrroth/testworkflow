#!/usr/bin/env python3
"""
AI Code Reviewer - Uses Claude to analyze code changes and provide feedback.
"""

import os
import anthropic


def read_diff():
    """Read the git diff from file."""
    try:
        with open("diff.txt", "r") as f:
            return f.read()
    except FileNotFoundError:
        return "No diff available"


def analyze_code_with_claude(diff: str) -> str:
    """Send the diff to Claude for analysis."""
    client = anthropic.Anthropic()

    prompt = f"""You are an expert code reviewer. Analyze the following git diff and provide a helpful code review.

Focus on:
1. **Code Quality**: Are there any bugs, logic errors, or potential issues?
2. **Best Practices**: Does the code follow best practices for the language/framework?
3. **Security**: Are there any security concerns?
4. **Performance**: Any performance implications?
5. **Suggestions**: What improvements would you recommend?

Be constructive and specific. If the code looks good, say so!

## Git Diff:
```diff
{diff}
```

Provide your review in markdown format with clear sections."""

    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=2048,
        messages=[{"role": "user", "content": prompt}],
    )

    return message.content[0].text


def main():
    diff = read_diff()

    if not diff.strip() or diff == "Initial commit":
        review = "## AI Code Review\n\n✅ Initial commit or no changes to review."
    else:
        print("🤖 Analyzing code changes with Claude...")
        review = f"## 🤖 AI Code Review\n\n{analyze_code_with_claude(diff)}"

    with open("review_output.md", "w") as f:
        f.write(review)

    print("Review complete! Output written to review_output.md")
    print("\n" + "=" * 50)
    print(review)


if __name__ == "__main__":
    main()
