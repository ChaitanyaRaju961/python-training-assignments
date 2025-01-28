#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install textblob


# In[4]:


from textblob import TextBlob
def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    return sentiment, polarity
text = "TextBlob makes it very simple to perform sentiment analysis."
sentiment, polarity = analyze_sentiment(text)
print(f"Text: {text}")
print(f"Sentiment: {sentiment}")
print(f"Polarity: {polarity:.2f}")


# In[ ]:




