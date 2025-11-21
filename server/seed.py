from app import app
from models import db, Episode, Guest, Appearance

with app.app_context():
    print("Clearing database...")
    Appearance.query.delete()
    Episode.query.delete()
    Guest.query.delete()

    print("Seeding episodes...")
    ep1 = Episode(date="1/11/99", number=1)
    ep2 = Episode(date="1/12/99", number=2)

    print("Seeding guests...")
    g1 = Guest(name="Michael J. Fox", occupation="actor")
    g2 = Guest(name="Sandra Bernhard", occupation="comedian")

    db.session.add_all([ep1, ep2, g1, g2])
    db.session.commit()

    print("Seeding appearances...")
    a1 = Appearance(rating=4, guest_id=g1.id, episode_id=ep1.id)

    db.session.add(a1)
    db.session.commit()

    print("Done seeding!")
