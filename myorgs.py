import firebase_admin
from firebase_admin import credentials, firestore, initialize_app

cred = credentials.Certificate("myorgs-config.json")
initialize_app(cred)
db = firestore.client()

def get():
    conn = db.collection('orgs')
    cur = conn.stream()
    data = []
    for doc in cur:
        org_data = doc.to_dict()
        org_data['id'] = doc.id
        data.append(org_data)
    return data

def getByName(name):
    conn = db.collection('orgs')
    query = conn.where('name', '==', name).limit(1)
    data = []
    docs = list(query.stream())
    if docs:
        org_data = docs[0].to_dict()
        org_data['id'] = docs[0].id
        data.append(org_data)
    return data

def UpdateByName(old_name, new_name, description, address, email, phone):
    conn = db.collection('orgs')
    query = conn.where('name', '==', old_name).limit(1)
    docs = list(query.stream())
    if docs:
        doc_ref = docs[0].reference
        doc_ref.update({
            'name': new_name,  # Add this line
            'description': description,
            'address': address,
            'email': email,
            'phone': phone
        })

def insert(name, description, address, email, phone):
    conn = db.collection('orgs')
    conn.add({
        'name': name,
        'description': description,
        'address': address,
        'email': email,
        'phone': phone
    })
    print("Data inserted successfully.")

def deleteByName(name):
    print("name" + str(name))
    conn = db.collection('orgs')
    query = conn.where('name', '==', name).limit(1)
    docs = query.stream()
    for doc in docs:
        doc.reference.delete()
    print("deleted")
