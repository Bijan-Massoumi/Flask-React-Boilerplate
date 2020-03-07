from flask_restful import Resource
from flask import render_template

class Hello(Resource):
    def get(self):
        return {"message": "Hello, World!"}


