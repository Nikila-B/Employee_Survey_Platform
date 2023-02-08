from app import ma


# class DivisionSchema(ma.Schema):
#     class Meta:
#         fields = ('divisionId', 'divisionName', 'technical', 'divisionCode')

# division_schema = DivisionSchema()
# divisions_schema = DivisionSchema(many=True)

class FavoritesSchema(ma.Schema):
    class Meta:
        fields = ('employeeId','employeeFirstName','employeeLastName','color','candy','sportsteam','snack','movie','place','food','soda','animal','holiday','season')

favorite_schema = FavoritesSchema()
favorites_schema = FavoritesSchema(many=True)

class SatisfactionSchema(ma.Schema):
    class Meta:
        fields = ('employeeId', 'employeeFirstName', 'employeeLastName', 'department', 'title', 'date', 'satisfacLevel', 'valueFeel', 'resource', 'stress')

satisfaction_schema = SatisfactionSchema()
satisfactions_schema = SatisfactionSchema(many=True)

class RemoteSchema(ma.Schema):
    class Meta:
        fields = ('employeeId', 'employeeFirstName', 'employeeLastName', 'department', 'remoteduration', 'remoteExp', 'haveOffice', 'positiveEffect', 'preferOffice', 'recommendRemote', 'avgHours', 'tiredRate', 'happiness', 'productivity', 'concern', 'InternetSpeed', 'teamConnect', 'workArea', 'improveProductivity', 'comments')

remote_schema = RemoteSchema()
remotes_schema = RemoteSchema(many=True)