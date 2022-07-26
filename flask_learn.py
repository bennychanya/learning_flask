from flask import Flask, render_template, url_for
app = Flask(__name__)

app.config['SECRET KEY'] = '10166cad78de9a5cb469ec53712fe2c0'

posts = [
    {
        'author': 'Benny Chan',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 20, 2018'
    }
]

@app.route('/')
@app.route('/home')
def hello():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

if __name__ == "__main__":
    app.run(debug=True)