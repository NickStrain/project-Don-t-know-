from transformers import pipeline
from transformers import AutoTokenizer,AutoModelForSequenceClassification

'''
This py file is to load the model and predict the value 
'''

class pre():
    def __init__(self) -> None:
        '''
        init all the args from the HF :);
        '''
        self.tokenizer = AutoTokenizer.from_pretrained("JungleLee/bert-toxic-comment-classification")
        self.model = AutoModelForSequenceClassification.from_pretrained("JungleLee/bert-toxic-comment-classification")
        self.pipe = pipeline("text-classification", model="JungleLee/bert-toxic-comment-classification")
    def pred(self,x) -> any  :
        '''
        Predict function:
        x: Input value 
        '''
        a  = self.pipe(x)

        return a


model = pre()
print(model.pred("wtf"))