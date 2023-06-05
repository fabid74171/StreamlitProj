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
 movie_titles = soup.find_all('td', class_='titleColumn')

    # Display the extracted movie titles in Streamlit

    for title in movie_titles:
        movie_name = title.a.text
        st.write(movie_name)
