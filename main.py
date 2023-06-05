import requests
from bs4 import BeautifulSoup
import streamlit as st

def scrape_movie_titles(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    movie_titles = []
    movie_elements = soup.select('.lister-item-header > a')
    
    for element in movie_elements:
        movie_titles.append(element.text)
    
    return movie_titles

# Streamlit web app
st.title("IMDb Movie Title Scraper")

# Input IMDb URL
url = st.text_input("Enter IMDb URL:", "https://www.imdb.com/chart/top")

# Scrape movie titles
if st.button("Scrape"):
    titles = scrape_movie_titles(url)
    
    # Display scraped movie titles
    if titles:
        st.header("Movie Titles")
        for title in titles:
            st.write(title)
    else:
        st.write("No movie titles found.")
