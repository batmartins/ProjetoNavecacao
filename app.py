from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/pessoa')
def fun_pessoa():
    return render_template('pessoas.html')

@app.route('/animal')
def fun_animal():
    return render_template('animal.html')

@app.route('/')
def fun_index():
    return render_template('index.html')

if __name__ =='__main__':
    app.run(debug=True)