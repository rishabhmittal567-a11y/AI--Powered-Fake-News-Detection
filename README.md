# AI--Powered-Fake-News-Detection
An end-to-end Machine Learning web application built to detect fake news articles using Natural Language Processing (NLP) and Streamlit.FeaturesMachine Learning Classification: Powered by a trained Random Forest classifier to distinguish between real and fake news.  TF-IDF Vectorization: Transforms textual news content into meaningful numerical feature representations.Interactive UI: Built with Streamlit for a fast, clean, and user-friendly experience.Large Dataset Support: Integrates Git LFS (Large File Storage) to manage large datasets and model artifacts seamlessly.Project StructurePlaintextD:\FakeNews\
│
├── .gitattributes          # Git LFS tracking rules
├── .gitignore              # Files to ignore from git
├── README.md               # Project documentation
├── app.py                  # Streamlit web application
├── random_forest.pkl       # Trained Random Forest model (Git LFS)
├── tfidf_vectorizer.pkl    # TF-IDF Vectorizer model
└── WELFake_Dataset.csv     # Dataset used for training (Git LFS)
Setup & InstallationFollow these steps to run the project locally:Clone the RepositoryDOSgit clone https://github.com/rishabhmittal567-a11y/AI--Powered-Fake-News-Detection.git
cd AI--Powered-Fake-News-Detection
Ensure Git LFS is InstalledIf you haven't installed Git LFS on your system yet, initialize it:DOSgit lfs install
git lfs pull
Install DependenciesMake sure you have Python installed, then install the required packages:DOSpip install streamlit pandas scikit-learn joblib
Run the Streamlit AppDOSstreamlit run app.py
