from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from flask_migrate import Migrate
from models import db, Hero, Power, Hero_Power
app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

# Default route
@app.route('/')
def default_route():
    return jsonify({'message': 'Welcome to the API!'})

# Error handling for 404 responses
@app.after_request
def handle_404(response):
    if response.status_code == 404:
        return jsonify({'error': 'Not Found'}), 404
    return response

# GET /heroes
@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    heroes_data = [{'id': hero.id, 'name': hero.name, 'super_name': hero.super_name} for hero in heroes]
    return jsonify(heroes_data)

# GET /heroes/:id
@app.route('/heroes/<int:hero_id>', methods=['GET'])
def get_hero(hero_id):
    hero = Hero.query.get(hero_id)

    if not hero:
        abort(404, {'error': 'Hero not found'})

    hero_data = {
        'id': hero.id,
        'name': hero.name,
        'super_name': hero.super_name,
        'powers': [{'id': power.id, 'name': power.name, 'description': power.description} for power in hero.powers]
    }
    return jsonify(hero_data)

# GET /powers
@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    powers_data = [{'id': power.id, 'name': power.name, 'description': power.description} for power in powers]
    return jsonify(powers_data)

# GET /powers/:id
@app.route('/powers/<int:power_id>', methods=['GET'])
def get_power(power_id):
    power = Power.query.get(power_id)

    if not power:
        abort(404, {'error': 'Power not found'})

    power_data = {'id': power.id, 'name': power.name, 'description': power.description}
    return jsonify(power_data)

# PATCH /powers/:id
@app.route('/powers/<int:power_id>', methods=['PATCH'])
def update_power(power_id):
    power = Power.query.get(power_id)

    if not power:
        abort(404, {'error': 'Power not found'})

    try:
        data = request.get_json()
        power.description = data['description']
        db.session.commit()
        return jsonify({'id': power.id, 'name': power.name, 'description': power.description})
    except KeyError:
        abort(400, {'errors': ['Invalid data format']})

# POST /hero_powers
@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    try:
        # Ensure 'Content-Type' is 'application/json'
        if request.headers.get('Content-Type') != 'application/json':
            abort(415, {'error': 'Unsupported Media Type. Use application/json.'})

        data = request.get_json()
        hero_id = data.get('hero_id')
        power_id = data.get('power_id')
        strength = data.get('strength')

        # Validate existence of hero and power
        hero = Hero.query.get(hero_id)
        power = Power.query.get(power_id)

        if not hero or not power:
            abort(404, {'errors': ['Hero or Power not found']})

        # Create HeroPower
        hero_power = Hero_Power(hero_id=hero_id, power_id=power_id, strength=strength)
        db.session.add(hero_power)
        db.session.commit()

        # Return updated hero data
        hero_data = {
            'id': hero.id,
            'name': hero.name,
            'super_name': hero.super_name,
            'powers': [{'id': power.id, 'name': power.name, 'description': power.description} for power in hero.powers]
        }
        return jsonify(hero_data), 201

    except KeyError:
        abort(400, {'errors': ['Invalid data format']})


if __name__ == '__main__':
    app.run(port=5555, debug=True)