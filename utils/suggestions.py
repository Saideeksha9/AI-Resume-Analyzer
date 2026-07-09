def generate_suggestions(score, missing_skills):

    suggestions = []

    if score >= 85:
        suggestions.append("Excellent ATS compatibility.")

    elif score >= 70:
        suggestions.append("Good resume. Add missing skills to improve the ATS score.")

    else:
        suggestions.append("Resume requires significant improvements.")

    if missing_skills:
        suggestions.append(
            "Consider adding these relevant skills: " +
            ", ".join(missing_skills)
        )

    suggestions.append("Use strong action verbs such as Developed, Implemented, Designed.")

    suggestions.append("Quantify achievements wherever possible (e.g., Improved performance by 20%).")

    suggestions.append("Keep the resume concise and ATS-friendly.")

    return suggestions