from flask import Flask , render_template 
import random 

app = Flask(__name__)


@app.route('/')
def index():
		return render_template('index.html')


@app.route('/predict')
def predict():
	if random.randint(0, 9) % 2==0:
		return render_template('predict1.html')
	else:
		return render_template('predict2.html')

if __name__ == '__main__':
	app.run(debug=True)