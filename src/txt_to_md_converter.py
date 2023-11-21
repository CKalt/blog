
def txt_to_md(txt_filename, output_filename):
    with open(txt_filename, "r") as f:
        txt_content = f.read()

    # Splitting the content by double line breaks
    sections = txt_content.split("\n\n")

    md_content = []

    i = 0
    while i < len(sections):
        section = sections[i]
        if section.startswith(("ME:", "CLAUDE:")):
            speaker = section.strip()
            i += 1
            message = sections[i] if i < len(sections) else ""
            md_section = f"> **{speaker}**\n>\n> {message}"
            md_content.append(md_section)
        elif section.startswith("    "):  # Detect indented sections
            indented_section = section.replace("    ", "")
            md_section = f">\n> - {indented_section}"
            md_content.append(md_section)
        else:
            # If the section doesn't match the above patterns, it's added as-is
            md_content.append(section)
        i += 1

    # Joining sections with the '---' separator, ensuring there's a newline before and after each separator
    md_transformed = "\n\n---\n\n".join(md_content)

    # Save to output file
    with open(output_filename, "w") as f:
        f.write(md_transformed)


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python script_name.py input_filename.txt")
        sys.exit(1)
    
    txt_filename = sys.argv[1]
    output_filename = txt_filename.replace(".txt", ".md")
    
    txt_to_md(txt_filename, output_filename)
    print(f"Converted file saved as: {output_filename}")

