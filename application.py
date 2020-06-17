from flask import Flask, abort, request, jsonify
from flair.models import TextClassifier
from flair.data import Sentence
from flask import render_template

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def sentimentAnalysis():

  # if the document is submitted
  if request.method=='POST':

    #this pre-fitted model is based on IMDB dataset
  	classifier = TextClassifier.load('en-sentiment')

    #variable to store the input query ('document') by the user 
  	inputQuery = request.form['query']

    #Sentence is a list of tokens, here, the input 
  	sentence = Sentence(inputQuery)

    #calling the .predict function on the sentence 
  	classifier.predict(sentence)
  	print('Sentiment: ', sentence.labels)
  	label = sentence.labels[0]
  	labscore = (label.score)*100
  	response = {'result': label.value, 'score': "%.2f" % labscore}

  	return jsonify(response)
  else:
    return render_template('index.html')