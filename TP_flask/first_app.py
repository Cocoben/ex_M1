from flask import Flask,render_template,jsonify
import os,json
app = Flask(__name__)


@app.route("/")
def index():
 return "hello my app"

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('name.html', name=name)

@app.route('/api/books')
def api():
    books = library()
    return jsonify(books)

@app.route('/api/books/id/<id>')
def apiid(id=None):
    books = library()
    for book in books : 
        if book['id'] == int(id):
            selected = book
    return selected

@app.route('/api/books/titre/<titre>')
def apititre(titre=None):
    books = library()
    for book in books :
        if book['titre'] == titre:
            selected = book
    return selected


@app.route('/api/json/')
def apijson():
    books = libraryjson()
    return render_template('book.html', books=books)




def library():
    book=[
        {
            'id':1,
            'titre' : 'un titre',
        },
        {
            'id':2,
            'titre': 'un autre titre random',
        }
    ]  
    return book 

def libraryjson():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static", "json", "books.json")
    return json.load(open(json_url))






if __name__ == '__main__':
    app.run(debug=True)

