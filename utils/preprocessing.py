import re
from nltk.tokenize import TweetTokenizer
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
import nltk

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

tk = TweetTokenizer()
stemmer = SnowballStemmer('english')
stop_words = set(stopwords.words('english'))

def clean_text(text: str) -> str:
    text = re.sub(r"[^A-Za-z0-9]", " ", text)
    tokens = tk.tokenize(text)
    tokens = [stemmer.stem(w.lower()) for w in tokens if len(w) >= 3 and w.lower() not in stop_words]
    return " ".join(tokens)
