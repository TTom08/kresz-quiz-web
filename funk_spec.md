# Funkcionális Specifikáció

## Felhasználói folyamatok --> User flow

A rendszer célja, hogy a felhasználó egy egyszerű, átlátható és interaktív folyamat során sajátíthassa el a KRESZ szabályait. A következőkben bemutatjuk a játékhoz tartozó felhasználói folyamatokat a belépéstől a kilépésig, lépésről lépésre.

### Használati esetek

1. **Játék indítása**

A felhasználó megnyitja a webalkalmazást a böngészőben. A kezdőképernyőn található egy mező, amelyben a saját nevét kell megadnia. Ez kötelező lépés, mivel a név a pontszámok mentéséhez és a toplistán való megjelenítéshez szükséges. A név beírása után a játékot elindító gomb aktívvá válik, és a felhasználó elindíthatja a kvízt.

2. **Kvíz képernyő**

A játék elindítása után megjelenik az első kérdés. A képernyő felső részén látható a kérdés szövege, valamint egy közlekedési tábla képe vagy egy rövid KRESZ-szabály. Az alatta elhelyezett négy gombon jelennek meg a válaszlehetőségek. A felhasználó ezek közül kattintással választ.

3. **Válaszadás**

Amikor a felhasználó rákattint egy válaszra, a rendszer azonnal visszajelzést ad:

- helyes válasz esetén a gomb zöld színűvé válik,

- hibás válasz esetén pirosra színeződik, és a helyes megoldás zöld színnel kerül kiemelésre.

4. **Pontszámítás és időkorlát**

A válaszadásra egy addott számú másodperc áll rendelkezésre. A pontszámot a rendszer automatikusan kiszámítja a válasz gyorsaságától függően: minél hamarabb adja meg a felhasználó a helyes választ, annál több pontot kap. A képernyő jobb felső részén látható a visszaszámláló, valamint az eddig elért pontszám.

5. **Továbblépés a következő kérdésre**

A visszajelzés megjelenítése után egy gomb segítségével léphetünk tovább a következő kérdésre. Ez ismételten tartalmaz egy rövid szöveget vagy képet, valamint a négy lehetséges választ. A folyamat mindaddig ismétlődik, amíg a felhasználó az összes kérdést meg nem válaszolta.

6. **Játék vége és eredmények**

Amikor a felhasználó az utolsó kérdésre is válaszolt, megjelenik az Eredmény képernyő. Itt látható a végső pontszám és a helyesen megválaszolt kérdések száma. Az eredmények automatikusan mentésre kerülnek a böngésző helyi tárhelyére, a felhasználó neve mellett.

7. **Ranglista megtekintése**

Az eredmény képernyőről, illetve a főmenüből elérhető a ranglista. Ez a helyi tárhelyben tárolt pontszámokat mutatja, csökkenő sorrendben.

8. **Újraindítás vagy kilépés**

Az eredmény képernyőről két lehetőség választható:

- Újraindítás: a felhasználó új játékot kezdhet, új kérdésekkel.

- Kilépés: a program bezárható, a ranglistán tárolt adatok megőrzésével.

## Forgatókönyv

- A felhasználó megnyitja a játékot, beírja a nevét és elindítja a kvízt.

- Az első kérdés megjelenik, a felhasználó elolvassa, majd kiválasztja a helyesnek gondolt választ.

- A rendszer azonnali színkódos visszajelzést ad.

- A pontszám azonnal frissül, és a felhasználó továbblép a következő kérdésre.

- A folyamat több kérdésen át ismétlődik, miközben a játékos figyeli az időzítőt és a pontszámát.

- A kvíz végén a felhasználó látja a végső pontszámát és helyezését a toplistán.

- Ezután újrakezdheti a játékot vagy kiléphet az alkalmazásból.

Ez a felhasználói folyamat biztosítja, hogy a játék egyszerű, intuitív és motiváló legyen, miközben segíti a KRESZ-szabályok elsajátítását.

## Megfeleltetés, hogyan fedik le a használati esetek a követelményeket

A felhasználói felület és a különböző funkciók szoros kapcsolatban állnak a követelményekkel. A fő cél, hogy a tanulók interaktív módon gyakorolhassák a KRESZ-szabályokat. Az alábbiakban bemutatjuk, hogyan fedik le az egyes UI-elemek a funkcionális követelményeket.

- **Felhasználói Felület ( K4 ):** 
    - A főképernyőn a felhasználó először megadja a nevét, amely lehetővé teszi az egyéni eredmények nyomon követését, majd a **START** gombbal elindíthatja a kvízt. Ezután megjelennek a kérdések és a válaszok, kiegészítve a pontszám és az idő kijelzésével.  
    - A **Ranglista** gomb segítségével megtekinthető a ranglista, ahol a felhasználó láthatja a legjobban teljesítők listáját és ezek eredményeit. 
    - A **Kilépés** gomb a program lezárását teszi lehetővé, felhasználói vezérlést biztosítva.

- **Kvíz képernyő kinézete:**  
  - A kvíz elindítása után, a kérdés mellett egy képkeretben megjelenik egy forgalmi tábla vagy egy rövid KRESZ-szabály (**K4**).  
  - A kérdés szövege és a négy válaszgomb az interaktív kvízlogikát testesíti meg (**K2**).  
  - A jobb felső sarokban látható visszaszámláló az időkorlát kezelését valósítja meg, amely növeli a játék dinamikáját és segít a koncentráció fenntartásában (**K3**).  
  - A folyamatos pontszámkijelzés valós idejű visszajelzést ad a felhasználónak az eddigi teljesítményéről (**K3**).

- **Visszajelzés színkódokkal:**  
  - Helyes válasz esetén a kiválasztott gomb zöld színű lesz (**K2**).  
  - Helytelen válasz esetén piros színezést kap, miközben a helyes válasz is megjelenik a képernyőn (**K2**).  
  - Ez azonnali vizuális megerősítést ad és ezáltal segíti a tanulókat, hogy minél gyorsabban elsajátíthassák a helyes közlekedési szabályokat.

- **Pontszám kijelzés közben és a végén:**  
  - A felhasználó minden helyes válaszért pontot kap, amely a válaszadás gyorsaságától is függ(**K3**). A pontszám dinamikusan frissül minden kérdés után.  
  - A kvíz befejezésekor a végső eredmény az **Eredmény** képernyőn jelenik meg (**K5**).  
  - Ez tartalmazza a helyesen megválaszolt kérdések számát, az összesített pontszámot és a ranglista helyezettjeit (**K5, K7**).

- **Ranglista:**  
  - A ranglista a főmenüből érhető el, ahol a felhasználó megtekintheti a globális ranglistát, amely az összes játékos teljesítményét tartalmazza, a pontszámok pedig egy PostgreSQL adatbázisban kerülnek tárolásra (**K7**).  
  - Ez motivációt nyújt a tanulóknak, hogy újra és újra próbálkozzanak a jobb eredmény eléréséért.  
  - A kérdésekhez használt közlekedési táblák képei segítik a vizuális tanulást és a valós helyzetek felismerését (**K4**).  

  ## Képernyő tervek
  A képernyő tervek részletesen bemutatják az alkalmazás főbb nézeteit, valamint azt, hogy hogyan támogatják a tanulási folyamatot és hogyan motiválják a felhasználót a gyakorlásra.
- **Főképernyő:**
  - A főképernyőn található a **Név** mező, amelynek kitöltése kötelező a játék elindításához.  
    - A mező kitöltése után aktiválódik a **START** gomb.  
    - Üres mező esetén a gomb inaktív, ezzel biztosítva, hogy minden felhasználó nevét kötelezően rögzítsük.
  - Három fő gomb található itt, amelyek az alábbiakban láthatók felsorolva:
    - **START**: elindítja a kvízt, betölti a kérdéseket az adatbázisból.
    - **Ranglista**: a felhasználó a legjobban teljesítők rangsorát láthatja, amelyeket egy PostgreSQL adatbázisból töltünk be.  
    - **Kilépés**: az alkalmazás bezárására szolgál.
  - Letisztult, egyszerű elrendezés, hogy a felhasználó gyorsan eligazodjon.
  - A gombok színe és mérete a felhasználói élményt támogatja, jól láthatóak és könnyen kattinthatóak.
- **Kvíz képernyő:**
  - Felső rész: a képernyő felső részén egy közlekedési tábla képe vagy egy rövid KRESZ-szabály szövege jelenik meg (**K4**).  
  - A kérdés szövege a kép felett helyezkedik el, egyértelműen megfogalmazva, könnyen olvasható betűmérettel.
  - Emellett még a képernyőn négy darab válaszgomb helyezkedik el egyenletes elosztásban, mindegyik gombhoz egyértelmű jelölés tartozik.
  - Jobb felső sarokban:
    - Egy visszaszámláló található itt: alapértelmezetten 40 másodperc áll rendelkezésére a felhasználónak a válaszadásra (**K3**).  
    - Aktuális pontszám: valós idejű visszajelzést ad a teljesítményről. Illetve minden kérdés után automatikusan frissül majd (**K3**).
  - Azonnali vizuális visszajelzés:
    - A helyes válasz: zöld színnel kerül kiemelésre.  
    - A hibás válasz: piros színnel kerül majd kiemelésre és ebben az esetben láthatjuk, hogy mi lett volna a helyes válasz is.
- **Eredmény képernyő:**
  - Itt kerül megjelenítésre a felhasználó végső pontszáma és a helyes válaszok száma is.  
  - Látható az aktuális ranglista is, benne a legjobb eredményekkel, motiválva ezáltal a játékosokat, hogy minél jobban teljesítsenek és izgalmas legyen számukra a kvízjáték.
  - **Újraindítás gomb**: lehetőséget biztosít a játék ismételt elindítására.  
  - **Kilépés gomb**: az alkalmazás bezárására szolgál.  
  - A pontszámok mellett rövid visszajelzés vagy értékelés is megjelenhet, mint például „Nagyszerű eredmény!” vagy „Gyakorlás javasolt”.

- **Ranglista képernyő:**
  - A ranglista a főmenüből érhető el.  
  - Felsorolja a globális rangsorban szereplő felhasználókat a legjobb pontszám szerint.  
  - A lista dinamikusan frissül az adatbázisban lévő adatok alapján(**K7**).    
  - Segít a felhasználóknak a versengésben és a motiváció növelésében.  
  - A rangsor a legmagasabb pontszám szerint csökkenő sorrendben jelenik meg.  
  - A felhasználó új pontszáma automatikusan bekerül az adatbázisba a játék befejezése után.  
  - A ranglista frissítése valós időben történik, amikor a felhasználó végez egy kvízzel.  
  - A lista egyszerű, jól áttekinthető dizájnnal jelenik meg, hogy mindenki könnyen olvashassa.  
  - A nevek és pontszámok jól elkülönített oszlopokban láthatók.  
  - A lista lehetővé teszi a gyors visszajelzést a saját teljesítményről, ezzel ösztönözve a felhasználót, hogy minél többet gyakoroljon.

 - **Reszponzív dizájn**  
   - A felület alapvetően asztali gépre és laptopra lesz tervezve, ezekre a képernyőméretekre optimális az elrendezés. A rendszer esetleg részlegesen alkalmazkodhat más képernyőméretekhez, például tabletekhez vagy kisebb kijelzőkhöz is.  

Összességében a képernyőtervek célja, hogy átlátható, motiváló és könnyen használható tanulási környezetet biztosítsanak a felhasználóknak.  
A vizuális elemek, a színkódok és a folyamatos visszajelzés együttesen segítik a felhasználót a közlekedési szabályok és táblák gyors és hatékony elsajátításában.

  ## Játéklogika és szabályok

A játék motorja a következő funkciókat valósítja meg, amelyek biztosítják a zökkenőmentes játékmenetet:

  | Modul ID | Név és Kifejtés |
| :--- | :--- |
| **K1** | **Adatkezelés**<br>A program a kvízkérdéseket, a válaszokat, a táblák képeit és a hozzájuk tartozó szabályokat egy **PostgreSQL adatbázisból** kéri le a backend segítségével. A frontend a **fetch() API**-n keresztül aszinkron módon kommunikál a **Flask backenddel**, amely feldolgozza a lekéréseket.Ha a fájl nem található, vagy a beolvasás sikertelen, a program hibaüzenetet küld a konzolra. |
| **K2** | **Kvíz Logika**<br>A rendszer véletlenszerűen, ismétlés nélkül választ kérdéseket az **adatbázisból**. A felhasználó válaszát a backend ellenőrzi, majd a frontend azonnali vizuális visszajelzést ad. Helyes válasz esetén zöld jelölés, helytelen esetén piros, ekkor a helyes válasz is zöld színnel kiemelt. |
| **K3** | **Pontszámítás**<br>Minden kérdésre **legfeljebb 1 pont** adható. Mivel a kvíz **10 kérdésből** áll, a megszerezhető maximális pontszám **10 pont**. A helyes válasz pontszáma a válaszadásra fordított időtől függ (40 másodperc időkorlát), a következő képlet szerint: **Pontszám = min(1, 1 * ((40 - eltelt idő) / 40))**. Hibás válasz vagy időtúllépés esetén a pontszám **0**. A végleges pontszám az összesített pontok összege. <br>**Példák a pontszámításra:**<ul><li>Ha 5 másodperc alatt válaszol a játékos: Pontszám = $\min(1, 1 \cdot ((40-5)/40)) = \min(1, 0.875) = 0.875$ pont.</li><li>Ha 30 másodperc alatt válaszol: Pontszám = $\min(1, 1 \cdot ((40-30)/40)) = \min(1, 0.25) = 0.25$ pont.</li><li>Ha 40 másodperc vagy több telik el: Pontszám = 0.</li></ul> |
| **K4** | **Felhasználói Felület**<br>**Főmenü:** név megadása. <br>**Kvíz felület:** forgalmi tábla képe, kérdés szövege, 4 válaszlehetőség (gombok), pillanatnyi pontszám, 40 másodperces visszaszámláló. **Modern, intuitív UX/UI**, elsősorban **asztali gépen/laptopon** való használatra optimalizálva. |
| **K5** | **Eredmény Képernyő**<br>A kvíz végén megjelenik a végső pontszám, a helyes válaszok száma. Gombokkal újraindítható a kvíz vagy kiléphető a programból. |
| **K6** | **Globális pontszám mentése**<br>A kvíz végén a program a felhasználó nevét és pontszámát elküldi a backendnek, amely az adatokat **PostgreSQL adatbázisba** menti, biztosítva a pontszámok tartós és központosított tárolását.
| **K7** | **Globális Ranglista**<br>A főmenüből megtekinthető a legjobban teljesítők globális listája, amely a backendről, a **PostgreSQL adatbázisból** kerül lekérésre, így az minden felhasználó számára egységes és naprakész.