import sqlite3
from flask_restful import Resource, reqparse

class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        query = "SELECT * FROM users WHERE username=?"
        result = cur.execute(query, (username, ))
        row = result.fetchone()
        if row:
            user = cls(*row)   #also can use (row[0], row[1], row[2])
        else:
            user = None
        conn.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        query = "SELECT * FROM users WHERE id=?"
        result = cur.execute(query, (_id, ))
        row = result.fetchone()
        if row:
            user = cls(*row)   #also can use (row[0], row[1], row[2])
        else:
            user = None
        conn.close()
        return user

class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type = str,
        required = True,
        help = 'username cannot be left blank'
        )
    parser.add_argument('password',
        type = str,
        required = True,
        help = 'password cannot be left blank'
        )

    @jwt_required()
    def post(self):
        data = UserRegister.parser.parse_args()
        if User.find_by_username(data['username']):
            return {'message': 'The username already exists'}, 400
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        query = "INSERT INTO users VALUES (NULL, ?, ?)"
        cur.execute(query, (data['username'], data['password']))
        conn.commit()
        conn.close()
        return {'message': 'User created successfully'}, 201
