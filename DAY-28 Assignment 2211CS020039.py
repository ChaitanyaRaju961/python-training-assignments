#!/usr/bin/env python
# coding: utf-8

# In[2]:


import spacy
nlp = spacy.load("en_core_web_sm")
def perform_ner(text):
    doc = nlp(text)
    print(f"{'Entity':<20} {'Type':<15}")
    print("-" * 35)
    for ent in doc.ents:
        print(f"{ent.text:<20} {ent.label_:<15}")
text = "Apple is looking at buying a startup in the UK for $1 billion."
perform_ner(text)


# In[ ]:




