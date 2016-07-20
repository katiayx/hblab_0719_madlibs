from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']



@app.route('/')
def say_hello():
    """Save hello to user."""

    player = request.args.get("person")
    yesno = request.args.get("yesno")

    return render_template("base.html",
                            person=player,
                            yesno=yesno)

@app.route('/game')
def yes_or_no():

    yesno = request.args.get("yesno")
    
    if yesno == "yes":
        return render_template("game.html")
    else:
        return render_template("goodbye.html")


# @app.route('/game')
# def play_game(): 
#     if yesno == "Yes": 
#         return render_template("base.html")


# @app.route('/goodbye')
# def goodbye(): 
#     # if yesno == "No": 
#         return render_template("base.html")



@app.route('/madlib')
def show_madlib_form():
    """Ask user whether they want to play the game"""

    name = request.args.get("name")
    color = request.args.get("color")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")

    return render_template("madlib.html", 
                            name=name,
                            color=color,
                            noun=noun,
                            adjective=adjective,
                            )


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
