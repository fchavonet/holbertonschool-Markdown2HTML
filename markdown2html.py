#!/usr/bin/python3

"""
Markdown to HTML converter.
"""

import sys
import os


def main():
    """
    Handle command-line arguments and check the existence of the Markdown file.
    """
    try:
        # Check if the correct number of arguments is provided.
        if len(sys.argv) != 3:
            raise ValueError("Usage: ./markdown2html.py README.md README.html")

        markdown_file = sys.argv[1]
        html_file = sys.argv[2]

        # Check if the Markdown file exists.
        if not os.path.isfile(markdown_file):
            raise FileNotFoundError(f"Missing {markdown_file}")

        # If no errors, exit with status 0 (success).
        sys.exit(0)

    except ValueError as ve:
        print(ve, file=sys.stderr)
        sys.exit(1)

    except FileNotFoundError as fnfe:
        print(fnfe, file=sys.stderr)
        sys.exit(1)

    # Handle any unexpected exceptions.
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
