# pip install spacy
# python -m spacy download en_core_web_sm
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import spacy
import codecs

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load('en_core_web_sm') 

text = codecs.open('bloomberg.txt', encoding="utf-8").read() # open a document
doc = nlp(text) # process it
#doc.to_disk('/customer_feedback_627.bin') # save the processed Doc

# Process whole documents
#text = ( u'A Sinovel wind turbine is seen in Charlestown, Mass., in 2013. U.S. District Judge James Peterson on Friday ordered Sinovel to pay restitution and fines up to $59 million for stealing trade secrets. Jessica Rinaldi for The Boston Globe via Getty Images hide caption toggle caption Jessica Rinaldi for The Boston Globe via Getty Images Jessica Rinaldi for The Boston Globe via Getty Images A federal judge has ordered Chinas largest wind-turbine firm, Sinovel, to pay $59 million for stealing trade secrets from a Massachusetts-based technology company. Last January, Sinovel was found guilty of stealing trade secrets in federal criminal court in Madison, Wis. The company paid an Austria-based employee of American Superconductor Corp. to steal its source code for software that powered wind turbines. This kind of intellectual property theft has been highlighted by the Trump administration as a reason for levying 25 percent tariffs on $34 billion of Chinese goods entering the U.S., which began on Friday. China retaliated with tariffs on $34 billion worth of U.S. goods. Sinovel was the largest customer of American Superconductor Corp. And then the Chinese company suddenly began rejecting shipments of American Superconductors electronic components in 2011. The Massachusetts tech company learned that Sinovel was using a pirated version of the software it made in the wind turbines it installed. The ordeal left American Superconductor in perilous financial shape, and Wall Street analysts wrote it off as dead. The U.S. Department of Justice said that the company lost more than $1 billion in shareholder equity and 700 jobs. Earlier this week, American Superconductor announced it had agreed to settle the lawsuit against the Chinese company for $57.5 million in restitution. U.S. District Judge James Peterson said Sinovel has a year to pay the restitution and it must also pay a fine of $1.5 million. "Through Sinovels and AMSCs joint efforts, we have signed a settlement agreement to resolve the previous disputes in a constructive manner that we believe will enable us to move on with our respective businesses," said Daniel McGahn, American Superconductors president and CEO. "This closes a challenging chapter for AMSC."')

#doc = nlp(text)

# Find named entities, phrases and concepts
#for entity in doc.ents:
   # print(entity.text, entity.label_)

nprDoc = codecs.open('npr.txt', encoding="utf-8").read() # open a document
doc1 = nlp(nprDoc) # process it    

bloombergDoc = codecs.open('bloomberg.txt', encoding="utf-8").read() # open a document
doc2 = nlp(bloombergDoc) # process it

# Determine semantic similarities
#doc1 = nlp(u"A federal criminal court had in January convicted Sinovel of paying an Austria-based employee of American Superconductor Corp. to steal the source code for software that powered wind turbines. ")
#doc2 = nlp(u"Chinese turbine maker Sinovel Wind Group Co. must pay $59 million for stealing trade secrets from wind technology firm, American Superconductor Corp., a U.S. judge ruled.")
similarity = doc1.similarity(doc2)
print(doc1.text, doc2.text, similarity)
