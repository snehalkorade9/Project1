"""This test the homepage"""
import pytest


def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'Home' in response.data
    assert b'<h3><a href="/Git">Git</a></h3>' in response.data

def test_request_git(client):
    """This makes the index page"""
    response = client.get("/Git")
    assert response.status_code == 200
    assert b'<h4>Git is Version control system, allowing you to work together and collabrate with ' in response.data


def test_request_docker(client):
    """This makes the index page"""
    response = client.get("/Docker")
    assert response.status_code == 200
    x = response.data
    if (x .find(b"https://hub.docker.com/u/sk1502") == -1):
        pytest.fail()
    assert b'$ docker start [OPTIONS] CONTAINER [CONTAINER...]' in response.data


def test_request_flask(client):
    """This makes the index page"""
    response = client.get("/Python_Flask")
    assert response.status_code == 200
    assert b"GitHub workflow is used to run when a particular action is triggred or complet" in response.data


def test_request_page_cicd(client):
    """This makes the index page"""
    response = client.get("/ci_cd")
    assert response.status_code == 200
    assert b"<li>Open Git Hub, create Repo and copy the path</li>" in response.data



def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 404
