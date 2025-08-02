from flask import Flask, render_template, request

app = Flask(__name__)
#List1 = []

@app.route("/")
def main_page():
    return render_template("loginpage.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/createaccount", methods=['POST'])
def create_db():
    username = request.form["username"]
    password = request.form["password"]
    email_id = request.form["email id"]

    with open("datafile.txt", "a") as file:
        file.write("Username: " + username + "\n")
        file.write("Password: " + password + "\n")
        file.write("Email ID: " + email_id + "\n")
        file.write("-----\n")  

    return "Your Account is Successfully Created!"


'''''

@app.route("/login", methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    flag = False
    for item in List1:
        if item.get('username') == username and item.get('password') == password:
            flag = True
            break
    if flag:
        return "YOU ARE SUCCESSFULLY LOGGED IN!"
    else:
        return "LOGIN FAILED!"
'''''
@app.route("/login", methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    file = open("datafile.txt", "r")
    for line in file:
        if username in line and password in line:
            file.close()
            return "YOU ARE SUCCESSFULLY LOGGED IN!"
    file.close()
    return "LOGIN FAILED!"


if __name__ == "__main__":
    app.run(debug=True)
