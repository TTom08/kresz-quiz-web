
from app import db
import pytest

from models import Score, User


def test_1_home_page_status(client):
    response = client.get('/')
    assert response.status_code == 200

def test_2_home_page_content(client):
    response = client.get('/')
    assert b'home.html' not in response.data
    assert b'<html' in response.data

def test_3_navigation_links_placeholder(client):
    response = client.get('/')
    assert b'J\xc3\xa1t\xc3\xa9k ind\xc3\xadt\xc3\xa1sa' in response.data
    assert b'Ranglista' in response.data


def test_4_home_page_has_main_headline(client):
    response = client.get('/')
    assert b'K\xc3\xa9sz\xc3\xbclj a vizsg\xc3\xa1ra, teszteld a tud\xc3\xa1sodat!' in response.data

def test_5_static_css_link_exists(client):
    response = client.get('/')
    assert b'/static/css/home.css' in response.data or b'home.css' in response.data

def test_6_home_page_has_cta_button(client):
    response = client.get('/')
    assert b'J\xc3\xa1t\xc3\xa9k ind\xc3\xadt\xc3\xa1sa' in response.data
    assert b'cta-button' in response.data

def test_7_home_page_has_leaderboard_button(client):
    response = client.get('/')
    assert b'Ranglista' in response.data
    assert b'secondary-button' in response.data

def test_8_home_page_has_exit_button(client):
    response = client.get('/')
    assert b'Kil\xc3\xa9p\xc3\xa9s' in response.data
    assert b'secondary-button' in response.data

def test_9_static_css_link_exists(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'/static/css/home.css' in response.data

def test_10_home_page_has_main_tag(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'<main>' in response.data
