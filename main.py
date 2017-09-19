from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

styles = """
body {
    background-color: #F0DC82;
}
form {
    background-color: #eee;
    padding: 20px;
    margin: 0 auto;
    width: 540px;
    font: 16px sans-serif;
    border-radius: 10px;
}
textarea {
    margin: 10px 0;
    width: 540px;
    height: 120px;
}
"""

page_header = """
<!DOCTYPE html>

<html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Web Caesar</title>
        <style>
            """ + styles + """
        </style>
    </head>
    <body>
"""

page_footer = """
    </body>
</html>
"""

form = """
    <form action="/" method="post">
        <label for="rot">Rotate by:</label>
        <input type="text" name="rot" value="0" />
        <textarea name="text">{0}</textarea>
        <br>
        <input type="submit" value="Submit Query" />
    </form>
"""


@app.route("/")
def index():
    return page_header + form.format("") + page_footer

@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = str(request.form['text'])
    encrypted = rotate_string(text,rot)
    return page_header + form.format(encrypted) + page_footer


if __name__ == '__main__':
    app.run()
