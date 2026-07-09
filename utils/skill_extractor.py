# List of predefined technical skills

skills = [
    "python",
    "java",
    "c",
    "c++",
    "sql",
    "mysql",
    "mongodb",
    "react",
    "html",
    "css",
    "javascript",
    "typescript",
    "node.js",
    "express",
    "git",
    "github",
    "docker",
    "kubernetes",
    "aws",
    "azure",
    "gcp",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "nlp",
    "tensorflow",
    "keras",
    "pytorch",
    "opencv",
    "pandas",
    "numpy",
    "matplotlib",
    "seaborn",
    "scikit-learn",
    "streamlit",
    "flask",
    "django",
    "linux",
    "excel",
    "power bi",
    "tableau",
    "oracle",
    "firebase",
    "rest api",
    "json",
    "bootstrap"
]


def extract_skills(text):
    """
    Extract predefined technical skills from text.
    """

    text = text.lower()

    detected_skills = []

    for skill in skills:
        if skill in text:
            detected_skills.append(skill.title())

    return sorted(list(set(detected_skills)))