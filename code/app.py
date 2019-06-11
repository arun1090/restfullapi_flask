import sqlite3
from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask( __name__ )
api = Api(app)



class Item(Resource):
    def get(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = 'select * from item where name = ?'
        result = cursor.execute(query,(name,))
        row = result.fetchone()
        connection.close()
        if row :
            return {'name' : row[0], 'price' : row[1]}
        else:
            return {'messege' : 'item not found'} ,404

    
    def post(self, name):
        
        parser = reqparse.RequestParser()
        parser.add_argument = ('name')
        parser.add_argument = ('price')  
        data = parser.parse_args()
        
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = 'Insert into item vaues(?, ?)'
        cursor.execute(query,(data['name'], data['price']))
        connection.commit()
        connection.close()
        return {'message' : 'user created'} ,200

    def delete(self, name):
        pass
    def put(self, name):
        pass
#class Itemlist(Resource):
#    def get(self):
#       pass



api.add_resource(Item, '/item/<string:name>')

app.run(port=500,debug = True)
