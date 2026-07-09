import pdfplumber


def extract_text(pdf_file):
    """
    Extract text from uploaded PDF resume.
    """

    text = ""

    try:
        with pdfplumber.open(pdf_file) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

    except Exception as e:
        return ""

    return text