# KRESZ Quiz - Unit Test Jegyzőkönyv
**Készítő:** Kovács Kinga-Kendra  
**Dátum:** 2025.09.24  
**Projekt:** KRESZ Quiz  

---
## 1. Teszt célja

Az egységtesztek célja annak ellenőrzése, hogy a kvíz logikai függvényei helyesen működnek, függetlenül az API-tól vagy az éles adatbázistól.  
Különösen az alábbi funkciókat vizsgáltam:

- `choose_questions(n)` – kérdések kiválasztása.
- `calculate_score(elapsed_time, correct)` – pontszám számítása.
- `add_score(username, score)` – pont hozzáadása felhasználóhoz.
- `get_leaderboard(limit)` – ranglista lekérése.

---

## 2. Teszt forgatókönyvek

| Teszt ID | Teszt neve                               | Cél                                                                                                          | Bemenet                             | Várt eredmény               | Tény eredmény               | Státusz |
|----------|------------------------------------------|--------------------------------------------------------------------------------------------------------------|-------------------------------------|-----------------------------|-----------------------------|---------|
| 1        | test_choose_questions_negative_number    | Ellenőrizni, hogy a kérdésszám negatív értéke ValueError-t dob                                               | n= -5                               | ValueError                  | ValueError                  | Sikeres |
| 2        | test_choose_questions_zero               | Ellenőrizni, hogy 0 kérdés kérése ValueError-t dob                                                           | n=0                                 | ValueError                  | ValueError                  | Sikeres |
| 3        | test_choose_questions_too_many           | Ellenőrizni, hogy a kért kérdésszám nagyobb, mint a DB-ben lévő kérdések száma, ValueError-t dob             | n = Question.query.count() + 1      | ValueError                  | ValueError                  | Sikeres |
| 4        | test_choose_questions_valid              | Ellenőrizni, hogy érvényes kérdésszám esetén a megfelelő számú kérdés jön vissza                             | n=2                                 | 2 kérdés listában           | 2 kérdés listában           | Sikeres |
| 5        | test_choose_questions_exact_total        | Pontosan annyi kérdés, mint a DB-ben van                                                                     | n=Question.query.count()            | Összes kérdés visszajön     | Összes kérdés visszajön     | Sikeres |
| 6        | test_calculate_score_negative_time       | Negatív idő esetén ValueError dobása                                                                         | elapsed_time=-1                     | ValueError                  | ValueError                  | Sikeres |
| 7        | test_calculate_score_wrong_type_correct  | Ellenőrizni, hogy a calculate_score függvény helyesen kezeli a hibás típusú bemenetet a correct paraméternél | elapsed_time=10, correct="yes"      | ValueError                  | ValueError                  | Sikeres |
| 8        | test_calculate_score_wrong_type_elapsed  | Hibás típusú elapsed_time paraméter esetén ValueError                                                        | elapsed_time="10", correct=True     | ValueError                  | ValueError                  | Sikeres |
| 9        | test_calculate_score_wrong_answer        | Hibás válasz esetén 0 pont                                                                                   | elapsed_time=10, correct=False      | 0                           | 0                           | Sikeres |
| 10       | test_calculate_score_time_exceeded       | Idő túllépés esetén 0 pont                                                                                   | elapsed_time=50, correct=True       | 0                           | 0                           | Sikeres |
| 11       | test_calculate_score_normal              | Normál eset számítása                                                                                        | elapsed_time=20, correct=True       | 5                           | 5                           | Sikeres |
| 12       | test_add_score_non_existing_user         | Nem létező felhasználó pont hozzáadása ValueError-t dob                                                      | username="NonExistentUser", score=5 | ValueError                  | ValueError                  | Sikeres |
| 13       | test_add_score_invalid_score_negative    | Negatív pontszám ValueError-t dob                                                                            | username="TestUser", score=-1       | ValueError                  | ValueError                  | Sikeres |
| 14       | test_add_score_invalid_score_too_high    | MAX_POINTS-nál nagyobb pont ValueError-t dob                                                                 | username="TestUser", score=20       | ValueError                  | ValueError                  | Sikeres |
| 15       | test_add_score_empty_username            | Üres felhasználónév esetén ValueError dob                                                                    | username="", score=5                 | ValueError                  | ValueError                  | Sikeres |
| 16       | test_add_score_invalid_score_type        | Hibás típusú pontszám (nem szám) ValueError-t dob                                                           | username="TestUser", score="öt"     | ValueError                  | ValueError                  | Sikeres |
| 17       | test_add_score_valid                     | Érvényes pont hozzáadás                                                                                      | username="TestUser", score=7        | Pont hozzáadva              | Pont hozzáadva              | Sikeres |
| 18       | test_add_score_zero_point                | 0 pont hozzáadás                                                                                             | username="TestUser", score=0        | 0 pont hozzáadva            | 0 pont hozzáadva            | Sikeres |
| 19       | test_add_score_max_point                 | MAX_POINTS pont hozzáadás                                                                                    | username="TestUser", score=10       | 10 pont hozzáadva           | 10 pont hozzáadva           | Sikeres |
| 20       | test_add_score_float                     | Ellenőrizni, hogy a függvény elfogadja a lebegőpontos pontszámokat                                           | username="TestUser", score=7.5      | Pont hozzáadva              | Pont hozzáadva              | Sikeres |
| 21       | test_get_leaderboard_empty               | Üres leaderboard kezelése                                                                                    | Nincs pont a DB-ben                 | Üres lista                  | Üres lista                  | Sikeres |
| 22       | test_get_leaderboard_single_user         | Ellenőrizni, hogy egy felhasználó a leaderboardon szerepel                                                   | username="TestUser" ponttal         | Felhasználó szerepel        | Felhasználó szerepel        | Sikeres |
| 23       | test_get_leaderboard_limit               | Leaderboard limit tesztelése                                                                                 | limit=1                             | Max. 1 felhasználó          | Max. 1 felhasználó          | Sikeres |
| 24       | test_get_leaderboard_limit_exceeds       | Leaderboard limit nagyobb, mint a felhasználók száma                                                         | limit=100                           | Minden felhasználó szerepel | Minden felhasználó szerepel | Sikeres |
| 25       | test_get_leaderboard_multiple_users      | Több felhasználó pontszámának összehasonlítása a leaderboardon                                               | Alice=8, Bob=10                     | Legjobb pontok sorrendben   | Legjobb pontok sorrendben   | Sikeres |
| 26       | test_get_leaderboard_limit_exceeds_users | Ellenőrizni, hogy több felhasználónál a limit nagyobb lehet, de minden felhasználó megjelenik                | limit=100, több user                | Minden felhasználó listázva | Minden felhasználó listázva | Sikeres |
| 27       | test_get_leaderboard_best_score_only     | Ellenőrizni, hogy egy felhasználónál csak a legmagasabb pont jelenik meg a leaderboardon                     | Eva=3 és Eva=9                      | Legmagasabb pont jelenik    | Legmagasabb pont jelenik    | Sikeres |

## 3. Megjegyzések

- A tesztek **in-memory SQLite adatbázison** futnak, így az éles adatbázis **nem változik**.  
- Minden függvény izolált, a tesztek egymástól függetlenek.  
- A jegyzőkönyv minden tesztre tartalmazza a bemenetet, várt eredményt és tényleges eredményt.  

---

## 4. Összegzés

- A kvíz logikai függvényei helyesen működnek minden tesztelt esetben.  
- Az érvényes és hibás bemenetek megfelelően kezelve vannak.  