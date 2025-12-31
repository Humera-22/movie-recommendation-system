# 🎬 Movie Recommendation System

A content-based movie recommendation system built using Machine Learning and Natural Language Processing (NLP).  
The application recommends movies similar to a selected movie based on metadata such as genres, keywords, cast, crew, and overview.

## 📌 Project Overview

This project implements a content-based recommendation engine that suggests movies similar to a selected title.  
The recommendation logic is based on textual similarity between movie metadata using Natural Language Processing techniques.

The system processes movie information, converts it into numerical vectors, and computes similarity scores to identify the most relevant recommendations.

## 🧠 Machine Learning Approach

The recommendation system follows a content-based filtering approach.

### Data Source
The project uses the TMDB 5000 Movies dataset, which contains detailed information about movies such as:
- Title
- Overview
- Genres
- Keywords
- Cast
- Crew

### Feature Engineering
Relevant textual attributes are combined into a single feature called `tags`.  
This includes:
- Movie overview
- Genres
- Keywords
- Top cast members
- Director name

The text data is cleaned, tokenized, lowercased, and stemmed to improve similarity detection.

### Vectorization
The processed text is transformed into numerical vectors using **CountVectorizer** with a limited vocabulary size and English stop words removed.

### Similarity Computation
Cosine similarity is used to measure the closeness between movies.  
Based on these similarity scores, the system recommends the top 5 most similar movies.

## 🗂 Project Structure

```text
movie-recommendation-system-docker/
│
├── app/
│   ├── mlproject.py          # Streamlit application
│   ├── Dockerfile            # Docker image configuration
│   ├── requirements.txt      # Application dependencies
│
├── notebook/
│   └── model_preparation.ipynb   # Data preprocessing & model training
│
├── docker-compose.yml
├── README.md
├── .gitignore
```
## 🚀 Application Features

- Interactive web interface built using Streamlit
- Dropdown-based movie selection
- Displays top 5 recommended movies
- Fetches movie posters dynamically using the TMDB API
- Clean and responsive user interface
- Fast similarity-based recommendations

## 🐳 Running the Application (Docker)

### Prerequisites
- Docker
- Docker Compose

### Steps
```bash
git clone https://github.com/Humera-22/movie-recommendation-system.git
cd movie-recommendation-system-docker
docker compose up --build
```
Open your browser and visit:
http://localhost:8501

## 🧪 Model Training & File Generation

The machine learning model and similarity matrix are generated using a Jupyter Notebook.

The notebook performs:
- Data loading and cleaning
- Feature engineering and text processing
- Vectorization using CountVectorizer
- Similarity computation using cosine similarity

The trained artifacts (`movie_dict.pkl` and `similarity.pkl`) are generated locally and used by the Streamlit application.

## 🛠️ Technologies Used

- Python
- Pandas, NumPy
- Scikit-learn
- NLTK
- Streamlit
- Docker & Docker Compose
- Git & GitHub

---









