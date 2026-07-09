import re


def keyword_match(resume_text, job_description):
    """
    Calculate keyword match percentage between
    resume and job description.
    """

    # Extract words (letters and numbers)
    resume_words = set(re.findall(r"\b[a-zA-Z0-9+#.]+\b", resume_text.lower()))
    jd_words = set(re.findall(r"\b[a-zA-Z0-9+#.]+\b", job_description.lower()))

    # Remove very short words
    jd_words = {word for word in jd_words if len(word) > 2}

    if len(jd_words) == 0:
        return 0

    matched = resume_words.intersection(jd_words)

    percentage = round((len(matched) / len(jd_words)) * 100, 2)

    return percentage
