from flask import Flask, render_template, request, redirect, session
import random 
app = Flask(__name__)    
app.secret_key = 'keep it secret, keep it safe'


@app.route("/")
def index():
	session['attempts'] = 5
	return render_template("index.html")

@app.route("/process", methods=["POST"])
def submit():
	user_number = request.form['user_number']
	session['random_number'] = random.randrange(1,100)
	session['attempts'] -= 1
	

	if session['attempts'] == 0:
		return render_template("correct_answer.html", )
	else:	
		if int(user_number) > session['random_number']:
			return render_template("wrong_answer.html", too_high='too high!', user_number=user_number)

		elif int(user_number) < session['random_number']:
			return render_template("wrong_answer.html", too_low='too low!', user_number=user_number)

		elif int(user_number) == session['random_number']:
			return render_template("correct_answer.html", )


@app.route('/reset')
def play_again ():
	session.pop('random_number')
	return redirect('/')


# app.run(debug=True) should be the very last statement! 

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.