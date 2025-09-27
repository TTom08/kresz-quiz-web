# Tesztjegyzőkönyv

**Projekt:** Kresz kviz weboldal

**Dátum:** 2025. szeptember 27.

**Tesztelő:** Zilahi Alexandra

---

## 1. Kliensoldali Megjelenés és Navigáció Tesztjei (Frontend/Flask)

Ez a rész a főoldal (`/`) elérését, a szükséges HTML elemeket, a CSS linket és a navigációs gombokat ellenőrzi. **Minden teszt sikeres.**

| Teszt ID | Teszt leírása | Végpont | HTTP Státuszkód | Tartalom Ellenőrzés | Eredmény | Megjegyzés |
| :---: | :--- | :--- | :---: | :--- | :---: | :--- |
| **01** | Főoldal elérésének státusza | `/` | `200 OK` | N/A | **Sikeres** | A főoldal sikeresen betöltődik. |
| **02** | Főoldal alapvető HTML szerkezete | `/` | `200 OK` | `<html>` tag megléte | **Sikeres** | Ellenőrizve, hogy HTML-t ad vissza. |
| **03** | Navigációs linkek szövege | `/` | `200 OK` | "Játék indítása", "Ranglista" | **Sikeres** | Helyes magyar szövegek megjelennek. |
| **04** | Adatbázis adatok template-be jutása | N/A | N/A | N/A | **Sikeres** | Placeholder teszt. |
| **05** | Statikus CSS fájl linkjének megléte (általános) | `/` | `200 OK` | `/static/css/home.css` link | **Sikeres** | A stíluslap be van illesztve a fejlécre. |
| **06** | CTA (Call to Action) gomb megléte | `/` | `200 OK` | "Játék indítása" és `cta-button` | **Sikeres** | A fő akció gomb látható. |
| **07** | Ranglista gomb megléte | `/` | `200 OK` | "Ranglista" és `secondary-button` | **Sikeres** | A másodlagos navigációs gomb látható. |
| **08** | Kilépés gomb megléte | `/` | `200 OK` | "Kilépés" és `secondary-button` | **Sikeres** | A kijelentkezés/kilépés gomb látható. |
| **09** | Statikus CSS fájl linkjének megléte (konkrétan) | `/` | `200 OK` | `/static/css/home.css` link | **Sikeres** | A stíluslap pontos útvonala ellenőrizve. |
| **10** | Fő szerkezeti tag (`<main>`) megléte | `/` | `200 OK` | `<main>` tag megléte | **Sikeres** | A fő tartalom tag a helyén van. |

---

## 2. Adatbázis Modell Tesztjei

Ez a rész az adatbázis modellek (User, Score, Question, Answer) helyes működését, a CRUD műveleteket és a relációkat vizsgálja. **Minden teszt sikeres.**

| Teszt ID | Teszt leírása | Modell | Művelet típusa | Várt Eredmény | Eredmény | Megjegyzés |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| **01** | `User` létrehozása (Create) | `User` | Létrehozás | Az objektum `id` mezője létezik | **Sikeres** | |
| **02** | `User` olvasása (Read) | `User` | Olvasás | A felhasználó adatai helyesek | **Sikeres** | |
| **03** | `User` adatainak frissítése (Update) | `User` | Frissítés | A felhasználónév megváltozott | **Sikeres** | |
| **04** | `User` törlése (Delete) | `User` | Törlés | A felhasználó nem található a DB-ben | **Sikeres** | |
| **05** | `Question` és `Answer` létrehozása | `Question`, `Answer` | Létrehozás, Reláció | A kérdéshez tartozik 1 válasz | **Sikeres** | Ellenőrzi a Question-Answer kapcsolatot. |
| **06** | `Question` és `Answer` olvasása | `Question`, `Answer` | Olvasás, Reláció | A válasz szövege helyes | **Sikeres** | Lekérdezés `Question.text` alapján. |
| **07** | `Score` időbélyeg megléte | `Score` | Létrehozás | A `timestamp` mező nem `None` | **Sikeres** | Pontszám rögzítés időbélyeggel. |
| **08** | `Answer` `image_path` NULL kezelése | `Answer` | Létrehozás | `image_path` értéke `None` | **Sikeres** | Az útvonal opcionális (`nullable=True`). |
| **09** | Duplikált felhasználónév ellenőrzése | `User` | Létrehozás (Constraint) | `Exception` dobás | **Sikeres** | Az egyediségi megszorítás érvényesül. |
| **10** | `User` törlése, de `Score` megőrzése | `User`, `Score` | Törlés, Reláció | A pontszám megmarad, `user_id` értéke `None` | **Sikeres** | A `SET NULL` kényszer ellenőrizve. |