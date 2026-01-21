import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib
import sys

def train():
    print("Loading data...")
    try:
        df = pd.read_csv('data/messages.csv')
    except FileNotFoundError:
        print("Error: data/messages.csv not found.")
        sys.exit(1)

    print(f"Loaded {len(df)} rows.")

    X = df['text']
    y = df['label']

    print("Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

    print("Training model...")
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(ngram_range=(1, 2), min_df=2)),
        ('clf', LogisticRegression(max_iter=1000, random_state=42))
    ])

    pipeline.fit(X_train, y_train)

    print("Evaluating model...")
    y_pred = pipeline.predict(X_test)
    print(classification_report(y_test, y_pred))

    print("Saving artifacts...")
    joblib.dump(pipeline, 'models/model_pipeline.joblib')
    # Note: Using a single pipeline object is cleaner, but the assignment asks for separate saves.
    # We can save the components separately to strictly adhere, but pipeline is industry standard.
    # Let's save the pipeline as the main 'model.joblib' effectively, or extract components.
    # Based on prompt "models/model.joblib" and "models/vectorizer.joblib"
    
    # Extracting for strict compliance if needed, but Pipeline object is usually what you load.
    # However, to facilitate easy usage similar to "vectorizer.transform" then "model.predict", let's save both.
    # Actually, saving the pipeline is safer for inference consistency. 
    # But let's stick to the prompt structure if strictly required, OR just save the pipeline which contains both.
    # The prompt says: "modules/model.joblib" and "modules/vectorizer.joblib".
    
    joblib.dump(pipeline.named_steps['tfidf'], 'models/vectorizer.joblib')
    joblib.dump(pipeline.named_steps['clf'], 'models/model.joblib')
    
    print("Done! Artifacts saved to models/")

if __name__ == "__main__":
    train()
