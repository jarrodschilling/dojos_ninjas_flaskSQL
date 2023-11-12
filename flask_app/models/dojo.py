from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja
#user

class Dojo:
    db = "dojos_and_ninjas_schema"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(cls.db).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    
    @classmethod
    def show_one_with_ninjas(cls, dojo_id):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        data = {'id': dojo_id}
        results = connectToMySQL(cls.db).query_db(query, data)
        dojo = cls(results[0])

        for row in results:
            ninja_data = {
                "id": row['ninjas.id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "age": row['age'],
                "dojo_id": row['dojo_id'],
                "created_at": row['ninjas.created_at'],
                "updated_at": row['ninjas.updated_at'],
            }
            dojo.ninjas.append(ninja.Ninja(ninja_data))
        return dojo.ninjas