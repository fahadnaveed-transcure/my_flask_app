from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    #return "Hello, Flask!"
    return render_template('imagetext.html')

@app.route('/ImageDesc')
def ImageDesc():
    return render_template('imagedes.html')

@app.route('/textsummary')
def textsummary():
    return render_template('textsummary.html')


@app.route('/textimage')
def textimage():
    return render_template('textimage.html')

if __name__ == '__main__':
    app.run(debug=True)
