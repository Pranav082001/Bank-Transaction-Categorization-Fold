from fastapi import FastAPI
from pickle5 import pickle
import re

from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier,AdaBoostClassifier
import sklearn

print(sklearn.__version__)
with open("files/rf_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("files/tfidf.pkl", "rb") as f:
    vectorizer = pickle.load(f)

def preprocess(txt):
    txt=txt.replace("/"," ")
    txt=re.sub("[0-9]","",txt)
    # txt=re.sub("^[a-zA-Z]X+","",txt)

    txt=" ".join([re.sub("^[a-zA-Z]X+","",w)for w in txt.split()])

    txt=re.sub("\s+"," ",txt)
    txt=re.sub("[^a-zA-Z0-9\s]","",txt)

    return txt

label_dict={
    0:"Food",
    1:"Medical",
    2:"Shopping",
    3:"Subscription",
    4:"Travel",
}

def recommend_tags(transaction):
    out={}
    transaction=preprocess(transaction)
    transaction_features = vectorizer.transform([transaction])
    probs = model.predict_proba(transaction_features)[0]
    predicted_tags={i:p for i,p in enumerate(probs)}
    predicted_tags=sorted(predicted_tags.items(),key= lambda x: x[1] , reverse=True)
    # recommended_tags = label_encoder.inverse_transform(predicted_tags)
    for k,v in predicted_tags[:3]:
      print(label_dict[k],v)
      out[label_dict[k]]=v
    return out
# Example usage:
transaction = "POS XXXXXXXXXXXX1111 DECATHLON SPORTS"
recommended_tags = recommend_tags(transaction)


app = FastAPI()

@app.get("/recommend_tags")
def get_recommend_tags(transaction:str):
    return recommend_tags(transaction)

