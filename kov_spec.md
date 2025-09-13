# Követelmény Specifikáció

## Áttekintés

A projekt célja egy olyan webes kvízjáték létrehozása, amely segíti a felhasználókat a KRESZ szabályainak elsajátításában és gyakorlásában. A KRESZ ismerete minden forgalomban közlekedő számára elengedhetetlen, de a tanulási folyamat gyakran unalmas és nehezen követhető. A mi célunk egy olyan eszköz készítése, amely játékos formában nyújt lehetőséget a tudás fejlesztésére.  

A választott platform a web, mivel ez a legkönnyebben elérhető mindenki számára. Nincs szükség telepítésre, elegendő egy böngésző, így a felhasználók gyorsan kipróbálhatják a játékot bármilyen nehézség elkerülésével. Ez különösen fontos, mert elsősorban a célközönség a fiatalság, amely jogosítványra készülő tanulókból és friss vezetőkből áll, akik már megszokták az online alkalmazások használatát.  

A projekt jól illeszkedik egyetemi miniprojekt kereteibe, mert kellően kicsi ahhoz, hogy rövid idő alatt megvalósítható legyen, ugyanakkor elég összetett ahhoz, hogy több csapattag párhuzamosan tudjon rajta dolgozni. A játék tartalmaz adatkezelést (JSON kérdésbázis), interaktív felhasználói felületet (kérdés-válasz megjelenítés), valamint pontozási rendszert, ami elegendő komplexitást biztosít a projekt értékeléséhez.

## Jelenlegi helyzet

Jelenleg a KRESZ vizsgára való felkészülés már online felületen keresztül történik, viszont úgy érezzük, hogy más megoldásokat alkalmazva jobban és könnyebben tudnának tanulni az emberek. Ezek a weboldalak (mint az e-Titán) sokszor monotonok, nehezen motiválják a tanulókat, és nem adnak azonnali visszajelzést a teljesítményről. Nem nyújtanak játékélményt, inkább a vizsga környezetét próbálják szimulálni.  

A hagyományos tesztelés nagy hátránya, hogy nem interaktív. A tanuló egyszerűen kiválasztja a választ, majd később ellenőrzi az eredményeket, ami nem annyira motiváló. Ráadásul a hibákból való tanulás is lassabb, hiszen nincs azonnali visszajelzés arról, hogy miért volt helytelen egy adott válasz. Ez csökkenti a tanulás hatékonyságát, és sokak számára fárasztóvá, sőt demotiválóvá teszi a felkészülést.

## Vágyálom rendszer



## Funkcionális követelmények

Az alkalmazás fő célja, hogy egy interaktív KRESZ-kvízt biztosítson a felhasználóknak, amely lehetővé teszi a közlekedési szabályok és táblák játékos formában történő gyakorlását. A program főmenüje biztosítja a kvíz indítását, a korábban elért pontszámok megtekintését,a játékos nevének megadását, valamint az alkalmazás bezárását is. A kvíz kérdései véletlenszerű sorrendben jelennek meg, így minden próbálkozás új kihívást jelent, ami fenntartja a játékos érdeklődését.

A kérdésekhez egy közlekedési tábla képe vagy egy rövid KRESZ-szabály tartozik, és ezekhez több válaszlehetőség is kapcsolódik. A felhasználó kattintással adhatja meg válaszát, amelynek helyességéről azonnali visszajelzést kap. Helyes válasz esetén a gomb zöld színt kap, hibás válasz esetén pirosra vált, emellett a helyes megoldás is megjelenik, hogy segítse a tanulási folyamatot. Minden helyes válaszért pont jár, a pontszám pedig a kitöltés közben folyamatosan nyomon követhető.

A rendszer időzítőt is tartalmaz, amely 40 másodpercet biztosít a kérdések megválaszolására. Ez fokozza a játék izgalmát, valamint a vizsgahelyzethez hasonló nyomást gyakorol a játékosra, ezzel felkészítve őt az éles vizsgára. A kvíz befejezése után az alkalmazás egy eredmény képernyőt jelenít meg, amely tartalmazza a felhasználó végső pontszámát, a helyesen megválaszolt kérdések számát, valamint egy toplistát, ahol a felhasználó megtekintheti a legjobban teljesítők helyi rangsorát.

A toplista lehetővé teszi a felhasználók számára, hogy összehasonlítsák teljesítményüket és motivációt nyerjenek a további gyakorláshoz. Az összes funkció együttesen egy könnyen kezelhető és vizuálisan vonzó rendszert alkot, amely nagyban elősegíti a KRESZ-tanulás folyamatát.

## Nem funkcionális követelmények és technológia

Ez a szakasz részletezi a kvíz alkalmazásunk technológiai döntéseit és nem funkcionális követelményeit. A célunk egy olyan termék létrehozása, amely hatékony, megbízható és felhasználóbarát.

A felhasználói felület megvalósításához **HTML**, **CSS** és **JavaScript** nyelveket használunk. A kvíz kérdései és válaszai egy **statikus JSON**-fájlban vannak tárolva. Ez a megközelítés egyszerűsíti az adatkezelést, mivel nincs szükség adatbázisra vagy szerveroldali adatokra.

**Teljesítmény**: Az alkalmazásnak **gyorsan be kell töltenie** a böngészőben, és gördülékenyen kell futnia a felhasználói interakciók során. A statikus JSON-fájl használata hozzájárul ehhez, mivel a böngészőnek nem kell szerveroldali kérésekre várnia.

**Megbízhatóság**: Az alkalmazásnak stabilnak kell lennie. Ez magában foglalja, hogy **ne fagyjon le** vagy **álljon le** a használat során, és minden kvízkérdés **elérhető** és **hibátlanul** megjelenjen.

**Felhasználóbarát UI**: A felület intuitív és könnyen kezelhető.

**Korlátok**: Mivel minden adat a kliens böngészőjében van, a felhasználók eredményei vagy a kvíz állapota nem menthető el a munkamenetek között. A felhasználóknak minden alkalommal elölről kell kezdeniük a kvízt.


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
| **K1** | **Adatkezelés**<br>A program képes a kérdéseket, válaszokat, a táblák képeit és a hozzájuk tartozó szabályokat egy **Json fájlból** beolvasni. Ha nem találja az adatokat, akkor hibaüzenetet küld, mert hibakezelést is szeretnénk belerakni. |
| **K2** | **Kvíz Logika**<br>A program véletlenszerűen választ ki kérdéseket a betöltött adatok közül. A felhasználó válaszát összehasonlítja a helyes válasszal. Ha rossz választ ad a felhasználó, a program attól még kiírja mi volt a helyes. |
| **K3** | **Pontszámítás**<br>Helyes válasz esetén pontot ad a felhasználónak. A pontszám a válaszadás **idejétől** is függ. |
| **K4** | **Felhasználói Felület**<br>A felhasználó beírhatja a nevét, majd **megjeleníti** a kvíz elemeit: **közlekedési tábla képe vagy szöveges kresz szabály**, kérdés, válaszlehetőségek gombjai, pontszám. |
| **K5** | **Eredmény Képernyő**<br>A kvíz végén **megjeleníti** a végleges pontszámot, és lehetővé teszi a kvíz újraindítását vagy a kilépést. |
| **K6** | **Helyi pontszám mentése**<br>A program a kvíz végén elmenti a felhasználó nevét és pontszámát a böngésző helyi tárhelyére (Local Storage).
| **K7** | **Helyi Toplista**<br>A főmenüből megtekinthető a legjobban teljesítők helyi listája, amely a böngészőben van eltárolva.

*Az alkalmazásunkkal a hagyományos tanulási folyamatot interaktívvá és dinamikussá tesszük. A diákok digitális felületen, játékos formában tesztelhetik tudásukat, azonnali visszajelzést kapva. A platform lehetőséget teremt az **önálló és egyéni tempójú tanulásra**, ami a hagyományos oktatásban sokszor nem valósul meg.*
