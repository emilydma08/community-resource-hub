from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def landing():
    return render_template('index.html')

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')

@app.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template('user-dashboard.html')

@app.route('/directory', methods=['GET'])
def directory():
    return render_template('directory.html')

# Still need route for resource subpage templates

@app.route('/your-organizations', methods=['GET'])
def your_orgs():
    return render_template('your-orgs.html')

#Still need route for organization subpage templates

@app.route('/profile', methods=['GET'])
def profile():
    return render_template('profile.html')


if __name__ == '__main__':
    app.run(debug=True)