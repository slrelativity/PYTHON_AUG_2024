# this model file interacts with the DB
# handle all data related to the table 'dogs'
# C R U D

from mysqlconnection import connect_to_mysql

DB = "dogs_db"

#crete the model for the dog that references the dog table
class Dog:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.age = data['age']
        self.breed = data['breed']
        self.color = data['color']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    # === ALL QUERIES ARE CLASSMETHODS ===

    # ----------- READ ALL ---------------
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dogs;"
        results = connect_to_mysql(DB).query_db(query)
        print("⭐⭐⭐ results =>", results) # return a list of dict [{},{},{}] or []

        dog_instances = []
        if results:
            for row in results:
                this_dog_instance = cls(row)
                dog_instances.append(this_dog_instance)
        return dog_instances # a list of Object instances [ {}, {}]
    
    # ------------ CREATE -----------------
    @classmethod
    def create(cls, data):
        print(">> inside create method model >> DATA :", data)
        query = """
            INSERT INTO dogs (name, age, breed, color)
            VALUES (%(name)s, %(age)s, %(breed)s, %(color)s);
        """
        result = connect_to_mysql(DB).query_db(query,data)
        return result
    
    # ------------ READ ONE ----------------
    @classmethod
    def get_one(cls, id):
        data = {
            'id' : id
        }
        query = """
            SELECT * FROM dogs
            WHERE id=%(id)s;
        """
        result = connect_to_mysql(DB).query_db(query,data)
        print(" ####### RESULT:", result)
        this_one_dog_instance = cls(result[0])
        return this_one_dog_instance
    
    # -------------- UPDATE --------------
    @classmethod
    def update(cls, data):
        query = """
            UPDATE dogs 
                SET 
                    name= %(name)s,
                    age= %(age)s,
                    breed= %(breed)s,
                    color= %(color)s
                WHERE id = %(id)s;
        """
        return connect_to_mysql(DB).query_db(query,data)