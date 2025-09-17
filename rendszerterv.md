




















































































# 5. Funkcionális terv
A rendszer célja egy interaktív és játékos webes alkalmazás létrehozása, amely segíti a felhasználókat a **KRESZ szabályok** és közlekedési táblák elsajátításában. A felhasználó pontszámokat kap arról, hogyan sikerült megoldania a feladatokat. A rendszer egyszerű és letisztult felhasználói felülettel rendelkezik, hogy a tanulás zökkenőmentes legyen. A program főszereplője a **Játékos** nevű felhasználó.

## Rendszerszereplők:
<ul>
  <li><b>Játékos</b>: Az a felhasználó, aki a kvízt kitölti, megtekinti az eredményeit és a ranglistát.</li>
</ul>

## Rendszerhasználati esetek és lefutásaik
<ul>
  <li><b>Kvíz indítása</b><br>A Játékos a főmenüből elindíthatja a kvízt. A rendszer véletlenszerűen választ ki kérdéseket az adatbázisból, minden kérdésre 40 másodperces időlimitet szabva.</li>
  <li><b>Válaszadás</b><br>A Játékos a megjelenő kérdésre a megadott válaszlehetőségek közül kattintással adhat választ. A rendszer azonnal visszajelzést ad: a helyes válasz zöld, a helytelen piros színű lesz. Ha a Játékos rossz választ ad, a helyes megoldás is megjelenik, segítve a tanulást.</li>
  <li><b>Pontszámítás</b><br>Minden helyes válaszért a Játékos pontot kap, és a rendszer folyamatosan mutatja az aktuális pontszámot.</li>
  <li><b>Eredmény képernyő</b><br>A kvíz befejezése után egy képernyő jelenik meg, amelyen a Játékos megtekintheti a végső pontszámát, és elmentheti a nevét, valamint a pontszámát a ranglistára.</li>
  <li><b>Ranglista megtekintése</b><br>A Játékos a főmenüből bármikor elérheti a ranglistát, ahol láthatja a legjobb eredményeket elért játékosokat.</li>
  <li><b>Navigáció</b><br>A Játékos a főmenüben navigálhat a Játék indítása, a Ranglista megtekintése és a Kilépés funkciók között.</li>
</ul>