import requests

url = "http://localhost:5001"

def test_homepage():
    response = requests.get(url)
    assert response.status_code == 200
    assert "green" in response.text.lower()
    print("✅ Green environment passed smoke test")

test_homepage()
