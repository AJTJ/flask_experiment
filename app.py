from flask import Flask, request
app = Flask(__name__)
print(__name__)


# decorator in front of a function declaration
@app.route("/")
def hello():
    return "apple sauce"


# accessing a sub directory
# greater/lesser-than symbols for variables
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


# casting a string to an integer with int (flask specific)
@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    # show the user profile for that user
    # casting back to a string
    return str(a + b)


@app.route('/fs/<file_name>', methods=['GET', 'POST'])
def login(file_name):
    if request.method == 'POST':
        content = request.form['content']
        with open(file_name, 'w') as f:
            f.write(content)
        return 'ok! Shit is done son'
    else:
        # with open instead open
        with open(file_name) as f:
            file_contents = f.read()
        return file_contents

# accessing the shell through flask
