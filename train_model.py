# train_model.py
import pandas as pd
import re
import nltk
from nltk.tokenize import TweetTokenizer
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import joblib
import os

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Load dataset
df = pd.read_csv(r'C:/Users/LOQ/Downloads/Telegram Desktop/EmotionDetection (1).csv')
df = df.dropna()
df = df.drop('Unnamed: 0', axis=1)

# Map emotions to sentiment classes
emotion_map = {
    'love': '1', 'relief': '1', 'fun': '1', 'happiness': '1', 'enthusiasm': '1', 'surprise': '1',
    'neutral': '0', 'empty': '0',
    'boredom': '-1', 'sadness': '-1', 'anger': '-1', 'worry': '-1', 'hate': '-1'
}
df['Emotion'] = df['Emotion'].replace(emotion_map)
texts = df['text']

# Initialize tokenizer, stemmer, stopwords
tk = TweetTokenizer()
stemmer = SnowballStemmer('english')
stop_words = set(stopwords.words('english'))

# Preprocessing function
def clean_text(text):
    text = re.sub(r'[^A-Za-z0-9]', ' ', text)
    tokens = tk.tokenize(text)
    tokens = [stemmer.stem(w.lower()) for w in tokens if len(w) >= 3 and w.lower() not in stop_words]
    return ' '.join(tokens)

texts = texts.apply(clean_text)
y = df['Emotion'].values

# Vectorization
vec = TfidfVectorizer()
X = vec.fit_transform(texts)

# Train-test split
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train SVM model
model = SVC()
model.fit(x_train, y_train)

# Save model and vectorizer
os.makedirs("models_ml", exist_ok=True)
joblib.dump(model, "models_ml/emotion_model.joblib")
joblib.dump(vec, "models_ml/vectorizer.joblib")

print("Training completed. Models saved in 'models_ml/' folder.") folder name 