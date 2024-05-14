# models/alumno.py

from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('mongodb+srv://barcenassaldanaalejandro:OyTnmHdbFJICKjiq@cluster0.7hxdjw5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['api_database']
collection = db['alumnos']

class Alumno:
    def __init__(self, alumno, edad, carrera, forma_del_ser):
        self.alumno = alumno
        self.edad = edad
        self.carrera = carrera
        self.forma_del_ser = forma_del_ser

    def to_dict(self):
        return {
            "alumno": self.alumno,
            "edad": self.edad,
            "carrera": self.carrera,
            "forma_del_ser": self.forma_del_ser
        }
