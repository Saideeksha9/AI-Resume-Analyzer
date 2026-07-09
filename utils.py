import re


def extract_contact_info(text):

    # Email
    email_pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
    emails = re.findall(email_pattern, text)

    email = emails[0] if emails else "Not Found"

    # Phone Number
    phone_pattern = r'(\+91[- ]?)?[6-9]\d{9}'
    phones = re.findall(phone_pattern, text)

    if phones:
        phone = phones[0]
        if isinstance(phone, tuple):
            phone = "".join(phone)
    else:
        phone = "Not Found"

    # Name (Simple Heuristic)
    lines = text.split("\n")

    name = "Not Found"

    for line in lines:
        line = line.strip()

        if len(line.split()) <= 4 and line.replace(" ", "").isalpha():
            name = line
            break

    return name, email, phone