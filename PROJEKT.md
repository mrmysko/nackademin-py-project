# Projektplanering - "I dno, nån prisfetcher-grej typ"

## Vad ska ditt program göra?

Mitt program ska, beroende på hur långt jag hinner:

```
    - Ta in data om produkter från en eller flera webbutiker.
    - Visa det för användaren i CLI.
    - Spara datan i en databas.
    - Kunna hämta data från databsen och visa den.
```

Det här är ju bara "the basic" base-caset. Det finns ju mycket man kan lägga till som jag spånar på längre ner. Men det är svårt att säga hur lång tid något kommer ta när man inte gjort det förut.

## Vad är motivationen till att skapa det?

För att jag måste.

## Detaljer

### Gränssnitt

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#eee',
'primaryTextColor':'#f00','primaryBorderColor':'#55f','lineColor': '#f00' }}}%%

classDiagram

class Shop
<<abstract>> Shop
Shop: self.name
Shop: self.base_url
Shop : get_data()*


class Some_Shop
Shop <|-- Some_Shop
Some_Shop : get_data(url) -> tuple

class Some_Shop2
Shop <|-- Some_Shop2
Some_Shop2 : get_data(url) -> tuple

class Product
Product: self.name
Product: self.url
Product: self.price
Product: update_price()

```

Användarinteraktionen kanske är att man typ kör programmet och presenteras en meny där man kan lägga till en produkt, visa alla produkter, ändra en produkt, eller ta bort en produkt.

Vill man lägga till en produkt så ger man den ett namn och en url. Webbutiken plockas ut från urlen och det motsvarar ett class-objekt för den butiken eftersom olika butiker behöver olika beatifulsoup-kod för att plocka ut relevant data. Finns inte butiken så måste man hantera det på nått sätt.

Jag vet inte vilken datatyp urlerna ska ha än...har jag inte funktionalitet för mer än en butik än så räcker ju en sträng, men med fler butiker kanske det ska vara en dict?

Sen har man väl nån funktion för att skriva data till databasen, I dno, har inte kommit så långt än.

### Hur förmedlar ditt program sitt resultat

CLI. Kommer inte ha tid att dilla med GUI.

### Vilka operativsystem ska ditt program fungera på?

Alla som kan köra python.

### Externa bibliotek

| Paket    | Beskrivning                            |
| -------- | -------------------------------------- |
| requests | Gör http requests och hämtar data      |
| bs4      | BeatifulSoup, parsar html och xml data |
| sqlite3  | Hanterar data in/ut till databasen     |

## Realistiskt startdatum för utförandet av projektet

Datum: 2024-03-26

Motivering? Börjar väl med research idag.

## Arbetsplan

Version 0.1: Hämta data och få ut relevant information, visa den i terminalen.

Version 0.2: Spara datan i en databas, kunna få ut den därifrån.

```
Grejer man kan bygga på:
    - Spara datan i en databas.
    - Om datan sparas i en databas, ha en metod för att uppdatera pris.
    - Visa alla grejer formaterade.
    - Lägga till fler butiker för samma produkt.
    - Hämta prisdata för samma produkt i olika färger.
    - Hantera användarinloggning för medlemspriser?
    - Automatisk uppdatering.
    - Statistik över tid.
    - Söka efter produkter direkt i CLI.
    - Leta upp produkter från en butik i andra butiker.
    - Crawla en webbutik med Scrapy.
    - Alternativa input-metoder, cli-args OCH meny.
    - GUI
```

[1]: [https://www.youtube.com/watch?v=1-SvuFIQjK8]
[2]: [https://www.atlassian.com/blog/productivity/how-to-write-smart-goals]
