from app import app
from .models import *
from .schema import *
from .const import *
from flask import request, jsonify, make_response, Response
import json

@app.route("/", methods=['GET'])
def hello():
    return "Employee Survey Platform!"


@app.route("/favorites/add", methods=['POST'])
def addFavorites():
    firstName = request.json.get('firstName')
    lastName = request.json.get('lastName')
    color = request.json.get('color')
    candy = request.json.get('candy')
    sportsTeam = request.json.get('sportsTeam')
    snack = request.json.get('snack')
    movie = request.json.get('movie')
    place = request.json.get('place')
    food = request.json.get('food')
    soda = request.json.get('soda')
    animal = request.json.get('animal')
    holiday = request.json.get('holiday')
    season = request.json.get('season')
    favorites = Favorites(firstName, lastName, color, candy, sportsTeam, snack, movie, place, food, soda, animal, holiday, season)
    print(favorites)
    db.session.add(favorites)
    db.session.commit()
    return make_response(favorite_schema.jsonify(favorites),
                         HttpStatus.CREATED)

@app.route("/favorites/get", methods=['GET'])
def getFavorites() -> list:
    records = Favorites.query.all()
    result = favorites_schema.dump(records)
    return make_response(jsonify(result),
                         HttpStatus.OK)

@app.route("/satisfaction/add", methods=["POST"])
def addSaticfaction():
    firstName = request.json.get('firstName')
    lastName = request.json.get('lastName')
    department = request.json.get('department')
    title = request.json.get('title')
    date = request.json.get('date')
    satisfacLevel = request.json.get('satisfacLevel')
    valueFeel = request.json.get('valueFeel')
    resource = request.json.get('resource')
    stress = request.json.get('stress')
    satisfaction = Satisfaction(firstName, lastName, department, title, date, satisfacLevel, valueFeel, resource, stress)
    db.session.add(satisfaction)
    db.session.commit()
    return make_response(satisfaction_schema.jsonify(satisfaction),
                         HttpStatus.CREATED)

@app.route("/satisfaction/get", methods=['GET'])
def getSatisfaction() -> list:
    records = Satisfaction.query.all()
    result = satisfactions_schema.dump(records)
    return make_response(jsonify(result),
                         HttpStatus.OK)

@app.route("/remote/add", methods=["POST"])
def addRTemote():
    firstName = request.json.get('firstName')
    lastName = request.json.get('lastName')
    department = request.json.get('department')
    duration = request.json.get('duration')
    experience = request.json.get('experience')
    office = request.json.get('office')
    effect = request.json.get('effect')
    preferOffice = request.json.get('preferOffice')
    recommendRemote = request.json.get('recommendRemote')
    avgHours = request.json.get('avgHours')
    tiredRate = request.json.get('tiredRate')
    happiness = request.json.get('happiness')
    productivity = request.json.get('productivity')
    concern = request.json.get('concern')
    internetSpeed = request.json.get('internetSpeed')
    teamConnection = request.json.get('satisfacLevel')
    workArea = request.json.get('workArea')
    improveProductivity = request.json.get('improveProductivity')
    comments = request.json.get('comments')
    remote = Remote(firstName, lastName, department, duration, experience, office, effect, preferOffice, recommendRemote, avgHours, tiredRate, happiness, productivity, concern, internetSpeed, teamConnection, workArea, improveProductivity, comments)
    db.session.add(remote)
    db.session.commit()
    return make_response(remote_schema.jsonify(remote),
                         HttpStatus.CREATED)

@app.route("/remote/get", methods=['GET'])
def getRemote() -> list:
    records = Remote.query.all()
    result = remotes_schema.dump(records)
    return make_response(jsonify(result),
                         HttpStatus.OK)