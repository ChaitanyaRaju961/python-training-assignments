#!/usr/bin/env python
# coding: utf-8

# In[3]:


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def calculate_cosine_similarity(string1, string2):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([string1, string2])
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return similarity[0][0]
string1 = "Natural Language Processing is amazing."
string2 = "I love learning about Natural Language Processing."
similarity_score = calculate_cosine_similarity(string1, string2)
print(f"Cosine Similarity: {similarity_score:.4f}")


# In[ ]:




