# Experimental Log: Metodičko-pedagoški dizajn i protokol istraživanja

Ovaj dokument predstavlja operativni plan i dnevnik sprovođenja pedagoško-metodičkog dela master rada iz oblasti metodike nastave matematike. Cilj je da se napredni matematički sadržaji (Milerova kubična površ, superkvadrike, Dupinove indikatrise i Plikerov konoid) didaktički oblikuju i empirijski provere u nastavnoj praksi.

---

## 1. Pedagoški i metodički okvir rada

### 1.1. Teorijska polazišta u nastavi matematike
* **Konstruktivizam i vođeno otkrivanje (Guided Discovery):** Umesto gotovih formula, učenicima/studentima se nude interaktivni 3D modeli u kojima samostalno menjaju parametre, formulišu hipoteze o promeni oblika površi i proveravaju ih algebarski.
* **Van Hieleov model razvoja geometrijskog mišljenja:**
  1. *Nivo 1 (Vizuelizacija):* Prepoznavanje oblika u prirodi i arhitekturi (analogija kamenčića na plaži, kupole, sedla, dizajn predmeta).
  2. *Nivo 2 (Analiza):* Uočavanje svojstava kroz ravanske preseke (kako ravni $z = c$ seku superkvadriku ili Milerovu površ).
  3. *Nivo 3 (Apstrakcija / Neformalna dedukcija):* Povezivanje algebarskog zapisa i geometrijskog oblika (razumevanje zašto paran eksponent $d$ daje zatvorenu površ, a neparan otvorenu).
  4. *Nivo 4 (Dedukcija):* Izvođenje jednačina transformacija (aksijalna inverzija u homogenim koordinatama, sferna inverzija oskulatornih krugova).
* **APOS teorija (Action – Process – Object – Schema):**
  * *Akcija:* Učenik unosi konkretne vrednosti parametara ($a, b, c, d$) u GeoGebru i posmatra crtež.
  * *Proces:* Učenik mentalno predviđa kako se površ deformiše pri kontinualnom klizanju parametra $d \in [1, 10]$.
  * *Objekat:* Superkvadrika ili konoid postaju celovit matematički objekat nad kojim se vrše nove operacije (preseci, inverzije).
  * *Šema:* Integracija klasičnih konika, kvadrika i njihovih generalizacija u jedinstvenu geometrijsku mrežu znanja.
* **Didaktička transpozicija (Yves Chevallard):** Prevođenje "naučnog znanja" (*savoir savant* – projektivna i diferencijalna geometrija) u "znanje koje se poučava" (*savoir à enseigner* – vizuelno-eksperimentalni moduli prilagođeni starijim razredima matematičke gimnazije ili uvodnim kursevima geometrije na fakultetu).

---

## 2. Struktura metodičkih modula (Nastavne jedinice)

### Modul 1: Od kružnice do superkvadrika – Eksperimentisanje eksponentom
* **Ciljna grupa:** Učenici 3. i 4. razreda gimnazije (posebno učenici specijalizovanih matematičkih odeljenja i dodatne nastave) ili studenti 1. godine matematike.
* **Metodički cilj:** Razumevanje uticaja promene stepena jednačine na geometrijski oblik u ravni $\mathbb{R}^2$ i prostoru $\mathbb{R}^3$.
* **Tok aktivnosti:**
  1. *Korak 1 (2D uvod – Lameove krive):* Učenici u GeoGebri crtaju krivu $\left|\frac{x}{a}\right|^d + \left|\frac{y}{b}\right|^d = 1$ sa klizačem $d \in [0.5, 10]$. Ispituju specijalne slučajeve: $d = 1$ (romb), $d = 2$ (elipsa), $d \to \infty$ (pravougaonik).
  2. *Korak 2 (3D proširenje – Superelipsoid):* Prelazak na $\left|\frac{x}{a}\right|^d + \left|\frac{y}{b}\right|^d + \left|\frac{z}{c}\right|^d = 1$. Učenici otkrivaju kako nastaje prelaz od oktaedra preko sfere do zaobljene kocke.
  3. *Korak 3 (Algebarska diskusija – Parni naspram neparnih stepena):* Uklanjanje apsolutnih vrednosti u $\left(\frac{x}{a}\right)^d + \left(\frac{y}{b}\right)^d + \left(\frac{z}{c}\right)^d = 1$ i upoređivanje grafika za $d = 2$ i $d = 3$. Diskusija o ograničenosti površi.
  4. *Korak 4 (Korelacija sa praksom):* Analiza industrijskog dizajna (oblik ekrana pametnih telefona – *squircle*, dizajn ambalaže, 3D modelovanje u igrama).

### Modul 2: Geometrijske transformacije u prostoru – Aksijalna inverzija i Milerova površ
* **Metodički cilj:** Proširenje srednjoškolskog pojma inverzije u odnosu na krug na trodimenzionalni prostor i razumevanje nastanka kubičnih površi.
* **Tok aktivnosti:**
  1. *Korak 1 (Aktivacija predznanja):* Kratko ponavljanje ravanske inverzije u odnosu na krug poluprečnika $R$: $OP \cdot OP' = R^2$, gde se prave koje ne prolaze kroz centar preslikavaju u krugove.
  2. *Korak 2 (Podizanje u treću dimenziju):* Postavljanje pitanja: *"Šta ako krug zamenimo beskonačnim cilindrom $x^2 + y^2 = R^2$, a $z$-koordinatu ostavimo nepromenjenom?"*
  3. *Korak 3 (Vizuelizacija preslikavanja ravni):* Posmatranje kako se kosa ravan $a + b x + c y + d z = 0$ transformiše u Milerovu kubičnu površ $(x^2 + y^2)(a + d z) + R^2(b x + c y) = 0$.
  4. *Korak 4 (Istraživanje preseka):* Učenici pomeraju horizontalnu ravan $z = k$ u GeoGebri 3D i beleže koje poznate krive drugog reda (krugove, elipse, hiperbole) uočavaju u preseku.

### Modul 3: Zakrivljenost površi i pravolinijske površi – Dupinove indikatrise i Plikerov konoid
* **Metodički cilj:** Razvijanje intuicije o lokalnom ponašanju glatkih površi i razumevanje kako se složene zakrivljene površi mogu konstruisati pomoću pravih linija.
* **Tok aktivnosti:**
  1. *Korak 1 (Taktilna i vizuelna analogija):* Klasifikacija tačaka na svakodnevnim objektima: vrh jajeta (eliptička tačka), prevoj na planinskom sedlu ili čips (hiperbolička tačka), omotač valjka (parabolička tačka).
  2. *Korak 2 (Preseci normalnim ravnima):* Korišćenje 3D apleta za rotaciju normalne ravni oko normale površi i očitavanje promene krivine (vizuelni doživljaj Ojlerove formule $\kappa_n(\theta) = \kappa_1 \cos^2\theta + \kappa_2 \sin^2\theta$ i Dupinove indikatrise).
  3. *Korak 3 (Od krugova do pravih linija – Plikerov konoid):* Prikaz generisanja Plikerovog konoida $z(x^2 + y^2) = c x y$ pomoću familije pravih koje pod pravim uglom seku $z$-osu.
  4. *Korak 4 (Interdisciplinarna primena):* Primena pravolinijskih površi u građevinarstvu i arhitekturi (mogućnost izrade zakrivljenih betonskih ili drvenih konstrukcija pomoću pravih oplatnih greda) i u optici.

---

## 3. Dnevnik realizacije pedagoškog eksperimenta (Log Entries)

### [FAZA 0] Definisanje istraživačkih pitanja i hipoteza
* **Status:** Planirano / Spremno za realizaciju
* **Glavno istraživačko pitanje:** U kojoj meri primena dinamičke 3D vizuelizacije i metode vođenog otkrivanja pri obradi generalizovanih kvadrika doprinosi razumevanju veze između algebarskog zapisa i prostornog oblika kod učenika/studenata?
* **Hipoteze:**
  * $H_1$: Učenici koji obrađuju generalizovane kvadrike kroz interaktivne GeoGebra 3D modele ostvaruju statistički značajno bolje rezultate na testu prostorne vizuelizacije i prepoznavanja ravanskih preseka u odnosu na tradicionalni frontalni pristup.
  * $H_2$: Korišćenje analognih primera i postepene generalizacije (2D $\to$ 3D) smanjuje kognitivno opterećenje i povećava motivaciju za izučavanje naprednih geometrijskih tema.

### [FAZA 1] Priprema i revizija teorijsko-metodičkog teksta rada
* **Status:** U toku
* **Aktivnosti:**
  * Dopuniti nedostajuće formule (`___`) u teorijskom delu rada.
  * Uskladiti uvodne analogije (kamenčići na plaži) sa sva tri stuba generalizacije.
  * Izraditi pojmovnu mapu koja povezuje srednjoškolsko gradivo sa sadržajem master rada.

### [FAZA 2] Razvoj nastavnih instrumenata i digitalnih resursa
* **Status:** Naredni korak
* **Artefakti koje treba kreirati:**
  1. **Tri interaktivna GeoGebra 3D apleta** (za superkvadrike, Milerovu površ i Plikerov konoid) sa jasno označenim klizačima i ravnima preseka.
  2. **Radni listovi za učenike** koncipirani po koracima vođenog otkrivanja (sa praznim tabelama za beleženje zapažanja i pitanjima za zaključivanje).
  3. **Inicijalni test (Pre-test):** Provera poznavanja klasičnih konika, kvadrika i prostorne orijentacije (trajanje: 15 minuta).
  4. **Finalni test (Post-test):** Zadaci prepoznavanja oblika na osnovu jednačine, određivanja ravanskih preseka i primene u realnom kontekstu (trajanje: 25 minuta).
  5. **Upitnik o stavovima i samoproceni (Likertova skala 1–5):** Procena jasnoće vizuelizacije, zanimljivosti teme i nivoa kognitivnog angažovanja.

### [FAZA 3] Sprovođenje pedagoške radionice / eksperimenta
* **Status:** Čeka realizaciju u školi / na fakultetu
* **Planirani uzorak:** Jedno odeljenje matematičke gimnazije ($N \approx 20\text{--}25$ učenika) ili grupa studenata osnovnih studija matematike (podeljena na eksperimentalnu grupu sa GeoGebra radionicom i kontrolnu grupu sa klasičnim predavanjem, ili studija slučaja sa merenjem pre i posle intervencije).
* **Trajanje:** Dva školska časa (blok čas od $90$ minuta) ili tri tematske radionice po $45$ minuta.
* **Protokol beleženja toka časa (Opservacioni list):**
  * Beleženje najčešćih učeničkih zabluda (npr. mešanje parametara razmere $a, b, c$ sa eksponentom oblika $d$; teškoće u zamišljanju neograničenih površi za neparno $d$).
  * Praćenje trenutaka "aha-efekta" prilikom pomeranja ravni preseka na Milerovoj površi i Plikerovom konoidu.

### [FAZA 4] Obrada podataka i evaluacija rezultata
* **Status:** Planirano nakon Faze 3
* **Kvantitativna analiza:** Poređenje prosečnog broja poena na pre-testu i post-testu (t-test za zavisne ili nezavisne uzorke, izračunavanje koeficijenta napredovanja).
* **Kvalitativna analiza:** Analiza učeničkih odgovora sa radnih listova, klasifikacija tipičnih grešaka i analiza komentara iz upitnika.

### [FAZA 5] Integracija u master rad i pisanje Zaključka
* **Status:** Završna faza
* **Cilj:** Povezati teorijske zaključke o bogatstvu oblika generalizovanih kvadrika sa empirijskim dokazima o efikasnosti njihove vizuelne i metodičke obrade u nastavi.

---

## 4. Primeri istraživačkih zadataka za radni list (Didaktički prilog)

1. **Zadatak (Superkvadrike):** Posmatraj jednačinu $\left|\frac{x}{2}\right|^d + \left|\frac{y}{2}\right|^d + \left|\frac{z}{2}\right|^d = 1$.
   * *a)* Kako izgleda presek ove površi sa ravni $z = 0$ kada je $d = 1$, kada je $d = 2$, a kada je $d = 6$?
   * *b)* Zašto se zapremina tela ograničenog ovom površi povećava kako eksponent $d$ raste, ali nikada ne prelazi zapreminu kocke stranice $4$?
2. **Zadatak (Milerova površ):** Data je ravan $z = 2$ i Milerova kubična površ dobijena aksijalnom inverzijom ravni $x + z - 3 = 0$ u odnosu na cilindar $x^2 + y^2 = 1$.
   * *a)* Odredi algebarsku jednačinu presečne krive u ravni $z = 2$.
   * *b)* Koju geometrijsku figuru predstavlja dobijeni presek i koliki je njen poluprečnik?
3. **Zadatak (Dupinova indikatrisa i Plikerov konoid):**
   * *a)* Odredi tip tačke na površi ako su njene glavne krivine $\kappa_1 = 3$ i $\kappa_2 = -2$. Kakvog je oblika njena Dupinova indikatrisa?
   * *b)* Objasni svojim rečima zašto se Plikerov konoid naziva *pravolinijskom površi* iako na prvi pogled izgleda potpuno zakrivljeno.