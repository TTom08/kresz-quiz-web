# Funkcionális Specifikáció













































## Megfeleltetés, hogyan fedik le a használati esetek a követelményeket

A felhasználói felület és a különböző funkciók szoros kapcsolatban állnak a követelményekkel. A fő cél, hogy a tanulók interaktív módon gyakorolhassák a KRESZ-szabályokat. Az alábbiakban bemutatjuk, hogyan fedik le az egyes UI-elemek a funkcionális követelményeket.

- **Felhasználói Felület ( K4 ):** 
    - A főképernyőn a felhasználó először megadja a nevét, amely lehetővé teszi az egyéni eredmények nyomon követését, majd a **Start** gombbal elindíthatja a kvízt. Ezután megjelennek a kérdések és a válaszok, kiegészítve a pontszám és az idő kijelzésével.  
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