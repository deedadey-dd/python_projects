from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func
import random


app = Flask(__name__)

# #Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# #Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


@app.route("/")
def home():
    return render_template("index.html")


# # HTTP GET - Read Record
@app.route('/random', methods=['GET'])
def random():
    if request.method == 'GET':
        all_cafes = Cafe.query.count()
        print(all_cafes)
        random_cafe = Cafe.query.order_by(func.random()).first()
        raw_response = {
            'cafe': {
                # 'id': random_cafe.id,
                'name': random_cafe.name,
                'map_url': random_cafe.map_url,
                'img_url': random_cafe.img_url,
                'location': random_cafe.location,
                'seats': random_cafe.seats,
                'has_toilet': random_cafe.has_toilet,
                'has_wifi': random_cafe.has_wifi,
                'has_sockets': random_cafe.has_sockets,
                'can_take_calls': random_cafe.can_take_calls,
                'coffee_price': random_cafe.coffee_price
            }
        }

        response = jsonify(raw_response)
        print(response)
        return response


@app.route('/all', methods=['GET'])
def all():
    if request.method == 'GET':
        all_cafes = Cafe.query.all()
        cafe_list = []
        for random_cafe in all_cafes:
            cafe_list.append(
                {
                    'id': random_cafe.id,
                    'name': random_cafe.name,
                    'map_url': random_cafe.map_url,
                    'img_url': random_cafe.img_url,
                    'location': random_cafe.location,
                    'seats': random_cafe.seats,
                    'has_toilet': random_cafe.has_toilet,
                    'has_wifi': random_cafe.has_wifi,
                    'has_sockets': random_cafe.has_sockets,
                    'can_take_calls': random_cafe.can_take_calls,
                    'coffee_price': random_cafe.coffee_price
                }
            )
        response = {
            'cafe': cafe_list
        }
        return jsonify(response)


@app.route('/search')
def search():
    search_location = request.args.get('loc', '').title()
    # print(search_location)
    locations = Cafe.query.filter(Cafe.location.ilike(f'%{search_location}%')).all()
    cafe_list = []
    # print(locations)

    if not locations:
        return jsonify({'message': f"Sorry... We don't have any cafes at {search_location}"})
    else:
        for location in locations:
            cafe_list.append(
                {
                    'id': location.id,
                    'name': location.name,
                    'map_url': location.map_url,
                    'img_url': location.img_url,
                    'location': location.location,
                    'seats': location.seats,
                    'has_toilet': location.has_toilet,
                    'has_wifi': location.has_wifi,
                    'has_sockets': location.has_sockets,
                    'can_take_calls': location.can_take_calls,
                    'coffee_price': f'${location.coffee_price}'
                }
            )
        response = {
            'cafe': cafe_list
        }
        return jsonify(response)

# # HTTP POST - Create Record


@app.route('/add', methods=['GET', 'POST'])
def add():
    def convert_bool(text):
        if text.title() == 'True':
            return True
        elif text.title() == 'False':
            return False
        else:
            return 'Invalid input'

    if request.method == 'POST':
        name = request.form.get('name')
        map_url = request.form.get('map_url')
        img_url = request.form.get("img_url")
        location = request.form.get("location")
        seats = request.form.get('seats')
        has_toilet = bool(convert_bool(request.form.get('has_toilet')))
        has_wifi = bool(convert_bool(request.form.get('has_wifi')))
        has_sockets = bool(convert_bool(request.form.get('has_sockets')))
        can_take_calls = bool(convert_bool(request.form.get('can_take_calls')))
        coffee_price = request.form.get('coffee_price')

        with app.app_context():
            new_cafe = Cafe(name=name, map_url=map_url, img_url=img_url, location=location, seats=seats,
                            has_toilet=has_toilet, has_wifi=has_wifi, has_sockets=has_sockets,
                            can_take_calls=can_take_calls, coffee_price=coffee_price)
            db.session.add(new_cafe)
            db.session.commit()
            success_response = {
                'success': 'Successfully added the new cafe.'
            }
            return jsonify(success_response)


# # HTTP PUT/PATCH - Update Record

@app.route('/update-price/<int:cafe_id>', methods=['PATCH'])
def update(cafe_id):
    cafe_with_id = Cafe.query.get(cafe_id)
    if cafe_with_id:
        new_price = request.args.get('new_price')
        if new_price == '':
            error_response = {
                'failed': 'Enter the new price in order to update coffee prices '
            }
            return jsonify(error_response), 400
        else:
            with app.app_context():
                cafe_to_update = Cafe.query.get(cafe_id)
                cafe_to_update.coffee_price = float(request.args.get('new_price'))
                db.session.commit()

                success_response = {
                    'success': f'Successfully updated the price to {new_price}'
                }
                return jsonify(success_response), 200
    else:
        error_response = {
            'failed': f'Could not find cafe with id {cafe_id}'
        }
        return jsonify(error_response), 404


# # HTTP DELETE - Delete Record

@app.route('/report-closed/<int:cafe_id>', methods=['DELETE'])
def closed(cafe_id):
    cafe_with_id = Cafe.query.get(cafe_id)
    if cafe_with_id:
        api_key = request.args.get('api_key')
        print(api_key)
        if api_key == 'Top5ecre+API' or api_key == 'API_Top5ecre+':
            with app.app_context():
                cafe_to_delete = Cafe.query.get(cafe_id)
                db.session.delete(cafe_to_delete)
                db.session.commit()

                success_response = {
                    'success': 'Successfully deleted.'
                }
                return jsonify(success_response), 200
        else:
            error_response = {
                'failed': 'Could not verify your API Key'
            }
            return jsonify(error_response), 401
    else:
        error_response = {
            'failed': f'Could not find cafe with id {cafe_id}'
        }
        return jsonify(error_response), 404


if __name__ == '__main__':
    app.run(debug=True)
