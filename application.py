from flask import Flask, abort, request, jsonify, json
from flair.models import TextClassifier
from flair.data import Sentence
from flask import render_template

app = Flask(__name__)


@app.route("/json", methods=['POST', 'GET'])
def sentimentAnalysis():

  # if the document is submitted
  if request.method=='POST':

    req_data = request.get_json(force=True)
    labscore=0
    n = len(req_data['messages'])
    for i in range(n):
      message = req_data['messages'][i]

      #this pre-fitted model is based on IMDB dataset
      classifier = TextClassifier.load('en-sentiment')

      #variable to store the input query ('document') by the user
      inputQuery = message

      #Sentence is a list of tokens, here, the input
      sentence = Sentence(inputQuery)

      #calling the .predict function on the sentence
      classifier.predict(sentence)

      label = sentence.labels[0]
      labscore += ((label.score)*100)
      labscore = labscore/n
    response = {'result': label.value, 'score': "%.2f" % labscore }
    return jsonify(response)
  else:
    return render_template('index.html')

