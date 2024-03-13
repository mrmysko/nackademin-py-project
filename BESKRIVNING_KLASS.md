# Beskrivning

Skapa en klass med namnet `MinKlass` som beräknar arean av en rektangel.

## Klassen `MinKlass`

Vad den ska göra.

### Konstruktor

- Konstruktorns signatur: `__init__(length: float, width: float) -> float`
- Utskrift: "Rektangelns area är: X"
- Returvärde: Inget

#### Exempel

1. Anrop: `__init__(5, 10)`

   - Utskrift: "Rektangelns area är: 50"
   - Returvärde: Inget

2. Anrop: `__init__(3.5, 2)`

   - Utskrift: "Rektangelns area är: 7"
   - Returvärde: Inget

3. Anrop: `__init__(7, 8)`
   - Utskrift: "Rektangelns area är: 56"
   - Returvärde: Inget

### Metoden `substitute`

Vad den ska göra.

- Signatur: `substitute(length: float, width: float) -> float`
- Utskrift: "Rektangelns area är: X"
- Returvärde: Funktionen ska returnera den beräknade arean som ett flyttal.

#### Exempel

1. Anrop: `substitute(5, 10)`

   - Utskrift: "Rektangelns area är: 50"
   - Returvärde: Inget

2. Anrop: `substitute(3.5, 2)`

   - Utskrift: "Rektangelns area är: 7"
   - Returvärde: Inget

3. Anrop: `substitute(7, 8)`
   - Utskrift: "Rektangelns area är: 56"
   - Returvärde: Inget

### Tips

- Kom ihåg, arean av en rektangel beräknas som `längd * bredd`.

- Se till att din funktion skriver ut det krävda meddelandet innan den
  returnerar arean.

### Exempel

1. Anrop: `calculate_area(5, 10)`

   - Utskrift: "Rektangelns area är: 50"
   - Returvärde: 50.0

2. Anrop: `calculate_area(3.5, 2)`

   - Utskrift: "Rektangelns area är: 7"
   - Returvärde: 7.0

3. Anrop: `calculate_area(7, 8)`
   - Utskrift: "Rektangelns area är: 56"
   - Returvärde: 56.0
