▚▚▚▚ Radera alla rader som börjar med ▚▚▚▚ samt ersätt alla ▚▚ inom text med en  
▚▚▚▚ lämpligt text.  
▚▚▚▚ Innan ni börjar fylla i dokumentet, läs igenom det i sin helhet samt  
▚▚▚▚ hela dokumentet [EXTRA_PROJEKTINFO](./EXTRA_PROJEKTINFO.md).  
# Projektplanering - ▚▚▚▚

## Vad ska ditt program göra?
▚▚▚▚  
▚▚▚▚ Nämn hur programmet tar in data som beskriver vad det ska göra eller den  
▚▚▚▚ data som det ska arbeta med. Nämn även om det är ett kommandoradsverktyg,  
▚▚▚▚ ett grafiskt program, ett serverbaserat program såsom t.ex. en backend  
▚▚▚▚ skapad med Flask.  
▚▚▚▚  
▚▚▚▚ Försök att täcka in det viktigaste. Det är bra om det är tillräckligt  
▚▚▚▚ detaljerat för att ge en uppfattning om hur svårt och tidskrävande det  
▚▚▚▚ blir, samtidigt som det inte heller ska ta lång tid att beskriva.  

## Vad är motivationen till att skapa det?
▚▚▚▚  
▚▚▚▚ Det är roligt att grunda projektet i en idé som ni ser fram emot att skapa.  
▚▚▚▚ Om det är möjligt så är det kul om projektet kan leva vidare efter kursen  
▚▚▚▚ och till slut bli någon slags fri mjukvara eller en produkt? Se till att  
▚▚▚▚ spara det efter kursens gång då repositories rensas bort inom några månader.  
▚▚▚▚  
▚▚▚▚ Det finns inget rätt eller fel här! Om någon bara vill bli klar med kursen  
▚▚▚▚ och fokusera på annat så kan det räcka gott. Men även i det läget så kanske  
▚▚▚▚ det är roligare att göra något roligt "så enkelt som möjligt" än att göra  
▚▚▚▚ något som är trist.  

## Detaljer

### Gränssnitt
▚▚▚▚  
▚▚▚▚ Om projektet innefattar en grafisk komponent, inkludera en preliminär skiss  
▚▚▚▚ som visar hur användargränssnittet förväntas se ut i något speciellt läge.  
▚▚▚▚  
▚▚▚▚ Om projektet inte innefattar en grafisk komponent, ska ni istället skapa  
▚▚▚▚ ett sekvensdiagram som översiktligt beskriver interaktionen mellan olika  
▚▚▚▚ delar av programmet i en specifik situation. Använd mermaid.js för att  
▚▚▚▚ skapa detta diagram direkt i ditt markdown-dokument. Det är inte nödvändigt  
▚▚▚▚ att ange metodnamn, typer, eller de exakta namnen på klasser och  
▚▚▚▚ funktioner. Fokusera på att, med vanlig svenska, beskriva syftet med varje  
▚▚▚▚ anrop och hur de interagerar med varandra.  

### Hur förmedlar ditt program sitt resultat
▚▚▚▚  
▚▚▚▚ Hur ditt program kommunicerar sitt resultat beror på programmets natur och  
▚▚▚▚ användargränssnitt. Här är några vanliga sätt för olika typer av program:  
▚▚▚▚  
▚▚▚▚ Grafiska program: Dessa program visar vanligtvis resultatet direkt i  
▚▚▚▚ användargränssnittet. Det kan vara genom uppdateringar av befintliga  
▚▚▚▚ element på skärmen, popup-fönster med meddelanden, eller nya fönster som  
▚▚▚▚ presenterar informationen på ett överskådligt sätt.  
▚▚▚▚  
▚▚▚▚ CLI-program (Command Line Interface): CLI-program skriver ofta ut  
▚▚▚▚ resultatet till terminalen eller kommandotolken. Detta kan vara en enkel  
▚▚▚▚ textutskrift som beskriver resultatet av en operation eller mer komplexa  
▚▚▚▚ textbaserade gränssnitt som uppdateras i realtid.  
▚▚▚▚  
▚▚▚▚ Filsystemsbaserade program: Vissa program kan generera resultat i form av  
▚▚▚▚ filer. Detta kan inkludera att skriva data till textfiler, skapa eller  
▚▚▚▚ uppdatera databasfiler, eller generera bilder och dokument. Användaren kan  
▚▚▚▚ sedan öppna dessa filer med lämpliga program för att se resultatet.  
▚▚▚▚  
▚▚▚▚ Ändringar i systeminställningar eller register: För program som är avsedda  
▚▚▚▚ att ändra konfigurationen på en dator, kan resultatet vara en ändring i  
▚▚▚▚ systemets inställningar eller i Windows-registret. Dessa ändringar är inte  
▚▚▚▚ alltid omedelbart synliga för användaren utan kan kräva att användaren  
▚▚▚▚ kontrollerar de specifika inställningarna eller använder ytterligare  
▚▚▚▚ verktyg för att se ändringarna.  

### Vilka operativsystem ska ditt program fungera på?
▚▚▚▚  
▚▚▚▚ Python är kompatibelt med de flesta större operativsystem. Dock kan ditt  
▚▚▚▚ program vara specialanpassat för att endast fungera på specifika  
▚▚▚▚ operativsystem. Vänligen specificera vilka operativsystem ditt program är  
▚▚▚▚ designat för. Det är acceptabelt att välja ett, flera, eller alla bland  
▚▚▚▚ Windows, MacOS och Linux. Det går även bra att välja något slags inbyggt  
▚▚▚▚ system, om det är vad ni brinner för.  

### Externa bibliotek

▚▚▚▚X Om ditt projekt i stor utsträckning bygger på ett eller ett par specifika  
▚▚▚▚X bibliotek, så bör dessa definitivt nämnas här. Det är inte nödvändigt att  
▚▚▚▚X listan innehåller allt då saker kan förändras under resans gång.  
▚▚▚▚X  
▚▚▚▚X För de bibliotek ni använder bör ni ta upp följande:  
▚▚▚▚X 1. Bibliotekets paketnamn på PyPi, det är vad som skrivs efter `pip install`.  
▚▚▚▚X 2. Vad biblioteket tillför projektet  
▚▚▚▚X 3. Om ni undersökt övergripande hur biblioteket används, och om det verkar  
▚▚▚▚X    gå att lära sig det som behövs och använda det.  

## Realistiskt startdatum för utförandet av projektet

Datum: 2024-▚▚-▚▚

▚▚▚▚ Datumet ovan ska vara det första datumet i rubriken YYYY nedan.  
▚▚▚▚ Motivera datumet kort med ord.  

## Plan för sekvensen av "heltidsarbetsdagar"
▚▚▚▚  
▚▚▚▚ Denna sektion är endast relevant för grupper med fler än en deltagare. Om  
▚▚▚▚ du arbetar ensam med ditt projekt, är denna rubrik inte tillämplig på din  
▚▚▚▚ situation och kan tas bort helt.  
▚▚▚▚  
▚▚▚▚ För grupper är syftet med denna plan att ni ska organisera och planera ert  
▚▚▚▚ arbete *som om* en person skulle utföra allt arbete. Det motiverar att  
▚▚▚▚ mängden arbete motsvarar det betyg gruppen siktar på att uppnå genom att  
▚▚▚▚ vara tre till sju "heltidsarbetsdagar" beroende på gruppens ambition och  
▚▚▚▚ storlek.  
▚▚▚▚  
▚▚▚▚ Anpassa antalet dagar efter ert projekt och ta bort de dagar som inte  
▚▚▚▚ behövs. Ange inga datum i den här delen, det räcker gott med dagens  
▚▚▚▚ ordningsnummer i projektets utförande.  

### Dag 1
▚▚▚▚ Försök använda SMARTa mål utan att för den saken bli för formell. Det finns  
▚▚▚▚ mycket information om sådana mål på Internet. Ett par bra exempel är  
▚▚▚▚ [denna Youtube-film](1) samt [denna artikel][2] av Atlassian.  
▚▚▚▚  
▚▚▚▚ Skriv inte upp några datum eller tidsestimat här! Rubriken utgör redan  
▚▚▚▚ tidsestimatet och en mer detaljerad nivå än så behövs inte. Skriv inte  
▚▚▚▚ heller upp något om vem som ska göra vad, då det är något som visar sig  
▚▚▚▚ under resans gång.  

### Dag 2
### Dag 3
### Dag 4
### Dag 5
### Dag 6
### Dag 7

## Arbetsplan
▚▚▚▚  
▚▚▚▚ Anpassa antalet kalenderdagar nedan efter ert projekt och ta bort de dagar  
▚▚▚▚ som inte behövs.  
### ▚▚▚▚-▚▚-▚▚
▚▚▚▚  
▚▚▚▚ Första rubriken bör vara startdatumet som ni angav i rubriken "Realistiskt  
▚▚▚▚ startdatum för utförandet av projektet" ovan.  
▚▚▚▚  
▚▚▚▚ Dagens innehåll för grupper med en ensam deltagare blir det som hade stått  
▚▚▚▚ i rubriken om "heltidsarbetsdagar" ovan. Den enda skillnaden är att du  
▚▚▚▚ pratar om ett specifikt datum. Ensamgrupper kan sluta läsa om den här  
▚▚▚▚ rubriken nu.  
▚▚▚▚  
▚▚▚▚ För grupper med flera deltagare så behöver ni inte skriva samma sak igen  
▚▚▚▚ igen utan kan hänvisa till dagar ovan under rubriken om  
▚▚▚▚ "heltidsarbetsdagar" för att beskriva varje dags mål.  
▚▚▚▚  
▚▚▚▚ Sådana grupper får dock motivera motivera hur de ska "tjäna kalendertid"  
▚▚▚▚ jämfört med en ensamgrupp. Det kan vara så enkelt som att skriva något i  
▚▚▚▚ stil med "vi når målen för dagssekvens 1 och halva 2 ovan eftersom vi kan  
▚▚▚▚ arbeta med NÅGOT och NÅGOT parallellt".  
### ▚▚▚▚-▚▚-▚▚
▚▚▚▚  
▚▚▚▚ Nästa datum... I övrigt samma sorts innehåll som ovan.  
### ▚▚▚▚-▚▚-▚▚
▚▚▚▚  
▚▚▚▚ Nästa datum... I övrigt samma sorts innehåll som ovan.  
### ▚▚▚▚-▚▚-▚▚
▚▚▚▚  
▚▚▚▚ Nästa datum... I övrigt samma sorts innehåll som ovan.  
### ▚▚▚▚-▚▚-▚▚
▚▚▚▚  
▚▚▚▚ Nästa datum... I övrigt samma sorts innehåll som ovan.  


[1]: [https://www.youtube.com/watch?v=1-SvuFIQjK8]
[2]: [https://www.atlassian.com/blog/productivity/how-to-write-smart-goals]
