# KRESZ Quiz – Kompatibilitási Tesztjegyzőkönyv

**Projekt:** KRESZ Quiz  
**Dátum:** 2025.09.27   
**Tesztelő:** Kovács Kinga Kendra  

---

## 1. Teszt célja

A kompatibilitási teszt célja annak ellenőrzése, hogy a backend API a frontend számára **megfelelő JSON formátumban** szolgáltatja az adatokat, így a kérdések és a ranglista helyesen jeleníthető meg.  

Külön hangsúlyt kapott a böngésző-kompatibilitás ellenőrzése a következő böngészőkben:  
- Google Chrome  
- Opera  
- Microsoft Edge  

---


## 2. Teszt forgatókönyvek

### 2.1 Ranglista API teszt (`/api/quiz/leaderboard`)

**Cél:** Ellenőrizni, hogy a ranglista API a frontendnek megfelelő formátumban adja vissza az adatokat.

| Lépés | Bemenet | Várt eredmény | Eredmény |
|-------|---------|---------------|---------|
| 1 | POST `/api/quiz/start` JSON: `{"username": "frontend"}` | Új felhasználó létrehozva, HTTP 201 | Sikeres |
| 2 | GET `/api/quiz/leaderboard` | JSON tartalmazza `leaderboard` kulcsot, minden felhasználó objektum tartalmazza `username` és `score` kulcsokat | Sikeres |

### 2.2 Kérdések API teszt (`/api/quiz/questions`)

**Cél:** Ellenőrizni, hogy a kérdések API a frontendnek megfelelő formátumban adja vissza az adatokat.

| Lépés | Bemenet | Várt eredmény | Eredmény |
|-------|---------|---------------|---------|
| 1 | GET `/api/quiz/questions` | JSON tömb, minden eleme tartalmazza `text` és `answers` kulcsokat | Sikeres |
| 2 | Minden válasz objektum tartalmazza `text` és `is_correct` kulcsokat | Válasz objektumok helyesen struktúráltak | Sikeres |

## 3. Megjegyzések

- A teszt in-memory SQLite adatbázist használ, így a kérdések nem az éles adatbázisból származnak, hanem tesztadatként jöttek létre.  
- Minden futtatáskor az adatbázis törlődik a fixture segítségével, így a tesztek egymástól függetlenek.  
- A tesztelés során különböző böngészőkben is ellenőriztem a kompatibilitást: Google Chrome, Opera, Microsoft Edge – mindhárom esetben a JSON adatok helyesen olvashatóak voltak a frontend számára.

---

## 4. Összegzés

A backend API a frontend számára megfelelő JSON formátumban szolgáltatja az adatokat.  
A kérdések és a ranglista adatai minden tesztelt böngészőben helyesen jelennek meg.  

 


