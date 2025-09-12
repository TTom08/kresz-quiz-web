# Funkcionális Specifikáció













































## Megfeleltetés, hogyan fedik le a használati esetek a követelményeket

A felhasználói felület és a különböző funkciók szoros kapcsolatban állnak a követelményekkel. A fő cél, hogy a tanulók interaktív módon gyakorolhassák a KRESZ-szabályokat. Az alábbiakban bemutatjuk, hogyan fedik le az egyes UI-elemek a funkcionális követelményeket.

- **Felhasználói Felület ( K4 ):** 
    - A főképernyőn a felhasználó először megadja a nevét, amely lehetővé teszi az egyéni eredmények nyomon követését, majd a **START** gombbal elindíthatja a kvízt. Ezután megjelennek a kérdések és a válaszok, kiegészítve a pontszám és az idő kijelzésével.  
    - A **Toplista** gomb segítségével megtekinthető a toplista, ahol a felhasználó láthatja a legjobban teljesítők helyi listáját és ezek eredményeit. 
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
  - Ez tartalmazza a helyesen megválaszolt kérdések számát, az összesített pontszámot és a toplista helyezettjeit (**K5, K7**).

- **Toplista:**  
  - A toplista a főmenüből érhető el, ahol a felhasználó megtekintheti a legjobban teljesítők helyi rangsorát. A pontszámok a böngésző helyi tárhelyében (Local Storage) kerülnek mentésre, így a rangsor a következő játék alkalmával is elérhető marad (**K7**).  
  - Ez motivációt nyújt a tanulóknak, hogy újra és újra próbálkozzanak a jobb eredmény eléréséért.  
  - A kérdésekhez használt közlekedési táblák képei segítik a vizuális tanulást és a valós helyzetek felismerését (**K4**).  

  ## Képernyő tervek
  A képernyő tervek részletesen bemutatják az alkalmazás főbb nézeteit, valamint azt, hogy hogyan támogatják a tanulási folyamatot és hogyan motiválják a felhasználót a gyakorlásra.
- **Főképernyő:**
  - A főképernyőn található a **Név** mező, amelynek kitöltése kötelező a játék elindításához.  
    - A mező kitöltése után aktiválódik a **START** gomb.  
    - Üres mező esetén a gomb inaktív, ezzel biztosítva, hogy minden felhasználó nevét kötelezően rögzítsük.
  - Három fő gomb található itt, amelyek az alábbiakban láthatók felsorolva:
    - **START**: elindítja a kvízt, betölti a kérdéseket a `questions.json` fájlból.
    - **Toplista**: a felhasználó a legjobban teljesítők helyi rangsorát láthatja, amelyeket a helyi tárolóból (Local Storage) töltünk be.  
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
  - Látható az aktuális toplista is, benne a legjobb eredményekkel, motiválva ezáltal a játékosokat, hogy minél jobban teljesítsenek és izgalmas legyen számukra a kvízjáték.
  - **Újraindítás gomb**: lehetőséget biztosít a játék ismételt elindítására.  
  - **Kilépés gomb**: az alkalmazás bezárására szolgál.  
  - A pontszámok mellett rövid visszajelzés vagy értékelés is megjelenhet, mint például „Nagyszerű eredmény!” vagy „Gyakorlás javasolt”.

- **Toplista képernyő:**
  - A toplista a főmenüből érhető el.  
  - Felsorolja a helyi rangsorban szereplő felhasználókat a legjobb pontszám szerint.  
  - A lista dinamikusan frissül a JSON fájl vagy a Local Storage tartalma alapján (**K7**).    
  - Segít a felhasználóknak a versengésben és a motiváció növelésében.  
  - A rangsor a legmagasabb pontszám szerint csökkenő sorrendben jelenik meg.  
  - A felhasználó új pontszáma automatikusan bekerül a helyi listába a játék befejezése után.  
  - A toplista frissítése valós időben történik, amikor a felhasználó végez egy kvízzel.  
  - A lista egyszerű, jól áttekinthető dizájnnal jelenik meg, hogy mindenki könnyen olvashassa.  
  - A nevek és pontszámok jól elkülönített oszlopokban láthatók.  
  - A lista lehetővé teszi a gyors visszajelzést a saját teljesítményről, ezzel ösztönözve a felhasználót, hogy minél többet gyakoroljon.

 - **Reszponzív dizájn**  
   - A felület alapvetően asztali gépre és laptopra lesz tervezve, ezekre a képernyőméretekre optimális az elrendezés. A rendszer esetleg részlegesen alkalmazkodhat más képernyőméretekhez, például tabletekhez vagy kisebb kijelzőkhöz is.  

Összességében a képernyőtervek célja, hogy átlátható, motiváló és könnyen használható tanulási környezetet biztosítsanak a felhasználóknak.  
A vizuális elemek, a színkódok és a folyamatos visszajelzés együttesen segítik a felhasználót a közlekedési szabályok és táblák gyors és hatékony elsajátításában.