import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download("stopwords", quiet=True)
nltk.download("wordnet", quiet=True)

lemmatizer = WordNetLemmatizer()

keep_words = {"no", "nor", "not", "never", "very", "too", "against"}
stop_words = {
    w for w in stopwords.words("english")
    if w not in keep_words and "n't" not in w
}


def basic_clean(text):
    text = str(text)
    text = re.sub(r"<.*?>", " ", text)
    text = re.sub(r"http\S+", " ", text)
    text = re.sub(r"[^a-zA-Z' ]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.lower().strip()


def clean_text(text):
    words = basic_clean(text).split()
    words = [lemmatizer.lemmatize(w) for w in words if w not in stop_words]
    return " ".join(words)