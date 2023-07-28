from flask import Flask , jsonify , request
import csv

# utf = universal transforamtion format , 8 bit values are used in encoding
all_books =[]
with open('books.csv' , encoding = 'utf-8') as f :
    reader =csv.reader(f)
    data = list(reader)
    all_books = data[1:]

liked_books =[]
not_liked_books = []
did_not_read = []

app = Flask(__name__)
@app.route('/get-books')
def get_movie():
    return jsonify({
        'data' : all_books[0],
        'status' : 'success'
    })

@app.route('/liked-books' , methods = ['POST'])
def liked_books():
    books = all_books[0]
    all_books = all_books[1:]
    liked_books.append(books)
    return jsonify ({
        'status' : 'success'
    }),201

@app.route('/unliked-books' , methods = ['POST'])
def unliked_books():
    books = all_books[0]
    all_books = all_books[1:]
    not_liked_books.append(books)
    return jsonify({
        'status' : 'success'
    }),201

@app.route('/did-not-read' , methods = ['POST'])
def did_not_watch():
    books = all_books[0]
    all_books = all_books[1:]
    did_not_read.append(books)
    return jsonify({
        'status' : 'success'
    }),201

if __name__ == '__main__' :
    app.run()