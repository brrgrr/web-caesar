from flask import Flask, request, render_template
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

title="Web Caesar 2.0"

@app.route("/")
def index():
    return render_template("form.html", title=title, text="")


@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = str(request.form['text'])
    encrypted = rotate_string(text, rot)
    return render_template("form.html", title=title, text=encrypted)


if __name__ == '__main__':
    app.run()
