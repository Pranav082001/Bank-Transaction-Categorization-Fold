# Bank-Transaction-Categorization-Fold

## Steps to run- 
1. Install all the dependency mentioned in requirements.txt  `pip install -r requirements.txt`
2) Run the fastapi server using  `python -m uvicorn app:app --reload`

## Approaches-
1) TfIDF+Random Forest- \
      a) Did couple of experimentation in this approach. Tried Countvectorizer for text encoding, In models experiemetned with SVM, Naives bayes, XgBoost. For all the combination got similar or average results. 

2) Bert_embedding+Random Forest- \
      a) Used bert to extract contextual information from the input text and then passed the embedding vectors throught random forest.
b) I was expecting this approach would work better. But it did not. The reason was data was very less and vocabulary was also different. Because of lack of data could not train the tokenizer which would have gained the knowledge of the keywords like POS, MPS... 

## Data-
1) The data was not sufficient for the for training as well as evaluation. So manuall generated couple of examples. \
2)  The problem in manual generaion was biasness. Not having much domain knowledge of transaction meaning, types, wording, resulted in bias which affetcted the models accuracy. So decided generated only 4-5 examples for evaluation purpose.
## Input- 
![image](https://github.com/Pranav082001/Bank-Transaction-Categorization-Fold/assets/66110778/6e50ec20-00b1-42dd-9ab3-47b9346e5369)

## Output-
![image](https://github.com/Pranav082001/Bank-Transaction-Categorization-Fold/assets/66110778/bf27828c-9638-4c45-aa2e-54db854689a0)


## Future Implementation- https://arxiv.org/pdf/2305.18430.pdf
