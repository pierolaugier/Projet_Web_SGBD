from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


@app.route('/f')
def index():
    return render_template("Projetwebmain.html")


# Sample data : modification
books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"id": 3, "title": "1984", "author": "George Orwell"}
]

# GET /books - returns all books


@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# GET /books/{id} - returns a specific book by id


@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = next((book for book in books if book["id"] == id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404

# POST /books - creates a new book


@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    book = {"id": len(books) + 1,
            "title": data["title"], "author": data["author"]}
    books.append(book)
    return jsonify(book), 201

# PUT /books/{id} - updates a specific book by id


@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    data = request.get_json()
    book = next((book for book in books if book["id"] == id), None)
    if book:
        book.update(data)
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404

# DELETE /books/{id} - deletes a specific book by id


@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    global books
    books = [book for book in books if book["id"] != id]
    return '', 204


if __name__ == '__main__':
    app.run(debug=True)
