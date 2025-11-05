from flask import Flask, render_template, request, jsonify, redirect, url_for
import psycopg2
import myorgs

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
        return render_template('your-orgs.html', orgs=orgs)
    
    org = myorgs.getByName(org_name)
    return render_template('edit-organization.html', org=org[0])

# Still need route for resource subpage templates

@app.route('/your-organizations', methods=['GET'])
def your_orgs():
    orgs = myorgs.get()
    return render_template('your-orgs.html', orgs=orgs)

#Still need route for organization subpage templates

@app.route('/profile', methods=['GET'])
def profile():
    return render_template('profile.html')

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
    return redirect(url_for('your_orgs'))

@app.route('/edit_form', methods=['POST'])
def edit_form():
    if request.method == 'POST':
        name = request.form.get('orgName')
        description = request.form.get('orgDescription')
        address = request.form.get('orgAddress')
        email = request.form.get('orgEmail')
        phone = request.form.get('orgPhone')
        myorgs.UpdateByName(name, description, address, email, phone)
    
        return redirect(url_for('your_orgs'))

@app.route('/delete_form', methods=['POST'])
def delete_form():
    name = request.form.get('orgName')
    if name:
        print("Deleting:", name)
        myorgs.deleteByName(name)
    orgs = myorgs.get()
    return redirect(url_for('your_orgs'))

if __name__ == '__main__':
    app.run(debug=True)