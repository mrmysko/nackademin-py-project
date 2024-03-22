# Extra projektinfo

## Tidsåtgång och betyg

Det är projektets planerade tidsåtgång som bestämmer deltagarnas betyg enligt
nedanstående tabell:

| Betyg | Gruppstorlek | Kalenderdagar | Totalt heltidsarbete |
|-------|--------------|---------------|----------------------|
| G     | Ensam        | ca 3          | ca 3 dagar           |
| G     | 2 personer   | ca 3          | ca 4 dagar           |
| G     | 3 personer   | ca 3          | ca 5 dagar           |
| VG    | Ensam        | ca 5          | ca 5 dagar           |
| VG    | 2 personer   | ca 5          | ca 6 dagar           |
| VG    | 3 personer   | ca 5          | ca 7 dagar           |

Ovan så är `Totalt heltidsarbete = Kalenderdagar * Gruppstorlek`. Det betyder
att trots att projektgrupper med fler deltagare behöver göra ett större projekt
så bör de tjäna tid på att vara fler som kan arbeta samtidigt.

### Prioritering av Python i Projektet

Minst 75% av projektets tid ska ägnas åt Python, inklusive dess språk, inbyggda
och externa bibliotek.

Max 25% får allokeras till andra aktiviteter som lödning eller fördjupning i
komplexa algoritmer för Fourier-transformation av signaler.

Med tanke på Pythons mångsidighet och projektets öppna natur är det viktigt att
vi betonar denna fördelning. Detta hjälper till att hålla projektets fokus på
programmering och tillämpning av Python, vilket är kursens huvudsyfte.

## Redovisning och deadlines

Projektet redovisas i seminarieform inom smågrupper som utbildaren
sammanställer. Alla deltagare kommer att få berätta vad kod från deras grupp
utför. Det är därför väldigt viktigt att grupperna internt delar kunskap under
resans gång.

Den kontrollerande aspekten av redovisningen kombineras med den rolig sidan att
visa vad de skapat för övriga seminariedeltagare! Det gör att varje grupp bör ta
med en dator som är redo att köra deras program.

Om projektet missar kursens vanliga deadline för inlämning den 4 april eller
redovisningen den 5 april så kommer det att erbjudas två separata tillfällen att
bli klar med projektet senare.

Deadline påverkar på intet sätt betyget. Det går med andra ord att redovisa sitt
projekt vid sista tillfället och få högsta betyget VG.

Även fast du kan få toppbetyget VG även om du lämnar in projektet sent, så kan
det vara smart att sikta på mot att vara klar vid kursens normala deadline. Att
klara av projektet i tid ger dig mer utrymme att fokusera på vad som kommer
härnäst.

## Krav

### Fokuserade och väl formulerade committs

Projektets Git-historik är också med i bedömningen. Det är en utökning från
inlämningsuppgifterna där det inte var med i bedömningen och är gjord för att
göra projektet mer realistiskt.

Det är viktigt att varje enskild commit:

1. Har ett tydligt fokus. Det kan till exempel vara att lägga till en ny
   funktion, att laga en bugg eller att refaktorera något. Gör inte två olika
   saker i samma commit.
   
2. Har ett bra commit-meddelande som gör det enkelt att förstå vad som är syftet
   med commiten. Bestäm er i projektgruppen för om ni vill följa råden i
   artikeln [How to Write a Git Commit Message][gc] eller [Conventional Commits][cc]
   och håll er till den stil ni väljer genom hela projektet.

3. Hjälp varandra och ta upp i varje Pull Request (PR) varje commit i den följer
   ovanstående och korrigera fel. Det går bra att "skriva om historiken" för de
   nya committarna i en PR innan den mergas in till main. När committarna väl
   landat i main så ska ingen historik där skrivas om.

Om något blir fel någon gång ibland så kommer det inte att behövas någon
komplettering. Men om det är fel väldigt ofta så kommer det att behöva åtgärdas
innan projektet är godkänt.

#### Exempel på olika fokus

Här är exempel på saker som bör vara i sin egen commit och inte blandas ihop med
något annat:

- Det är helt okej att kalla den första commiten för "Initial commit", "Initial
  commit" eller liknande. Den committens fokus är att gå från inget alls till
  ett meningsfullt utgångsläge att arbeta vidare. I denna commit kan ni därför
  blanda "hejvilt" då ert fokus är mer övergripande.
- Ny funktionalitet X. Varje ny funktion i er lösning bör ha sin egen commit.
- Laga en specifik bugg ni hittat.
- Refaktorera något. Om ni vill förbättra koden så att den blir enklare att läsa
  eller utöka utan att för den sakens skull skapa ny funktionalitet eller laga
  en bugg så kallas det en refaktorering.
- Stil. Om ni bara vill köra Black Formatter på all kod för att få den att se
  snyggare ut utan att ändra något som inte är "vita tecken" så är det en rent
  stilistisk ändring.
- Byggkedja. Om ni har en skriptfil som ni kör vilken kör era tester och kanske
  gör något mer, så har ni en enkel byggkedja. Förändringar till den bör vara
  sitt eget fokus.

#### Oops! Att skriva om Git-historiken

Om du skrivit ett dåligt commit-meddelande så är det enkelt attkorrigera. Har du
råkat blanda ihop saker i en commit och vill dela upp den är det svårare men
fullt möjligt. Oavsett så får du bara ändra i Git-historiken i commits som ännu
**inte nått main-branchen**.

Relaterade länkar:

- [Git Pro: 7.6 Git Tools - Rewriting History][gh]
- [Git documentation git-push --set-upstream][gp]
- [How to undo (almost) anything with Git][u]

### Pull Request (PR) och arbetsflöde

Alla grupper, även de med en ensam medlem, bör skapa en ny branch för varje ny
sak som ni vill få in i `main`. Gör alltså inga commits direkt i `main`!

Det du konkret gör under projektarbetet är att:

1. Först undersöka om det finns någon Pull Request av en gruppkollega som du bör
   godkänna eller ge feedback på.
2. Var säker på att du är i `main` och har den senaste koden.

```bash
$ git branch
* main
$ git pull
Already up to date.
```

3. Sedan skapar du en branch. Försök att hålla branch-namnen tydliga men korta.

```bash
$ git checkout -b masken-exploderar
Switched to a new branch 'masken-exploderar'
```

4. Alla skriver sin kod och gör sina commits enligt "Fokuserade och väl
   formulerade committs" ovan.

5. När du är klar så pushar du din kod och är redo att skapa sin PR på GitHub
   genom att följa länken.

```bash
$ git push
Total 12 (delta 12), reused 3 (delta 5), pack-reused 3
remote:
remote: Create a pull request for 'masken-exploderar' on GitHub by visiting:
remote:      https://github.com/nackc8/py-projekt-ganget/pull/new/masken-exploderar
remote:
To github.com:nackc8/py12-gendoc.git
* [new branch]      masken-exploderar -> masken-exploderar
branch 'masken-exploderar' set up to track 'origin/masken-exploderar'.
```

6. Inom grupper med flera deltagare så måste alla få en "Approve" av någon annan
   i projektgrupper. Invänta "Approve" och först när du fått det så klickar du
   "Merge". Merge av någon annans kod görs endast i undantagsfall.

#### Feedback

Ofta så uppstår förändringar i ens PR som ett resultat av feedback från
gruppkollegor. Var noga med att skriva saker på ett **snällt** sätt! Alla kan
och kommer att göra många fel så att vara ödmjuk kan ge ödmjukhet tillbaka. Båda
parter behöver ha ett öppet sinne och uppskatta att ni "lyfter varandra".

### Tekniska krav

#### VS Code-tillägg

För att underlätta kodformatering och identifiering av potentiella problem i ert
projekt, rekommenderas följande VS Code-tillägg:

- Kodformaterings- och lintingverktyg:
  - [Black Formatter][b], `isort`, `Prettier`, `Ruff`, `shell-format`, och
    `shellcheck` är alla tillägg som hjälper till med kodformatering och
    kvalitetskontroll. Dessa tillägg rekommenderas och är förkonfigurerade i
    projektets inställningar.

- Använda projektinställningar:
  - För att dra nytta av de förkonfigurerade inställningarna, öppna projektets
    katalog med "Open Folder"-funktionen i VSCode. Detta är särskilt viktigt när
    ni arbetar i grupp för att säkerställa enhetliga inställningar.

- Anpassning av regler:
  - Ni har friheten att välja vilka regler från "lintverktygen" [Ruff][r] eller
    [shellcheck][sc] som ni vill ignorera. Besök verktygens officiella webbsidor för
    att lära er mer om hur ni kan anpassa eller ignorera specifika regler. Detta
    görs genom att justera inställningarna i "Open Workspace Settings".
  - Det är tillåtet (men inte rekommenderat) att helt inaktivera lintverktygen.

#### Tester

Använd [pytest][t] för projektets tester och döp dina testfiler mest `test_`
före modulens namn som ska testas.

Om projektet inte har andra externa beroenden än pytest så måste projektet
innehålla minst 20 st tester vilka körs med [pytest][t].

I annat fall så är tester valfritt.

#### Externa beroenden

`requirements.txt` ska finnas och beskriva projektets beroenden. Den ska gå att
använda med `pip install -r requirements.txt` för att sedan kunna köra
projektet.

#### Att köra projektet via en startfil

För att utbildaren enkelt ska kunna köra ert projekt bör en skriptfil vid namn
`start.sh` eller `start.ps1` skapas. Skriptet bör säkerställa att en virtuell
miljö finns och att `requirements.txt` används.

Det finns en färdig [start.sh](s) tillgänglig om ni vill utgå från den och ändra
så att Python anropar rätt fil i ert projekt. Om ni väljer ett PowerShell-skript
istället så kan ni radera Bash-versionen.

Det här är troligen inte det sätt som ni använder när ni utvecklar och testar
ert projekt. Det tar nämligen längre tid att hålla på och radera och skapa
virtuella miljöer hela tiden.

[b]:  https://github.com/psf/black
[cc]: https://www.conventionalcommits.org/en/v1.0.0
[gc]: https://cbea.ms/git-commit
[gh]: https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History
[gp]: https://git-scm.com/docs/git-push#Documentation/git-push.txt---set-upstream
[r]:  https://github.com/astral-sh/ruff
[s]:  ./start.sh
[sc]: https://github.com/koalaman/shellcheck
[t]:  https://docs.pytest.org/en/8.0.x/
[u]:  https://github.blog/2015-06-08-how-to-undo-almost-anything-with-git
