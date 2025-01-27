#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup

def fetch_webpage_title(url):
    """
    Fetches and prints the title of the webpage at the given URL.
    
    Parameters:
        url (str): The URL of the webpage.
    
    Returns:
        str: The title of the webpage.
    """
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the webpage content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the title tag
        title = soup.title.string if soup.title else "No title found"
        return title

    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

# Test the function
url = 'https://example.com'
title = fetch_webpage_title(url)
print(f"Title of the webpage: {title}")


# In[ ]:




