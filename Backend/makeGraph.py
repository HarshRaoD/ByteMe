from wordcloud import WordCloud, get_single_color_func
import matplotlib.pyplot as plt
import random
import base64
import io
from flask import Flask, jsonify, make_response

# Define a function to generate random colors
def _random_color_func(word=None, font_size=None, position=None, orientation=None, font_path=None, random_state=None):
    h = int(random.uniform(0, 360))
    s = int(random.uniform(60, 100))
    l = int(random.uniform(30, 70))
    return "hsl({}, {}%, {}%)".format(h, s, l)

def make_wordcloud(words:list, weights: list):
    # Convert the lists to a dictionary
    word_weights = dict(zip(words, weights))

    # Generate the word cloud with custom colors
    wordcloud = WordCloud(width=400, height=400, background_color='white', color_func=_random_color_func)
    wordcloud.generate_from_frequencies(word_weights)

    # Display the word cloud
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.tight_layout(pad=0)

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img_str = base64.b64encode(buf.read()).decode('utf-8')

    # include the image in the response as a JSON object
    response = {
        'message': 'Success',
        'image': img_str
    }
    return make_response(jsonify(response), 200)