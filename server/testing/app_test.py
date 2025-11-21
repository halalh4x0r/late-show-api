import json

# ---- GET test ----
def test_get_bakeries(client):
    response = client.get("/bakeries")
    assert response.status_code == 200
    assert isinstance(response.json, list)

# ---- POST test ----
def test_create_bakery(client, session):
    payload = {"name": "Test Bakery"}

    response = client.post(
        "/bakeries",
        data=json.dumps(payload),
        content_type="application/json"
    )

    assert response.status_code == 201
    assert response.json["name"] == "Test Bakery"

# ---- PATCH/PUT test ----
def test_update_bakery(client, session):
    from server.models import Bakery
    bakery = Bakery(name="Before")
    session.add(bakery)
    session.commit()

    payload = {"name": "After"}

    response = client.patch(
        f"/bakeries/{bakery.id}",
        data=json.dumps(payload),
        content_type="application/json"
    )

    assert response.status_code == 200
    assert response.json["name"] == "After"

# ---- DELETE test ----
def test_delete_bakery(client, session):
    from server.models import Bakery
    bakery = Bakery(name="DeleteMe")
    session.add(bakery)
    session.commit()

    response = client.delete(f"/bakeries/{bakery.id}")
    assert response.status_code == 204
