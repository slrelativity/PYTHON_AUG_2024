# this model interacts with the DB
from flask_app.config.mysqlconnection import connect_to_mysql
from flask_app import DATABASE
from flask_app.models import dog_model

class Award:
    def __init__(self, data):
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.title = data['title']
        self.dog_id = data['dog_id']

    
    #  ========== CREATE ============
    @classmethod
    def create(cls, data):
        query = """
            INSERT INTO awards (title, dog_id)
            VALUES (%(title)s, %(dog_id)s);
        """
        return connect_to_mysql(DATABASE).query_db(query, data)
    
    # =========== READ ALL ===========
    # all awards and their recipient
    @classmethod
    def all_awards(cls):
        query = """
            SELECT * FROM awards
            LEFT JOIN dogs
            ON awards.dog_id = dogs.id;
        """
        results = connect_to_mysql(DATABASE).query_db(query)
        print(" \n **********************\n RESULTS ==>", results)
        this_award = cls(results[0])
        print("--------", this_award)
        # TODO....
