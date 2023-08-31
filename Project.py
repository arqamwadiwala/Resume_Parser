import docx2txt
import spacy
spacy.load("en_core_web_sm")
import re
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger


#Extracting text from DOCX
def doctotext(m):
    temp = docx2txt.process(m)
    resume_text = [line.replace('\t', ' ') for line in temp.split('\n') if line]
    text = ' '.join(resume_text)
    return (text)


## Extracting text from PDF
def pdftotext(m):
    # pdf file object
    # you can find find the pdf file with complete code in below
    pdfFileObj = open(m, 'rb')

    # pdf reader object
    pdfFileReader = PdfFileReader(pdfFileObj)

    # number of pages in pdf
    num_pages = pdfFileReader.numPages

    currentPageNumber = 0
    text = ''

    # Loop in all the pdf pages.
    while(currentPageNumber < num_pages ):

        # Get the specified pdf page object.
        pdfPage = pdfFileReader.getPage(currentPageNumber)

        # Get pdf page text.
        text = text + pdfPage.extractText()

        # Process next page.
        currentPageNumber += 1
    return (text)
  
if __name__ == '__main__': 

    FilePath = 'CV.pdf'
    FilePath.lower().endswith(('.png', '.docx'))
    if FilePath.endswith('.docx'):
      textinput = doctotext(FilePath) 
    elif FilePath.endswith('.pdf'):
      textinput = pdftotext(FilePath)
    else:
      print("File not support")
import spacy
import en_core_web_sm
from spacy.matcher import Matcher

# load pre-trained model
nlp = en_core_web_sm.load()

# initialize matcher with a vocab
matcher = Matcher(nlp.vocab)


def extract_name(resume_text):
    nlp_text = nlp(resume_text)
    
    # First name and Last name are always Proper Nouns
    pattern = [{'POS': 'PROPN'}, {'POS': 'PROPN'}]
    
    matcher.add('NAME', [pattern])
    
    matches = matcher(nlp_text)
    
    for match_id, start, end in matches:
        span = nlp_text[start:end]
        return span.text
print('Name: ',extract_name(textinput))
def extract_mobile_number(resume_text):
    phone = re.findall(re.compile(r'(?:(?:\+?([1-9]|[0-9][0-9]|[0-9][0-9][0-9])\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([0-9][1-9]|[0-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?'), resume_text)
    
    if phone:
        number = ''.join(phone[0])
        if len(number) > 10:
            return number
        else:
            return number
print('Mobile Number: ',extract_mobile_number(textinput))
def extract_email_addresses(string):
    r = re.compile(r'[\w\.-]+@[\w\.-]+')
    return r.findall(string)
print('Mail id: ',extract_email_addresses(textinput))
import re
from nltk.corpus import stopwords


# Grad all general stop words
STOPWORDS = set(stopwords.words('english'))

# Education Degrees
EDUCATION = [
            'BE','B.E.', 'B.E', 'BS', 'B.S', 
            'ME', 'M.E', 'M.E.', 'M.B.A', 'MBA', 'MS', 'M.S', 
            'BTECH', 'B.TECH', 'M.TECH', 'MTECH', 
            'SSLC', 'SSC' 'HSC', 'CBSE', 'ICSE', 'X', 'XII'
        ]

def extract_education(resume_text):
    nlp_text = nlp(resume_text)

    # Sentence Tokenizer
    nlp_text = [sent.text.strip() for sent in nlp_text.sents]

    edu = {}
    # Extract education degree
    for index, text in enumerate(nlp_text):
        for tex in text.split():
            # Replace all special symbols
            tex = re.sub(r'[?|$|.|!|,]', r'', tex)
            if tex.upper() in EDUCATION and tex not in STOPWORDS:
                edu[tex] = text + nlp_text[index + 1]
                
                

    # Extract year
    education = []
    for key in edu.keys():
        year = re.search(re.compile(r'(((20|19)(\d{})))'), edu[key])
        if year:
            education.append((key, ''.join(year[0])))
        else:
            education.append(key)
    return education
print('Qualification: ',extract_education(textinput))
import pandas as pd
import spacy
nlp = spacy.load('en_core_web_sm')
doc=nlp("Python, Statistics, Data Handling, Data Visualization,Linear Algebra, Neural Networks, Transfer Learning,Feature Extraction, Deep Learning, Sci-kit Learn, Keras,OpenCV, SQLite, Html, CSS, GUI using Pyqt module, Git GitHub,C, C++, etc.")
print ("Skills:\n")
for chunk in doc.noun_chunks:       # iterate over the noun chunks in the Doc
   print(chunk.text)
