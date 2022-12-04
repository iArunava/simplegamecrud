from flask import render_template, request, redirect, flash
from app import app, db
from app.models import Game

ERROR={
1: "Validation Error"
}

@app.route('/')
@app.route('/index')
def index():
    games = Game.query.all()
    return render_template('index.html', games=games)

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        form = request.form
        name = form.get('name')
        description = form.get('description')
        author = form.get('author')
        url = form.get('url')
        if not name or description:
            #try:
            entry = Game(name = name, description = description, author=author, url=url)
            db.session.add(entry)
            db.session.commit()
            #except:
                #return redirect("/error/1")
            return redirect('/')
    return "unknown method"

@app.route('/show/<int:id>')
def showRoute(id):
    if not id or id != 0:
        entry = Game.query.get(id)
        if entry:
            return render_template('show.html', game=entry)
    return "unknown game"

@app.route('/update/<int:id>')
def updateRoute(id):
    if not id or id != 0:
        entry = Game.query.get(id)
        if entry:
            return render_template('update.html', game=entry)
    return "unknown method"

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    if not id or id != 0:
        entry = Game.query.get(id)
        if entry:
            form = request.form
            name = form.get('name')
            description = form.get('description')
            author = form.get('author')
            url = form.get('url')
            entry.name = name
            entry.description = description
            entry.author = author
            entry.url = url
            db.session.commit()
        return redirect('/')
    return "unknown methods"

@app.route('/delete/<int:id>')
def delete(id):
    if not id or id != 0:
        entry = Game.query.get(id)
        if entry:
            db.session.delete(entry)
            db.session.commit()
        return redirect('/')
    return "unknown method"

@app.route('/error/<int:id>')
def error(id):
    id=int(id)
    if id and int(id) in ERROR.keys():
        return render_template('error.html', message=ERROR[id])
    return "unknown method"
