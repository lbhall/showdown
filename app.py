from flask import Flask, request
import json

app = Flask("showdown")

tourneys = []

@app.route('/tourneys')
def get_tourneys():
    return json.dumps(tourneys, indent=2)

@app.route('/tourneys', methods=['POST'])
def add_tourney():
    tourney = request.json
    tourneys.append(tourney)
    return json.dumps(tourney, indent=2)