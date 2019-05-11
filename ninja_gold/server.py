from flask import Flask, render_template, request, redirect, session, Markup
import random
import datetime

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

your_gold = 0
gold_num = 0
info = []
steps = 11

@app.route("/")
def logIn():
	return render_template("index.html")

@app.route("/process", methods=["POST"])
def process_form():
	print("*"*50)
	print(request.form)
	print(f"adding user {request.form['username']} to the database")
	session['username'] = request.form['username']
	session['useremail'] = request.form['email']
	print(f"username submitted: {request.form['username']}")
	print(f"email submitted: {request.form['email']}")
	return redirect("/process_money")

@app.route("/process_money")
def random_boxes():
	session['location_1'] = 'FARM'
	session['location_2'] = 'CAVE'
	session['location_3'] = 'HOUSE'
	session['location_4'] = 'CASINO'

	if session['steps'] == 1:
		return redirect('/your_score')

	num = random.randrange(1,5)
	if num == 1:
		num  = '1px 1px 10px black'
		session['steps'] -= 1
		return render_template("main.html", num1 = num,
		username=session['username'], action_cave='disabled=""',
		action_house='disabled=""', action_casino='disabled=""',
		color1='orange', text_color1='white', border_farm='none',
		activities=session['info'])

	if num == 2:
		num  = '1px 1px 10px black'
		session['steps'] -= 1
		return render_template("main.html", num2 = num,
		username=session['username'], action_farm='disabled=""',
		action_house='disabled=""', action_casino='disabled=""',
		color2='orange', text_color2='white', border_cave='none',
		activities=session['info'])

	if num == 3:
		num  = '1px 1px 10px black'
		session['steps'] -= 1
		return render_template("main.html", num3 = num,
		username=session['username'], action_farm='disabled=""',
		action_cave='disabled=""', action_casino='disabled=""',
		color3='orange', text_color3='white', border_house='none',
		activities=session['info'])

	if num == 4:
		num  = '1px 1px 10px black'
		session['steps'] -= 1
		return render_template("main.html", num4 = num,
		username=session['username'], action_farm='disabled=""',
		action_cave='disabled=""', action_house='disabled=""',
		color4='orange', text_color4='white', border_casino='none',
		activities=session['info'])

@app.route("/add_gold", methods=['POST'])
def add_gold():
	hiddenInput = request.form['building']
	if hiddenInput == 'Farm':
		session['gold_num'] = random.randrange(10,21)
		session['your_gold'] += session['gold_num']
		now = datetime.datetime.now()
		session['info'].append('Earned ' + str(session['gold_num']) + 
		' golds from the ' + str(session['location_1']) + '! ' + '(' + 
		str(now) + ')')
		return redirect("/process_money")

	if hiddenInput == 'Cave':
		session['gold_num'] = random.randrange(5,11)
		session['your_gold'] += session['gold_num']
		now = datetime.datetime.now()
		session['info'].append('Earned ' + str(session['gold_num']) + 
		' golds from the ' + str(session['location_2']) + '! ' + 
		'(' + str(now) + ')')
		return redirect("/process_money")

	if hiddenInput == 'House':
		session['gold_num'] = random.randrange(2,6)
		session['your_gold'] += session['gold_num']
		now = datetime.datetime.now()
		session['info'].append('Earned ' + str(session['gold_num']) + 
		' golds from the ' + str(session['location_3']) + '! ' + 
		'(' + str(now) + ')')
		return redirect("/process_money")

	if hiddenInput == 'Casino':
		plus_or_minus = random.randrange(0,2)
		if plus_or_minus == 1:
			session['gold_num'] = random.randrange(0,51)
			session['your_gold'] += session['gold_num']
			now = datetime.datetime.now()
			session['info'].append('Earned ' + str(session['gold_num']) + 
			' golds from the ' + str(session['location_4']) + '! ' + 
			'(' + str(now) + ')')
			return redirect("/process_money")
		else:
			session['gold_num'] = random.randrange(0,51)
			session['your_gold'] -= session['gold_num']
			now = datetime.datetime.now()
			session['info'].append('Lost ' + str(session['gold_num']) + 
			' golds from the ' + str(session['location_4']) + '! ' + 
			'(' + str(now) + ')')
			return redirect("/process_money")

@app.route('/your_score')
def your_score():
	if session['your_gold'] > 0:
		session['text_reset'] = Markup('Congratulation!</br><span class="flat">You have </span><span class="flat_color">' + 
			str(session['your_gold']) + '</span><span class="flat"> golds!</span>')
	else:
		session['text_reset'] = Markup('Unfortunately!</br><span class="flat">You hane </span><span class="flat_color">' + 
			str(session['your_gold']) + '</span><span class="flat"> golds!</br>Try again!</span>')
	return render_template("reset.html")

@app.route('/play_again', methods=['POST'])
def play_again():
	session['your_gold'] = 0
	session['steps'] = 11
	session['info'] = []
	return redirect('/process_money')

@app.route('/reset', methods=['POST'])
def reset():
	session.pop('username')
	session.pop('useremail')
	session['your_gold'] = 0
	session['steps'] = 11
	session['info'] = []
	return redirect('/')

if __name__=="__main__":
    app.run(debug=True)