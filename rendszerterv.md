# Rendszerterv: KRESZ Kvízjáték

## A rendszer célja

A rendszer célja egy olyan webes alkalmazás megvalósítása, amely játékos formában segít a felhasználóknak a KRESZ-szabályok és a közlekedési táblák megismerésében. A felhasználók egy interaktív kvíz keretein belül mérhetik fel tudásukat, azonnali visszajelzést kapnak a helyes és helytelen válaszokról, valamint pontszámokat gyűjthetnek a teljesítményük alapján. Az interaktivitás biztosítása érdekében a rendszer nem pusztán egy statikus tesztfelület, hanem játékos elemeket is tartalmaz: a pontszámítás az eltelt idő függvényében történik, így a gyors válaszadás előnyt jelent. A felhasználó teljesítménye rögzítésre kerül az adatbázisban, és összehasonlítható más játékosok eredményeivel egy ranglista segítségével. Ez versenyhelyzetet teremt, amely motiválja a felhasználókat a jobb eredmény elérésére és a gyakorlás folytatására.

Mivel a kvízjáték webes felületen keresztül érhető el, a cél, hogy egyszerűen futtatható legyen bármely modern böngészőben asztali számítógépen vagy laptopon. A reszponzivitás biztosítása érdekében a rendszer esetleg részlegesen alkalmazkodhat más képernyőméretekhez, például tabletekhez vagy kisebb kijelzőkhöz is. A központi adatbázis biztosítja az adatok konzisztens és biztonságos tárolását.

Összességében a rendszer célja egy olyan tanulást támogató játékos környezet létrehozása, amely a KRESZ-vizsgára való felkészülést könnyíti meg, mindezt szórakoztató, interaktív módon.

# Projektterv

A fejlesztést egy háromfős csapat végzi. A feladatok felosztása úgy lett kialakítva, hogy minden tag részt vegyen frontend és backend fejlesztésben, valamint a tesztelési folyamatokban is. Ez a struktúra biztosítja, hogy a csapattagok átfogó rálátással rendelkezzenek a teljes rendszerről, és a végtermék minden szempontból kiegyensúlyozott legyen.

## Projektszerepkörök és felelősségek

### Csapattag 1: Adatkezelés és felhasználói adatfolyamok

**Backend:**
- PostgreSQL adatbázis tervezése és implementálása.
- Felhasználónév megadása a játék előtt.
- API végpont fejlesztése a felhasználónév mentésére.
- Hibakezelés érvénytelen vagy hiányzó név esetén.

**Frontend:**
- Felhasználónév megadása a játék indítása előtt.
- Hibajelzések a név mezőhöz (pl. üres név).

**Tesztelés:**
- Felhasználónév mentésének és visszaolvasásának ellenőrzése.
- Adatbázis műveletek és hibakezelés ellenőrzése.

---

### Csapattag 2: Kvízlogika és pontszámítás

**Backend:**
- Kvízkérdések kezelése és kiszolgálása az API-n keresztül.
- Pontszámítási algoritmus megvalósítása.
- Hibakezelés, ha nincs kérdés vagy érvénytelen választ kap a rendszer.

**Frontend:**
- Kérdés–válasz modul fejlesztése.
- Dinamikus elemek (pl. visszaszámláló, pontszám kijelzés).
- Hibajelzések a játék közben (pl. „Nincs több kérdés”).

**Tesztelés:**
- Játéklogika és pontszámítás ellenőrzése.
- Hibakezelés ellenőrzése.

---

### Csapattag 3: Játékállapot és felhasználói élmény

**Backend:**
- Játékállapot kezelése: új játék indítása, játék vége, pontok mentése.
- Ranglista kezelése (pontszámok mentése, rangsorolás név alapján).
- API stabilitás és naplózás biztosítása.
- Hibakezelés a játékfolyamathoz kapcsolódva (pl. ha nem található játék session).

**Frontend:**
- Reszponzív játékfelület és navigáció (asztali nézet támogatása, alkalmazkodás kisebb képernyőméretekhez is).
- Toplista megjelenítése a játék után.
- Állapot-visszajelzések: „Játék indult”, „Játék véget ért”.
- Egységes hibajelző és visszajelző komponens (piros/zöld üzenetek).

**Tesztelés:**
- Játékindítás és játék lezárás folyamatainak tesztelése.
- Toplista frissítésének és megjelenítésének ellenőrzése.
- Reszponzivitás és felhasználói élmény ellenőrzése.
- Hibakezelés kipróbálása (pl. játék indítása nem létező session-nel).

## Ütemterv

| Feladat / Task | Prioritás | Becslés (óra) | Aktuális becslés (óra) | Eltelt idő (óra) | Hátralévő idő (óra) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Követelmény specifikáció | 0 | 4 | 4 | 4 | 0 |
| Funkcionális specifikáció | 0 | 4 | 4 | 4 | 0 |
| Rendszerterv | 0 | 8 | 8 | 4 | 4 |
| Adatbázis séma és kapcsolatok tervezése | 1 | 8 | 0 | 0 | 8 |
| Flask API fejlesztése (felhasználónév kezelése) | 1 | 10 | 0 | 0 | 10 |
| Kvízlogika és pontszámítás implementálása | 1 | 12 | 0 | 0 | 12 |
| Frontend felület (kvíz, ranglista) | 1 | 14 | 0 | 0 | 14 |
| Kommunikáció a frontend és backend között | 1 | 10 | 0 | 0 | 10 |
| Funkcionális tesztelés | 2 | 6 | 0 | 0 | 6 |
| Telepítési és karbantartási terv | 3 | 4 | 0 | 0 | 4 |

## Mérföldkövek

- A PostgreSQL adatbázis és az alap API működőképes.

- A kvízlogika és pontszámítás implementálva van.

- A frontend és a backend össze van kötve, a játék futtatható.

- Teljes tesztelés és végleges verzió átadása.


# Üzleti folyamatok modellje

A rendszer működésének középpontjában a kvíz kitöltése áll. A felhasználó megnyitja az alkalmazást, beírja a nevét, majd elindítja a kvízt. A rendszer véletlenszerűen kérdéssort generál az adatbázisból, amelyet a játékos sorban megválaszol.

Minden válasz beküldésekor a kliens elküldi az adatokat a szervernek, amely kiértékeli azokat, visszajelzést ad a helyességről és visszaküldi az eredményt. Ha a válasz helyes, a játékos pontot kap, a pontérték pedig az eltelt idő függvényében csökkenhet. A kvíz végén a rendszer összesíti a pontszámokat, eltárolja azokat az adatbázisban, majd megjeleníti a ranglistát.

Ez a folyamat biztosítja a tanulás mellett a játékélményt is és versenyhelyzetet teremt, amely motiválja a felhasználókat a folyamatos gyakorlásra.