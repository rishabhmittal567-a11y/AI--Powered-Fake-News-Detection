# AI--Powered-Fake-News-Detection
# 📰 AI-Powered Fake News Detection using NLP

## 📌 Overview

The **AI-Powered Fake News Detection** project is a Natural Language Processing (NLP) and Machine Learning application that classifies news articles as **Real** or **Fake**. The system preprocesses textual news content, converts it into numerical features using **TF-IDF Vectorization**, and predicts authenticity using a trained **Random Forest Classifier**.

The project includes a user-friendly **Streamlit web application** that allows users to paste news text and receive an instant prediction.

---

## 🚀 Features

- Detects whether a news article is **Real** or **Fake**
- NLP-based text preprocessing
- TF-IDF feature extraction
- Random Forest Machine Learning model
- Interactive Streamlit web application
- Fast and accurate predictions
- Clean and simple user interface

---

## 🛠️ Technologies Used

- Python
- Natural Language Processing (NLP)
- Scikit-learn
- Pandas
- NumPy
- NLTK
- Joblib
- Streamlit

---

## 📂 Project Structure

```
AI-Powered-Fake-News-Detection/
│
├── app.py                     # Streamlit application
├── requirements.txt           # Required dependencies
├── README.md                  # Project documentation
│
├── data/
│   └── WELFake_Dataset.csv
│
├── models/
│   ├── random_forest.pkl
│   └── tfidf_vectorizer.pkl
│
├── notebooks/
│   └── model_training.ipynb
│
└── images/
    └── screenshot.png
```

---

## 📊 Dataset

This project uses the **WELFake Dataset**, which contains thousands of labeled news articles.

Dataset Columns:

- **Title**
- **Text**
- **Label**
  - 0 → Real News
  - 1 → Fake News

---

## ⚙️ Workflow

1. Load Dataset
2. Data Cleaning
3. Text Preprocessing
4. Tokenization
5. Stopword Removal
6. Lemmatization
7. TF-IDF Vectorization
8. Train Random Forest Model
9. Save Model using Joblib
10. Deploy using Streamlit

---

## 🧹 Text Preprocessing

The following NLP techniques are applied:

- Convert text to lowercase
- Remove punctuation
- Remove numbers
- Remove special characters
- Remove stopwords
- Lemmatization

---

## 🤖 Machine Learning Model

**Algorithm Used**

- Random Forest Classifier

**Feature Extraction**

- TF-IDF Vectorizer

---

## 📈 Model Performance

| Metric | Score |
|---------|-------|
| Accuracy | 98.43% |
| Precision | 98.51% |
| Recall | 98.48% |
| F1 Score | 98.49% |

---

## 💻 Installation

Clone the repository

```bash
git clone https://github.com/your-username/AI-Powered-Fake-News-Detection.git
```

Move into the project folder

```bash
cd AI-Powered-Fake-News-Detection
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 🖥️ Usage

1. Launch the Streamlit application.
2. Paste or type a news article.
3. Click the **Predict** button.
4. View whether the news is **Real** or **Fake**.

---

## 📸 Application Screenshot

Add your Streamlit application screenshot here.

Example:

```
images/screenshot.png
```

---

## 📦 Required Libraries

```
streamlit
pandas
numpy
scikit-learn
nltk
joblib
```

---

## 🔮 Future Improvements

- Deep Learning models (LSTM, Bi-LSTM)
- Transformer-based models (BERT, RoBERTa)
- Explainable AI (SHAP/LIME)
- News URL verification
- Multilingual fake news detection
- Real-time news API integration
- Confidence score visualization
- Model comparison dashboard

---

## 📚 References

1. Ahmed, H., Traore, I., & Saad, S. (2018). Detecting opinion spams and fake news using text classification. *Security and Privacy*, 1(1).
2. Shu, K., Sliva, A., Wang, S., Tang, J., & Liu, H. (2017). Fake News Detection on Social Media: A Data Mining Perspective.
3. Pedregosa, F., et al. (2011). Scikit-learn: Machine Learning in Python. *Journal of Machine Learning Research*.
4. Bird, S., Klein, E., & Loper, E. (2009). *Natural Language Processing with Python*. O'Reilly Media.
5. WELFake Dataset: https://github.com/IITGuwahati-AI/WELFake-Dataset

---

## 👨‍💻 Author

**Rishabh Mittal**

M.Tech (Engineering Systems)

Interested in:
- Artificial Intelligence
- Machine Learning
- Natural Language Processing
- Data Science

GitHub:
https://github.com/rishabhmittal567-a11y

LinkedIn:
(Add your LinkedIn profile here)

---

## ⭐ Support

If you found this project useful, consider giving it a **⭐ Star** on GitHub.

Contributions, suggestions, and feedback are always welcome.

---

## 📄 License

This project is licensed under the **MIT License**.
