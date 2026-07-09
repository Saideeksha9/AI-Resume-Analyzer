def generate_questions(skills):

    questions = []

    skill_questions = {

        "Python":[
            "Explain Python decorators.",
            "What are Python lists and tuples?",
            "What is list comprehension?",
            "What are generators in Python?"
        ],

        "Java":[
            "Explain JVM, JDK and JRE.",
            "What is polymorphism?",
            "Explain method overloading and overriding."
        ],

        "SQL":[
            "What is the difference between DELETE, TRUNCATE and DROP?",
            "Explain SQL JOINs.",
            "What is normalization?"
        ],

        "React":[
            "Explain React components.",
            "What are React Hooks?",
            "Difference between State and Props?"
        ],

        "Machine Learning":[
            "Explain supervised and unsupervised learning.",
            "What is overfitting?",
            "Explain bias and variance."
        ],

        "Deep Learning":[
            "What is a neural network?",
            "Explain CNN.",
            "Difference between CNN and ANN?"
        ],

        "Nlp":[
            "What is TF-IDF?",
            "Explain Cosine Similarity.",
            "What is tokenization?"
        ],

        "Git":[
            "Difference between Git and GitHub?",
            "Explain git merge and git rebase."
        ]
    }

    for skill in skills:

        if skill in skill_questions:
            questions.extend(skill_questions[skill])

    if len(questions)==0:

        questions.append("Explain one project from your resume.")

    return questions[:10]