# ZavrsniRad

# Shiny aplikacija za pomoć pri odabiru digitalnih alata za edukaciju koristeći SMART metodu 

# Shiny App for Assisting With Choosing Digital Tools for Education Utilizing the SMART Method

Luka Ritoša

**Sveučilište:** Sveučilište Juraja Dobrile u Puli

**Studij:** Fakultet Informatike u Puli

**Akademska godina:** 2025/2026

**Kolegij:** Operacijska istraživanja

**Mertor:** doc. dr. sc. Katarina Kostelić

## Uvod

U periodu digitaliziranja edukacije nastavnici su preplavljeni raznim alatima za nastavu. Cilj ovog rada je razvoj sustava za potporu odlučivanju pri odabiru nastavnih alata. 

EduToolSelector (ili koji bod naziv bude bio na krau) je shiny aplikacija koristi SMART metodu za prijedlog alata određene kategorije, tako da korisnik bira bitne kriterije, rangira ih i dodijeljuje koliko je puta npr. kriterij x2 važniji od kriterija x1. 

Projekt uključuje prikupljanje podataka u Pyhton virtualnom okruženju preko G2 API-a i Rapid API web scraper-a.  

## Razrada 

### Teorijska podloga

bla bla višestruko odlučivanje bla bla smart metoda

### Prikupljanje i priprema podataka

Izvor podataka je G2 (https://www.g2.com/). G2 je web stranica sa recenzijama poslovnih software alata, te jedna od kategorija je edukacija.

G2 API se koristio za prikupljanje kategorija i alata u tim kategorijama, dok je za podatke o karakteristikama alata (recenzije za specifične funkcionalnosti) korišten scraper RapidAPI. Python dio projekta je podijeljen u 8 koraka.

U koraku 1 su se prikupljale pod-kategorije edukacije, nakon prikupljanja su ručno izabrane kategorije relevantne za širu publiku nastavnika (Virtual Classroom, Assessment, Classroom Management, Study Tools, Classroom Messaging, Tutoring). U koraku 2 su se tražili alati u tim kategorijama, G2 API vraća prvih pet proizvoda rangiranih prema recenzijama U koraku 3 su se podatci spremili u csv, zbog nižih ocjrna i manjeg broja recenzija je kategorija Tutoring izbacila iz skupa podataka. Konačan skup obuhvaća 16 alata u pet kategorija.Podatci koji su se izvukli su: naziv, slug (bitan za kasnije pronalaženje urla predloženog alata), recenzija te funkcionalnosti (kriteriji kojima se rangira važnost i predlaže alat).

Korak 4 razdvaja podatke po kategorijama i miče funkcije u kriterijima gdje niti jedan alat nema podatak (recenziju) o funkcionalnosti. Korak 5 služi za pomoč pri odlučivanju ručnog micanja funkcionalnosti, alata ili kategorija. Classroom Management alati su imali 100% međusobnu pokrivenost funkcionalnosti, Assets je bila kategorija sa najviše funkcionalnosti no one su se preklapale u samo par navrata, kod Classroom Messageing je 2/3 alata imalo zajedničke funkcionalnosti, Study Tools je kategorija kod koje je samo jedan alat imao recenzije funkcionalnosti, dok su kod Virtual Classroom oba dvije aplikacije imale zajedničke funkcionalnosti. Nakon alanize se u 6. koraku izbacilo kategoriju Study Tools i obrisallo null vrijednosti Assessment kategorije. 

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
  


-G2 izvor
-G2 API proizvodi
-RapidAPI feature podatci
Python
Odabir
Prevođenje

### Implementacija SMART modela

Kriteriji po kategorijama
Rank sum
Swing weight
Kombinacija

### Shiny aplikacija

Arhitektura
Korisnički flow
Inmplementacija
Opis sučelja

## Zaključak 

Što je ostvareno
Ograničenja
Moguća poboljšanja

## Literatura i izvori

https://rpubs.com/kakoste/uvod_MCDM

Scraper:
  https://rapidapi.com/pradeepbardiya13/api/g2-data-api

G2API:
  https://documentation.g2.com/docs/developer-portal
  


  ## Upote korištenja
