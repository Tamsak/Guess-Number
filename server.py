import random
from flask import Flask, render_template,redirect,session,request
app = Flask(__name__)
app.secret_key = 'jkjjkggguyp'

@app.route('/')
def index():
    num = random.randint(1,100)
    session['number'] = num
    return render_template('index.html')

@app.route('/num', methods=['post'])
def guess():
    num = session['number']
    guess_num = request.form['guess_num']
    if int(guess_num)>num:
        result = "Too high."
        class_name="red"
        link= ""
    elif int(guess_num)<num:
        result = "Too low"
        class_name="red"
        link= ""
    else:
        result = str(guess_num)+" was the right number!"
        class_name="green"
        link= "Try Again"
       
    return render_template('index.html', result=result, class_name=class_name, link=link)

    

app.run(debug=True)
