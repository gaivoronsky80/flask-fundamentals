from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

# @app.route('/')          # The "@" decorator associates this route with the function immediately following
# def hello_world():
#     return 'Hello World!'  # Return the string 'Hello World!' as a response

# @app.route('/dojo')          
# def dojo():
#     return 'Dojo!'   

# @app.route('/say/<name>') 
# def hi(name):
#     print(name)
#     return "Hi, " + name + "!"

# @app.route('/repeat/<num>/<name>')
# def repeat(num, name):
# 	return f'{name}\n' * int(num)

# @app.route('/say/<name>') 
# def hi(name):
# 	if type(name) != str:
# 		return False
# 	else:
# 		print(name)
# 		return "Hi, " + name + "!"

# @app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
# def show_user_profile(username, id):
#     print(username)
#     print(id)
#     return "username: " + username + ", id: " + id

# @app.route('/')
# def hello_world():
# 	return render_template('index.html')


# @app.route('/<phrase>/<times>')
# def hello_person(phrase, times):
# 	return render_template("name.html", phrase=phrase, times=int(times))

@app.route('/play')
def playground_1():
	return render_template('playground.html')

@app.route('/play/<times>')
def playground_1(times):
	return render_template('playground.html', times=int(times))

@app.route('/play/<times>/<color>')
def playground_1(times, color):
	return render_template('playground.html', times=int(times), color=color)

# @app.route('/checkerboard/<times_row>/<times_col>/<color1>/<color2>')
# def playground_1(times_row, times_col, color1, color2):
# 	return render_template('checkerboard.html', times_row=int(times_row), times_col=int(times_col), color1=color1, color2=color2)

# @app.route('/lists')
# def render_lists():
	
# 	students_info = [
# 		{'name' : 'Michael', 'age' : 35},
# 		{'name' : 'John', 'age' : 30},
# 		{'name' : 'Mark', 'age' : 25},
# 		{'name' : 'KB', 'age' : 27}
# 	]
# 	return render_template("lists.html", random_numbers = [3,1,5], students = students_info)

# @app.route('/')
# def render_html_table():
	
# 	users_info = [
# 		{'first_name' : 'Michael', 'last_name' : 'Choi'},
# 		{'first_name' : 'John', 'last_name' : 'Supsupin'},
# 		{'first_name' : 'Mark', 'last_name' : 'Guillen'}
# 	]
# 	return render_template("html_table.html", users = users_info)












# app.run(debug=True) should be the very last statement! 

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.