import re

def extract_contact_info(text):
    name = "Not Found"

    lines = text.split("\n")
    if lines:
        name = lines[0].strip()

    email_match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)
    email = email_match.group() if email_match else "Not Found"

    phone_match = re.search(r'(\+?\d[\d\s-]{8,}\d)', text)
    phone = phone_match.group() if phone_match else "Not Found"

    return name, email, phone