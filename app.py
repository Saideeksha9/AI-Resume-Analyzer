import streamlit as st

# --------------------------
# Backend Modules
# --------------------------
from utils.pdf_parser import extract_text
from utils.skill_extractor import extract_skills
from utils.suggestions import generate_suggestions
from utils.contact_info import extract_contact_info

from analysis.ats_score import calculate_score
from analysis.keyword_match import keyword_match

from reports.report_generator import create_report

from interview_questions import generate_questions
from roadmap import generate_roadmap

# --------------------------
# UI Components
# --------------------------
from components.sidebar import show_sidebar
from components.header import show_header
from components.metrics import show_metrics
from components.candidate_card import show_candidate
from components.skills_card import show_skills
from components.charts import skill_chart
from components.footer import show_footer

# --------------------------
# Page Configuration
# --------------------------
st.set_page_config(
    page_title="ResumeIQ AI",
    page_icon="🚀",
    layout="wide"
)

# --------------------------
# Header & Sidebar
# --------------------------
show_sidebar()
show_header()

# --------------------------
# Input Section
# --------------------------
resume_file = st.file_uploader(
    "📄 Upload Resume",
    type=["pdf"]
)

job_description = st.text_area(
    "📝 Paste Job Description",
    height=220
)

# --------------------------
# Analyze Button
# --------------------------
if st.button("🚀 Analyze Resume"):

    if resume_file is None:
        st.error("Please upload your resume.")
        st.stop()

    if job_description.strip() == "":
        st.error("Please paste the Job Description.")
        st.stop()

    with st.spinner("🔍 Analyzing Resume..."):

        # --------------------------
        # Resume Parsing
        # --------------------------
        resume_text = extract_text(resume_file)

        resume_skills = extract_skills(resume_text)
        jd_skills = extract_skills(job_description)

        matched = list(set(resume_skills).intersection(jd_skills))
        missing = list(set(jd_skills) - set(resume_skills))

        # --------------------------
        # Scores
        # --------------------------
        tfidf_score = calculate_score(
            resume_text,
            job_description
        )

        keyword_score = keyword_match(
            resume_text,
            job_description
        )

        if len(jd_skills) > 0:
            skill_match = (
                len(matched) /
                len(jd_skills)
            ) * 100
        else:
            skill_match = 0

        score = round(
            (0.40 * tfidf_score)
            + (0.30 * keyword_score)
            + (0.30 * skill_match),
            2
        )

        # --------------------------
        # Candidate Details
        # --------------------------
        name, email, phone = extract_contact_info(
            resume_text
        )

        # --------------------------
        # Suggestions
        # --------------------------
        suggestions = generate_suggestions(
            score,
            missing
        )

        questions = generate_questions(
            resume_skills
        )

        roadmap = generate_roadmap(
            missing
        )

        report = create_report(
            score,
            resume_skills,
            missing,
            suggestions
        )

        st.success("✅ Resume Analysis Completed Successfully!")

                # =====================================================
        # ATS DASHBOARD
        # =====================================================

        st.markdown("## 📊 ATS Dashboard")

        show_metrics(
            score,
            len(resume_skills),
            len(matched),
            len(missing)
        )

        if score >= 85:
            st.success(
                "🌟 Excellent! Your resume is highly compatible with the Job Description."
            )
        elif score >= 70:
            st.info(
                "👍 Good Resume! Add a few missing skills to improve further."
            )
        elif score >= 50:
            st.warning(
                "⚠ Moderate Match. Improve your resume before applying."
            )
        else:
            st.error(
                "❌ Low ATS Match. Resume requires significant improvements."
            )

        st.markdown("---")

        # =====================================================
        # TWO COLUMN LAYOUT
        # =====================================================

        left, right = st.columns([1, 2])

        # =====================================================
        # LEFT COLUMN
        # =====================================================

        with left:

            show_candidate(
                name,
                email,
                phone
            )

            st.markdown("---")

            st.subheader("📈 Resume Statistics")

            st.metric(
                "Total Skills",
                len(resume_skills)
            )

            st.metric(
                "Matched Skills",
                len(matched)
            )

            st.metric(
                "Missing Skills",
                len(missing)
            )

            st.metric(
                "Skill Match",
                f"{skill_match:.1f}%"
            )

        # =====================================================
        # RIGHT COLUMN
        # =====================================================

        with right:

            tab1, tab2, tab3 = st.tabs(
                [
                    "🛠 Skills",
                    "❌ Missing Skills",
                    "📊 Charts"
                ]
            )

            # -----------------------------
            # Skills Tab
            # -----------------------------
            with tab1:

                show_skills(
                    "Skills Found",
                    resume_skills
                )

            # -----------------------------
            # Missing Skills
            # -----------------------------
            with tab2:

                show_skills(
                    "Missing Skills",
                    missing
                )

            # -----------------------------
            # Charts
            # -----------------------------
            with tab3:

                skill_chart(
                    len(matched),
                    len(missing)
                )

        st.markdown("---")

        # =====================================================
        # SCORE BREAKDOWN
        # =====================================================

        st.subheader("📈 Score Breakdown")

        c1, c2, c3 = st.columns(3)

        with c1:

            st.metric(
                "TF-IDF Score",
                f"{tfidf_score:.2f}%"
            )

        with c2:

            st.metric(
                "Keyword Match",
                f"{keyword_score:.2f}%"
            )

        with c3:

            st.metric(
                "Skill Match",
                f"{skill_match:.2f}%"
            )

        st.markdown("---")

                # =====================================================
        # AI SUGGESTIONS
        # =====================================================

        st.subheader("💡 AI Suggestions")

        if suggestions:
            for suggestion in suggestions:
                st.success(f"✔ {suggestion}")
        else:
            st.info("No suggestions available.")

        st.markdown("---")

        # =====================================================
        # INTERVIEW QUESTIONS
        # =====================================================

        st.subheader("🎯 AI Interview Questions")

        if questions:

            qcol1, qcol2 = st.columns(2)

            half = (len(questions) + 1) // 2

            with qcol1:
                for question in questions[:half]:
                    st.write(f"✅ {question}")

            with qcol2:
                for question in questions[half:]:
                    st.write(f"✅ {question}")

        else:
            st.info("No interview questions generated.")

        st.markdown("---")

        # =====================================================
        # LEARNING ROADMAP
        # =====================================================

        st.subheader("📚 Personalized Learning Roadmap")

        if roadmap:

            for i, step in enumerate(roadmap, 1):

                st.info(f"Week {i}: {step}")

        else:

            st.success("Your resume already contains all required skills.")

        st.markdown("---")

        # =====================================================
        # RESUME PREVIEW
        # =====================================================

        with st.expander("📄 Resume Preview", expanded=False):

            st.text_area(
                "Extracted Resume Text",
                resume_text,
                height=350
            )

        st.markdown("---")

        # =====================================================
        # DOWNLOAD REPORT
        # =====================================================

        st.subheader("📥 Download Report")

        with open(report, "rb") as pdf:

            st.download_button(
                label="📄 Download Resume Analysis Report",
                data=pdf,
                file_name="Resume_Analysis_Report.pdf",
                mime="application/pdf"
            )

        st.markdown("---")

        # =====================================================
        # ABOUT DASHBOARD
        # =====================================================

        with st.expander("ℹ About ResumeIQ AI"):

            st.write("""
ResumeIQ AI analyzes resumes using:

- 📄 Resume Parsing
- 🧠 TF-IDF Similarity
- 🔍 Keyword Matching
- 🛠 Skill Extraction
- 📈 ATS Score Calculation
- 🎯 AI Interview Questions
- 📚 Personalized Learning Roadmap
- 📑 PDF Report Generation
            """)

        # =====================================================
        # FOOTER
        # =====================================================

        show_footer()