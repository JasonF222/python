from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']



    @classmethod
    def save(cls,data):
        query = "INSERT INTO dojos ( name, created_at, updated_at ) VALUES ( %(name)s, NOW(), NOW() );"
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        dojos_from_db =  connectToMySQL('dojos_and_ninjas').query_db(query)
        dojos =[]
        for d in dojos_from_db:
            dojos.append(cls(d))
        return dojos

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM dojos WHERE dojos.id = %(id)s;"
        dojos_from_db = connectToMySQL('dojos_and_ninjas').query_db(query,data)

        return cls(dojos_from_db[0])

