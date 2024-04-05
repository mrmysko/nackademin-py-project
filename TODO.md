# TODO (Osorterad)

### Faktorisera om

Gör om, gör rätt.

### Fixa mail-alert

Jag maila inte om användaren manuellt kör en update i CLI.

### Få ut mer data/kategorier från produkter

<https://www.netonnet.se/art/dator-surfplatta/laptop/laptop-14-16-tum/angstrom-angstrom-m1home/1028915.8908/> t.ex. Kommer ut som "Ångström (M1HOME)", vilket inte säger någonting. (Det är en laptop btw.) t.ex. kan man få ut kategorier från breadcrumben.

### Göm credentials

Mail-credentials ligger i klartext i mailalert filen...stoppa i en credentials fil eller nått och hasha.

### Felhantering

Hantera fel på ett bättre sätt...nu är det i princip tre try except som bubblar upp ett exception som fångas i main för om en användare skriver in en felaktig länk.

- Om databasen inte är tillgänglig.
  - Vad ska hända? = Raise nått fel och stäng programmet. Hur kan jag differentiera från olika sätt den är unavailable på? Locked/Permissions/Corrupt etc.

- Om ett databas-värde inte finns längre (En produkt kanske bytt namn, url eller blivit borttaget)

### Verbosity

Options/Argparse flagga för att öka output till konsolen.

### Options table

Ha options i uit och spara dom i databasen. t.ex. sorting/display options, update interval, databasfil, mail-recipients.

### Ökad formatering på databas-prints

Sorteringsinställningar, bara visa x-antal rader i taget som less/more etc.

Jag har en alternativ printout för konsoler med lägre bredd, borde gå att göra mer dynamiskt.

### Uppdatera med threading

Använd threading för att uppdatera databasen kontinuerligt, även om programmet väntar på användarinput eller håller på med något annat.

Sätt update_all funktionen i en subprocess.

### Loggfil

Skicka grejer som hur många produkter som uppdaterades eller vad som lagts till till en loggfil.

### Rensa urlen på onödig info

En url kan lägga på massa en massa grejer som inte behövs för att komma åt en sida. Och en url som lagt på massa data kommer inte matcha varandra i update.

### Statistik

Mer statistik så som hur länge priset legat, tids-graf, olika priser i olika butiker vid olika tidpunkter etc.

Att ens visa ett timestamp vore en improvement tbh.

### GUI

GUI för alla funktioner.

### Fler butiker

Amazon, Inet, Webhallen, Komplett etc...speciellt Amazon eftersom deras sida är oöverskådlig och byter priser när som helst baserat på vad som helst.

### Samma modell i olika färg

En produkt kan ofta ha olika priser i olika färger.

### Update progressbar

En progressbar för uppdate_all.

### Hämta produkter från olika butiker

Med urlen från en butik kunna hämta samma produkt från flera butiker.

### "Hämta pris"

<https://www.netonnet.se/art/tv/mediaspelare/google-chromecast/google-chromecast-with-google-tv-hd/1026559.18273>
<https://www.netonnet.se/art/vitvaror/mikrovagsugn/andersson-mikrovagsugn-meo-2-6/226770.18008>

Genereras med javascript, så priset renderas på annat sätt. requests kör inte js. Priset ligger i en h2-tag med "art-nr"-price som vissa attribut.

Få ut art nr från url elr html, leta efter pris med bs4 typ find("h2", {"name": "1026559-price"}.get_text(strip=True))

Prova dryscrape elr qt4
<https://pythonprogramming.net/javascript-dynamic-scraping-parsing-beautiful-soup-tutorial/>

Netonnet har ett API
<https://api.netonnet.se/reservation/api/v1/isreservable?MarketId=1&SiteType=1&ArticleNumber=1026559&ArticlePriceIncVat=499&CustomerId=-1>

Nvm, kommer inte åt det om inte origin är deras front-end. Also beta.netonnet.se finns och verkar va en ny site som bygger på react.

### Butikslogin

Hantera butiksinloggning för medlemspriser.

### Clean commits

Commits kostar tydligen prestanda och låser databsen...istället för att commita efter varje ändring så kan man commita när man stänger databasen, men riskerar att förlora ocommitad data om programmet kraschar.

Men t.ex. update_all kanske inte behöver en commit efter varje insert, commita efter hela loopen är körd.

"timeout (float) – How many seconds the connection should wait before raising an OperationalError when a table is locked. If another connection opens a transaction to modify a table, that table will be locked until the transaction is committed. Default five seconds." - Om jag inte commitar på remove tills programmet avslutas så är den tabellen låst.

### Cursor-problemet

För att kunna hantera fel måste jag kolla värdet i cursorn, men kollar jag värdet så flyttar jag "pointern".

Lösningen är att jag läser in allt i minne med .fetchone/all/many. och skickar det till define_product istället för ett cursor-object, men då måste jag skriva om define_product IGEN, och gå tillbaka till att läsa in allt i minnet.

Jag vet inte vad som är mest tidseffektivt, men jag skulle i get_product_data kunna köra queryn, kolla om den kom tillbaka tom och om den inte gjorde det så kör jag samma query igen för att få en ny pointer.

### SQLite timedate

SQLite kan hantera timedate själv på något sätt, då kan den hålla reda på när tabeller blir uppdaterade själv.

### Daemon-halvmesyr

Daemon är något av en halvmesyr, om man schemalägger den så öppnas en ny instans varje gång som ligger i bakgrunden. Ta bort loopen och låt -d köra update_all EN gång.

### Refactor dump

Behöver jag dumpa databasen varje gång jag vill printa den eller göra något med den? Är det bättre att läsa in den i minne och spara den, och sen commita den till databasen när programmet är färdigt?

### Prune db

Lägg till ett sätt att plocka bort produkter med döda länkar ur databasen.
