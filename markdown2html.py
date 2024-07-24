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


def parse_unordered_list(lines, index):
    """
    Parse a Markdown unordered list and return the corresponding HTML.
    """
    html_lines = ["<ul>"]

    # Process list items until a non-list item is encountered.
    while index < len(lines) and lines[index].startswith("- "):
        item_text = lines[index][2:].strip()
        html_lines.append(f"<li>{item_text}</li>")
        index += 1

    html_lines.append("</ul>")

    return html_lines, index


def parse_ordered_list(lines, index):
    """
    Parse a Markdown ordered list and return the corresponding HTML.
    """
    html_lines = ["<ol>"]

    #
    while index < len(lines) and lines[index].startswith("* "):
        item_text = lines[index][2:].strip()
        html_lines.append(f"<li>{item_text}</li>")
        index += 1

    html_lines.append("</ol>")

    return html_lines, index


def convert_markdown_to_html(markdown_file, html_file):
    """
    Convert a Markdown file to HTML and save it to the output file.
    """
    # Open the Markdown file for reading.
    with open(markdown_file, "r") as open_markdown_file:
        lines = open_markdown_file.readlines()

    html_lines = []
    index = 0

    while index < len(lines):
        line = lines[index].strip()
        # Check if the line is a heading.
        if line.startswith("#"):
            html_lines.append(parse_heading(line))
            index += 1
        # Check if the line is an unordered list item.
        elif line.startswith("- "):
            parsed_lines, index = parse_unordered_list(lines, index)
            html_lines.extend(parsed_lines)
        # Check if the line is an ordered list item.
        elif line.startswith("* "):
            parsed_lines, index = parse_ordered_list(lines, index)
            html_lines.extend(parsed_lines)
        # Treat the line as a normal text line.
        else:
            html_lines.append(line)
            index += 1

    # Open the HTML file and write each line to it.
    with open(html_file, "w") as open_html_file:
        for html_line in html_lines:
            open_html_file.write(html_line + "\n")


def main():
    """
    Handle `args`, check file existence and convert Markdown to HTML.
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
