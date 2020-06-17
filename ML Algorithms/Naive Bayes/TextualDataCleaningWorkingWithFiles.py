import sys
from cleaningText import getCleanText

def getStemmedDocument(inputFile,outputFile):
    out=open(outputFile,'w',encoding="utf8")
    with open(inputFile,encoding="utf8") as f:
        reviews=f.readlines()
        
    for review in reviews:
        cleaned_review=getCleanText(review)
        print(cleaned_review,file=out)
    
    out.close()
    
#Read Command Line Arguments
inputFile=sys.argv[1]
outputFile=sys.argv[2]
getStemmedDocument(inputFile,outputFile)
        
              