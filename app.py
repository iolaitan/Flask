from flask import Flask, render_template

app = Flask(__name__)

#ensures we do not get a 404 error and #defines what we want to be displayed
@app.route('/')

def render_the_map():
    return render_template('All States.html')

if __name__ == "__main__":
    app.run(debug=True)