from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

resource_categories = [
    {"name": "Category 1", "icon": "bars-3"},
    {"name": "Category 2", "icon": "plus"},
    {"name": "Category 3", "icon": "check"},
    {"name": "Category 4", "icon": "clock"},
    {"name": "Category 5", "icon": "chevron-down"},
    {"name": "Category 6", "icon": "arrows-up-down"},
    {"name": "Category 7", "icon": "arrow-right"},
    {"name": "Category 8", "icon": "minus"},
    {"name": "Category 9", "icon": "plus"}
]

@app.route('/')
def landing():
    return render_template('index.html', categories=resource_categories)

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html', categories=resource_categories)

@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html', categories=resource_categories)

@app.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template('user-dashboard.html', categories=resource_categories)

@app.route('/directory/<string:category>', methods=['GET'])
def directory(category):
    return render_template('directory.html', category=category, categories=resource_categories)

# Still need route for resource subpage templates

@app.route('/your-organizations', methods=['GET'])
def your_orgs():
    return render_template('your-orgs.html', categories=resource_categories)

#Still need route for organization subpage templates

@app.route('/profile', methods=['GET'])
def profile():
    return render_template('profile.html', categories=resource_categories)


if __name__ == '__main__':
    app.run(debug=True)