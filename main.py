import sys

def main(input_file, output_file=None):
    with open(input_file, 'r', encoding='utf-8') as f:
        md_text = f.read()

    html = md_text

    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html)
    else:
        print(html)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python md_to_html.py <input_file.md> [--out <output_file.html>]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = None

    if len(sys.argv) == 4 and sys.argv[2] == '--out':
        output_file = sys.argv[3]

    main(input_file, output_file)