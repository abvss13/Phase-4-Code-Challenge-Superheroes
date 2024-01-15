

from app.models import db, Hero, Power, HeroPower
import random

def seed_data():
    db.create_all()

    # Seeding powers
    powers_data = [
        {"name": "super strength", "description": "gives the wielder super-human strengths"},
        {"name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed"},
        {"name": "super human senses", "description": "allows the wielder to use her senses at a super-human level"},
        {"name": "elasticity", "description": "can stretch the human body to extreme lengths"}
    ]

    powers = [Power.create(**power_data) for power_data in powers_data]

    # Seeding heroes
    heroes_data = [
        {"name": "Kamala Khan", "super_name": "Ms. Marvel"},
        {"name": "Doreen Green", "super_name": "Squirrel Girl"},
        {"name": "Gwen Stacy", "super_name": "Spider-Gwen"},
        {"name": "Janet Van Dyne", "super_name": "The Wasp"},
        {"name": "Wanda Maximoff", "super_name": "Scarlet Witch"},
        {"name": "Carol Danvers", "super_name": "Captain Marvel"},
        {"name": "Jean Grey", "super_name": "Dark Phoenix"},
        {"name": "Ororo Munroe", "super_name": "Storm"},
        {"name": "Kitty Pryde", "super_name": "Shadowcat"},
        {"name": "Elektra Natchios", "super_name": "Elektra"}
    ]

    heroes = [Hero.create(**hero_data) for hero_data in heroes_data]

    # Adding powers to heroes
    strengths = ["Strong", "Weak", "Average"]
    for hero in heroes:
        for _ in range(random.randint(1, 3)):
            # Get a random power
            power = random.choice(powers)

            HeroPower.create(hero_id=hero.id, power_id=power.id, strength=random.choice(strengths))

    print("🦸‍♀️ Done seeding!")

if __name__ == '__main__':
    seed_data()
