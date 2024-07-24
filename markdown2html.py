#!/usr/bin/python3

"""
Markdown to HTML converter.
"""

import sys
import os


def parse_heading(line):
    """
    Parse Markdown headings and return the corresponding HTML.
    """
    heading_level = 0

    # Count the number of "#" characters to determine the heading level.
    while heading_level < len(line) and line[heading_level] == "#":
        heading_level += 1

    # Extract the heading text after the "#" characters.
    heading_text = line[heading_level:].strip()

    return f"<h{heading_level}>{heading_text}</h{heading_level}>"


def convert_markdown_to_html(markdown_file, html_file):
    """
    Convert a Markdown file to HTML and save it to the output file.
    """
    # Open the Markdown file for reading.
    with open(markdown_file, "r") as open_markdown_file:
        lines = open_markdown_file.readlines()

    html_lines = []

    for line in lines:
        line = line.strip()
        if line.startswith("#"):
            html_lines.append(parse_heading(line))
        else:
            html_lines.append(line)

    # Open the HTML file and write each line to it.
    with open(html_file, "w") as open_html_file:
        for html_line in html_lines:
            open_html_file.write(html_line + "\n")


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

        convert_markdown_to_html(markdown_file, html_file)

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
