from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://patrikdark:suman123@localhost/dark'
app.config['SECRET_KEY'] = "#eshfdshfgsg&332bjfv"
db = SQLAlchemy(app)


class story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(50))
    content = db.Column(db.String(1500))

    def __init__(self, author, content):
        self.author = author
        self.content = content

    def __repr__(self):
        return '<Author %r>' % self.author


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if not request.form['author'] or not request.form['content']:
             flash('All fields are required')
        else:
            story_temp = story(request.form['author'], request.form['content'])
            db.session.add(story_temp)
            db.session.commit()
            flash('Story Added Successfully')
    stories = story.query.order_by(desc(story.id))
    return render_template('index.html', stories=stories)


if __name__ == '__main__':
    app.run()
