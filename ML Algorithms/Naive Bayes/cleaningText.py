from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords 

def getCleanText(text):
    text=text.lower()
    text=text.replace("<br/><br/>"," ")
    
    #Init objects
    tokenizer=RegexpTokenizer(r'\w+')
    en_stopwords=set(stopwords.words('english'))
    ps=PorterStemmer()
    
    #Tokenize
    tokens=tokenizer.tokenize(text)
    new_tokens=[token for token in tokens if token not in en_stopwords]
    stemmed_tokens=[ps.stem(token) for token in new_tokens]
    cleaned_text=' '.join(stemmed_tokens)
    return cleaned_text