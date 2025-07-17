from weasyprint import HTML


def create_pdf_from_blocks(blocks: list, output_path: str, styled: bool = True) -> None:
    html_content = "<html><body>"

    for block in blocks:
        html_content += "<p>"
        for span in block["content"]:
            t = span["text"]
            if styled:
                if span.get("highlight"):
                    t = f"<mark>{t}</mark>"
                if span.get("underline"):
                    t = f"<u>{t}</u>"
                if span.get("strike"):
                    t = f"<s>{t}</s>"
            html_content += f"{t} "
        html_content += "</p>"
    html_content += "</body></html>"

    HTML(string=html_content).write_pdf(output_path)
