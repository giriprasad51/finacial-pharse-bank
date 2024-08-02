import torch
import pandas as pd
import string
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download("wordnet", "/usr/share/nltk_data/")
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


# Load your trained model (skip this if using the model from the current session)
model = AutoModelForSequenceClassification.from_pretrained('C:/Users/giri.pusunuru/Documents/AIframeworks/finacial-pharse-bank/fine-tuned-model')

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')

# Function to clean text
def clean_text(text):
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Convert text to lowercase
    text = text.lower()
    # Tokenize text
    words = word_tokenize(text)
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    # Lemmatize words
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    # Join words back into a single string
    return ' '.join(words)

# Example new texts for inference
def inference(texts):
    new_texts = [clean_text(text) for text in texts]
    # Tokenize new data
    inputs = tokenizer(new_texts, padding=True, truncation=True, return_tensors="pt")

    # Make predictions
    model.eval()  # Set the model to evaluation mode
    with torch.no_grad():
        outputs = model(**inputs)
        predictions = torch.argmax(outputs.logits, dim=-1)

    # Map predictions to labels
    label_map = {0:'negative', 1:'neutral', 2:'positive'}
    labeled_predictions = [label_map[pred.item()] for pred in predictions]

    print(labeled_predictions)
    return labeled_predictions