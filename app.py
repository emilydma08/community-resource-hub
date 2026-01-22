from flask import Flask, render_template, request, jsonify, redirect, url_for
import myorgs
import json
import os
from urllib.parse import unquote

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data.json")

try:
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
except FileNotFoundError:
    data = {"resources": []}  

resource_categories = [
    {"name": "Health & Wellness", "icon": "health.png"},
    {"name": "Education & Youth", "icon": "education.png"},
    {"name": "Social Services & Support", "icon": "support.png"},
    {"name": "Arts & Culture,", "icon": "arts-culture.png"},
    {"name": "Environmental & Sustainability", "icon": "environment.png"},
    {"name": "Sports & FItness", "icon": "sports-rec.png"},
]

@app.route('/')
def landing():
    return render_template('index.html')

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
    return render_template('user-dashboard.html', categories=resource_categories); 
@app.route('/data/resources', methods=['GET'])
def resources():
    return jsonify(data['resources'])
@app.route('/directory/<string:category>', methods=['GET'])
def directory(category):
    category = unquote(category).replace('-', ' ').strip().title()  
    filtered_resources = [r for r in data["resources"] if r["category"] == category]
    return render_template('directory.html', category=category, categories=resource_categories, resources=filtered_resources, num_resources=len(filtered_resources))

@app.route('/resource/<int:resource_id>', methods=['GET'])
def resource_subpage(resource_id):
    resource = None
    for r in data["resources"]:
        if r['id'] == resource_id:
            resource = r
            break
    return render_template('resource-subpage.html', resource=resource, categories=resource_categories)

@app.route('/edit-organization/<string:org_name>', methods=['GET', 'POST'])
def edit_organization(org_name):
    print(org_name)

    if request.method == 'POST':
        org_description = request.form['orgDescription']
        org_address = request.form['orgAddress']
        org_email = request.form['orgEmail']
        org_phone = request.form['orgPhone']
        org_website = request.form['orgWebsite']
        org_category = request.form['orgCategory']

        myorgs.UpdateByName(org_name, org_description, org_address, org_email, org_phone, org_website, org_category)
        
        orgs = myorgs.get()  # Fetch all users
        return render_template('my-orgs.html', orgs=orgs)
    
    org = myorgs.getByName(org_name)
    return render_template('edit-organization.html', org=org)


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
        website = request.form.get('orgWebsite')
        category = request.form.get('orgCategory')
        print("name:" + str(name))
        myorgs.insert(name, description, address, email, phone, website, category)
    return redirect(url_for('my_orgs'))

@app.route('/edit_form', methods=['POST'])
def edit_form():
    if request.method == 'POST':
        old_name = request.form.get('oldOrgName')
        new_name = request.form.get('orgName')
        description = request.form.get('orgDescription')
        address = request.form.get('orgAddress')
        email = request.form.get('orgEmail')
        phone = request.form.get('orgPhone')
        website = request.form.get('orgWebsite')
        category = request.form.get('orgCategory')
        myorgs.UpdateByName(old_name, new_name, description, address, email, phone, website, category)

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
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
    
