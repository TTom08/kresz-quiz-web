# Követelmény Specifikáció

## Áttekintés

A projekt célja egy olyan webes kvízjáték létrehozása, amely segíti a felhasználókat a KRESZ szabályainak elsajátításában és gyakorlásában. A KRESZ ismerete minden forgalomban közlekedő számára elengedhetetlen, de a tanulási folyamat gyakran unalmas és nehezen követhető. A mi célunk egy olyan eszköz készítése, amely játékos formában nyújt lehetőséget a tudás fejlesztésére.  

A választott platform a web, mivel ez a legkönnyebben elérhető mindenki számára. Nincs szükség telepítésre, elegendő egy böngésző, így a felhasználók gyorsan kipróbálhatják a játékot bármilyen nehézség elkerülésével. Ez különösen fontos, mert elsősorban a célközönség a fiatalság, amely jogosítványra készülő tanulókból és friss vezetőkből áll, akik már megszokták az online alkalmazások használatát.  

A projekt jól illeszkedik egyetemi miniprojekt kereteibe, mert kellően kicsi ahhoz, hogy rövid idő alatt megvalósítható legyen, ugyanakkor elég összetett ahhoz, hogy több csapattag párhuzamosan tudjon rajta dolgozni. A játék tartalmaz adatkezelést (JSON kérdésbázis), interaktív felhasználói felületet (kérdés-válasz megjelenítés), valamint pontozási rendszert, ami elegendő komplexitást biztosít a projekt értékeléséhez.

## Jelenlegi helyzet

Jelenleg a KRESZ vizsgára való felkészülés már online felületen keresztül történik, viszont úgy érezzük, hogy más megoldásokat alkalmazva jobban és könnyebben tudnának tanulni az emberek. Ezek a weboldalak (mint az e-Titán) sokszor monotonok, nehezen motiválják a tanulókat, és nem adnak azonnali visszajelzést a teljesítményről. Nem nyújtanak játékélményt, inkább a vizsga környezetét próbálják szimulálni.  

A hagyományos tesztelés nagy hátránya, hogy nem interaktív. A tanuló egyszerűen kiválasztja a választ, majd később ellenőrzi az eredményeket, ami nem annyira motiváló. Ráadásul a hibákból való tanulás is lassabb, hiszen nincs azonnali visszajelzés arról, hogy miért volt helytelen egy adott válasz. Ez csökkenti a tanulás hatékonyságát, és sokak számára fárasztóvá, sőt demotiválóvá teszi a felkészülést.

## Vágyálom rendszer

Az ideális rendszer egy olyan színes és interaktív webes alkalmazás, amely játékos formában tanítja a KRESZ szabályokat. A kérdések nem csupán szövegesek, hanem képekkel is kiegészíthetők, például közlekedési táblák vagy forgalmi szituációk illusztrációival. Ez jelentősen növeli a tanulás hatékonyságát, mert a vizuális elemek jobban rögzülnek a felhasználók memóriájában.  

A játék tartalmazna ranglistát is, amely motivációt adna a felhasználóknak. A tanulók láthatnák saját eredményeiket, és összehasonlíthatnák más játékosokkal, ami egészséges versenyt szül. Az azonnali visszajelzés – például a helyes válasz zöld színnel, a hibás válasz pirossal – segíti a gyorsabb tanulást és a hibák elkerülését a jövőben.  

Az álomrendszer tehát nem csak egy kvíz lenne, hanem egy tanulási élmény. Egy olyan platform, ahol a felhasználó nem kényszerből tanul, hanem sokkal könnyebben és majdnem szórakozva sajátítja el a közlekedési szabályokat. Ezáltal a felkészülés hatékonyabb, gyorsabb és élvezetesebb lesz, ami végső soron jobb vizsgaeredményeket és biztonságosabb közlekedést eredményezhet.

## Funkcionális követelmények

Az alkalmazás fő célja, hogy egy interaktív KRESZ-kvízt biztosítson a felhasználóknak, amely lehetővé teszi a közlekedési szabályok és táblák játékos formában történő gyakorlását. A program főmenüje biztosítja a kvíz indítását, a korábban elért pontszámok megtekintését,a játékos nevének megadását, valamint az alkalmazás bezárását is. A kvíz kérdései véletlenszerű sorrendben jelennek meg, így minden próbálkozás új kihívást jelent, ami fenntartja a játékos érdeklődését.

A kérdésekhez egy közlekedési tábla képe vagy egy rövid KRESZ-szabály tartozik, és ezekhez több válaszlehetőség is kapcsolódik. A felhasználó kattintással adhatja meg válaszát, amelynek helyességéről azonnali visszajelzést kap. Helyes válasz esetén a gomb zöld színt kap, hibás válasz esetén pirosra vált, emellett a helyes megoldás is megjelenik, hogy segítse a tanulási folyamatot. Minden helyes válaszért pont jár, a pontszám pedig a kitöltés közben folyamatosan nyomon követhető.

A rendszer időzítőt is tartalmaz, amely 40 másodpercet biztosít a kérdések megválaszolására. Ez fokozza a játék izgalmát, valamint a vizsgahelyzethez hasonló nyomást gyakorol a játékosra, ezzel felkészítve őt az éles vizsgára. A kvíz befejezése után az alkalmazás egy eredmény képernyőt jelenít meg, amely tartalmazza a felhasználó végső pontszámát, a helyesen megválaszolt kérdések számát, valamint egy ranglistát, ahol a felhasználó megtekintheti a legjobban teljesítők globális rangsorát.

A ranglista lehetővé teszi a felhasználók számára, hogy összehasonlítsák teljesítményüket és motivációt nyerjenek a további gyakorláshoz. Az összes funkció együttesen egy könnyen kezelhető és vizuálisan vonzó rendszert alkot, amely nagyban elősegíti a KRESZ-tanulás folyamatát.

## Nem funkcionális követelmények és technológia

Ez a szakasz részletezi a kvíz alkalmazásunk technológiai döntéseit és nem funkcionális követelményeit. A célunk egy olyan termék létrehozása, amely hatékony, megbízható és felhasználóbarát.

A felhasználói felület megvalósításához frontendhez **HTML**, **CSS** és **JavaScript** nyelveket használunk, backendhez pedig **Pythont**, ezen belül **Flask** keretrendszert. A kvíz kérdései és válaszai egy **PostgreSQL**-adatbázisba vannak tárolva. A kvíz legvégén pedig rangsorolva lesznek a játékosok, melyeket ugyancsak egy **PostgreSQL**-adatbázisba tárolunk.

**Teljesítmény**: Az alkalmazásnak **gyorsan be kell töltenie** a böngészőben, és gördülékenyen kell futnia a felhasználói interakciók során. A **Python/Flask** backend gyorsan képes lekérdezni a kérdéseket a PostgreSQL adatbázisból, így biztosítva a zökkenőmentes élményt.

**Megbízhatóság**: Az alkalmazásnak **stabilnak** kell lennie, **nem szabad lefagynia** vagy **leállnia** a használat során. A **PostgreSQL** robusztus adatkezelése garantálja, hogy minden kvízkérdés és a felhasználói rangsor hibátlanul és megbízhatóan elérhető legyen.

**Felhasználóbarát UI**: A felület intuitív és könnyen kezelhető. A **HTML**, **CSS** és **JavaScript** kombinációja biztosítja, hogy a design letisztult és a navigáció egyszerű legyen, a felhasználói élmény optimalizálása érdekében.

**Korlátok**: Mivel a felhasználók **eredményeit** és **rangsorát PostgreSQL** adatbázisban tároljuk, az adatok tartósan megmaradnak, és a felhasználók visszatérő munkamenetek során is elérhetik a korábbi eredményeiket. A rendszer lehetővé teszi, hogy a játékosok ranglistája **folyamatosan frissüljön** és a legmagasabb pontszámokat tároljuk.


## Jelenlegi üzleti folyamatok modellje

A KRESZ-tanulás Magyarországon ma már elsősorban digitális platformokon keresztül történik, amelyek online teszteket és vizsgaszimulációkat kínálnak. Ezek a megoldások azonban többnyire a hagyományos tananyag digitalizált másai, statikus kérdésekkel, szöveges magyarázatokkal és kevés vizuális visszajelzéssel.  Hiányoznak belőlük az interaktív elemek, mint például az időzítő vagy a pontszámok versenyszerű összehasonlítása.  

A meglévő platformok nem mindig alkalmazkodnak a felhasználó egyéni tempójához, így a diákok gyakran nem kapnak azonnali megerősítést, ami lassítja a tanulási folyamatot és csökkenti a motiváltságukat.  
  
A projektünk célja, hogy egy interaktív kvízjátékot biztosítson, amely a közlekedési táblák felismerésére és a KRESZ-szabályok elsajátítására épül, miközben a játékos elemek, mint az időzítő és a toplista, ösztönzik a tanulókat a gyakorlásra és a fejlődésre.

## Igényelt üzleti folyamatok modellje

Az alkalmazásunk a tanulási folyamatot interaktívvá és dinamikussá teszi, játékos elemekkel kiegészítve ezt. A felhasználók egy digitális felületen, saját tempójukban gyakorolhatják a KRESZ-szabályokat és a közlekedési táblákat. A rendszer azonnali visszajelzést ad a válaszok helyességéről, így a hibák gyorsan korrigálhatók, és ezáltal a tanulás is hatékonyabbá válik. A pontozási rendszer és az időzítő fokozza a kihívást, valamint a toplista motivációt nyújt a további gyakorláshoz.

Ez az alkalmazás tehát kiegészíti a meglévő online tanulási módszereket és modern, hatékony alternatívát nyújt a KRESZ-tudás elsajátításához. 

## Követelménylista

| Modul ID | Név és Kifejtés |
| :--- | :--- |
| **K1** | **Adatkezelés**<br>A program a kvízkérdéseket, válaszokat, a táblák képeit és a hozzájuk tartozó szabályokat egy **PostgreSQL adatbázisból** olvassa be. Ha az adatok nem elérhetőek, a program hibakezeléssel reagál, és megfelelő hibaüzenetet küld. |
| **K2** | **Kvíz Logika**<br>A program véletlenszerűen választ ki kérdéseket a betöltött adatok közül. A felhasználó válaszát összehasonlítja a helyes válasszal. Ha rossz választ ad a felhasználó, a program attól még kiírja mi volt a helyes. |
| **K3** | **Pontszámítás**<br>Helyes válasz esetén pontot ad a felhasználónak. A pontszám a válaszadás **idejétől** is függ. |
| **K4** | **Felhasználói Felület**<br>A felhasználó beírhatja a nevét, majd **megjeleníti** a kvíz elemeit: **közlekedési tábla képe vagy szöveges KRESZ szabály**, kérdés, válaszlehetőségek gombjai, pontszám. |
| **K5** | **Eredmény Képernyő**<br>A kvíz végén **megjeleníti** a végleges pontszámot, és lehetővé teszi a kvíz újraindítását vagy a kilépést. |
| **K6** | **Adatbázisba mentés**<br>A kvíz végén a program a felhasználó nevét és pontszámát elküldi a backendnek, amely az adatokat a **PostgreSQL adatbázisba** menti a tartós tárolás érdekében.
| **K7** | **Globális Ranglista**<br>A főmenüből megtekinthető a legjobban teljesítők listája, amely a **PostgreSQL adatbázisból** kerül lekérésre, így az eredmények minden felhasználó számára elérhetőek.

*Alkalmazásunkkal a hagyományos tanulási folyamatot egy interaktív és dinamikus online élménnyé tesszük. A diákok digitális felületen, játékos formában tesztelhetik tudásukat, és **azonnali visszajelzést** kapnak. A rendszerünk az adatok központosított, **adatbázisba** való mentésével lehetővé teszi a felhasználói rangsorok valós idejű, globális frissítését, ami motiváló versenyt hoz létre. A platform lehetőséget teremt az önálló és egyéni tempójú tanulásra, miközben egy közösségi elemet is beépít a ranglista funkción keresztül, ami a hagyományos oktatásban sokszor nem valósul meg.
*
