from flask import Flask, render_template, request, url_for, redirect
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/', methods = ['GET' , 'POST']) # What methods are needed?
def home():
	if request.method == "POST":
		try:
			age = request.form['age']
			name = request.form['name']
			quote = request.form['quote']
			login_session['age'] = age
			login_session['name'] = name
			login_session['quote'] = quote
			return render_template('thanks.html')
		except:
			return render_template('error.html')
	else:
		return render_template('home.html')
	

@app.route('/error')
def error():

	return render_template('error.html')


@app.route('/display')
def display():
	print(login_session)
	return render_template('display.html', name = login_session['name'], age = login_session['age'], quote = login_session['quote']) # What variables are needed?


@app.route('/thanks')
def thanks():

	return render_template('thanks.html')


if __name__ == '__main__':
	app.run(debug=True)