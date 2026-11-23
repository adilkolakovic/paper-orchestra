# Idea Sparse: Generalizovane kvadrike u nastavi i vizuelizaciji matematike

## 1. Osnovni podaci i identitet rada
* **Tema:** Generalizovane kvadrike
* **Studijski program:** Master akademske studije matematike – nastavnički smer
* **Ključna ideja (Core Thesis):** Klasične površi drugog reda (kvadrike) predstavljaju temelj analitičke i projektivne geometrije, ali njihova prava obrazovna i naučna snaga dolazi do izražaja tek kada se posmatraju kroz proces *matematičke generalizacije*. Rad povezuje tri različita pravca generalizacije kvadrika (algebarsko-projektivni, parametarsko-stepeni i diferencijalno-geometrijski) sa savremenom metodičkom transpozicijom u nastavi matematike pomoću dinamičkog softvera za 3D vizuelizaciju.

---

## 2. Matematičko jezgro rada (Tri stuba generalizacije)

### Stub I: Algebarsko-projektivna generalizacija – Milerova (Müller) kubična površ
* **Polazni pojam:** Ravanska inverzija u odnosu na krug (poznata iz srednjoškolske geometrije) proširena u prostor $\mathbb{R}^3$ kao aksijalna (cilindrična) inverzija u odnosu na osnovni rotacioni cilindar $x^2 + y^2 = R^2$.
* **Matematička formulacija:**
  * Afine jednačine aksijalne inverzije tačke $P(x, y, z)$:
    $$x' = \frac{R^2 x}{x^2 + y^2}, \quad y' = \frac{R^2 y}{x^2 + y^2}, \quad z' = z$$
  * Homogene koordinate $(x_0 : x_1 : x_2 : x_3)$, gde je $x = \frac{x_1}{x_0}$, $y = \frac{x_2}{x_0}$, $z = \frac{x_3}{x_0}$:
    $$x_0' : x_1' : x_2' : x_3' = (x_1^2 + x_2^2)x_0 : R^2 x_0^2 x_1 : R^2 x_0^2 x_2 : (x_1^2 + x_2^2)x_3$$
  * Preslikavanje generičke ravni $a x_0 + b x_1 + c x_2 + d x_3 = 0$ daje Milerovu kubičnu površ:
    $$a(x_1^2 + x_2^2)x_0 + b R^2 x_0^2 x_1 + c R^2 x_0^2 x_2 + d(x_1^2 + x_2^2)x_3 = 0$$
* **Geometrijski uvid:** Preseci ove površi sa ravnima $z = \text{const}$ i cilindrima daju familije krugova, elipsi i hiperbola, čime se direktno povezuje kubična površ sa klasičnim konikama.

### Stub II: Stepena i parametarska generalizacija – Superkvadrike
* **Polazni pojam:** Zamena eksponenta $2$ u kanonskim jednačinama elipsoida i hiperboloida proizvoljnim prirodnim ili realnim stepenom $d$.
* **Matematička formulacija:**
  * Implicitna jednačina superkvadrike:
    $$\left(\frac{x}{a}\right)^d + \left(\frac{y}{b}\right)^d + \left(\frac{z}{c}\right)^d = 1 \quad \text{ili} \quad \left|\frac{x}{a}\right|^d + \left|\frac{y}{b}\right|^d + \left|\frac{z}{c}\right|^d = 1$$
  * Ravanski preseci (Lameove krive):
    $$\left(\frac{x}{a}\right)^d + \left(\frac{y}{b}\right)^d = 1$$
  * Superhiperboloid (jednodelni i dvodelni):
    $$\left(\frac{x}{a}\right)^d + \left(\frac{y}{b}\right)^d - \left(\frac{z}{c}\right)^d = \pm 1$$
* **Geometrijski uvid:** Za paran stepen $d$ bez apsolutnih vrednosti dobijaju se zatvorene i ograničene površi (od oktaedra za $d=1$ sa apsolutnim vrednostima, preko elipsoida za $d=2$, do zaobljenog kvadra za $d \to \infty$), dok neparan stepen $d$ generiše neograničene površi. Široka primena u CAD sistemima, robotici i kompjuterskoj grafici.

### Stub III: Diferencijalno-geometrijska i kinematička generalizacija – Dupinove indikatrise i Plikerov (Plücker) konoid
* **Polazni pojam:** Lokalna aproksimacija proizvoljne glatke površi pomoću kvadrika u tangentnoj ravni i sferna inverzija familije oskulatornih krugova.
* **Matematička formulacija:**
  * Ojlerova (Euler) formula za normalnu krivinu u pravcu pod uglom $\theta$ u odnosu na prvi glavni pravac:
    $$\kappa_n(\theta) = \kappa_1 \cos^2\theta + \kappa_2 \sin^2\theta$$
  * Dupinova indikatrisa u tangentnoj ravni:
    $$\kappa_1 x^2 + \kappa_2 y^2 = \pm 1$$
    (elipsa u eliptičkoj tački $\kappa_1 \kappa_2 > 0$, par konjugovanih hiperbola u hiperboličkoj tački $\kappa_1 \kappa_2 < 0$, par paralelnih pravih u paraboličkoj tački $\kappa_1 \kappa_2 = 0$).
  * Plikerov konoid (cilindroid), nastao sfernom inverzijom jednoparametarske familije oskulatornih krugova:
    $$z(x^2 + y^2) = c x y \quad \text{odnosno} \quad z = \frac{c}{2}\sin(2\theta)$$
* **Geometrijski uvid:** Pokazuje kako se zakrivljenost bilo koje površi lokalno svodi na klasične konike, dok inverzija familije krugova stvara pravolinijsku površ (Plikerov konoid) čiji preseci sa rotacionim cilindrima daju dvoparametarsku familiju konika.

---

## 3. Pedagoško-metodička osa (Specifičnost nastavničkog smera)
* **Problem u nastavi:** Učenici i studenti često doživljavaju analitičku geometriju u prostoru kao skup nepovezanih algebarskih formula bez jasne vizuelne predstave.
* **Rešenje (Didaktička transpozicija):**
  1. Korišćenje principa *variranja parametara* (od poznatog ka nepoznatom: kružnica $\to$ elipsa $\to$ Lameova kriva $\to$ superelipsoid).
  2. Upotreba dinamičkih geometrijskih okruženja (GeoGebra 3D) za aktivno istraživanje i otkrivanje osobina površi.
  3. Povezivanje matematike sa realnim svetom (arhitektura, optika, dizajn ambalaže, 3D modelovanje) radi povećanja unutrašnje motivacije učenika.

---

## 4. Dijagnostika trenutnog nacrta (Uočeni nedostaci koje treba rešiti)
1. **Konceptualna neusklađenost Uvoda i Razrade:** U poglavljima *Uvod* i *Ciljevi istraživanja* trenutno su opisane osnovne kvadrike (elipsoid, hiperboloid, paraboloid) i ravanski konusni preseci, dok *Razrada* obrađuje napredne generalizacije (Milerovu površ, superkvadrike, Plikerov konoid). **Akcija:** Uskladiti *Uvod* i *Ciljeve* tako da klasične kvadrike budu predstavljene kao *polazna osnova*, a navedene tri oblasti kao *glavni predmet generalizacije*.
2. **Nedostajuće matematičke formule (`___`):** U tekstu razrade postoje praznine na mestima gde treba da stoje ključne jednačine. **Akcija:** Ubaciti rigorozne formule definisane u odeljku 2 ovog dokumenta.
3. **Nedostaje metodičko poglavlje i Zaključak:** Radu nedostaje poglavlje o pedagoško-metodičkoj primeni (nastavni scenariji, radni listovi, analiza pedagoškog eksperimenta) i sintetički *Zaključak*.

---

## 5. Predložena finalna struktura master rada
1. **Uvod, motivacija i ciljevi rada** (usklađeni sa temom generalizacije i nastavničkim ciljevima)
2. **Klasične kvadrike i konusni preseci – polazna osnova za generalizaciju** (kratak sistematizovan pregled potrebnih predznanja)
3. **Teorijska analiza generalizovanih kvadrika**
   * 3.1. Milerova kubična površ i aksijalna inverzija
   * 3.2. Superkvadrike i Lameove krive
   * 3.3. Lokalna teorija površi, Dupinove indikatrise i Plikerov konoid
4. **Metodičko-pedagoški pristup obradi generalizovanih kvadrika**
   * 4.1. Didaktička transpozicija i razvoj prostorne intuicije (Van Hiele model i APOS teorija)
   * 4.2. Dizajn interaktivnih GeoGebra 3D modela i radionica za vođeno otkrivanje
   * 4.3. Protokol i analiza rezultata pedagoškog eksperimenta / studije slučaja
5. **Zaključak i smernice za budući rad**
6. **Literatura i prilozi (radni listovi i uputstva za softver)**