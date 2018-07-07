# pip install spacy
# python -m spacy download en_core_web_sm
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from urllib2 import Request, urlopen
from StringIO import StringIO

import spacy
import codecs
import PyPDF2 

#pypdf2 stuff
url = 'http://www.pdf995.com/samples/pdf.pdf' 
remoteFile = urlopen(Request(url)).read()
memoryFile = StringIO(remoteFile)
pdfFile = PyPDF2.PdfFileReader(memoryFile)

#open allows you to read the file
#pdfFileObj = open(pdfFile,'rb')

#The pdfReader variable is a readable object that will be parsed
#pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

#discerning the number of pages will allow us to parse through all #the pages
num_pages = pdfFile.numPages
count = 0
text = ""
#The while loop will read each page
while count < num_pages:
    pageObj = pdfFile.getPage(count)
    count +=1
    text += pageObj.extractText()

#check pdf is turned to string
print('PDF String: \n'text)

#spacy stuff

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load('en_core_web_sm') 

#text = codecs.open('bloomberg.txt', encoding="utf-8").read() # open a document
#doc = nlp(text) # process it
#doc.to_disk('/customer_feedback_627.bin') # save the processed Doc

# Process the text 
doc = nlp(text)

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)

nprDoc = codecs.open('npr.txt', encoding="utf-8").read() # open a document
doc1 = nlp(nprDoc) # process it    

bloombergDoc = codecs.open('bloomberg.txt', encoding="utf-8").read() # open a document
doc2 = nlp(bloombergDoc) # process it

# Determine semantic similarities
#doc1 = nlp(u"A federal criminal court had in January convicted Sinovel of paying an Austria-based employee of American Superconductor Corp. to steal the source code for software that powered wind turbines. ")
#doc2 = nlp(u"Chinese turbine maker Sinovel Wind Group Co. must pay $59 million for stealing trade secrets from wind technology firm, American Superconductor Corp., a U.S. judge ruled.")
similarity = doc1.similarity(doc2)
#print(doc1.text, doc2.text, similarity)
