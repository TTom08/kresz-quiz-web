# KRESZ Quiz – Teljesítmény Tesztjegyzőkönyv

**Teszt típusa:** Teljesítmény (Sok felhasználó, ranglista gyors frissítése)  
**Dátum:** 2025.09.27  
**Projekt:** KRESZ Quiz  
**Tesztelő:** Kovács Kinga Kendra  

---

## 1. Teszt célja

A teljesítményteszt célja annak ellenőrzése, hogy a backend API **nagy számú felhasználó esetén** is képes:

- Egyidejű pontszámok kezelésére (Score mentése minden felhasználónál)
- Ranglista gyors frissítésére, akár 500 felhasználó esetén is

---


## 2. Teszt forgatókönyv

### 2.1 Fixture létrehozása (`client_with_many_users`)

**Cél:** Nagyszámú felhasználó létrehozása és pontszámok hozzárendelése az in-memory adatbázisban.

| Lépés | Tevékenység | Eredmény                             |
|-------|-----------|--------------------------------------|
| 1 | 500 felhasználó létrehozása, minden felhasználónak 1–10 közötti pontszám | Felhasználók létrejöttek             |
| 2 | A fixture elmenti a felhasználókat és pontszámokat az adatbázisba | Adatbázis készen a teszt futtatására |

### 2.2 Ranglista API teljesítmény teszt (`/api/quiz/leaderboard`)

**Cél:** Ellenőrizni, hogy a ranglista lekérés gyorsan történik 500 felhasználó esetén.

| Lépés | Tevékenység | Várt eredmény | Eredmény |
|-------|------------|---------------|---------|
| 1 | GET `/api/quiz/leaderboard` | HTTP 200 státusz | Sikeres |
| 2 | JSON adat tartalmazza `leaderboard` kulcsot | Top 10 felhasználó adatai | Sikeres |
| 3 | Lekérés idejének mérése | < 1.0 másodperc | Sikeres |

## 3. Megjegyzések

- A teszt in-memory SQLite adatbázist használ, így a teljesítmény gyorsan mérhető és izolált.
- Minden teszt lefutása után az adatbázis törlődik a fixture segítségével.


---

## 4. Eredmények

| Teszt neve | Eredmény | Megjegyzés               |
|------------|---------|--------------------------|
| Ranglista lekérése 500 felhasználóval | Sikeres | A lekérés ideje: ~0.09 s |

---

## 5. Összegzés

- A backend API képes kezelni nagyszámú felhasználót.
- A ranglista lekérése gyors és hatékony, az előírt 1 másodperces határ alatt teljesül.



