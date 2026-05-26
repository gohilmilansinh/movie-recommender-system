# 🎬 Movie Recommender System

A content‑based movie recommendation engine that suggests 5 similar movies based on a user’s selection. Built with **Python**, **Streamlit**, and **scikit‑learn**, using data from **TMDB** (The Movie Database).

## ✨ Features

- Recommends 5 movies similar to your chosen title.
- Uses **overview**, **genres**, **keywords**, **cast**, and **crew** for similarity calculation.
- Clean, interactive web interface built with Streamlit.
- Fast similarity search using cosine similarity on TF‑IDF vectors.

## 🧠 How It Works

1. **Data preprocessing** – Merges `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`.
2. **Feature extraction** – Combines overview, genres, keywords, cast (top 3), and director.
3. **Text vectorization** – Converts text into TF‑IDF vectors (5000 features).
4. **Similarity calculation** – Computes cosine similarity between all movies.
5. **Recommendation** – Given a movie, returns the 5 most similar movies.

## 📁 Project Structure
#### Movies-Recommender-system/
#### ├── app.py # Streamlit web app
#### ├── requirements.txt # Python dependencies
#### ├── procfile # For deployment (Heroku / Render)
#### ├── setup.sh # Startup script for Streamlit Cloud
#### ├── .gitignore # Ignores large pickle files & environment
#### ├── Notebook/ # (not synced to Git) Jupyter notebooks & raw CSVs
#### │ ├── movie_recommender_system.ipynb
#### │ ├── tmdb_5000_movies.csv
#### │ └── tmdb_5000_credits.csv
#### └── README.md


> **Note:** The large `similarity.pkl` (184 MB) and `movies.pkl` files are **excluded from Git** due to GitHub’s 100 MB file limit. They are generated at runtime on the deployment server (or locally when you run the notebook).

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Movies-Recommender-system.git
cd Movies-Recommender-system```

### 2. Set up a virtual environment (optional but recommended)
```bash
python -m venv .venv
source .venv/bin/activate      # Linux/macOS
.venv\Scripts\activate         # Windows```

### 3. Install dependencies
```bash
pip install -r requirements.txt```

### 4. Download the dataset
You need the two CSV files from TMDB (they are not included in this repo due to size).
Place them inside the Notebook/ folder:

tmdb_5000_movies.csv

tmdb_5000_credits.csv

You can download them from Kaggle.

### 5. Generate the model files (run once)
Open and run the Jupyter notebook:

```bash
cd Notebook
jupyter notebook movie_recommender_system.ipynb
Execute all cells. This will create movies.pkl and similarity.pkl in the Notebook/ folder.
Move or copy them to the project root (../):```

```bash
cp movies.pkl ../
cp similarity.pkl ../
⚠️ These files are ignored by Git – never push them to GitHub.```

### 6. Run the Streamlit app
```bash
streamlit run app.py
Open your browser at http://localhost:8501.```
