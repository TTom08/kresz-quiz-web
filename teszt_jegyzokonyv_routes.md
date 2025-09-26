# Tesztjegyzőkönyv

**Projekt:** Kresz kviz weboldal
**Dátum:** 2025. szeptember 26.
**Tesztelő:** Tóth Tamás

---

## 1. /api/quiz/start végpont tesztjei (Kvíz indítása)

| Teszt ID | Teszt leírása | Végpont | HTTP Metódus | Eredmény | HTTP Státuszkód | Megjegyzés |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| **01** | Sikeres kvízindítás, új felhasználó létrehozása | `/api/quiz/start` | `POST` | **Sikeres** | `201 Created` | Az 'ujfelhasznalo' létrejött. |
| **02** | Kvízindítás foglalt felhasználónévvel | `/api/quiz/start` | `POST` | **Sikeres** | `409 Conflict` | Hibaüzenet: "Ez a felhasználónév már foglalt". |
| **03** | Kvízindítás hiányzó felhasználónévvel | `/api/quiz/start` | `POST` | **Sikeres** | `400 Bad Request` | Hibaüzenet: "Felhasználónév kötelező". |
| **04** | Kvízindítás üres (szóközökből álló) felhasználónévvel | `/api/quiz/start` | `POST` | **Sikeres** | `400 Bad Request` | Érvénytelen bemenet. |
| **05** | Felhasználók számának növekedése sikeres indítás után | `/api/quiz/start` | `POST` | **Sikeres** | `201 Created` | A felhasználók száma 1-gyel nőtt. |

---

## 2. /api/quiz/submit végpont tesztjei (Pontszám elküldése)

| Teszt ID | Teszt leírása | Végpont | HTTP Metódus | Eredmény | HTTP Státuszkód | Megjegyzés |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| **06** | Sikeres pontszám elküldés létező felhasználóval | `/api/quiz/submit` | `POST` | **Sikeres** | `201 Created` | Visszajelzés: "Pontszám elmentve". |
| **07** | Pontszám elküldés ismeretlen felhasználóval | `/api/quiz/submit` | `POST` | **Sikeres** | `404 Not Found` | Hibaüzenet: "Ismeretlen felhasználó". |
| **08** | Pontszám elküldés hiányzó `score` adattal | `/api/quiz/submit` | `POST` | **Sikeres** | `400 Bad Request` | Hibaüzenet: "Hiányzó adatok". |
| **09** | Pontszámok számának növekedése sikeres elküldés után | `/api/quiz/submit` | `POST` | **Sikeres** | `201 Created` | A pontszámok száma 1-gyel nőtt. |
| **10** | Nulla (0) pontszám sikeres elküldése | `/api/quiz/submit` | `POST` | **Sikeres** | `201 Created` | A 0 pontszám sikeresen rögzítésre került. |

---

## 3. /api/quiz/leaderboard végpont tesztjei (Ranglista)

| Teszt ID | Teszt leírása | Végpont | HTTP Metódus | Eredmény | HTTP Státuszkód | Megjegyzés |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| **11** | Ranglista helyes sorrendje (legjobb pontszám alapján) | `/api/quiz/leaderboard` | `GET` | **Sikeres** | `200 OK` | A sorrend: 'zoli', 'tomi', 'anna'. |
| **12** | Üres adatbázis (felhasználók és pontszámok nélkül) kezelése | `/api/quiz/leaderboard` | `GET` | **Sikeres** | `200 OK` | Az eredménylista üres. |
| **13** | Ranglista korlátozása (limit 10) | `/api/quiz/leaderboard` | `GET` | **Sikeres** | `200 OK` | A visszaadott elemek száma pontosan 10. |
| **14** | Legjobb pontszám kiválasztása több eredmény esetén | `/api/quiz/leaderboard` | `GET` | **Sikeres** | `200 OK` | 'tomi' legjobb pontszáma 100. |
| **15** | Ranglista pontszámok nélkül (csak felhasználók vannak) | `/api/quiz/leaderboard` | `GET` | **Sikeres** | `200 OK` | Az eredménylista üres. |

---

## 4. /api/quiz/questions végpont tesztjei (Kérdések lekérése)

| Teszt ID | Teszt leírása | Végpont | HTTP Metódus | Eredmény | HTTP Státuszkód | Megjegyzés |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| **16** | Kérdések számának korlátozása (limit 10) | `/api/quiz/questions` | `GET` | **Sikeres** | `200 OK` | A visszaadott kérdések száma pontosan 10. |
| **17** | Kérdés képe elérési útvonalának ellenőrzése | `/api/quiz/questions` | `GET` | **Sikeres** | `200 OK` | A 2. kérdéshez van `image_path`, az 1. kérdéshez nincs. |
| **18** | Válasz képe elérési útvonalának ellenőrzése | `/api/quiz/questions` | `GET` | **Sikeres** | `200 OK` | A "Helyes 3" válaszhoz van `image_path`, a "Helytelen 3" válaszhoz nincs. |
| **19** | Helyes válasz jelző (flag) ellenőrzése | `/api/quiz/questions` | `GET` | **Sikeres** | `200 OK` | A helyes válasz `is_correct` értéke `True`, a helytelené `False`. |
| **20** | Üres adatbázis (kérdések és válaszok nélkül) kezelése | `/api/quiz/questions` | `GET` | **Sikeres** | `200 OK` | Az eredménylista üres. |