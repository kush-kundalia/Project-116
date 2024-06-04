# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Kush" # write your name
    age = "16" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def father ():

    name="Kartik Kundalia"
    age="42"

    return render_template('father.html', name=name, age=age)

@app.route("/mother")
def mother ():

    name="Kesha Kundalia"
    age="40"

    return render_template('mother.html', name=name, age=age)

@app.route("/friend")
def friend ():

    name="Sidharth Parmar"
    age="16"

    return render_template('friend.html', name=name, age=age)




# define the route to mother webpage


# define the route to friends webpage


# add other routes, if you want




# run the file

app.run(debug=True)
