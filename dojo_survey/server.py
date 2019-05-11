from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'keep it secret, keep it safe'

@app.route("/")
def index():
	return render_template("dojo_survey_index.html")

@app.route("/process", methods=["POST"])
def process_form():
	print("*"*50)
	print(request.form)
	print(f"adding user {request.form['username']} to the database")
	session['username'] = request.form['username']
	session['location'] = request.form['location']
	session['language'] = request.form['language']
	session['comment'] = request.form['comment']
	print(f"username submitted: {request.form['username']}")
	print(f"location submitted: {request.form['location']}")
	print(f"language submitted: {request.form['language']}")
	print(f"comment submitted: {request.form['comment']}")
	return redirect('/success')


@app.route("/success")
def success():
	print(request.form)
	return render_template("info.html")








# app.run(debug=True) should be the very last statement! 

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.