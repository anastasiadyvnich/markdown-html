import re
import sys

def md_to_html(md_text):
    html = md_text

    html = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', html)
    html = re.sub(r'_(.*?)_', r'<i>\1</i>', html)
    html = re.sub(r'```\n(.*?)\n```', r'<pre>\1</pre>', html, flags=re.DOTALL)
    html = re.sub(r'`(.*?)`', r'<tt>\1</tt>', html)

    paragraphs = re.split(r'\n\s*\n', html)
    paragraphs = ['<p>{}</p>'.format(p.replace("\n", " ")) for p in paragraphs]
    html = "\n".join(paragraphs)

    return html

def main(input_file, output_file=None):
    with open(input_file, 'r', encoding='utf-8') as f:
        md_text = f.read()

    html = md_to_html(md_text)

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