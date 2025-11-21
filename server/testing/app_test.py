from server.models import Episode, Guest, Appearance, db
import json

def test_get_all_episodes(client):
    e1 = Episode(date="1/1/2000", number=1)
    db.session.add(e1)
    db.session.commit()

    res = client.get("/episodes")
    assert res.status_code == 200

    data = res.get_json()
    assert len(data) == 1
    assert data[0]["number"] == 1

def test_get_single_episode(client):
    e1 = Episode(date="1/1/2000", number=1)
    g1 = Guest(name="John Doe", occupation="actor")
    a1 = Appearance(rating=5, episode=e1, guest=g1)

    db.session.add_all([e1, g1, a1])
    db.session.commit()

    res = client.get(f"/episodes/{e1.id}")
    assert res.status_code == 200

    data = res.get_json()
    assert data["number"] == 1
    assert len(data["appearances"]) == 1

def test_delete_episode(client):
    e1 = Episode(date="1/1/2000", number=1)
    db.session.add(e1)
    db.session.commit()

    res = client.delete(f"/episodes/{e1.id}")
    assert res.status_code == 204

def test_post_appearance(client):
    e1 = Episode(date="1/1/2000", number=1)
    g1 = Guest(name="John Doe", occupation="actor")

    db.session.add_all([e1, g1])
    db.session.commit()

    res = client.post(
        "/appearances",
        json={"rating": 5, "episode_id": e1.id, "guest_id": g1.id}
    )

    assert res.status_code == 201
    data = res.get_json()

    assert data["rating"] == 5
    assert data["episode"]["id"] == e1.id
    assert data["guest"]["id"] == g1.id
