# 🤖 AI Resume & Job Matching Tool

An NLP-powered web application that analyses how well a candidate's
resume matches a job description.

## Features

-   Upload a resume in PDF format
-   Paste a job description
-   Extract resume text automatically
-   Calculate TF-IDF keyword similarity
-   Calculate semantic similarity using Sentence Transformers
-   Generate an overall match score
-   Identify matching skills
-   Identify skills that may need development
-   Calculate required-skills match percentage
-   Provide basic match interpretation and recommendations
-   Interactive Streamlit interface

## Technologies

-   Python
-   Streamlit
-   Pandas
-   NumPy
-   Scikit-learn
-   Sentence Transformers
-   PyMuPDF
-   Plotly

## Project Structure

``` text
AI Resume Job Matcher/
├── app.py
├── matcher.py
├── resume_parser.py
├── requirements.txt
├── README.md
└── skills.csv
    
```

## How It Works

``` text
Resume PDF
    |
    v
Text Extraction
    |
    v
Resume + Job Description
    |
    +------------------+
    |                  |
    v                  v
TF-IDF             Semantic
Similarity         Similarity
    |                  |
    +--------+---------+
             |
             v
       Overall Score
             |
             v
       Skill Analysis
             |
             v
      Recommendations
```

### Resume extraction

PyMuPDF extracts text from the uploaded PDF resume.

### Keyword similarity

TF-IDF compares vocabulary between the resume and job description.

### Semantic similarity

Sentence Transformers create embeddings that capture meaning, helping
identify related concepts even when exact words differ.

### Skill analysis

A predefined skills database is used to identify skills appearing in the
resume and job description.

### Overall score

The current implementation combines TF-IDF similarity and semantic
similarity, with greater weight given to semantic similarity.

## Installation

### 1. Clone the repository

``` bash
git clone https://github.com/YOUR-USERNAME/AI-Resume-Job-Matcher.git
cd AI-Resume-Job-Matcher
```

### 2. Create a virtual environment

``` bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows PowerShell:

``` powershell
venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution:

``` powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then:

``` powershell
venv\Scripts\Activate.ps1
```

### 4. Install dependencies

``` bash
pip install -r requirements.txt
```

## Run the Application

``` bash
streamlit run app.py
```

The application should open in your browser. If it does not, use the
local URL shown by Streamlit, normally:

``` text
http://localhost:8501
```

## Example Output

The application provides:

-   Overall Match Score
-   Keyword Match Score
-   Semantic Match Score
-   Required Skills Match
-   Matching Skills
-   Skills to Develop
-   Basic recommendations

## Privacy

Do not upload or commit personal resumes, API keys, passwords, or other
sensitive information to a public GitHub repository.

For portfolio demonstrations, use an anonymised or sample resume.

## Future Improvements

-   AI-generated resume improvement suggestions
-   Job requirement extraction
-   Experience and education matching
-   More robust NLP-based skill extraction
-   Interactive charts
-   Resume keyword recommendations
-   Ranking multiple job descriptions
-   LLM-powered explanations
-   Deployment using Streamlit Community Cloud

## Author

**Diya Susan Eapen**

Master of Data Science \| Data Science \| AI \| Data Analytics

Built as a practical portfolio project exploring NLP, semantic
similarity and explainable AI.
