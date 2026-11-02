from config import BASE_URL

def test_gp_smoke(api_session):
    response = api_session.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200


