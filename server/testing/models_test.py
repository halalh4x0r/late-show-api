from server.models import User, Bakery, BakedGood

def test_user_password_hashing(session):
    user = User(username="moha")
    user.password_hash = "secret123"
    session.add(user)
    session.commit()

    assert user.id is not None
    assert user._password_hash != "secret123"
    assert user.authenticate("secret123") is True
    assert user.authenticate("wrongpass") is False

def test_bakery_model_creation(session):
    bakery = Bakery(name="Sunrise Bakery")
    session.add(bakery)
    session.commit()

    assert bakery.id is not None
    assert bakery.name == "Sunrise Bakery"

def test_relationships(session):
    bakery = Bakery(name="Mama’s Bakery")
    good = BakedGood(name="Donut", price=120, bakery=bakery)

    session.add_all([bakery, good])
    session.commit()

    assert good.bakery == bakery
    assert len(bakery.baked_goods) == 1
