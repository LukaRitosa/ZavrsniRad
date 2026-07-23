# Shiny aplikacija za pomoć pri odabiru digitalnih alata za edukaciju koristeći SMART metodu 

# Shiny App for Assisting with Choosing Digital Tools for Education Utilizing the SMART Method

Luka Ritoša

**Sveučilište:** Sveučilište Juraja Dobrile u Puli

**Studij:** Fakultet Informatike u Puli

**Akademska godina:** 2025/2026

**Kolegij:** Operacijska istraživanja

**Mentor:** doc. dr. sc. Katarina Kostelić

<img width="2664" height="700" alt="slika" src="https://github.com/user-attachments/assets/dd51b9a2-8d6e-45fa-84a2-2e175dde0986" />

## Uvod

U periodu digitaliziranja edukacije nastavnici su preplavljeni raznim alatima za nastavu. Cilj ovog rada je razvoj aplikacije za potporu odlučivanju pri odabiru nastavnih alata. 

EduToolSelector (ili koji bod naziv bude bio na krau) je shiny aplikacija koristi SMART metodu za prijedlog alata određene kategorije, tako da korisnik bira bitne kriterije, rangira ih i dodijeljuje koliko je puta npr. kriterij x2 važniji od kriterija x1. 

Projekt uključuje prikupljanje podataka u Pyhton virtualnom okruženju preko G2 API-a i Rapid API web scraper-a.  

## Razrada 

### Teorijska podloga

Kod problema odabira digitlnih nastavnih alata nastavnici pri odabiru ne razmatraju samo jednu karakteristiku alata, već istodobno uzimaju u obzir više međusobno različitih kriterija. Budući da neki alati mogu biti bolji prema jednom, a lošiji prema drugom kriteriju, nije moguće odrediti najbolju alternativu promatrajuči samo jednu značajku, što ovaj problem čini problemom višekriterijskog odlučivanja.

**Višekriterijsko odlučivanje** je grana operacijskih istraživanja koja se bavi metodama za odabir između više alternativa prema više kriterija istovremeno. Za razliku od jednokriterijskih problema optimizacije, u svarnim situacijama odluke se rijetko donose prema donose prema samo jednom cilju. Cilj metoda višekriterijskog odlučivanja nije pronaći univerzalno najbolju alternativu, već onu koja najbolje odgovara preferencama donositelja odluke.

Prilikom odabira metode višekriterijskog odlučivanja potrebno je uzeti u obzir karakteristike problema te odabrati metodu koja je dovoljno jednostavna za primjenu, ali istovremeno omogućuje pouzdano donošenje odluka. Prema Saaty i Ergu (2015) metoda je loše odabrana ukoliko je njena logika komplicirana i mogu ju razumijeti samo eksperti u donošenju odluka, odnosno dobro odabrana metoda je razumljiva i može se implementirati sa strane većine korisnika u praksi. Iz tog razloga je odabrana SMART metoda, koja predstavlja jednostavan, ali učinkovit pristup riješenja ovakvih problema. 

**SMART** (engl. _Simple Multi-Atribute Technique_) metodu razvio je Edwards 1971, dok su Edwards i Barron (1994) kasnije predstavili unaprijeđenje inačice SMARTS i SMARTER. Metoda se temelji na određivanju težina kriterija te izračunu ukupne vrijednosti svake alternative kao ponderiranog zbroja njezinih vrijednosti prema odabranim kriterijima. Zbog jednostavne implementacije, transparentnosti odabira alternativa i lako razuljivih rezultata SMART metoda često se koristi u problemima odabira alternativa i sustavima za potporu olučivanju (Olson, 1996; Patel i sur., 2017). 

Prednost metode je upotreba linearne funkcije kao funkcije vrijednosti, jednostavnost, odluka koja je nezavisna od alternativa i robustnost na promjene alternativa. Dok su nedostatci povećanje kompleksnisti kod povećanja broja kriterija, brzo odbacivanje nisko rangiranih alternativa, problematično određivanje odgovarajućih vaganja i nekonzistentnost zbog subjektivnog pristupa provedbi metode.


#### Matematičke formule korištene u radu

**Izračun težina kriterija**

Početna težina posljednjeg kriterija postavlja se na vrijednost 10:

$$
W_n = 10
$$

Težine ostalih kriterija računaju se unatrag korištenjem omjera važnpsti koje odredi korisnik:

$$
W_i = W_{i+1} · r_i
$$

gdje je:

- $W_i$ početna težina kriterija,
- $r_i$ omjer važnosti između susjednih kriterija koji određuje korisnik.

Dobivene težine zatim se normaliziraju kako bi njihov zbroj bio jednak 1:

$$
w_i = \frac{W_i}{\sum_{j=1}^{n} W_j}
$$



**Izračun SMART rezultata:**

Nakon određivanja normaliziranih težina za svaki alat izračunava se ukupni SMART rezultat kao ponderirani zbroj vrijednosti svih odabranih kriterija:

$$
S_k=\sum_{i=1}^{n} w_i \cdot x_{ki}
$$

gdje je:

- $S_k$ ukupni SMART rezultat alternative,
- $w_i$ normalizirana težina kriterija,
- $x_{ki}$ vrijednost alternative prema kriteriju $i$.
- $n$ broj odabranih kriterija




### Prikupljanje i priprema podataka

Izvor podataka je G2 (https://www.g2.com/). G2 je web stranica sa recenzijama poslovnih software alata, te jedna od kategorija je edukacija.

G2 API se koristio za prikupljanje kategorija i alata u tim kategorijama, dok je za podatke o karakteristikama alata (recenzije za specifične funkcionalnosti) korišten scraper RapidAPI. Python dio projekta je podijeljen u 8 koraka.

U koraku 1 su se prikupljale pod-kategorije edukacije, nakon prikupljanja su ručno izabrane kategorije relevantne za širu publiku nastavnika (Virtual Classroom, Assessment, Classroom Management, Study Tools, Classroom Messaging, Tutoring). U koraku 2 su se tražili alati u tim kategorijama, G2 API vraća prvih pet proizvoda rangiranih prema recenzijama U koraku 3 su se podatci spremili u csv, zbog nižih ocjrna i manjeg broja recenzija je kategorija Tutoring izbacila iz skupa podataka. Konačan skup obuhvaća 16 alata u pet kategorija.Podatci koji su se izvukli su: naziv, slug (bitan za kasnije pronalaženje urla predloženog alata), recenzija te funkcionalnosti (kriteriji kojima se rangira važnost i predlaže alat).

Korak 4 razdvaja podatke po kategorijama i miče funkcije u kriterijima gdje niti jedan alat nema podatak (recenziju) o funkcionalnosti. Korak 5 služi za analizu pokrivenosti funkcionalnosti, alata ili kategorija. Na temelju dobivenih rezultata donesene su odluke o uklanajnju kategorija ili alata kod kojih nije bilo dovoljno zajedničkih kriterija za smisleno višekriterijsko uspoređivanje. Classroom Management alati su imali 100% međusobnu pokrivenost funkcionalnosti, Assets je bila kategorija sa najviše funkcionalnosti no one su se preklapale u samo par navrata, kod Classroom Messageing je 2/3 alata imalo zajedničke funkcionalnosti, Study Tools je kategorija kod koje je samo jedan alat imao recenzije funkcionalnosti, dok su kod Virtual Classroom oba dvije aplikacije imale zajedničke funkcionalnosti. Nakon alanize se u 6. koraku izbacilo kategoriju Study Tools i obrisallo null vrijednosti Assessment kategorije. 

Korak 7 je bio korak prevođenja naziva kategorija i funkcionalnosti na hrvatski jezik. Cilj nije bio doslovno prevesti nazive s platforme G2, već ih prilagoditi terminologiji razuljivoj široj skupini nastavnika. Zbog toga je provedena dodatna analiza funkcionalnosti kako bi odabrani nazivi što vijernije opisivali njihovu svrhu u kontekstu nastave. Tijekom tog procesa donesena je odluka o uklanjanju _Classroom Messaging_ kategorije, zbog previše specifičnčnih funkcionalnosti kategorije koje nisu bile relevantne za širu skupinu nastavnika. Osim toga, u većini škola/fakulteta je kanal komunikacije porukama standardiziran na razini ustanove.

**Napomena:** prijevodi korišteni u radu su subjektivno izrađeni za potrebe ovog projekta te ne predstavljaju službene prijevode platforme G2.

Deteljniji postupak prevođenja i prijevodi: https://github.com/LukaRitosa/ZavrsniRad/blob/main/7_prevodenje.py.
  

Zadnji korak je bio prenošenje prevedenih podataka u Shiny okruženje.

**Napomena:** zbog ograničenja besplatnih verzija API servisa podaci se ne dohvaćaju dinamički pri svakom pokretanju aplikacije. Nakon završetka procesa prikupljanja i obrade podaci su spremljeni u CSV datoteke koje se učitavaju lokalno. Stoga splikacija predstavlja **_proof-of-concept_** kojim se demostrira mogućnost primjene SMART metode u odabiru digitalnih alata za edukaciju, dok bi produkcijska verzija trebala uključiti automatsko dohvaćanje i redovito ažuriranje podataka.

### Implementacija SMART modela

Kriteriji za svaku kategoriju preuzeti su iz G2 _detailed_features_ podataka, svaka funkcionalnost ima postotak zadovoljnih korisnika temeljen na stvarnim recenzijama. Ti postotci (0-100) koriste se direktno kao vrijednost alternativa u SMART modelu, što eliminira potrebu za ručnom normalizacijom podataka.

**Odabir kriterija**

Prvi korak omogućuje korisniku odabir kriterija koje želi uzeti u obzir pri odlučivanju. Time se iz analize mogu isključiti funkcionalnosti koje korisniku nisu važne.

*_screenshot_

**Rangiranje kriterija**

Nakon odabira kriterija korisnik ih raspoređuje metodom _drag and drop_ od najvažnijeg prema najmanje važnom. Dobivani korak koristi se kao osnova za određivanje relativnih režina kriterija.

*_screenshot_

**Određivanje težina (Swing Weighting)**

Samo rangiranje ne govori koliko je jedan kriterij važniji od drugoga, korisnik zatim određuje omjer važnosti između susjednih kriterija. Za svaki par kriterija odgovara na pitanje "Koliko Vam je kriterij A bitniji od kriterija B?", odgovori se izražavaju u omjerima 2-10.

Na temelju omjera izračunavaju se težine kriterija. Izračun započinje od posljednjeg kriterija kojem se dodjeljuje početna vrijednost 10, nakon čega se težine računaju unatrag množenjem s odabranim omjerima:

        tezine[n] <- 10
        
        for(i in (n-1):1){
          tezine[i] <- tezine[i+1] * weight_omjeri[i]
        }
        
        tezine_norm <- tezine / sum(tezine)


*_screenshot_


**Rezultat**

Nakon određivanja normaliziranih težina, za svaki alat računa se ukupni SMART rezultat. Svaka funkcionalnost alata množi se pripadajućom težinom kriterija, a zatim se svi umnošci zbrajaju. Budući da su vrijednosti kriterija izražene kao postotak zadovoljnih korisnika, nije bila potrebna dodatna normalizacija podataka. Alat s najvećim ukupnim rezultatom smatra se najprikladnijim izborom za zadane korisničke preferencije.
Dobiveni SMART skor predstavlja ukupnu ocjenu alata. Alati se sortiraju silazno prema ostvarenom rezultatu te se korisniku prikaže preporučeni alat (sa linkom na G2 stranicu alata i G2 recenzijom alata) zajedno sa kompletnom rang-listom.

*_screenshot_


**Napomena:** u klasičnoj SMART metodi vrijednosti alternative često se prethodno normaliziraju kako bi bile usporedive. U ovom radu taj korak nije bio potreban jer G2 za svaku funkcionalnost već daje postotak zadovoljnih korisnika (0-100), pas u sve vrijednosti već izražene na istoj mjernoj ljestvici.

### Shiny aplikacija

**Arhitektura**

Aplikacija je razvijena korištenjem programskog jezika R i paketa **Shiny**, dok jwe za _drag and drop_ funkcionalnost korišten paket **sortable**. Implementacija je podijeljena u 3 glavne datoteke:
- **ui.R** definira korisničko sučelje
- **server.R** sadrži logiku aplikacije, implementaciju SMART metode i reakcije na korisničke akcije
- **data.R** učitava CSV datoteke i priprema podatke za prikaz u aplikaciji

**Dinamičko generiranje korisničkog sučelja**

Jedna od glavnih karakteristika aplikacije je da korisničko sučelje nije ručno izrađeno za svaku kategoriju alata, već se generira dinamički iz učitanih podataka.
Nakon učitavanja CSV datoteka u datoteci **data.R** korištenjem funkcije _lapply()_ iz tih se podataka automatski stvaraju:
- gumbovi za odabir kategorije
- karice (tabovi) za svaku kategoriju
- popis kriterija
- elementi ta rangiranje kriterija
- elementi za određivanje težina

Na taj način aplikcija nije vezana uz unaprijed definirani broj kategorija/kriterija. Dodavanjem nove CSV datoteke odgovarajuće strukture moguće je proširiti aplikaciju bez izmjena korisničkog sučelja.

**_User flow_**

Korisnik prolazi kroz četiri uzastopn koraka:
1. odabir kriterija
2. rangiranje kriterija
3. određivanje omjera važnosti između kriterija
4. prikaz preporučenih alata i kompletne rang-liste

## Zaključak 

Cilj ovog rada bio je razviti aplikaciju za potporu u odlučivanju koji nastavnicima olkšava odabir digitalnih alata za nastavu primjenom SMART metode višekriterijskog odlučivanja. Razvijena je Shiny aplikacija koja korisniku omogućuje uži odabir alata, biranje (subjektivno?) relevantnih kriterija, njihovo rangiranje i određivanje relativne važnosti, nakon čega se izračunava rang-lista dostupnih alata te prikazuje najprikladnija alternativa.

Prilikom prevođenja kategorija i kriterija nastojalo se koristiti terminologiju koja je uobičajena i razuljiva ciljanoj skupini korisnika - nastavnicima u Republici Hrvatskoj.

Arhitektura aplikacije omogućuje jednostavno proširenje novim kategorijama i alatima dodavanjem odgovarajućih CSV datoteka, bez potrebe za značajnim izmjenama korisničkog sučelja ili implementacije SMART modela.

**Ograničenja**

Zbog ograničenja besplatnih verzija oba korištena API-a nije moguće dobiti podatke u stvarnom vremenu, nego samo slike podataka u određenom vremenu. Ukoliko se ažurirnjem alata promijene mišljenja korisnika ili pojave novi relevantni alati na G2 aplikacija neće predstavljati relevantnu sliku stvarnosti. Također postoje relevantne kategorije za nastavnike koje nisu uključene u aplikaciju zboig manjka recenzija za feature/kriterije.

Aplikcija ne uzima se u obzir jesu li alati besplatni/kavke su recenzije besplatnih verzija, može predložiti skupi alat korisniku koji nije spreman trošiti osobni novac za najprikladniji alat.

Ocjenjivanje kriterija na G2 je binarno. Korisnici za pojedinu funkcionalnost označuju jesu li njome zadovoljni ili nisu, što znači da korisnik koji bi za neku funkcionalnost dao npr. 6/10 u dekadskoj ljestvici će tu funkcionalnost ocijeniti tako da je zadovoljan. Budući da takvo ocjenjivanje označava udio zadovoljnih korisnika, ali ne njihov intenzitet zadovoljstva, takav način prikupljanja podataka može dovesti do precjenjivanja pojedinih funkcionalnosti.

SMART metoda temelji se na linearnom ponderiranom zbroju kriterija, zbog čega pretpostavlja da se doprinos svakog kriterija ukupnom rezultatu može izraziti neovisno o ostalim kriterijima. U ovom radu nije razmatrana moguća međusobna ovisnost pojedinih funkcionalnosti alata.

U implementaciji SMART metode svi odabrani kriteriji tretiraju se kao kompenzacijski. To znači da vrlo dobra ocjena prema jednom kriteriju može nadoknaditi  lošju ocjenu prema drugome, iako u stvarnoj situaciji korisnik neke funkcionalnosti može smatrati poželjnima, a ne obaveznima. Primjerice u slučaju gdje je kod alata za video razgovore ključna funkcionalnost (npr. dijeljenje zaslona) lošije ocijenjena dok su sporedne funkcionalnosti (npr. prilagođivanje UI-a, analitika) prosječno vrlo visoko ocijenjene taj alat može biti preporučen.

**Moguća poboljšanja**

Moguča poboljšanja:

- dinamičko prikupljanje podataka
- proširenje kategorija
- označavanje jesu li alati besplatni, imaju li besplatnu verziju i koja su ograničenja te verzije
- aplikacija koja služi za prijedlog bilo koje kategorije
- usporedba SMART metode s drugim metodama višekriterijskog odlučivanja

## Literatura i izvori

Kostelić K. (2025). Uvod u višekriterijsko odlučivanje
https://rpubs.com/kakoste/uvod_MCDM
(pristupljeno 21.7.2026.)

Edwards, W., & Barron, F. H. (1994). SMARTS and SMARTER: Improved simple methods for multiattribute utility measurement. Organizational Behavior and Human Decision Processes, 60(3), 306–325.

Olson, D. L. (1996). Decision aids for selection problems. Journal of the Operational Research Society, 48(5), 541-542. 

Patel, M. R., Vashi, M. P., & Bhatt, B. V. (2017). SMART–Multi-criteria decision-making technique for use in planning activities. New Horizons in Civil Engineering (NHCE 2017), 1–6.

Saaty, T. L. and Ergu, D. (2015). When is a decision-making method trustworthy? Criteria for
evaluating multi-criteria decision-making methods. International Journal of Information Technol-
ogy and Decision Making, 14(6), 1171–1187.

Scraper:
  https://rapidapi.com/pradeepbardiya13/api/g2-data-api

G2API:
  https://documentation.g2.com/docs/developer-portal
  


  ## Upute korištenja


možda maknut
