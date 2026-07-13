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

G2 API se koristio za prikupljanje kategorija i alata u tim kategorijama, dok je za podatke o karakteristikama alata (recenzije za specifične funkcionalnosti) korišten scraper RapidAPI. 

U koraku 1 su se prikupljale pod-kategorije edukacije, nakon prikupljanja su ručno izabrane kategorije relevantne za širu publiku nastavnika (Virtual Classroom, Assessment, Classroom Management, Study Tools, Classroom Messaging, Tutoring). U koraku 2 su se tražili alati u tim kategorijama


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
