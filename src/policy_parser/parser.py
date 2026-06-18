import fitz
import os


# Get current file directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build absolute path to PDF
PDF_PATH = os.path.abspath(
    os.path.join(
        BASE_DIR,
        "..",
        "..",
        "compliance_policy",
        "Compliance_Policy_Manual.pdf"
    )
)


def extract_text(pdf_path):
    text = ""

    pdf = fitz.open(pdf_path)

    for page in pdf:
        text += page.get_text()

    pdf.close()

    return text


if __name__ == "__main__":

    print("=" * 50)
    print("CHECKING PDF PATH")
    print("=" * 50)

    print(PDF_PATH)
    print()

    print("FILE EXISTS:", os.path.exists(PDF_PATH))
    print()

    if not os.path.exists(PDF_PATH):
        print("ERROR: PDF NOT FOUND")
        exit()

    text = extract_text(PDF_PATH)

    print("=" * 50)
    print("PDF LOADED SUCCESSFULLY")
    print("=" * 50)

    print(text[:3000])