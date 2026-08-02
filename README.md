## 🚀 Live Demo

🌐 https://ai-resume-analyzer-kabtkwquexmlsfananle6n.streamlit.app/

# 🤖 AI Resume Analysis & Interview Question Generator

An AI-assisted resume analysis project that generates **technical interview questions based on the skills identified from a candidate's resume**.

The system maintains a collection of technical questions for different skills such as Python, Java, SQL, React, Machine Learning, Deep Learning, NLP, and Git. Based on the skills provided, relevant interview questions are selected and combined to create a personalized interview preparation set.

## 📌 Project Overview

Preparing for technical interviews can be difficult because students may not know which questions to practice for the skills mentioned in their resume.

This project addresses this problem by generating interview questions according to the candidate's technical skills.

For example, if the candidate has:

```text
Python
SQL
React
```

the system generates questions related to these technologies.

The generated questions are limited to a maximum of **10 questions** for focused interview preparation.

## ✨ Features

* Skill-based interview question generation
* Supports multiple technical skills
* Predefined question bank for each supported skill
* Generates questions dynamically based on provided skills
* Maximum of 10 questions per request
* Provides a fallback project-based question when no matching skill is found

## 🧠 Currently Supported Skills

The current question bank supports:

* Python
* Java
* SQL
* React
* Machine Learning
* Deep Learning
* NLP
* Git

## 📝 Example

### Input

```python
skills = ["Python", "SQL", "React"]
```

### Output

The system can generate questions such as:

```text
1. Explain Python decorators.
2. What are Python lists and tuples?
3. What is list comprehension?
4. What are generators in Python?
5. What is the difference between DELETE, TRUNCATE and DROP?
6. Explain SQL JOINs.
7. What is normalization?
8. Explain React components.
9. What are React Hooks?
10. Difference between State and Props?
```

The system returns at most **10 questions**.

## ⚙️ How It Works

```text
        Candidate Skills
               │
               ▼
      generate_questions()
               │
               ▼
      Check Skill Question Bank
               │
        ┌──────┴──────┐
        │             │
     Match          No Match
        │             │
        ▼             ▼
Generate Questions   Generic
        │            Project Question
        └──────┬──────┘
               ▼
       Maximum 10 Questions
               │
               ▼
       Interview Questions
```

## 🔍 Question Generation Logic

The project uses a dictionary-based question bank.

Each skill is associated with a set of technical questions.

For example:

```python
"Python": [
    "Explain Python decorators.",
    "What are Python lists and tuples?",
    "What is list comprehension?",
    "What are generators in Python?"
]
```

The program loops through the provided skills and adds questions for every supported skill.

If no questions are generated, it provides:

```text
Explain one project from your resume.
```

Finally, the result is restricted to the first 10 questions.

## 🛠️ Technologies

The current implementation is written in:

* Python
* Python Lists
* Python Dictionaries
* Loops
* Conditional Statements
* Functions

## 📂 Project Structure

```text
AI-Resume-Analysis/
│
├── generate_questions.py
└── README.md
```

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd AI-Resume-Analysis
```

### 2. Run the Python program

```bash
python generate_questions.py
```

### 3. Provide skills

The function accepts a list of skills:

```python
skills = ["Python", "Java", "SQL"]

questions = generate_questions(skills)

for question in questions:
    print(question)
```

## 🎯 Use Case

This project can be useful for:

* College students preparing for placements
* Technical interview preparation
* Resume-based interview practice
* Generating skill-specific technical questions
* Personalized interview preparation


## 💡 Workflow

The project can eventually evolve into:

```text
        Upload Resume
              │
              ▼
       Extract Resume Text
              │
              ▼
        Extract Skills
              │
              ▼
      Analyze Job Description
              │
              ▼
       Match Skills with JD
              │
              ▼
      Generate Interview Questions
              │
              ▼
       Personalized Preparation
```



This project is developed for educational and portfolio purposes.
