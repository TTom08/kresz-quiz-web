# Tesztjegyzőkönyv

**Projekt:** Kresz kviz weboldal

**Dátum:** 2025. szeptember 26.

**Tesztelő:** Zilahi Alexandra

---

## 1. Kliensoldali Megjelenés és Navigáció Tesztjei (Frontend/Flask)

Ez a rész a főoldal (home page) elérését, a szükséges HTML elemeket, a CSS linket és a navigációs gombokat ellenőrzi.

| Teszt ID | Teszt leírása | Végpont | HTTP Státuszkód | Tartalom Ellenőrzés | Eredmény | Megjegyzés |
| :---: | :--- | :--- | :---: | :--- | :---: | :--- |
| **01** | Főoldal elérésének státusza | `/` | `200 OK` | N/A | **Sikeres** | A főoldal sikeresen betöltődik. |
| **02** | Főoldal alapvető HTML szerkezete | `/` | `200 OK` | `<html>` tag megléte | **Sikeres** | Ellenőrizve, hogy HTML-t ad vissza, nem template nevet. |
| **03** | Navigációs linkek szövege | `/` | `200 OK` | "Játék indítása", "Ranglista" szövegek | **Sikeres** | Helyes magyar szövegek megjelennek. |
| **05** | Statikus CSS fájl linkjének megléte | `/` | `200 OK` | `/static/css/style.css` link | **Sikeres** | A stíluslap be van illesztve a fejlécre. |
| **06** | CTA (Call to Action) gomb megléte | `/` | `200 OK` | "Játék indítása" és `cta-button` osztály | **Sikeres** | A fő akció gomb látható. |
| **07** | Ranglista gomb megléte | `/` | `200 OK` | "Ranglista" és `secondary-button` osztály | **Sikeres** | A másodlagos navigációs gomb látható. |
| **08** | Kilépés gomb megléte | `/` | `200 OK` | "Kilépés" és `secondary-button` osztály | **Sikeres** | A kijelentkezés/kilépés gomb látható. |
| **10** | Fő szerkezeti tag (`<main>`) megléte | `/` | `200 OK` | `<main>` tag megléte | **Sikeres** | A fő tartalom tag a helyén van. |

---

## 2. Adatbázis Modell Tesztjei (ORM/Unit Tesztek)

Ez a rész az adatbázis modellek (User, Score, Question, Answer) helyes működését, a CRUD (Create, Read, Update, Delete) műveleteket és a relációkat vizsgálja.

| Teszt ID | Teszt leírása | Modell | Művelet típusa | Várt Eredmény | Eredmény | Megjegyzés |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| **01** | `User` létrehozása | `User` | Létrehozás (Create) | Az objektum `id` mezője létezik | **Sikeres** | A felhasználó sikeresen létrejött a DB-ben. |
| **02** | `User` olvasása | `User` | Olvasás (Read) | A felhasználó adatai helyesek | **Sikeres** | |
| **03** | `User` adatainak frissítése | `User` | Frissítés (Update) | A felhasználónév megváltozott | **Sikeres** | |
| **04** | `User` törlése | `User` | Törlés (Delete) | A felhasználó nem található a DB-ben | **Sikeres** | |
| **05** | `Question` és `Answer` reláció | `Question`, `Answer` | Reláció | A kérdéshez tartozik 1 válasz | **Sikeres** | |
| **07** | `Score` időbélyeg megléte | `Score` | Létrehozás | A `timestamp` mező nem `None` | **Sikeres** | Pontszám rögzítés időbélyeggel. |
| **08** | `Answer` `image_path` NULL kezelése | `Answer` | Létrehozás | `image_path` értéke `None` | **Sikeres** | Az útvonal opcionális, ha nincs kép. |
| **09** | Duplikált felhasználónév | `User` | Létrehozás (Constraint) | `Exception` dobás | **Sikeres** | Az egyediségi (Unique) megszorítás érvényesül. |
| **10** | `User` törlése, de `Score` megőrzése | `User`, `Score` | Törlés, Reláció | A pontszám megmarad, `user_id` értéke `None` | **Sikeres** | Cascade delete beállítás ellenőrzése (SET NULL). |