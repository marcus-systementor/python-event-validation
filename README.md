# Validering – Event / konsert

Programmet kör redan, men det skyddar inte reglerna tillräckligt bra. Er uppgift är att stegvis göra ett litet event-system säkrare med tydliga **validation functions** och **operation functions**. En validation function svarar `True` eller `False` på om något är tillåtet; en operation function gör ändringen **bara om** svaret tillåter det.

```text
validation function → får detta göras?
operation function  → kontrollera först, ändra sedan state
```

Det här är en labb i grupp för **Grundläggande programmering i Python, dag 14**. Den tränar procedurell Python med `dict`, variables, functions, `if`, `return`, `and`, `or`, `not`, enkel `while`, `input()` och `print()`. Kärnan är steg 1–9, 11 och 12; steg 10 (meny) är valfri fördjupning. Ni behöver inga classes, filer, paket eller automatiserade test. Vi utgår från att de givna värdena har rätt Python-typ; uppgiften gäller **verksamhetsregler**, inte exception handling.

## Kom igång och samarbeta

Om läraren delar en publik GitHub-template skapar ni ett personligt, normalt **Private**, repo från den. Git är inte huvudmomentet: gör gärna en liten `commit` efter varje färdigt steg och turas om att skriva och granska.

Öppna mappen med `README.md` i terminalen och kör `python main.py` (på Windows kan `py main.py` fungera; på vissa datorer `python3 main.py`). Inga paket ska installeras.

## Filerna du arbetar med

| Fil | Använd den till |
| --- | --- |
| [event_system.py](event_system.py) | **Här ändrar ni reglerna.** Förbättra validation functions och operation functions här. |
| [main.py](main.py) | **Här kontrollerar ni resultatet.** Kör observationerna och lägg små egna kontroller längst ned. |
| [HJALP.md](HJALP.md) | Ledtrådar för steget ni arbetar med. Läs när ni har kört fast. |
| [REFLECTION.md](REFLECTION.md) | Reflektionsfrågor att svara på när ni är klara. |
| `facit/` | Lärarens lösning. Öppna bara när läraren ber er göra det. |

Arbeta så här i varje steg: läs regeln tillsammans, bestäm ett `True`-fall och ett `False`-fall, skriv ändringen och kontrollera om ni får det förväntade resultatet. Om ni behöver pausa: spara ert senaste **fungerande** steg.

**Tempo:** Kärnarbetet är steg 1–9, 11 och 12. Som riktmärke kan ni göra steg 1–5 först, steg 6–9 därefter och steg 11–12 sist, med pauser och tid för gemensam felsökning. Steg 10 (meny) är **valfri fördjupning** som ni gör om tiden räcker.

## Utgångsläge och gemensamma regler

`main.py` skapar **nya** `event`- och `attendee`-dictionaries för varje scenario. Därför kan ni jämföra utskrifterna utan att ett scenario råkar ändra nästa. Varje scenario visar rubrik, state före, anrop, return-värde, state efter och en fråga. Programmet ska starta utan traceback. Till exempel kan en bokning med `tickets_left = 0` ändå returnera `True` och lämna `tickets_left = -1`. Det är ett logiskt fel, inte ett syntaxfel.

De två dictionary-mönstren ser ut så här i startprogrammet:

```python
event = {
    "name": "Python Live",
    "is_event_open": True,
    "is_cancelled": False,
    "minimum_age": 18,
    "tickets_left": 5,
}

attendee = {
    "name": "Alex",
    "age": 20,
    "has_ticket": False,
    "has_guest_pass": False,
    "has_valid_id": True,
    "is_checked_in": False,
}
```

Använd samma enkla kontrakt genom hela labben: en operation returnerar `True` om den lyckades och `False` om den nekades. Vid `False` får **varken** `event` **eller** `attendee` ändras. Validation functions returnerar bara ett svar; de får aldrig ändra dictionaries. Försök inte lösa reglerna genom att enbart dölja felmeddelanden i `main.py`.

Alla uppgiftens function-namn finns redan i [event_system.py](event_system.py), och de är importerade i [main.py](main.py).

### Små kontroller i main.py

Stegen nedan har korta kodexempel. Klistra in dem **längst ned i `main.py`, efter raden `run_observations()`** och kör `python main.py`. (Har ni valt att bygga menyn i steg 10: lägg kontrollerna före anropet till `run_menu()`, annars körs de först när menyn avslutas.) Observationerna skrivs ut först och era kontroller sist. Skapa alltid nya data med `make_event()` och `make_attendee()` för varje oberoende scenario, och ta bort kontrollerna när de inte längre hjälper.

**Viktigt:** De förväntade resultaten gäller **efter att ni har gjort det aktuella steget**. Startkoden är medvetet ofullständig och kan ge andra svar. Att ett gammalt scenario fortfarande visar fel kan vara väntat: i steg 4 fungerar `can_book_ticket()`, men först i steg 5 börjar `book_ticket()` använda svaret. Samma sak gäller inträde och `check_in()` i steg 6–8.

## Steg 1 – undersök utan att ändra kod

**Mål:** Hitta logiska fel i ett program som ändå kör utan traceback.

**Gör:** Kör `python main.py`. Läs minst scenarierna 1, 3, 5 och 9. Skriv tillsammans ner fyra operationer som borde nekas och vilket state eller return-värde som blir fel. Ändra ännu ingen kod.

**Klar när:** Alla i gruppen kan peka på minst fyra fel och förklara varför ”kör utan att krascha” inte betyder ”följer reglerna”. Scenario 1 visar `tickets_left = -1`; scenario 9 visar att ett cancelled event fortfarande är öppet. Ingen `commit` behövs för observationssteget.

## Steg 2 – en rimlig ålder

**Mål:** Skilja ett giltigt `int` från en giltig ålder.

**Gör:** Ändra bara `is_valid_age(age)` i `event_system.py`. Funktionen ska returnera `False` när `age` är negativ och `True` när den är 0 eller större. Spara inget nytt state. Prova tillfälligt i `main.py` att skriva ut svaren för `-1`, `0` och `18`.

**Klar när:** `is_valid_age(-1)` ger `False`, `is_valid_age(0)` och `is_valid_age(18)` ger `True`. Scenario 7 visar nu `False`. Övriga startproblem finns kvar tills deras regler kopplas in senare.

**Commit:** `Validate attendee age`

## Steg 3 – biljett eller gästpass

**Mål:** Använda `or` för två sätt att få ett entry pass.

**Gör:** Förbättra `has_entry_pass(attendee)`. Den ska svara `True` om `has_ticket` **eller** `has_guest_pass` är `True`; annars `False`. Funktionen får inte ändra attendee. Prova med tre nya attendees: bara biljett, bara gästpass och inget av dem. Använd `make_attendee()` och ändra en bool-key åt gången före anropet.

**Klar när:** De tre svaren är `True`, `True`, `False` i den ordningen. Scenario 4 visar nu `True`. En gästpass-innehavare får fortfarande ingen automatisk biljett: `has_ticket` förblir `False`.

**Commit:** `Add entry pass validation`

## Steg 4 – får en biljett bokas?

**Mål:** Skriva en **validation function** som bara svarar.

**Gör:** Förbättra `can_book_ticket(event, attendee)` med fyra villkor: eventet är öppet, eventet är **inte** cancelled, `tickets_left > 0` och personen har **inte** redan biljett. Använd gärna tydliga lokala boolean variables som `is_open`, `is_not_cancelled`, `has_tickets_left` och `does_not_have_ticket`, och kombinera dem med `and` och `not`. Läs bara dictionary-värden; ändra ingenting här.

**Klar när:** Med ett nytt öppet event och ny attendee är svaret `True`. Ändra **en** sak i taget på nya data: 0 biljetter, stängt event, cancelled event eller redan ägd biljett ger var för sig `False`. Jämför state före och efter anropet: det ska vara identiskt. Scenario 1–3 kan ännu vara fel eftersom `book_ticket()` inte använder valideringen förrän i nästa steg.

**Kontrollera (efter steg 4):**

```python
event = make_event()
attendee = make_attendee()
print(can_book_ticket(event, attendee))  # True
event["tickets_left"] = 0
print(can_book_ticket(event, attendee))  # False
print(event["tickets_left"], attendee["has_ticket"])  # 0 False (oförändrat)
```

**Commit:** `Validate ticket booking`

## Steg 5 – boka utan ogiltigt state

**Mål:** Låta en **operation function** använda valideringen före ändring.

**Gör:** Förbättra `book_ticket(event, attendee)`. Anropa först `can_book_ticket(...)`. Om den svarar `False`: avsluta direkt med `return False`. Annars minska `tickets_left` med 1, sätt `has_ticket = True` och returnera `True`. Låt dessa två state-ändringar ske **efter** kontrollen.

**Klar när:** Ny attendee och 5 biljetter ger `True`, 4 biljetter kvar och `has_ticket = True`. Scenario 1–3 nekas nu: inget negativt antal, ingen bokning av stängt event och ingen extra biljett till samma person. Prova också `is_cancelled = True`: både event och attendee ska vara oförändrade efter `False`.

**Kontrollera (efter steg 5):**

```python
event = make_event()
attendee = make_attendee()
print(book_ticket(event, attendee))  # True
print(event["tickets_left"], attendee["has_ticket"])  # 4 True
print(book_ticket(event, attendee))  # False (har redan biljett)
print(event["tickets_left"], attendee["has_ticket"])  # 4 True

event = make_event()
attendee = make_attendee()
event["tickets_left"] = 0
print(book_ticket(event, attendee))  # False
print(event["tickets_left"], attendee["has_ticket"])  # 0 False
```

**Commit:** `Protect ticket booking state`

## Steg 6 – får personen gå in?

Steg 6 är uppdelat i två delar. **Båda delarna förbättrar samma function:** `can_enter_event(event, attendee)`. Den fullständiga inträdesregeln är färdig först efter **6B**. Funktionen ska bara returnera en bool och aldrig ändra state.

### 6A – eventets regler

**Mål:** Kontrollera först det som gäller eventet.

**Gör:** Låt `can_enter_event(event, attendee)` svara `False` om eventet inte är öppet eller om det är cancelled. Använd gärna boolean variables som `is_open` och `is_not_cancelled`. Er nuvarande kontroll av `has_entry_pass(attendee)` får vara kvar tills vidare.

**Klar när:** En attendee med biljett får `True` när eventet är öppet och inte cancelled. Stängt event och cancelled event ger var för sig `False` (på nya data). Eventet-reglerna kräver ännu inte ID eller ålder.

**Kontrollera (efter 6A):**

```python
event = make_event()
attendee = make_attendee()
attendee["has_ticket"] = True
print(can_enter_event(event, attendee))  # True
event["is_event_open"] = False
print(can_enter_event(event, attendee))  # False
```

**Commit:** `Validate event rules for entry`

### 6B – personens regler

**Mål:** Lägg till personens krav **utan att tappa eventets krav från 6A**.

**Gör:** Fortsätt i samma function. Utöver 6A ska attendee ha entry pass (`has_entry_pass(attendee)`), ha `has_valid_id`, ha en giltig, icke-negativ age (`is_valid_age(attendee["age"])`) och en age som är minst `minimum_age`. Alla krav – både 6A och 6B – måste vara sanna. Använd hellre några tydliga boolean variables än en svårläst lång rad.

**Klar när:** En 20-åring med biljett och ID får `True`. För var och en av följande **separata** nya dictionaries blir svaret `False`: stängt event, cancelled event (6A), inget pass, ogiltigt ID, age `-1` eller age `17` vid gränsen 18. Age **exakt 18** med pass och ID ger `True`. `check_in()` ändrar fortfarande state för lätt fram till steg 8; det är väntat.

**Kontrollera (efter 6B):**

```python
event = make_event()
attendee = make_attendee()
attendee["has_ticket"] = True
print(can_enter_event(event, attendee))  # True (age 20)
attendee["age"] = 18
print(can_enter_event(event, attendee))  # True (exakt minimum_age)
attendee["age"] = 17
print(can_enter_event(event, attendee))  # False
attendee["age"] = 18
attendee["has_valid_id"] = False
print(can_enter_event(event, attendee))  # False

event = make_event()
attendee = make_attendee()
attendee["has_guest_pass"] = True
event["is_cancelled"] = True
print(can_enter_event(event, attendee))  # False (6A gäller fortfarande)
```

**Commit:** `Validate attendee entry rules`

## Steg 7 – en incheckning per person

**Mål:** Låta en validation function bygga vidare på en annan.

**Gör:** Förbättra `can_check_in(event, attendee)`. Den ska svara `True` bara om `can_enter_event(...)` svarar `True` **och** `is_checked_in` ännu är `False`. Den ska inte ändra attendee. Prova en giltig person före och efter att du tillfälligt ändrat `is_checked_in` på en ny dictionary.

**Klar när:** Giltig, ännu inte incheckad person ger `True`; samma data med `is_checked_in = True` ger `False`. En person utan pass ger också `False`. State före/efter själva validation-anropet är identiskt.

**Kontrollera (efter steg 7):**

```python
event = make_event()
attendee = make_attendee()
attendee["has_ticket"] = True
print(can_check_in(event, attendee))  # True
attendee["is_checked_in"] = True
print(can_check_in(event, attendee))  # False
print(attendee["is_checked_in"])  # True (validation ändrar inget)
```

**Commit:** `Validate attendee check in`

## Steg 8 – checka in säkert

**Mål:** Ge `check_in()` samma skydd som dess validation function.

**Gör:** Förbättra `check_in(event, attendee)`: anropa `can_check_in(...)` **innan** `is_checked_in` ändras. Vid nekad operation: `return False` och ändra inget. Vid tillåten operation: sätt `is_checked_in = True` och `return True`. Inga andra keys ska ändras.

**Klar när:** Scenario 5, 6 och 8 nekas och lämnar state oförändrat. Prova separat en 17-åring med biljett och ID: `False`. Prova en 20-åring med biljett och ID: första anropet ger `True`, andra `False`; `is_checked_in` förblir `True` efter det andra. Age 18 ska lyckas om övriga regler uppfylls.

**Kontrollera (efter steg 8):**

```python
event = make_event()
attendee = make_attendee()
attendee["has_ticket"] = True
print(check_in(event, attendee))  # True
print(attendee["is_checked_in"])  # True
print(check_in(event, attendee))  # False (andra försöket)
print(attendee["is_checked_in"])  # True (oförändrat)

event = make_event()
attendee = make_attendee()
print(check_in(event, attendee))  # False (inget pass)
print(attendee["is_checked_in"])  # False
```

**Commit:** `Protect attendee check in state`

## Steg 9 – ställ in eventet säkert

**Mål:** Hindra en upprepad cancellation och skydda senare operationer.

**Gör:** Förbättra `cancel_event(event)`. Om `is_cancelled` redan är `True`, returnera `False` utan ändring. Annars sätt `is_cancelled = True`, sätt `is_event_open = False` och returnera `True`. Kontrollera sedan att dina befintliga regler för bokning och inträde använder detta state; lägg inte specialregler i `main.py`.

**Klar när:** Scenario 9 ger `True` för första cancellation, `False` för andra och `False` för bokningen efteråt; eventet är både cancelled och stängt. Prova sedan separat en ny attendee med biljett, giltigt ID och age 20 mot det inställda eventet: `check_in(...)` ger `False` utan state-ändring; annars skulle personen ha fått gå in. Prova också att cancel ett redan stängt men ännu inte cancelled event: första cancellation är fortfarande tillåten enligt denna labbs enkla regel.

**Kontrollera (efter steg 9):**

```python
event = make_event()
attendee = make_attendee()
print(cancel_event(event))  # True
print(cancel_event(event))  # False
print(event["is_cancelled"], event["is_event_open"])  # True False
print(book_ticket(event, attendee))  # False
print(event["tickets_left"], attendee["has_ticket"])  # 5 False
```

**Commit:** `Validate event cancellation`

## Steg 10 – Fördjupning – valfri meny

**Valfritt:** Ni kan hoppa över menyn och gå direkt till steg 11 och 12. Gör den här delen bara om ni har tid kvar efter steg 9. Ingen annan del av labben kräver en meny.

**Mål:** Skilja valet i en meny från reglerna i functions.

**Gör:** Behåll `run_observations()` för senare kontroll, men byt **det sista anropet** i `main.py` mot ett anrop till en ny `run_menu()`. I `run_menu()`, skapa **ett** event och **en** attendee före en enkel `while`-loop. Visa valen nedan, läs `choice = input("Choose: ")` varje varv och använd `if`/`elif`/`else` för valet. `0` avslutar loopen. `1` anropar `show_state(event, attendee)`. `2`, `3` och `4` anropar respektive `book_ticket`, `check_in` och `cancel_event`; skriv ett tydligt meddelande utifrån return-värdet. Ett okänt val ska bara ge ett hjälpsamt meddelande och fråga igen. Ändra **inte** dictionary-regler direkt i menygrenarna.

```text
1. Show status
2. Book ticket
3. Check in
4. Cancel event
0. Exit
```

**Klar när:** `1, 2, 1, 3, 1, 3, 4, 2, 0` i en körning visar först inga rättigheter, sedan en biljett, en lyckad incheckning, ett nekat andra incheckningsförsök, cancellation och en nekad bokning efteråt. Kör sedan **på nytt** med `4, 2, 0`: bokning nekas även för en person som inte redan har biljett, eftersom eventet är cancelled. `0` avslutar; ett okänt val kraschar inte. Menyn fattar inte egna beslut om age, pass eller biljetter – den använder functions i `event_system.py`.

**Commit:** `Connect validation to menu flow`

## Steg 11 – prova sex manuella scenarier

**Mål:** Förutsäga och kontrollera både tillåtna och nekade operationer.

**Gör:** Skapa minst **sex** egna scenarier med `make_event()` och `make_attendee()`; kör dem med vanliga function-anrop och `print()`, inte ett testing framework. Lägg era scenarier längst ned i `main.py`, efter `run_observations()`, eller i en liten egen function i samma fil. Ni behöver ingen meny. Använd **nya dictionaries per scenario**. Förutsäg return-värde och state **innan** ni kör. Ha minst två giltiga fall, tre ogiltiga och ett gränsfall. Age lika med `minimum_age` och `tickets_left = 0` är användbara gränser.

Kopiera gärna tabellen till era gruppanteckningar och fyll i efter körning:

| Scenario | Förväntat return-värde | Förväntat state | Faktiskt resultat |
| --- | --- | --- | --- |
| 1 – giltigt |  |  |  |
| 2 – giltigt |  |  |  |
| 3 – ogiltigt |  |  |  |
| 4 – ogiltigt |  |  |  |
| 5 – ogiltigt |  |  |  |
| 6 – gränsfall |  |  |  |

**Klar när:** Ni kan förklara sex körningar. Varje nekad **operation** lämnade både event och attendee oförändrade. Ni har minst en kontroll där `age == minimum_age` ger ett tillåtet inträde och en där `tickets_left == 0` nekar bokning. Detta är manuell kontroll som förbereder tankesättet inför senare undervisning om testing; inga testverktyg behövs nu.

**Commit:** `Add manual validation scenarios`

## Steg 12 – gör reglerna läsbara

**Mål:** Kunna läsa, granska och förklara gruppens validation logic.

**Gör:** Läs igenom [event_system.py](event_system.py) tillsammans. Är boolean names med `is_`, `has_` och `can_` tydliga? Ändrar någon validation function state av misstag? Kan en operation returnera `False` **efter** en state-ändring? Återanvänder `can_check_in()` regler från `can_enter_event()`? Håll functions små och ändra bara sådant som gör dem tydligare eller rättar en upptäckt regelmiss. Kör sedan `python main.py` och minst två av era manuella scenarier igen (och menyn, om ni byggde den).

**Klar när:** Varje person i gruppen kan förklara minst tre functions, inklusive en validation function och en operation function. Alla tidigare giltiga och ogiltiga kontrollfall fungerar fortfarande. Skriv ett kort gemensamt svar i [REFLECTION.md](REFLECTION.md) och låt varje person lägga till en egen mening om vad hen förstår bättre nu.

**Commit:** `Refactor validation rules`

## Frivilligt om ni blir klara tidigt

Välj högst en liten utökning efter kärnstegen (1–9, 11 och 12). Steg 10 (menyn) är också en fördjupning. Använd samma enkla `dict`/function-mönster och kör både ett `True`-fall och ett `False`-fall:

- **Guest list:** lägg till `is_on_guest_list` och låt det vara ytterligare ett sätt att få entry pass.
- **Reopen event:** skriv en operation med en uttalad regel för när ett event får öppnas igen.
- **Multiple attendees:** ha en `list` med flera attendee-dictionaries och låt menyn (om ni har byggt den) välja en av dem.
- **Förklara nekande:** skriv tydligare text om varför en operation nekades (i menyn om ni har en, annars i era kontroller), utan att flytta reglerna dit.

Utökningarna är **inte krav**. De ska inte lägga till classes, filer, externa paket eller automatiserade test.
