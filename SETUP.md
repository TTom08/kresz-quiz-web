# KRESZ Kvíz – Részletes Telepítési és Futtatási Útmutató

Ez a dokumentum a KRESZ kvíz webalkalmazás környezetének beállítását és futtatását írja le.

---

## 1. Fejlesztői Érvelés: Saját Adatbázisok

Mivel egy miniprojektről van szó, a cél a teljes technológiai lánc (PostgreSQL + Flask-Migrate) bemutatása volt. Ezért a projekt úgy van tervezve, hogy minden felhasználó **saját, független adatbázist** hozzon létre a telepítés során.

### Miért ez a megoldás?

- **A Migrációk Tesztelése (Fő Érv):**  
Az adatbázis kezelő kód (ORM és Flask-Migrate) helyes működésének ellenőrzéséhez fontos, hogy minden környezetben újra létrejöjjenek a táblák. Ez biztosítja, hogy a modelljeink és a migrációs fájlok mindig pontosan működjenek, és ne legyenek hibák.

- **Fejlesztői Izoláció:**  
 A lokális PostgreSQL használata biztosítja, hogy minden fejlesztő saját környezetben dolgozzon. Így elkerülhetők a hálózati beállítások, külső szolgáltatók és biztonsági kockázatok, ami túl bonyolult lenne a miniprojekt számára.

- **Adatmegosztás Hiánya:**  
  A pontszámok és felhasználók lokálisan tárolódnak. A felhasználó csak azokat az adatokat fogja látni, amiket a saját tesztkörnyezetében, a futtatás során hoz létre (pl. kitölt egy kvízt).

---

## 2. Követelmények

A projekt sikeres futtatásához a következőkre van szükség:

- Python 3.x
- PostgreSQL Server (lokálisan telepítve és futtatva a tesztgépen)
- `requirements.txt` függőségek


---

## 3. Lépésről Lépésre Telepítés

### Lépés 1: Függőségek Telepítése

Hozza létre és aktiválja a virtuális környezetet, majd telepítse a szükséges Python csomagokat:

```bash

pip install -r requirements.txt
```

### Lépés 2: PostgreSQL Előkészítése és Konfiguráció

Az alkalmazás az alapértelmezett, lokális PostgreSQL beállításokat használja (`app.py`):

- **Adatbázis neve:** `kresz_db`  
- **Felhasználónév:** `kresz`  
- **Jelszó:** `kresz`  

Kérjük, hozza létre a fenti paraméterekkel az adatbázist a saját PostgreSQL szerverén.

**Tipp:** Ha eltérő beállításokat használ, állítsa be a `DATABASE_URL` környezeti változót a saját csatlakozási stringjével.

### Lépés 3: Adatbázis Táblák Létrehozása (Migráció)

A táblák létrehozásához (Users, Scores, Questions, Answers) használja a Flask-Migrate parancsot. Ez hozza létre a teljes séma struktúrát a lokális adatbázisban.

### Lépés 3.1: Jogosultságok beállítása a migráció előtt

A migráció előtt érdemes megadni a szükséges jogosultságokat a `kresz` felhasználónak, hogy a táblák létrehozása és módosítása zökkenőmentes legyen:

```sql
GRANT ALL PRIVILEGES ON SCHEMA public TO kresz;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO kresz;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO kresz;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON TABLES TO kresz;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON SEQUENCES TO kresz;
```
### Lépés 3.2: Migráció lépések

Inicializálás (ha ez az első alkalom):
```bash

flask db init
```
Táblák létrehozása vagy frissítése az adatbázisban a modelljeink alapján:

```bash

flask db upgrade
```
### Lépés 4: Tesztadatok Feltöltése
A kvíz futtatásához szükséges a kérdések feltöltése. Futtassa a csoportunk által biztosított adatfeltöltő szkriptet:
```bash

python seed.py
```
### Lépés 5: Alkalmazás Indítása
Indítsa el az alkalmazást:
```bash 

flask run
```
Ezután a böngészőben navigálhat a [http://127.0.0.1:5000/](http://127.0.0.1:5000/) címre.


**Megjegyzés:** A sikeres futtatáshoz a PostgreSQL szervernek futnia kell a Flask alkalmazás indítása előtt.
