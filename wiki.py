from transformers import pipeline 
import wikipediaapi 
summariser = pipeline('summarization')
from flask import Flask, request, jsonify, render_template
wiki_wiki = wikipediaapi.Wikipedia('en')
# page_py = wiki_wiki.page('Uruguay')

# #print(page_py.text) 


# print("SUMMARY:")

# # print(summariser(page_py.text[0:1000], max_length=130, min_length=30))

# import requests

# S = requests.Session()

# URL = "https://en.wikipedia.org/w/api.php"

# PARAMS = {
#     "action": "query",
#     "format": "json",
#     "list": "random",
#     "rnlimit": "1"
# }

# R = S.get(url=URL, params=PARAMS)

# DATA = R.json()

# RANDOMS = DATA["query"]["random"]     

# title = RANDOMS[0]['title']

# page_py = wiki_wiki.page(title)
# print(page_py.text)
# # print(len(RANDOMS))
# # for r in RANDOMS:
# #     print(r["title"])

# #print(RANDOMS.text)


import requests

app = Flask(__name__)


#page_py = wiki_wiki.page(page["title"])
#print(page_py.text)

@app.route('/', methods=['POST', 'GET'])
def home():
    page = requests.get("https://en.wikipedia.org/api/rest_v1/page/random/summary").json()
    page_py = wiki_wiki.page(page["title"])
    summary = summariser(page_py.text[0:2000], max_length=len(page_py.text), min_length=30)
    return render_template('index.html', article_summary= 'Summary: {}'.format(summary[0]['summary_text']), article_title=page['title'])

# @app.route('/generate', methods=['POST'])

# def generate():
#     page = requests.get("https://en.wikipedia.org/api/rest_v1/page/random/summary").json()
#     page_py = wiki_wiki.page(page["title"])
#     summary = summariser(page_py.text[0:1000], max_length=len(page_py.text), min_length=30)
#     return render_template('index.html', article_summary='Summary:{}'.format(summary[0]['summary_text']))


if __name__ == '__main__':
    app.run(debug=True)