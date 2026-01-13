from app import app, db
from models import Hero, Power, HeroPower

with app.app_context():
    print("🌱 Seeding database...")

    # Clear old data
    HeroPower.query.delete()
    Hero.query.delete()
    Power.query.delete()

    # Add powers
    flight = Power(name="Flight")
    strength = Power(name="Super Strength")
    invisibility = Power(name="Invisibility")
    db.session.add_all([flight, strength, invisibility])
    db.session.commit()

    # Add heroes (ensure all NOT NULL fields are filled)
    hero1 = Hero(name="Clark Kent", super_name="Superman")
    hero2 = Hero(name="Susan Storm", super_name="Invisible Woman")
    db.session.add_all([hero1, hero2])
    db.session.commit()

    # Assign powers
    hero1_powers = [
        HeroPower(hero_id=hero1.id, power_id=flight.id),
        HeroPower(hero_id=hero1.id, power_id=strength.id)
    ]
    hero2_powers = [
        HeroPower(hero_id=hero2.id, power_id=invisibility.id)
    ]
    db.session.add_all(hero1_powers + hero2_powers)
    db.session.commit()

    print("✅ Database seeded successfully!")
