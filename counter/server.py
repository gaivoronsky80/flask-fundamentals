from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'keep it secret, keep it safe'

counter = 0

@app.route("/")
def reloads():
	global counter
	session['counter'] += 1
	return render_template("index.html", counter = session['counter'])




@app.route("/destroy_session", methods=["POST"])
def destroy_form():
	session['counter'] = 0
	return redirect("/")

@app.route("/add_2", methods=["POST"])
def counter_add_2():
	session['counter'] += 1
	return redirect("/")


# app.run(debug=True) should be the very last statement! 

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.