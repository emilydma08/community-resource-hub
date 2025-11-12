from flask import Flask, render_template, request, jsonify, redirect, url_for
import myorgs

app = Flask(__name__)

resource_categories = [
    {"name": "Category 1", "icon": "bars-3"},
    {"name": "Category 2", "icon": "plus"},
    {"name": "Category 3", "icon": "check"},
    {"name": "Category 4", "icon": "clock"},
    {"name": "Category 5", "icon": "chevron-down"},
    {"name": "Category 6", "icon": "arrows-up-down"},
]

resources = [
    {"id": 0, "name": "Food Bank", "description": "This food bank provides free meals for low-income families. Residents can also donate canned or boxed food", "coords": [47.67, -122.12]},
    {"id": 1, "name": "Animal Shelter", "description": "At this animal shelter residents can adopt pets, as well as volunteer their time to improve the wellbeing of animals", "coords": [47.65, -122.14]},
    {"id": 2, "name": "Community Clinic", "description": "This community clinic provides affordable/free healthcare for residents who cannot afford health insurance and/or a hospital", "coords": [47.64, -122.12]},
    {"id": 3, "name": "Police Station", "description": "This police station is where residents go to for assistance, including with emergencies, safety concerns, etc.", "coords": [47.66, -122.11]},
    {"id": 4, "name": "Food Bank", "description": "This food bank provides free meals for low-income families. Residents can also donate canned or boxed food", "coords": [47.65, -122.11]},
    {"id": 5, "name": "Animal Shelter", "description": "At this animal shelter residents can adopt pets, as well as volunteer their time to improve the wellbeing of animals", "coords": [47.66, -122.13]},
    {"id": 6, "name": "Community Clinic", "description": "This community clinic provides affordable/free healthcare for residents who cannot afford health insurance and/or a hospital", "coords": [47.63, -122.14]},
    {"id": 7, "name": "Police Station", "description": "This police station is where residents go to for assistance, including with emergencies, safety concerns, etc.", "coords": [47.65, -122.11]},
]

@app.route('/')
def landing():
    return render_template('register.html')

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html', categories=resource_categories)

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html', categories=resource_categories)

@app.route('/survey', methods=['GET'])
def survey():
    return render_template('survey.html', categories=resource_categories)

@app.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template('user-dashboard.html', categories=resource_categories)

@app.route('/directory/<string:category>', methods=['GET'])
def directory(category):
    return render_template('directory.html', category=category, categories=resource_categories, resources=resources)

@app.route('/resource/<int:resource_id>', methods=['GET'])
def resource_subpage(resource_id):
    resource = None
    for r in resources:
        if r['id'] == resource_id:
            resource = r
            break
    return render_template('resource-subpage.html', resource=resource, categories=resource_categories)

@app.route('/edit-organization/<string:org_name>', methods=['GET', 'POST'])
def edit_organization(org_name):
    print(org_name)

    if request.method == 'POST':
        org_description = request.form['org_description']
        org_address = request.form['org_address']
        org_email = request.form['org_email']
        org_phone = request.form['org_phone']

        myorgs.UpdateByName(org_name, org_description, org_address, org_email, org_phone)
        
        orgs = myorgs.get()  # Fetch all users
        return render_template('my-orgs.html', orgs=orgs)
    
    org = myorgs.getByName(org_name)
    return render_template('edit-organization.html', org=org[0])


@app.route('/my-organizations', methods=['GET'])
def my_orgs():
    orgs = myorgs.get()
    return render_template('my-orgs.html', orgs=orgs, categories=resource_categories)

#Still need route for organization subpage templates

@app.route('/profile', methods=['GET'])
def profile():
    return render_template('profile.html', categories=resource_categories)

@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form.get('orgName')
        description = request.form.get('orgDescription')
        address = request.form.get('orgAddress')
        email = request.form.get('orgEmail')
        phone = request.form.get('orgPhone')
        print("name:" + str(name))
        myorgs.insert(name, description, address, email, phone)
    return redirect(url_for('my_orgs'))

@app.route('/edit_form', methods=['POST'])
def edit_form():
    if request.method == 'POST':
        name = request.form.get('orgName')
        description = request.form.get('orgDescription')
        address = request.form.get('orgAddress')
        email = request.form.get('orgEmail')
        phone = request.form.get('orgPhone')
        myorgs.UpdateByName(name, description, address, email, phone)
    
        return redirect(url_for('my_orgs'))

@app.route('/delete_form', methods=['POST'])
def delete_form():
    name = request.form.get('orgName')
    if name:
        print("Deleting:", name)
        myorgs.deleteByName(name)
    orgs = myorgs.get()
    return redirect(url_for('my_orgs'))

if __name__ == '__main__':
    app.run(debug=True)