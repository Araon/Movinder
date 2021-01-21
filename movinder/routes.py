from movinder import app
from flask import render_template, url_for, redirect
import random
import csv

def getMovie():
    with open('movinder\MovieGenre.csv','rt',newline='',errors='ignore') as f:
        data_list = list(csv.reader(f))
        n = random.randrange(40000)
        movie = {'title': data_list[n+1][2],
                'genre':data_list[n+1][4],
                'poster': data_list[n+1][5],
                'link': data_list[n+1][1]}

        return movie

@app.route("/")
def home():

    data = getMovie()
    movie_title = data['title']
    movie_cover = data['poster']
    movie_genre = data['genre']
    movie_link = data['link']

    return render_template("index.html" ,movie_title = movie_title,movie_cover = movie_cover, movie_genre = movie_genre, movie_link = movie_link)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/addtolist", methods = ['GET', 'POST'])
def addtolist():

    f = open("likedList.txt", "a")
    f.write(getMovie()['title'])
    f.write("\n")
    f.close()
        
    return redirect('/')
    

