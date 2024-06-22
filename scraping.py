import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
from deep_translator import GoogleTranslator
from transformers import pipeline

def get_news():
   
    url = "https://www.cnbce.com/piyasalar"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    post_cards = soup.find_all('div', class_='post-card-title')

    titles = []
    for post_card in post_cards:
        a_tag = post_card.find('a')
        if a_tag:
            text = a_tag.get_text().strip()
            titles.append(text)

    translated_titles = []
    for title in titles:
        translated_title = GoogleTranslator(source='auto', target='en').translate(title)
        translated_titles.append(translated_title)
        
    df = pd.DataFrame({'Turkish': titles, 'English': translated_titles})

    sentiment_analysis = pipeline(
        'sentiment-analysis',
        model='soleimanian/financial-roberta-large-sentiment'
    )

    results = []
    for english_title in df['English']:
        result = sentiment_analysis(english_title)
        results.append(result[0])

    df['Label'] = [res['label'].title() for res in results]
    df['Score'] = [res['score'] for res in results]

    return df

def color_label(val):
    color = ''
    if val == 'Positive':
        color = 'background-color: skyblue; color: black'
    elif val == 'Negative':
        color = 'background-color: lightcoral; color: black'
    elif val == 'Neutral':
        color = 'background-color: lightgrey; color: black'
    return color
