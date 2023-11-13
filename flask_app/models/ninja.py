from flask_app.config.mysqlconnection import connectToMySQL
#books
class Ninja:
    db = 'dojos_and_ninjas_schema'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo = None

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL(cls.db).query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas
    
    @classmethod
    def create_ninja(cls, ninja_data):
        query = """
            INSERT INTO ninjas (first_name, last_name, age, dojo_id)
            VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s)
            ;"""
        return connectToMySQL(cls.db).query_db(query, ninja_data)
