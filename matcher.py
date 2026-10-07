from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_tfidf_similarity(resume_text, job_text):

    documents = [resume_text, job_text]

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )[0][0]

    return round(similarity * 100, 2)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def calculate_semantic_similarity(resume_text, job_text):

    resume_embedding = model.encode(
        [resume_text]
    )

    job_embedding = model.encode(
        [job_text]
    )

    similarity = cosine_similarity(
        resume_embedding,
        job_embedding
    )[0][0]

    return round(similarity * 100, 2)

def calculate_overall_score(
    tfidf_score,
    semantic_score
):

    overall = (
        tfidf_score * 0.4
        + semantic_score * 0.6
    )

    return round(overall, 2)

def extract_skills(text, skills):

    text_lower = text.lower()

    found_skills = []

    for skill in skills:

        if skill.lower() in text_lower:
            found_skills.append(skill)

    return found_skills

def compare_skills(resume_skills, job_skills):

    resume_set = set(
        skill.lower()
        for skill in resume_skills
    )

    job_set = set(
        skill.lower()
        for skill in job_skills
    )

    matching = resume_set.intersection(job_set)

    missing = job_set - resume_set

    return matching, missing