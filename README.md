# Shiny aplikacija za pomoć pri odabiru digitalnih alata za edukaciju koristeći SMART metodu 

# Shiny App for Assisting With Choosing Digital Tools for Education Utilizing the SMART Method

Luka Ritoša

**Sveučilište:** Sveučilište Juraja Dobrile u Puli

**Studij:** Fakultet Informatike u Puli

**Akademska godina:** 2025/2026

**Kolegij:** Operacijska istraživanja

**Mertor:** doc. dr. sc. Katarina Kostelić

<img width="2664" height="700" alt="slika" src="https://github.com/user-attachments/assets/dd51b9a2-8d6e-45fa-84a2-2e175dde0986" />

## Uvod

U periodu digitaliziranja edukacije nastavnici su preplavljeni raznim alatima za nastavu. Cilj ovog rada je razvoj sustava za potporu odlučivanju pri odabiru nastavnih alata. 

EduToolSelector (ili koji bod naziv bude bio na krau) je shiny aplikacija koristi SMART metodu za prijedlog alata određene kategorije, tako da korisnik bira bitne kriterije, rangira ih i dodijeljuje koliko je puta npr. kriterij x2 važniji od kriterija x1. 

Projekt uključuje prikupljanje podataka u Pyhton virtualnom okruženju preko G2 API-a i Rapid API web scraper-a.  

## Razrada 

### Teorijska podloga

**Višekriterijsko odlučivanje** je grana operacijskih istraživanja koja se bavi metodama za odabir između više alternativa prema više kriterija istovremeno. Za razliku od jednokriterijskih problema optimizacije, u svarnim situacijama odluke se rijetko donose prema donose prema samo jednom cilju - nastavnik koji bira digitalni alat za nastavu uzima u obzir više faktora.

**SMART** (engl. _Simple Multi-Atribute Technique_) metodu razvio je Edwards 1971. Njena jednostavnost proizlazi iz direktonog ocjenjivanja alternativa iu korištenje prirodne mjerne ljestvice, vaganja kriterija i odvajanja alternativa kriterija. Prednost metode je upotreba linearne funkcije kao funkcije vrijednosti, jednostavnost, odluka koja je nezavisna od alternativa i robustnost na promjene alternativa. Dok su nedostatci povećanje kompleksnisti kod povećanja broja kriterija, brzo odbacivanje nisko rangiranih alternativa, problematično određivanje odgovarajućih vaganja i nekonzistentnost zbog subjektivnog pristupa provedbi metode.

### Prikupljanje i priprema podataka

Izvor podataka je G2 (https://www.g2.com/). G2 je web stranica sa recenzijama poslovnih software alata, te jedna od kategorija je edukacija.

G2 API se koristio za prikupljanje kategorija i alata u tim kategorijama, dok je za podatke o karakteristikama alata (recenzije za specifične funkcionalnosti) korišten scraper RapidAPI. Python dio projekta je podijeljen u 8 koraka.

U koraku 1 su se prikupljale pod-kategorije edukacije, nakon prikupljanja su ručno izabrane kategorije relevantne za širu publiku nastavnika (Virtual Classroom, Assessment, Classroom Management, Study Tools, Classroom Messaging, Tutoring). U koraku 2 su se tražili alati u tim kategorijama, G2 API vraća prvih pet proizvoda rangiranih prema recenzijama U koraku 3 su se podatci spremili u csv, zbog nižih ocjrna i manjeg broja recenzija je kategorija Tutoring izbacila iz skupa podataka. Konačan skup obuhvaća 16 alata u pet kategorija.Podatci koji su se izvukli su: naziv, slug (bitan za kasnije pronalaženje urla predloženog alata), recenzija te funkcionalnosti (kriteriji kojima se rangira važnost i predlaže alat).

Korak 4 razdvaja podatke po kategorijama i miče funkcije u kriterijima gdje niti jedan alat nema podatak (recenziju) o funkcionalnosti. Korak 5 služi za analizu pokrivenosti funkcionalnosti, alata ili kategorija. Na temelju dobivenih rezultata donesene su odluke o uklanajnju kategorija ili alata kod kojih nije bilo dovoljno zajedničkih kriterija za smisleno višekriterijsko uspoređivanje. Classroom Management alati su imali 100% međusobnu pokrivenost funkcionalnosti, Assets je bila kategorija sa najviše funkcionalnosti no one su se preklapale u samo par navrata, kod Classroom Messageing je 2/3 alata imalo zajedničke funkcionalnosti, Study Tools je kategorija kod koje je samo jedan alat imao recenzije funkcionalnosti, dok su kod Virtual Classroom oba dvije aplikacije imale zajedničke funkcionalnosti. Nakon alanize se u 6. koraku izbacilo kategoriju Study Tools i obrisallo null vrijednosti Assessment kategorije. 

Korak 7 je bio korak prevođenja naziva kategorija i funkcionalnosti na hrvatski jezik. Bitan aspekt prevođenja je bio korištenje jezika poznat široj nastavničkoj skupini, što je zahtijevalo dodatnu analizu funkcionalnosti, ta dodatna analiza je dovela do odluke o uklanjanju Classroom Messaging kategorije zbog previše specifičnčnih funkcionalnosti kategorije, uz to u većini škola/fakulteta je kanal komunikacije porukama standardiziran na razini ustanove.

Prijevodi:
  "Assessment": "Procjena znanja"
  
        "Administration | Mobile compatibility": "Prilagođeno mobilnim uređajima",
        
        "Administration | White-labeling": "Prilagodba izgleda",
        
        "Assessment delivery | Pre-made content": "Gotovi sadržaji",
        
        "Assessment delivery | Question variety": "Raznolikost vrsta pitanja",
        
        "Assessment delivery | Real-time assessment": "Procjena u stvarnom vremenu",
        
        "Grading and reporting | Analytics dashboard": "Analitika",
        
        "Grading and reporting | Gamification": "Elementi igre"


  "Classroom Management": "Upravljanje učionicom",
  
        "Platform Features | Instant Messaging": "Razmjena poruka u stvarnom vremenu",
        
        "Platform Features | Interactive Quizzes": "Interaktivni kvizovi",
        
        "Platform Features | Remote Computer Monitoring": "Praćenja rada",
        
        "Platform Features | Student Assignment Distribution": "Dodjela zadataka",
        
        "Platform Features | Teacher/Student Screensharing": "Djeljenje zaslona"

            
  "Virtual Classroom": "Virtualna učionica"
  
        "Collaboration | Hand Raising": "Dizanje ruke",
        
        "Collaboration | Participation Controls": "Upravljanje sudjelovanjem",
        
        "Collaboration | Screen Sharing": "Dijeljenje zaslona",
        
        "Collaboration | Survey Tools": "Alati za ankete",
        
        "Collaboration | Whiteboard": "Digitalna ploča",
        
        "Content Sharing | File Sharing": "Dijeljenje datoteka",
        
        "Content Sharing | Session Recording": "Snimanje sastanka/nastave",
        
        "Content Sharing | Video Streaming": "Prijenos videa uživo",
        
        "Functionality | Live Chat": "Slanje poruka",
        
        "Functionality | Markup Tools": "Alati za označavanje",
        
        "Functionality | Technical Support": "Tehnička podrška"
  

Zadnji korak je bio prenošenje prevedenih podataka u Shiny okruženje.

**Napomena:** zbog ograničenja besplatnih verzija API servisa podaci se ne dohvaćaju dinamički pri svakom pokretanju aplikacije. Nakon završetka procesa prikupljanja i obrade podaci su spremljeni u CSV datoteke koje se učitavaju lokalno.

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

Što je ostvareno
Ograničenja
Moguća poboljšanja

## Literatura i izvori

https://rpubs.com/kakoste/uvod_MCDM

Edwards, W., & Barron, F. H. (1994). SMARTS and SMARTER: Improved simple methods for multiattribute utility measurement. Organizational Behavior and Human Decision Processes, 60(3), 306–325.

Scraper:
  https://rapidapi.com/pradeepbardiya13/api/g2-data-api

G2API:
  https://documentation.g2.com/docs/developer-portal
  


  ## Upute korištenja
