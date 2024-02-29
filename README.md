# Uppgift X - Beskrivande titel

## <a name='Syfte'></a>Syfte

Vad denna uppgift lär ut.

<!-- vscode-markdown-toc -->

- [Syfte](#Syfte)
- [Förberedelser](#Frberedelser)
- [Beskrivning](#Beskrivning)
  - [Detaljer](#Detaljer)
    - [Skapa en funktion](#Skapaenfunktion)
    - [Tips](#Tips)
    - [Exempel](#Exempel)
  - [Inlämningsinstruktioner](#Inlmningsinstruktioner)
- [Anteckningar](#Anteckningar)

<!-- vscode-markdown-toc-config
	numbering=false
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

## <a name='Frberedelser'></a>Förberedelser

- Nödvändiga förberedelsesteg.

## <a name='Beskrivning'></a>Beskrivning

Skriv en funktion med namnet `calculate_area` som beräknar arean av en
rektangel.

### <a name='Detaljer'></a>Detaljer

#### <a name='Skapaenfunktion'></a>Skapa en funktion

- **Funktionsignatur:** `def calculate_area(length: float, width: float) ->
float:`
- **Vad den ska göra:** Funktionen tar två argument, `length` och `width`, och
  returnerar rektangelns area.
- **Vad den ska skriva ut:** Funktionen ska skriva ut "Rektangelns area är: X"
  innan den returnerar, där X är den beräknade arean.
- **Vad den ska returnera:** Funktionen ska returnera den beräknade arean som
  ett flyttal.

#### <a name='Tips'></a>Tips

- Kom ihåg, arean av en rektangel beräknas som `längd * bredd`.
- Se till att din funktion skriver ut det krävda meddelandet innan den
  returnerar arean.

#### <a name='Exempel'></a>Exempel

1. **Anrop:** `calculate_area(5, 10)`
   - **Förväntad utskrift:** "Rektangelns area är: 50"
   - **Förväntat returvärde:** 50.0
2. **Anrop:** `calculate_area(3.5, 2)`
   - **Förväntad utskrift:** "Rektangelns area är: 7"
   - **Förväntat returvärde:** 7.0
3. **Anrop:** `calculate_area(7, 8)`
   - **Förväntad utskrift:** "Rektangelns area är: 56"
   - **Förväntat returvärde:** 56.0

### <a name='Inlmningsinstruktioner'></a>Inlämningsinstruktioner

För att lämna in din uppgift, vänligen följ dessa steg:

1. **Använda Github Classroom:**

   - Du har troligen redan accepterat uppgiften via en länk som tillhandahålls
     av utbildaren och gjort en `git clone` av det tilldelade repositoriet då du
     läser denna text. Det är i detta repository du kommer att hitta `README.md`
     med ytterligare instruktioner.

2. **Modifiera `uppgift.py`:**

   - Din lösning på uppgiften ska skrivas i `uppgift.py`. Det finns specifika
     instruktioner i `uppgift.py` om var du ska placera din källkod.

3. **Lämna in med Git:**

   - När du är klar med din uppgift, använd kommandona `git add .`, `git commit`
     följt av `git push` för att skicka in dina ändringar till GitHub.

4. **Automatiska "smoke tests":**

   - Efter att du har pushat din kod kommer automatiska "smoke tests" att köras.
     Dessa tester indikeras med en grön bock om de passerar, eller ett rött
     kryss om de misslyckas. Om du får ett rött kryss, är det viktigt att du
     klickar dig fram i GitHub tills du kan se varför testerna inte passerade.

5. **Feedback och granskning från utbildaren:**

   - Om dina tester passerar med en grön bock, kan du invänta feedback från din
     utbildare. Utbildaren kan antingen sätta "request changes" om ytterligare
     förändringar behövs, eller "approve" om uppgiften är godkänd som den är.
     Det är viktigt att du inväntar någon av dessa innan du fortsätter.
   - Efter att utbildaren har gjort "approve" på din inlämning, får du göra en
     "merge" av din pull request till huvudgrenen (main/master), men inte förrän
     godkännande har erhållits.

6. **Initiera diskussioner i pull requesten:**
   - Som student är du uppmuntrad att aktivt delta i processen genom att
     initiera diskussioner i din pull request. Detta är en viktig del av
     inlärningsprocessen, där du kan ställa frågor, begära förtydliganden eller
     diskutera lösningar och feedback med din utbildare. Att engagera sig i
     dessa diskussioner ger dig möjlighet att djupare förstå uppgiftens krav och
     förbättra din kod baserat på interaktionen.

Det är också viktigt att noggrant granska feedbacken och göra de nödvändiga
justeringarna baserat på utbildarens anvisningar för att säkerställa att din
uppgift uppfyller alla krav.

## <a name='Anteckningar'></a>Anteckningar

Inga.
