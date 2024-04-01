# TODO (Osorterad)

### Få ut mer data/kategorier från produkter

<https://www.netonnet.se/art/dator-surfplatta/laptop/laptop-14-16-tum/angstrom-angstrom-m1home/1028915.8908/> t.ex. Kommer ut som "Ångström  (M1HOME)", vilket inte säger någonting. (Det är en laptop btw.)

### Update progressbar

En progressbar för uppdate_all.

### Uppdatera bara databasen när product.update() får ny data

Just nu uppdaterar update varje gång, även om datan va samma.

Men samtidigt så kanske man vill uppdatera för att last_updated ska uppdateras, så man vet senaste requesten?

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

### Rensa urlen på onödig info

En url kan lägga på massa en massa grejer som inte behövs för att komma åt en sida. Och en url som lagt på massa data kommer inte matcha varandra i update.

### Mail-alering

Om ett pris ändras, använd smtplib för att maila om det.

Hur fungerar det nu?

update_all() dumpar databasen till en lista med produkter -> Loopar .update() över den med threadpool -> Skickar dom uppdaterade produkterna till db.update_product_data()

Vad skulle krävas?
Att .update() skickar tillbaka om priset faktiskt är uppdaterat. -> Om det är det, spara den produkten -> Skicka dom sparade produkterna till db.update_product_data OCH mail-funktionen.

### Fler butiker

### Samma modell i olika färg

En produkt kan ofta ha olika priser i olika färger.

### Hämta produkter från olika butiker

Med urlen från en butik kunna hämta samma produkt från flera butiker.

### Gör en maxlängd på namn

<https://www.netonnet.se/art/mobil-smartwatch/smartwatch/apple-watch/apple-apple-watch-series-9-gps-45mm-midnight-aluminium-case-with-midnight-sport-band-ml/1031339.13980/>
"Apple Watch Series 9 GPS 45mm Midnight Aluminium Case with Midnight Sport Band - M/L"

Sätt en max längd på namn, typ 40 chars.

### "Hämta pris"

Vissa netonnet-produkters sidor genereras med react och priset ligger i divar med random genererade namn, priser ligger i en h2-tag med "art-nr"-price som vissa attribut.

För att hantera dom sidorna - Få ut art nr från url elr html, leta efter pris med bs4 typ find("h2", {"name": "1026559-price"}.get_text(strip=True))
