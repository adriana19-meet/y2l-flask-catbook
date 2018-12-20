from flask import Flask,render_template, request
from flask import render_template
<<<<<<< HEAD
from flask import request
from database import get_all_cats
=======
from database import get_all_cats, find_cat, create_cat
>>>>>>> 99f6c5c5474db4767939c4d93959e4a68fcce36f

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


<<<<<<< HEAD
#if __name__ == '__main__':
   #app.run(debug = True)
=======
@app.route('/cats/<int:number>')
def view_details(number):
	cat = find_cat(number)
	return render_template("cat.html",cat= cat)

@app.route('/create', methods=['GET','POST'])
def make_cat():
	if request.method =="GET":
		return render_template("addcat.html")
	else:
		name = request.form['firstname']
		create_cat(name)
		cats = get_all_cats()
		return render_template('home.html', cats=cats)

if __name__ == '__main__':
    app.run(debug = True)
>>>>>>> 99f6c5c5474db4767939c4d93959e4a68fcce36f
