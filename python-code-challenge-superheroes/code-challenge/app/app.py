from flask import Flask, jsonify
from models import db, Hero, Power, HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Use SQLite for simplicity

# Initialize the database
with app.app_context():
    db.init_app(app)
    db.create_all()

# Routes
@app.route('/')
def home():
    return 'Hello, welcome to the superheroes code challenge!'

@app.route('/heroes')
def get_heroes():
    heroes = Hero.query.all()
    return jsonify({'heroes': [{'id': hero.id, 'name': hero.name} for hero in heroes]})

@app.route('/powers')
def get_powers():
    powers = Power.query.all()
    return jsonify({'powers': [{'id': power.id, 'description': power.description} for power in powers]})

if __name__ == '__main__':
    app.run(debug=True)
