from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource

from server.models import db, Episode, Guest, Appearance

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)


@app.route("/")
def index():
    return {"message": "Late Show API running"}, 200


# ---------------------- RESOURCES ----------------------

class Episodes(Resource):
    def get(self):
        episodes = Episode.query.all()
        return [e.to_dict(only=("id", "date", "number")) for e in episodes], 200


class EpisodeByID(Resource):
    def get(self, id):
        episode = Episode.query.get(id)
        if not episode:
            return {"error": "Episode not found"}, 404
        return episode.to_dict(), 200

    def delete(self, id):
        episode = Episode.query.get(id)
        if not episode:
            return {"error": "Episode not found"}, 404
        db.session.delete(episode)
        db.session.commit()
        return "", 204


class Guests(Resource):
    def get(self):
        guests = Guest.query.all()
        return [g.to_dict(only=("id", "name", "occupation")) for g in guests], 200


class Appearances(Resource):
    def post(self):
        data = request.get_json()
        rating = data.get("rating")
        guest_id = data.get("guest_id")
        episode_id = data.get("episode_id")

        try:
            new_appearance = Appearance(
                rating=rating,
                guest_id=guest_id,
                episode_id=episode_id
            )
            db.session.add(new_appearance)
            db.session.commit()

            return new_appearance.to_dict(), 201

        except Exception:
            return {"errors": ["validation errors"]}, 400


# ---------------------- ROUTES ----------------------

api.add_resource(Episodes, "/episodes")
api.add_resource(EpisodeByID, "/episodes/<int:id>")
api.add_resource(Guests, "/guests")
api.add_resource(Appearances, "/appearances")


# ---------------------- RUN ----------------------
if __name__ == "__main__":
    app.run(port=5555)
