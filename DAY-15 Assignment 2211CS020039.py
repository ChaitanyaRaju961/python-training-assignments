#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re

def extract_emails(text):
    """
    Extracts all email addresses from the given string using regular expressions.
    
    Parameters:
        text (str): The input string.
    
    Returns:
        list: A list of extracted email addresses.
    """
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)
    return emails
test_string = 'Contact us at support@example.com and sales@example.org.'
extracted_emails = extract_emails(test_string)
print(extracted_emails)


# In[ ]:




