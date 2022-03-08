"""This test the homepage"""
import pytest


def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" href="/Git">Git</a>' in response.data
    assert b'<a class="nav-link" href="/Home">Home</a>' in response.data
    assert b'<a class="nav-link" href="/Docker">Page 4</a>' in response.data


def test_request_index_sk(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<h3><a href="/Docker">Docker</a></h3>' in response.data


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


def test_request_flask(client):
    """This makes the index page"""
    response = client.get("/Python_Flask")
    assert response.status_code == 200
    assert b"Page 3" in response.data


def test_request_page3(client):
    """This makes the index page"""
    response = client.get("/page3")
    assert response.status_code == 200
    assert b"Page 3" in response.data


def test_request_page4(client):
    """This makes the index page"""
    response = client.get("/page4")
    assert response.status_code == 200
    assert b"Page 4" in response.data


def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 404
