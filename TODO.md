# TODO (Osorterad)

### Faktorisera om

Gör om, gör rätt.

### Fixa mail-alert

Jag mailar om användaren manuellt kör en update all i CLI, onödigt.

Just nu mailar jag om priset är lägre än det lägsta, men jag borde maila om priset är lägre än nuvarnade, oavsett vad det lägsta var...Typ "product price now x, was y, lowest ever z"

### Få ut mer data/kategorier från produkter

<https://www.netonnet.se/art/dator-surfplatta/laptop/laptop-14-16-tum/angstrom-angstrom-m1home/1028915.8908/> t.ex. Kommer ut som "Ångström (M1HOME)", vilket inte säger någonting. (Det är en laptop btw.) t.ex. kan man få ut kategorier från breadcrumben.

### Update progressbar

En progressbar för uppdate_all.

### kwargs

Byt ut args i product-klassen till kwargs.

### Fel-hantering

- Hantera om användaren skriver in ett index som inte finns i databasen.
- Om användaren skriver in en länk som inte har den data ExtractData letar efter.
- Om databasen inte är tillgänglig.
- Om requests inte kan hämta webbsidan.

### Verbosity

Options/Argparse flagga för att öka output till konsolen.

### Ökad formatering på databas-prints

Sorteringsinställningar, bara visa x-antal rader i taget som less/more etc.

Jag har en alternativ printout för konsoler med lägre bredd, borde gå att göra mer dynamiskt.

### Uppdatera med threading

Använd threading för att uppdatera databasen kontinuerligt, även om programmet väntar på användarinput eller håller på med något annat.

Sätt update_all funktionen i en subprocess.

### Logga meddelanden

Skicka grejer som hur många produkter som uppdaterades eller vad som lagts till till en loggfil.

### Fixa update output

Update visar inte hur många saker som faktiskt blivit uppdaterade just nu.

### Rensa urlen på onödig info

En url kan lägga på massa en massa grejer som inte behövs för att komma åt en sida. Och en url som lagt på massa data kommer inte matcha varandra i update.

### Statistik

Mer statistik så som hur länge priset legat, tids-graf, olika priser i olika butiker vid olika tidpunkter etc.

### GUI

GUI för alla funktioner.

### Fler butiker

### Samma modell i olika färg

En produkt kan ofta ha olika priser i olika färger.

### Hämta produkter från olika butiker

Med urlen från en butik kunna hämta samma produkt från flera butiker.

### "Hämta pris"

<https://www.netonnet.se/art/tv/mediaspelare/google-chromecast/google-chromecast-with-google-tv-hd/1026559.18273>
<https://www.netonnet.se/art/vitvaror/mikrovagsugn/andersson-mikrovagsugn-meo-2-6/226770.18008>

Genereras med javascript, så priset renderas på annat sätt. requests kör inte js. Priset ligger i en h2-tag med "art-nr"-price som vissa attribut.

Få ut art nr från url elr html, leta efter pris med bs4 typ find("h2", {"name": "1026559-price"}.get_text(strip=True))

### Stäng databasen

Databasen står öppen när programmet körs, även om den inte används till något. Stäng den efter varje operation, eller använd "with" för att göra det automatiskt.

### Butikslogin

Hantera butiksinloggning för medlemspriser.
