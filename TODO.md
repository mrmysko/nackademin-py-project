# TODO (Osorterad)

### Få ut mer data/kategorier från produkter?

<https://www.netonnet.se/art/dator-surfplatta/laptop/laptop-14-16-tum/angstrom-angstrom-m1home/1028915.8908/> t.ex. Kommer ut som "Ångström  (M1HOME)", vilket inte säger någonting. (Det är en laptop btw.)

### Update progressbar

En progressbar för uppdate_all.

### Uppdatera bara databasen när product.update() får ny data

### Fel-hantering

- Hantera om användaren skriver in ett index som inte finns i databasen.
- Om användaren skriver in en länk som inte har den data ExtractData letar efter.
- Om databasen inte är tillgänglig.
- Om requests inte kan hämta webbsidan.

### Verbosity

Options/Argparse flagga för att öka output till konsolen.

### Ökad formatering på databas-prints

Sorteringsinställningar, bara visa x-antal rader i taget som less/more etc.

### Uppdatera med threading

Använd threading för att uppdatera databasen kontinuerligt, även om programmet väntar på användarinput eller håller på med något annat.

### Logga meddelanden

Skicka grejer som hur många produkter som uppdaterades eller vad som lagts till till en loggfil.

### Fixa update output

Update visar inte hur många saker som faktiskt blivit uppdaterade just nu.

### Komma i lowest_price

lowest_price har ett komma som tusendelare i databasen medan price inte har det.

### Rensa urlen på onödig info

En url kan lägga på massa en massa grejer som inte behövs för att komma åt en sida. Och en url som lagt på massa data kommer inte matcha varandra i update.

### Slå ihop update och insert

Det borde finnas nån funktion i SQLite som kan uppdatera data om den finns, men inserta om den inte finns.

(Efter lite research verkar det som att det bästa sättet är två queries, så skickar datan till update först och om den ger tillbaka 0 rowcount så går den vidare till insert.)

### Mail-alering

Om ett pris ändras, använd smtplib för att maila om det.
