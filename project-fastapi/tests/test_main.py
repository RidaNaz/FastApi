# `test_` prefix is must in test's filename and in its functaion names

from fastapi.testclient import TestClient
from project_fastapi.main import app

def test_rootPath():
    client = TestClient (app = app)   # (parameter = fastapi variable)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello" : "World"}

def test_piaic_info():
    client = TestClient (app = app)
    response = client.get("/piaic/")
    assert response.status_code == 200
    assert response.json() == {"Organization" : "PIAIC"}

def test_check_failed():
    client = TestClient (app = app)
    response = client.get("/piaic/")
    assert response.status_code == 200
    assert response.json() == {"Organization" : "ABC"}