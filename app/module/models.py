from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# class Division(db.Model):
#     divisionId = db.Column(db.Integer, primary_key=True)
#     divisionName = db.Column(db.String(45))
#     technical = db.Column(db.Boolean)
#     divisionCode = db.Column(db.String(50))

#     def __init__(self, divisionName, technical, code):
#         self.divisionName = divisionName
#         self.divisionCode = code
#         self.technical = technical

#     def __repr__(self):
#         return "<Division Id: {}, DivisionName: {}, Technical: {}, DivisionCode: {}>".format(self.divisionId, self.divisionName, self.technical, self.divisionCode)


# Employee Favourites form
class Favorites(db.Model):
    employeeId = db.Column(db.Integer, primary_key=True)
    employeeFirstName = db.Column(db.String(45))
    employeeLastName = db.Column(db.String(45))
    color = db.Column(db.String(45))
    candy = db.Column(db.String(45))
    sportsTeam = db.Column(db.String(45))
    snack = db.Column(db.String(45))
    movie = db.Column(db.String(45))
    place = db.Column(db.String(45))
    food = db.Column(db.String(45))
    soda = db.Column(db.String(45))
    animal = db.Column(db.String(45))
    holiday = db.Column(db.String(45))
    season = db.Column(db.String(45))

    def __init__(self,firstname,lastname,color,candy,sportsteam,snack,movie,place,food,soda,animal,holiday,season):
        self.employeeFirstName = firstname
        self.employeeLastName = lastname
        self.color = color
        self.candy = candy
        self.sportsTeam = sportsteam
        self.snack = snack
        self.movie = movie
        self.place = place
        self.food = food
        self.soda = soda
        self.animal = animal
        self.holiday = holiday
        self.season = season

    def __repr__(self):
        return "<Employee ID: {}, First Name: {}, Last Name: {}, Color: {}, Candy: {}, Sports Team: {}, Snack: {}, Movie: {}, Place: {}, Food: {}, Soda: {}, Animal: {}, Holiday: {}, Season: {}>".format(self.employeeId, self.employeeFirstName, self.employeeLastName, self.color, self.candy, self.sportsTeam, self.snack, self.movie, self.place, self.food, self.soda, self.animal, self.holiday, self.season)
    

# Employee Satisfactory form
class Satisfaction(db.Model):
    employeeId = db.Column(db.Integer, primary_key=True)
    employeeFirstName = db.Column(db.String(45))
    employeeLastName = db.Column(db.String(45))
    department = db.Column(db.String(45))
    title = db.Column(db.String(45))
    date = db.Column(db.String(20))
    satisfacLevel = db.Column(db.Integer)
    valueFeel = db.Column(db.String(10))
    resource = db.Column(db.String(10))
    stress = db.Column(db.String(10))

    def __init__(self, firstName,lastName,dept,title,date,satisLevel,valueFeel,resource,stress):
        self.employeeFirstName = firstName
        self.employeeLastName = lastName
        self.department = dept
        self.title = title
        self.date = date
        self.satisfacLevel = satisLevel
        self.valueFeel = valueFeel
        self.resource = resource
        self.stress = stress

    def __repr__(self):
        return "<Employee ID: {}, First Name: {}, Last Name: {}, Department: {}, Title: {}, Date: {}, Satisfaction Level: {}, Feeling valued: {}, Resource: {}, Stress: {}>".format(self.employeeId, self.employeeFirstName, self.employeeLastName, self.department, self.title, self.date, self.satisfacLevel, self.valueFeel, self.resource, self.stress)
    
class Remote(db.Model):
    employeeId = db.Column(db.Integer, primary_key=True)
    employeeFirstName = db.Column(db.String(45))
    employeeLastName = db.Column(db.String(45))
    department = db.Column(db.String(45))
    remoteDuration = db.Column(db.String(20))
    remoteExp = db.Column(db.Integer)
    haveOffice = db.Column(db.Boolean)
    positiveEffect = db.Column(db.String(45))
    preferOffice = db.Column(db.String(45))
    recommendRemote = db.Column(db.String(45))
    avgHours = db.Column(db.Integer)
    tiredRate = db.Column(db.Integer)
    happiness = db.Column(db.String(45))
    productivity = db.Column(db.String(45))
    concern = db.Column(db.String(45))
    internetSpeed = db.Column(db.String(45))
    teamConnection = db.Column(db.String(45))
    workArea = db.Column(db.String(45))
    improveProductivity = db.Column(db.String(45))
    comments = db.Column(db.String(100))

    def __init__(self, firstName,lastName,department,duration,experience,office,effect,preferOffice,recommendRemote,avgHours,tiredRate,happiness,productivity,concern,internetSpeed,teamConnection,workArea,improveProductivity,comments):
        self.employeeFirstName = firstName
        self.employeeLastName = lastName
        self.department = department
        self.remoteDuration = duration
        self.remoteExp = experience
        self.haveOffice = office
        self.positiveEffect = effect
        self.preferOffice = preferOffice
        self.recommendRemote = recommendRemote
        self.avgHours = avgHours
        self.tiredRate = tiredRate
        self.happiness = happiness
        self.productivity = productivity
        self.concern = concern
        self.internetSpeed = internetSpeed
        self.teamConnection = teamConnection
        self.workArea = workArea
        self.improveProductivity = improveProductivity
        self.comments = comments

    def __repr__(self):
        return "<Employee ID: {}, First Name: {}, Last Name: {}, Duration: {}, Remote Experience: {}, Have Office: {}, Positive Effect: {}, Prefer Office: {}, Recommend Office: {}, Avg Work Hours: {}, Tired Rate: {}, Happiness: {}, Productivity: {}, Concern: {}, Internet Speed: {}, Team Connection: {}, Work Area: {}, Improve Productivity: {}, Comments: {}>".format(self.employeeFirstName, self.remoteDuration, self.remoteExp, self.haveOffice, self.positiveEffect, self.preferOfffice, self.recommendRemote, self.avgHours, self.tiredRate, self.happiness, self.productivity, self.concern, self.internetSpeed, self.teamConnection, self.workArea, self.improveProductivity, self.comments)

