from flask import Flask
from flask import render_template
from flask import request
from database import get_all_cats

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-VERY-SECRET-SHHH'

@app.route('/',methods = ["GET" , "POST"])

def catbook_home():
	if request.method == "GET":
		cats = get_all_cats()  
	else :
		name = request.form["firstname"]

		cats = get_all_cats()
	return render_template("home.html" , cats = cats )

@app.route('/cats/<int:id>')	   

def catbook_name(id):
	cat = get_cat(id)
	return render_template("cat_html" , cat = cat)


#if __name__ == '__main__':
   #app.run(debug = True)
