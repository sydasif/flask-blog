from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        "author": "Corey Schafer",
        "title": "Blog Post 1",
        "content": "1st post content",
        "date_posted": "July 08, 2024"
    },
    {
        "author": "Syed Asif",
        "title": "Blog Post 2",
        "content": "2nd post content",
        "date_posted": "July 09, 2024"
    },

]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


if __name__ == "__main__":
    app.run(debug=True)
