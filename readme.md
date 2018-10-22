This python script uses SpaCy - https://github.com/explosion/spaCy

Here's what it does:

1. Takes a website url, strips it of it's html tags, gives plain text
2. Takes a pdf and converts it to plain text
3. Parses keywords from the website and/or pdf
4. Can take 2 articles/text and gives a similarity score. Uses SpaCy's NLP to process each article using vector objects. Great for flaggin duplicates.

Future developments:

Web version
Smart keywords & machine learning on those keywords.
Add a summarizer option

**************************************************************************

To run the program from the command line with python2:

1. git clone git@github.com:aj-medianet/content-aggregator.git
2. cd content-aggregator/
3. source venv/bin/activate

Intall python libraries - you must already have pip installed:

4. pip install bs4
5. pip install spacy
6. pip install PyPDF2
7. python -m spacy download en

Then run the program:
8. python main.py

To get out of the virtual envirnment run:
9. deactivate 
