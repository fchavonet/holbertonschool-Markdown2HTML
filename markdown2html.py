#!/usr/bin/python3

"""
Markdown to HTML converter.
"""

import hashlib
import os
import sys


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

    # Parse bold and emphasis text within the the heading text.
    heading_text = parse_bold_and_emphasis(heading_text)
    # Parse custom syntax within the the heading text.
    heading_text = parse_custom_syntax(heading_text)

    return f"<h{heading_level}>{heading_text}</h{heading_level}>"


def parse_unordered_list(lines, index):
    """
    Parse a Markdown unordered list and return the corresponding HTML.
    """
    html_lines = ["<ul>"]

    # Process unordered list items until a non-list item is encountered.
    while index < len(lines) and lines[index].startswith("- "):
        # Parse bold and emphasis text within the unordered list item.
        item_text = parse_bold_and_emphasis(lines[index][2:].strip())
        # Parse custom syntax within the unordered list item.
        item_text = parse_custom_syntax(item_text)

        html_lines.append(f"<li>{item_text}</li>")
        index += 1

    html_lines.append("</ul>")

    return html_lines, index


def parse_ordered_list(lines, index):
    """
    Parse a Markdown ordered list and return the corresponding HTML.
    """
    html_lines = ["<ol>"]

    # Process ordered list items until a non-list item is encountered.
    while index < len(lines) and lines[index].startswith("* "):
        # Parse bold and emphasis text within the ordered list item.
        item_text = parse_bold_and_emphasis(lines[index][2:].strip())
        # Parse custom syntax within the ordered list item.
        item_text = parse_custom_syntax(item_text)

        html_lines.append(f"<li>{item_text}</li>")
        index += 1

    html_lines.append("</ol>")

    return html_lines, index


def parse_paragraph(lines, index):
    """
    Parse Markdown paragraphs and return the corresponding HTML.
    """
    paragraph_text = []

    # Process paragraph lines until an empty line is encountered.
    while index < len(lines) \
            and lines[index].strip() != "" \
            and not lines[index].startswith("#")\
            and not lines[index].startswith("- ")\
            and not lines[index].startswith("* "):
        # Parse bold and emphasis text within the paragraph.
        line = parse_bold_and_emphasis(lines[index].strip())
        # Parse custom syntax within the paragraph.
        line = parse_custom_syntax(line)

        paragraph_text.append(line)
        index += 1

    paragraph_html = "<p>\n" + "\n<br/>\n".join(paragraph_text) + "\n</p>"

    return [paragraph_html], index


def parse_bold_and_emphasis(line):
    """
    Parse bold and emphasis text and return the corresponding HTML.
    """
    # Replace bold text with <b> tags.
    while "**" in line:
        line = line.replace("**", "<b>", 1).replace("**", "</b>", 1)

    # Replace emphasis text with <em> tags.
    while "__" in line:
        line = line.replace("__", "<em>", 1).replace("__", "</em>", 1)

    return line


def parse_custom_syntax(line):
    """
    Parse custom syntax for MD5 and removing "c" characters.
    (Disclaimer: made with ChetGPT)
    """
    # Replace content in [[ ]] with its MD5 hash.
    while "[[" in line and "]]" in line:
        start_index = line.index("[[")
        end_index = line.index("]]", start_index)
        content = line[start_index + 2:end_index]
        md5_hash = hashlib.md5(content.encode()).hexdigest()
        line = line[:start_index] + md5_hash + line[end_index + 2:]

    # Remove "c" and "C" characters from content in (( )).
    while "((" in line and "))" in line:
        start_index = line.index("((")
        end_index = line.index("))", start_index)
        content = line[start_index + 2:end_index]
        content_no_c = content.replace("c", "").replace("C", "")
        line = line[:start_index] + content_no_c + line[end_index + 2:]

    return line


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

        # Skip empty lines.
        elif line == "":
            index += 1

        # Treat the line as a paragraph.
        else:
            parsed_lines, index = parse_paragraph(lines, index)
            html_lines.extend(parsed_lines)

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

        # Convert the Markdown file to HTML and save the result to the output. 
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
