from flask import Flask, request, render_template
from functions import user_login, user_signup, input_predict, user_tests

app = Flask(__name__, template_folder='template', static_folder='template/static/')

username_in_use = ''

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form_choice', methods=['POST', 'GET'])
def choice():
    if request.form['action'] == 'login':
        return render_template("loginPage.html")
    if request.form['action'] == 'signup':
        return render_template("signUpPage.html")



@app.route('/form_login', methods=['POST', 'GET'])
def login():
    name = request.form['username']
    pwd = request.form['password']
    data = user_login()
    flag = 0
    for i in data:
        if(i[0] == name):
            if(i[1] == pwd):
                flag = 1
                break
            else:
                flag = 2
                continue
        else:
            flag = 0
            continue
    if(flag==1):
        global username_in_use
        username_in_use = name
        return render_template('user_page.html', name=name, past_data=user_tests(username_in_use))
    elif(flag==2):
        render_template("login.html", msg="Wrong password. Try again!")
    else:
        render_template('login.html')

@app.route('/form_signup', methods=['POST', 'GET'])
def signup():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    f_name = request.form['f_name']
    l_name = request.form['l_name']
    user_signup(username, password, email, f_name, l_name)
    return render_template('loginPage.html')

@app.route('/form_prediction_page', methods=['POST', 'GET'])
def open_pred_page():
    return render_template('predictionPage.html')

@app.route('/form_predict', methods=['POST', 'GET'])
def user_predict():
    from datetime import date
    gender = request.form['gender']
    age = request.form['age']
    hypertension = request.form['hypertension']
    heartdisease = request.form['heartdisease']
    evermarried = request.form['evermarried']
    worktype = request.form['worktype']
    recidencetype = request.form['recidencetype']
    glucoselevel = request.form['glucoselevel']
    bmi = request.form['bmi']
    smokingstatus = request.form['smokingstatus']
    answer = input_predict(username_in_use, gender, age, hypertension, heartdisease, 
    evermarried, worktype, recidencetype, 
    glucoselevel, bmi, smokingstatus)
    return render_template('predictionOutput.html', answer=answer)

@app.route('/form_navbar', methods=['POST', 'GET'])
def navigation():
    if request.form['navi'] == 'Home':
        return render_template("mainPage.html")
    elif request.form['navi'] == 'Predict':
        return render_template('predictionPage.html')
    elif request.form['navi'] == 'Profile':
        return render_template('user_page.html', name=username_in_use, past_data=user_tests(username_in_use))
    elif request.form['navi'] == 'Graphs':
        return render_template('providing.html')
    else:
        return render_template('choose.html')

if __name__ == "__main__":
    app.run(debug=True)
