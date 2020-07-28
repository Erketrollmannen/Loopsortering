# Loopsorting

Lite script som leiter sorterer looptegninger etter utestasjon og tag. 

## Virkemåte

Programet scanner alle PDFer som ligger i mappa programmet blir kjørt frå. Den oppreter så ei mappe per utestasjon.  Den leiter etter ein streng som har samme mønster som eit Tag. Taget blir det nye navnet på fila.
Dersom programmet finner fleire tag, vil den velge den første. Filen blir så flytta til mappa med utestasjonen som den fant. Dersom loopen går i fleire utestasjoner vil den velge den første den fant. 



## Krav

For å kunne bruke programet må ein ha Python interpreteren installert. Den finner du på AccsessIT. For meir info om å få Python til å kjøre på Equinor PC sjå [Equinor Wiki](https://wiki.equinor.com/wiki/index.php/Software:Python)

Følgende biblotek er må installeres:

- PyPDF2

Dette gjeres med følgende kommando i CMD:

pip3 install --user PyPDF2

## Bruk

1. Scan ein bonke med looptegninger.

2. Gjer det scanna dokumentet lesbart med Adobe Acrobat sin Scan & OCR, Recognize Text funksjon.

3. Split det storedokumentet i mange filer slik at det blir ei side per fil. Dette gjeres også med Adobe Acrobat. 

3. La filene ligge i samme mappe som du kjører programmet frå. 

For å kunne sjå evnetuelle feilmeldinger må du kjøre programet via CMD. Dette gjeres med å bruke kommandoen "cd" for å navigere til mappa der programmet ligger. 

Programmet kjøres med å skrive følgende kommando:

python loopsorter
