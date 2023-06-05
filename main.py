import streamlit as st
import requests
from bs4 import BeautifulSoup

def main():
    st.title("Movie Title Scraper")

    # Set the URL
    url = "https://www.imdb.com/chart/top"

    # Make a GET request to the website
    response = requests.get(url)

    # Create BeautifulSoup object
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the movie titles
    movie_titles = soup.find_all('td', class_='titleColumn')

    # Display the extracted movie titles in Streamlit
    for title in movie_titles:
        movie_name = title.a.text
        st.write(movie_name)

if _name_ == '_main_':
    main()
