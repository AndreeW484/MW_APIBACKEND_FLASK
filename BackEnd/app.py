from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://AndreeW484:Invierno2024@127.0.0.1:3306/apiflask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)

class ContactSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Contact
        load_instance = True

contact_schema = ContactSchema()
contacts_schema = ContactSchema(many=True)

@app.route('/contact', methods=['GET'])
def get_contacts():
    page = request.args.get('page', None, type=int)
    page_size = request.args.get('page_size', None, type=int)
    
    if page is not None and page_size is not None:
        contacts_pagination = Contact.query.paginate(page=page, per_page=page_size)
        contacts = contacts_pagination.items
        result = contacts_schema.dump(contacts)
        return jsonify({
            'contacts': result,
            'total': contacts_pagination.total,
            'pages': contacts_pagination.pages,
            'current_page': contacts_pagination.page,
            'page_size': page_size
        })
    else:
        all_contacts = Contact.query.all()
        result = contacts_schema.dump(all_contacts)
        return jsonify(result)

@app.route('/contact/<int:id>', methods=['GET'])
def get_contact(id):
    contact = Contact.query.get(id)
    if contact is None:
        return jsonify({'message': 'Contacto no encontrado'}), 404
    return jsonify(contact_schema.dump(contact))

@app.route('/contact', methods=['POST'])
def add_contact():
    name = request.json['name']
    phone = request.json['phone']
    email = request.json['email']
    country = request.json['country']
    city = request.json['city']
    
    new_contact = Contact(name=name, phone=phone, email=email, country=country, city=city)
    db.session.add(new_contact)
    db.session.commit()
    
    return jsonify(contact_schema.dump(new_contact)), 201

@app.route('/contact/<int:id>', methods=['PUT'])
def update_contact(id):
    contact = Contact.query.get(id)
    if contact is None:
        return jsonify({'message': 'Contacto no encontrado'}), 404
    
    contact.name = request.json['name']
    contact.phone = request.json['phone']
    contact.email = request.json['email']
    contact.country = request.json['country']
    contact.city = request.json['city']
    
    db.session.commit()
    return jsonify(contact_schema.dump(contact))

@app.route('/contact/<int:id>', methods=['DELETE'])
def delete_contact(id):
    contact = Contact.query.get(id)
    if contact is None:
        return jsonify({'message': 'Contacto no encontrado'}), 404
    
    db.session.delete(contact)
    db.session.commit()
    return jsonify({'message': 'Contacto eliminado'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)