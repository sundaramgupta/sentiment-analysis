from flask import Flask, abort, request, jsonify, json
from flair.models import TextClassifier
from flair.data import Sentence
from flask import render_template

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def sentimentAnalysis():
  if request.method == 'POST':
    req_data = request.get_json(force=True)
    messages = req_data['messages']
    final = ' '.join(messages)
    classifier = TextClassifier.load('en-sentiment')
    sentence = Sentence(final)
    classifier.predict(sentence)
    print('Sentiment: ', sentence.labels)
    label = sentence.labels[0]
    labscore = (label.score)*100
    response = {'sentiment': label.value, 'score': "%.2f" % labscore}
    return jsonify(response)
  else:
    return render_template('index.html')
