




















































































# Funkcionális terv
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

## Menü-hierarchia
Az alkalmazás menüstruktúrája egyszerű és könnyen átlátható, egyértelmű navigációt biztosítva a felhasználónak. A főmenüben a játékos a legfontosabb funkciók közül választhat.
<ul>
  <li><b>Játék indítása</b>: Ezzel a gombbal indíthatja el a felhasználó a KRESZ kvízt.</li>
  <li><b>Ranglista</b>: Ide kattintva megtekintheti a legjobb pontszámokat elért játékosok listáját.</li>
  <li><b>Kilépés</b>: Ez a funkció bezárja az alkalmazást.</li>
</ul>

# Fizikai környezet

A projekt egy webes alkalmazás formájában valósul meg, amely a felhasználó böngészőjében fut. A rendszer telepítést nem igényel, minden a webes környezeten keresztül történik.

* **Platform:** Az alkalmazás bármilyen eszközön (asztali számítógép, laptop, táblagép, valamint esetlegesen kisebb képernyő méretek) futtatható, amely rendelkezik modern webböngészővel, mint például a Google Chrome, Mozilla Firefox, vagy Microsoft Edge.
* **Hálózat:** A webalkalmazás a kliens (böngésző) és a szerver (backend) között kommunikál az interneten keresztül.
* **Fejlesztői eszközök:**
    * **Backend:** Python, Flask keretrendszer, PostgreSQL adatbázis.
    * **Frontend:** HTML, CSS, JavaScript.
    * **Kódszerkesztő:** Visual Studio Code és PyCharm.
    * **Adatbázis kezelő:** pgAdmin.
    * **Verziókezelés:** Git és GitHub.

# Absztrakt domain modell

Az absztrakt domain modell a rendszer fő entitásait és a köztük lévő kapcsolatokat írja le, segítve a rendszer logikai felépítésének megértését.

* **Játékos:** A felhasználó, akinek a neve és a pontszáma tárolásra kerül. Ez az entitás tartalmazza a **Játékos ID-t**, a **Nevet**, és a **Pontszámot**.
* **Kérdés:** Egy kvízkérdés, amely több válaszlehetőséggel rendelkezik. Tartalmazza a **Kérdés szövegét**, az opcionális **Kép elérési útját** és a **Helyes válasz ID-t**.
* **Válaszlehetőség:** A Kérdéshez tartozó lehetséges válaszok. Minden válaszlehetőségnek van egy egyedi **Válasz ID-je** és egy **Szövege**.
* **Ranglista:** A legjobb pontszámokat tároló lista. Ez az entitás a **Játékos nevével** és a hozzá tartozó **Pontszámmal** kapcsolódik a Játékos entitáshoz.

