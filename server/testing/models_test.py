from server.models import Episode, Guest, Appearance, db
import pytest

def test_episode_guest_relationship(test_app):
    episode = Episode(date="1/1/2000", number=1)
    guest = Guest(name="John Doe", occupation="actor")
    appearance = Appearance(rating=4, episode=episode, guest=guest)

    db.session.add_all([episode, guest, appearance])
    db.session.commit()

    assert guest in episode.guests
    assert episode in guest.episodes

def test_rating_validation(test_app):
    episode = Episode(date="1/1/2000", number=1)
    guest = Guest(name="Jane Doe", occupation="singer")

    with pytest.raises(ValueError):
        bad_appearance = Appearance(rating=10, episode=episode, guest=guest)
        db.session.add(bad_appearance)
        db.session.commit()

def test_cascade_delete(test_app):
    episode = Episode(date="1/1/2000", number=1)
    guest = Guest(name="John Doe", occupation="actor")
    appearance = Appearance(rating=4, episode=episode, guest=guest)

    db.session.add_all([episode, guest, appearance])
    db.session.commit()

    db.session.delete(episode)
    db.session.commit()

    assert Appearance.query.count() == 0
