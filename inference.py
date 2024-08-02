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
# list1 = [
#     "Finnish high technology provider Vaahto Group reports net sales of EUR 41.8 mn in the accounting period September 2007 - February 2008 , an increase of 11.2 % from a year earlier .",
#     "Net sales of Finnish food industry company L+�nnen Tehtaat 's continuing operations increased by 13 % in 2008 to EUR 349.1 mn from EUR 309.6 mn in 2007 .",
#     "An individual promotion also generated slightly higher-than-expected revenues .",
#     "Biohit already services many current Genesis customers and the customer base is expected to expand as a result of this agreement .",
#     "Both operating profit and turnover for the three-month period increased , respectively from EUR0 .9 m and EUR8 .3 m , as compared to the corresponding period in 2005 .",
#     "Circulation revenue has increased by 5 % in Finland and 4 % in Sweden in 2008 .",
#     "Clothing chain Sepp+�l+� 's net sales increased by 7.0 % to EUR 30.8 mn .",
#     "Construction volumes meanwhile grow at a rate of 10-15 percent annually .",

#     "Compared with the FTSE 100 index , which rose 94.9 points ( or 1.6 % ) on the day , this was a relative price change of -0.4 % .",
#     "Peer Peugeot fell 0.81 pct as its sales rose only 6.3 pct from the same period last year .",
#     "Pharmaceuticals group Orion Corp reported a fall in its third-quarter earnings that were hit by larger expenditures on R&D and marketing .",
#     "However , the growth margin slowed down due to the financial crisis .",

#     "Cencorp , headquartered in Virkkala , Finland , develops and supplies automation solutions to the electronics and semiconductor industry that enhance productivity .",
#     "Following the increase , Huhtamaki Oyj 's registered share capital is EUR 358,706,290.00 and the number of shares outstanding is 105,501,850 .",
#     "Following this increase Huhtamaki 's registered share capital is EUR360 .62 m and the number of shares outstanding is 106,063,320 .",
#     "The company has also supplied more than 200 MW of power generating equipment for a number of projects in Papua New Guinea , including 12 engines of the Wartsila 32 type to Lihir Gold ."
# ]
# inference(list1)