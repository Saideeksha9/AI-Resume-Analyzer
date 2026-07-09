def generate_roadmap(missing_skills):
    """
    Generate a personalized learning roadmap
    based on missing skills.
    """

    roadmap = []

    skill_resources = {
        "Aws": "Learn AWS Cloud Fundamentals",
        "Docker": "Learn Docker Containers",
        "Kubernetes": "Learn Kubernetes Basics",
        "React": "Build React Projects",
        "Machine Learning": "Complete a Machine Learning Course",
        "Deep Learning": "Learn Neural Networks and CNNs",
        "Nlp": "Study NLP and Text Processing",
        "Sql": "Practice Advanced SQL Queries",
        "Git": "Master Git and GitHub",
        "Java": "Practice Object-Oriented Programming in Java",
        "Python": "Solve Python Coding Problems",
        "MongoDB": "Learn MongoDB CRUD Operations",
        "Flask": "Build REST APIs using Flask"
    }

    if len(missing_skills) == 0:
        roadmap.append("🎉 Great! Your resume already matches the job description well.")
        roadmap.append("Practice coding and interview questions.")
        return roadmap

    roadmap.append("📌 Suggested Learning Roadmap")

    for skill in missing_skills:
        if skill in skill_resources:
            roadmap.append(skill_resources[skill])
        else:
            roadmap.append(f"Learn {skill}")

    roadmap.append("Build a project using the above technologies.")
    roadmap.append("Upload the project to GitHub.")
    roadmap.append("Practice interview questions.")
    roadmap.append("Apply for relevant roles.")

    return roadmap