import streamlit as st
import pandas as pd

from resume_parser import extract_text_from_pdf

from matcher import (
    calculate_tfidf_similarity,
    calculate_semantic_similarity,
    calculate_overall_score,
    extract_skills,
    compare_skills
)


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Resume & Job Matcher",
    page_icon="🤖",
    layout="wide"
)


# ============================================================
# TITLE
# ============================================================

st.title("🤖 AI Resume & Job Matching Tool")

st.write(
    """
    Upload your resume and paste a job description to analyse
    how well your profile matches the role.
    """
)


# ============================================================
# RESUME UPLOAD
# ============================================================

uploaded_file = st.file_uploader(
    "📄 Upload your resume",
    type=["pdf"]
)


# Store resume text
resume_text = None


if uploaded_file:

    try:

        resume_text = extract_text_from_pdf(
            uploaded_file
        )

        st.success("✅ Resume successfully uploaded!")

        # Optional: show extracted text
        with st.expander("View extracted resume text"):

            st.text(resume_text)

    except Exception as e:

        st.error(
            f"Error reading the resume: {e}"
        )


# ============================================================
# JOB DESCRIPTION
# ============================================================

job_text = st.text_area(
    "📋 Paste the job description here",
    height=300,
    placeholder="Paste the full job description here..."
)


# ============================================================
# ANALYSE BUTTON
# ============================================================

if st.button(
    "🔍 Analyse Match",
    type="primary"
):

    # --------------------------------------------------------
    # CHECK INPUTS
    # --------------------------------------------------------

    if uploaded_file is None:

        st.warning(
            "⚠️ Please upload your resume first."
        )

    elif resume_text is None:

        st.warning(
            "⚠️ Unable to extract text from your resume."
        )

    elif not job_text.strip():

        st.warning(
            "⚠️ Please paste a job description."
        )

    else:

        # ----------------------------------------------------
        # MATCHING
        # ----------------------------------------------------

        with st.spinner(
            "🤖 Analysing your resume against the job description..."
        ):

            # TF-IDF similarity
            tfidf_score = calculate_tfidf_similarity(
                resume_text,
                job_text
            )

            # Semantic similarity
            semantic_score = calculate_semantic_similarity(
                resume_text,
                job_text
            )

            # Combined score
            overall_score = calculate_overall_score(
                tfidf_score,
                semantic_score
            )


        st.success(
            "✅ Analysis complete!"
        )


        # ====================================================
        # MATCH SCORE
        # ====================================================

        st.divider()

        st.header("📊 Match Score")


        col1, col2, col3 = st.columns(3)


        with col1:

            st.metric(
                "Overall Match",
                f"{overall_score}%"
            )


        with col2:

            st.metric(
                "Keyword Match",
                f"{tfidf_score}%"
            )


        with col3:

            st.metric(
                "Semantic Match",
                f"{semantic_score}%"
            )


        # ====================================================
        # SKILL ANALYSIS
        # ====================================================

        st.divider()

        st.header("🛠️ Skills Analysis")


        try:

            # Load skills database
            skills_df = pd.read_csv(
                "skills.csv"
            )

            skills = skills_df[
                "skill"
            ].dropna().tolist()


            # Extract skills from resume
            resume_skills = extract_skills(
                resume_text,
                skills
            )


            # Extract skills from job description
            job_skills = extract_skills(
                job_text,
                skills
            )


            # Compare skills
            matching, missing = compare_skills(
                resume_skills,
                job_skills
            )


            # ------------------------------------------------
            # DISPLAY MATCHING / MISSING SKILLS
            # ------------------------------------------------

            col1, col2 = st.columns(2)


            with col1:

                st.subheader(
                    "✅ Matching Skills"
                )


                if matching:

                    for skill in sorted(matching):

                        st.write(
                            f"• {skill}"
                        )

                else:

                    st.info(
                        "No matching skills were identified."
                    )


            with col2:

                st.subheader(
                    "⚠️ Skills to Develop"
                )


                if missing:

                    for skill in sorted(missing):

                        st.write(
                            f"• {skill}"
                        )

                else:

                    st.success(
                        "No missing skills identified!"
                    )


            # ------------------------------------------------
            # SKILL MATCH SCORE
            # ------------------------------------------------

            if len(job_skills) > 0:

                skill_score = (
                    len(matching)
                    / len(job_skills)
                ) * 100

            else:

                skill_score = 0


            st.divider()


            col1, col2 = st.columns(2)


            with col1:

                st.metric(
                    "Required Skills Match",
                    f"{skill_score:.1f}%"
                )


            with col2:

                st.metric(
                    "Skills Found in Resume",
                    len(resume_skills)
                )


            # ------------------------------------------------
            # JOB SKILLS
            # ------------------------------------------------

            with st.expander(
                "View skills identified in the job description"
            ):

                if job_skills:

                    for skill in sorted(job_skills):

                        st.write(
                            f"• {skill}"

                        )

                else:

                    st.write(
                        "No predefined skills were identified."
                    )


        except FileNotFoundError:

            st.error(
                """
                The skills database could not be found.

                Please make sure this file exists:

                `skills.csv`
                """
            )


        except Exception as e:

            st.error(
                f"Error analysing skills: {e}"
            )


        # ====================================================
        # MATCH INTERPRETATION
        # ====================================================

        st.divider()

        st.header("💡 Match Interpretation")


        if overall_score >= 80:

            st.success(
                "🌟 Strong Match — your profile appears to "
                "align very well with this role."
            )

        elif overall_score >= 65:

            st.info(
                "👍 Good Match — you have several relevant "
                "skills and experiences, with some potential gaps."
            )

        elif overall_score >= 50:

            st.warning(
                "⚠️ Moderate Match — there are some relevant "
                "areas, but the role may require additional skills."
            )

        else:

            st.error(
                "❗ Low Match — there appears to be a significant "
                "difference between the resume and job requirements."
            )


        # ====================================================
        # BASIC RECOMMENDATIONS
        # ====================================================

        st.header("💡 Recommendations")


        if missing:

            st.write(
                "Consider highlighting or developing the following "
                "skills if they are relevant to your experience:"
            )


            for skill in sorted(missing):

                st.write(
                    f"• **{skill}**"
                )

        else:

            st.write(
                "Your resume contains the main skills identified "
                "in the job description."
            )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "AI Resume & Job Matching Tool | "
    "Python • NLP • Machine Learning • Streamlit"
)