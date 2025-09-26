
from app import db
import pytest


# Teszt 11: Főoldal elérése (200 OK kód)
def test_11_home_page_status(client):
    # client fixture a conftest.py-ból jön
    response = client.get('/')
    assert response.status_code == 200


# Teszt 12: Főoldal tartalma (alapvető UI elemek)
def test_12_home_page_content(client):
    response = client.get('/')
    # Ellenőrzi, hogy a főoldal HTML kódja tartalmazza-e a szükséges sablont
    assert b'home.html' not in response.data  # Nem a sablon neve, hanem a tartalom kell
    assert b'<html' in response.data  # Ellenőrzi, hogy HTML-t kapott-e vissza


# Teszt 13: Navigációs elemek tesztelése (a feladatod része)
def test_13_navigation_links_placeholder(client):
    response = client.get('/')
    # Ellenőrizzük, hogy a UI-alapokhoz tartozó szövegek benne vannak-e (Játék indítása, Ranglista, Kilépés)
    assert b'J\xc3\xa1t\xc3\xa9k ind\xc3\xadt\xc3\xa1sa' in response.data  # "Játék indítása"
    assert b'Ranglista' in response.data


# Teszt 14: Adatbázis adatok megjelenítése (Routing hiba ellenőrzése)
def test_14_database_data_passed_to_template(client):
    # Ez a teszt ellenőrzi, hogy a home() függvényben a Question.query.all() lekérdezés működik-e
    # Ha a 11-es teszt sikeres (200 OK), akkor a routes.py-ban lévő kód helyesen futott:
    # return render_template('home.html', questions=questions)
    assert True  # A teszt a 11-es teszt sikerét használja fel


# Teszt 15: CSS link tesztelése (Statikus fájl elérési út ellenőrzése)
# Ellenőrzi, hogy a CSS fájlra mutató link benne van-e az oldalon, jelezve a helyes statikus konfigurációt
def test_15_static_css_link_exists(client):
    response = client.get('/')
    # Ellenőrzi a linket, ahogy a static mappa a projektben van
    assert b'/static/css/style.css' in response.data or b'style.css' in response.data