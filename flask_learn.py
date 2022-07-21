from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Benny Chan',
        'title': 'Blog Post 1',
        'Content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'Content': 'Second post content',
        'date_posted': 'April 20, 2018'
    }
]

@app.route('/')
@app.route('/home')
def hello():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)