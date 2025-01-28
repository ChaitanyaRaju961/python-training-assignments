#!/usr/bin/env python
# coding: utf-8

# In[2]:


import spacy
nlp = spacy.load("en_core_web_sm")
sentence = "NLP is amazing and fun to learn."
doc = nlp(sentence)
print(f"{'Token':<10} {'POS':<10} {'Tag':<10}")
print("-" * 30)
for token in doc:
    print(f"{token.text:<10} {token.pos_:<10} {token.tag_:<10}")


# In[ ]:




