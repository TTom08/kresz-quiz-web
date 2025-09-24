# KRESZ Quiz - Unit Test Jegyzőkönyv
**Készítő:** Kovács Kinga-Kendra  
**Dátum:** 2025.09.24  
**Projekt:** KRESZ Quiz  

| Teszt neve | Cél | Bemenet | Várt eredmény | Tény eredmény | Státusz |
|------------|-----|---------|---------------|---------------|---------|
| test_choose_questions_negative_number | Ellenőrizni, hogy a kérdésszám negatív értéke ValueError-t dob | n=-5 | ValueError | ValueError | ✅ |
| test_choose_questions_zero | Ellenőrizni, hogy 0 kérdés kérése ValueError-t dob | n=0 | ValueError | ValueError | ✅ |
| test_choose_questions_too_many | Ellenőrizni, hogy a kért kérdésszám nagyobb, mint a DB-ben lévő kérdések száma, ValueError-t dob | n = Question.query.count() + 1 | ValueError | ValueError | ✅ |
| test_choose_questions_valid | Ellenőrizni, hogy érvényes kérdésszám esetén a megfelelő számú kérdés jön vissza | n=2 | 2 kérdés listában | 2 kérdés listában | ✅ |
| test_calculate_score_negative_time | Negatív idő esetén ValueError dobása | elapsed_time=-1 | ValueError | ValueError | ✅ |
| test_calculate_score_wrong_type_correct | Ellenőrizni, hogy a calculate_score függvény helyesen kezeli a hibás típusú bemenetet a correct paraméternél | elapsed_time=10, correct="yes" | ValueError | ValueError | ✅ |
| test_calculate_score_wrong_type_elapsed | Hibás típusú elapsed_time paraméter esetén ValueError | elapsed_time="10", correct=True | ValueError | ValueError | ✅ |
| test_calculate_score_wrong_answer | Hibás válasz esetén 0 pont | elapsed_time=10, correct=False | 0 | 0 | ✅ |
| test_calculate_score_time_exceeded | Idő túllépés esetén 0 pont | elapsed_time=50, correct=True | 0 | 0 | ✅ |
| test_calculate_score_normal | Normál eset számítása | elapsed_time=20, correct=True | 5 | 5 | ✅ |
| test_add_score_non_existing_user | Nem létező felhasználó pont hozzáadása ValueError-t dob | username="NonExistentUser", score=5 | ValueError | ValueError | ✅ |
| test_add_score_invalid_score_negative | Negatív pontszám ValueError-t dob | username="TestUser", score=-1 | ValueError | ValueError | ✅ |
| test_add_score_invalid_score_too_high | MAX_POINTS-nál nagyobb pont ValueError-t dob | username="TestUser", score=20 | ValueError | ValueError | ✅ |
| test_add_score_valid | Érvényes pont hozzáadás | username="TestUser", score=7 | Pont hozzáadva | Pont hozzáadva | ✅ |
| test_get_leaderboard_empty | Üres leaderboard kezelése | Nincs pont a DB-ben | Üres lista | Üres lista | ✅ |
| test_get_leaderboard_single_user | Ellenőrizni, hogy egy felhasználó a leaderboardon szerepel | username="TestUser" ponttal | Felhasználó szerepel | Felhasználó szerepel | ✅ |
| test_get_leaderboard_limit | Leaderboard limit tesztelése | limit=1 | Max. 1 felhasználó | Max. 1 felhasználó | ✅ |
| test_choose_questions_exact_total | Pontosan annyi kérdés, mint a DB-ben van | n=Question.query.count() | Összes kérdés visszajön | Összes kérdés visszajön | ✅ |
| test_add_score_zero_point | 0 pont hozzáadás | username="TestUser", score=0 | 0 pont hozzáadva | 0 pont hozzáadva | ✅ |
| test_add_score_max_point | MAX_POINTS pont hozzáadás | username="TestUser", score=10 | 10 pont hozzáadva | 10 pont hozzáadva | ✅ |
| test_get_leaderboard_limit_exceeds | Leaderboard limit nagyobb, mint a felhasználók száma | limit=100 | Minden felhasználó szerepel | Minden felhasználó szerepel | ✅ |

