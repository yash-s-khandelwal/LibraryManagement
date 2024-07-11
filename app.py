from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy

#creating app
app=Flask(__name__)

#connecting our app to sqlite database
#this command will tell ourr program to connect with a sqlite database named taskmanager.db 
app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///records.db'

#creating an object of sqlalchemy, parameter tells which flask app to connect to
database= SQLAlchemy(app) 

class Book(database.Model):
    BookNo=database.Column(database.String(10), primary_key=True)

    BookName=database.Column(database.String(100), nullable=False)

    BookAuthor= database.Column(database.String(100), nullable=False)

    BookGenre=database.Column(database.String(100), nullable=False)




@app.route('/')
def index():
    return render_template("index.html",)


@app.route('/contact')
def contact():
    return render_template('contact.html')



@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/addBook")
def addBook():
    return render_template("addBook.html")

@app.route("/records")
def records():
    return render_template("records.html")


@app.route("/add", methods=['GET','POST'])
def add():
    if request.method=="POST":
        bookNo=request.form.get("BookNo")
        bookName=request.form.get("BookName")
        bookAuthor=request.form.get("BookAuthor")
        bookGenre=request.form.get("BookGenre")

        bookRecord = Book(BookNo=bookNo,BookName=bookName,BookAuthor=bookAuthor,BookGenre=bookGenre)

        database.session.add(bookRecord)
        database.session.commit()

        return redirect("/")







if __name__=="__main__":
    app.run(debug=True) #running app