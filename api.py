from flask import Flask, request, Response, jsonify
from mongoConnection import *
from bson import json_util, ObjectId
from checking import check_params
from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId
from bson import json_util


app = Flask("harrypotterapi")

# Endpoints

#Bienvenid@ a la API!

@app.route("/welcome") #FUNCIONA!
def welcome():
    return "Welcome to the magical world of Harry Potter"

# Mostrar todos los quotes;

@app.route("/phrase") #FUNCIONA!
def list_phrases():
    qts = get_quotes()
    return jsonify(qts)

# Mostrar un quote;

@app.route("/phrase/<phrase>") #FUNCIONA!
def list_one_phrase(phrase):
    qo = get_one_quote(phrase)
    return jsonify(qo)   

# Mostrar todos los persoanajes;    

@app.route("/characters") #FUNCIONA!
def list_characters():
    ch = get_characters()
    return jsonify(ch)

# Mostrar un persoanaje;   

@app.route("/characters/<character>") #FUNCIONA!
def list_one_char(character):
    co = get_one_char(character)
    return jsonify(co)  

# Mostrar todas las peliculas;  

@app.route("/movies") #FUNCIONA!
def list_movies():
    mv = get_movies()
    return jsonify(mv)

# Mostrar una pelicula; 

@app.route("/movies/<movie>") #FUNCIONA!
def list_one_movie(movie):
    mo = get_one_movie(movie)
    return jsonify(mo)

# Insertar un quote;

@app.route("/add/new_quote/<Characters>/<Phrase>/<Movie>/<Year>") #FUNCIONA!
def add_new_quote(Characters, Phrase, Movie, Year):
    params_obl = [Characters, Phrase, Movie, Year]
    if len(params) == 4:
        insert_quote(Characters, Phrase, Movie, Year)
        return "The new quote has been added correctly"
    else: 
        return "Please insert the correct parameters to add a new quote"
        #el return no me funciona!!

# Insertar un personaje;

@app.route("/add/new_char/<Characters>/<Role>/<Actorname>") 
def add_new_char(Characters, Role, Actorname):
    params = [Characters, Role, Actorname]
    if len(params) == 3:
        insert_char(Characters, Role, Actorname)
        return "The character has been added correctly"
    else: 
        return "Please insert the correct parameters to add a new character"
        #el return no me funciona!!

# Eliminar un quote;

@app.route("/delete_quote/<Characters>/<Phrase>/<Movie>/<Year>") 
def delete_quote(Characters, Phrase, Movie, Year):
    params_ob = [Characters, Phrase, Movie, Year]
    for param in params_ob:
        if param in params_ob:
            delete_quote(Characters, Phrase, Movie, Year)
            return "The quote has been successfully deleted"
        else:
            return "Please insert the correct parameters to delete quote"
    #el return no me funciona!!


# Eliminar un personaje;

@app.route("/delete_char/<Characters>/<Role>/<Actorname>") 
def delete_char(Characters, Role, Actorname):
    params = [Characters, Role, Actorname]
    if params in params:
        delete_char(Characters, Phrase, Movie, Year)
        return "The quote has been successfully deleted"
    else:
        return "Please insert the correct parameters to delete quote"

 #el return no me funciona!!

app.run(debug=True)