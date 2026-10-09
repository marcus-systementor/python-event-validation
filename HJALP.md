# Hjälp – ett steg i taget

Öppna bara det steg ni arbetar med. Steg 1–9, 11 och 12 är kärnan; steg 10 är valfritt. Läs först frågan, prova en ändring och kör `python main.py`. Läs den tydligare ledtråden först om ni fortfarande sitter fast. Hints visar **vad ni ska kontrollera**, inte en färdig function.

## Steg 1 – observation

**Första hint:** Jämför `tickets_left` före och efter scenario 1. Vilken function ändrade värdet?

**Mer hjälp:** Scenario 4 har inget felaktigt state – där är i stället boolean-svaret för snävt. Både state-fel och felaktiga svar kan visa att en regel saknas. Leta efter fyra olika orsaker, inte bara fyra olika utskrifter.

## Steg 2 – age

**Första hint:** Ska 0 vara en tillåten ålder? Ska -1 vara det?

**Mer hjälp:** `is_valid_age(age)` behöver bara **jämföra** argumentet med 0 och returnera jämförelsens bool-svar. Ändra ingen dictionary i denna function. Prova gränsen 0.

## Steg 3 – entry pass

**Första hint:** Räcker biljett **eller** gästpass? Vilka keys innehåller de svaren?

**Mer hjälp:** Bygg ett bool-svar från `has_ticket` och `has_guest_pass` med `or`. Prova var och en separat. Ett gästpass ska inte skriva om `has_ticket`.

## Steg 4 – can_book_ticket()

**Första hint:** Vilka fyra frågor måste alla få rätt svar innan en bokning tillåts?

**Mer hjälp:** Läs `is_event_open`, `is_cancelled`, `tickets_left` och `has_ticket`. Ge gärna varje del ett tydligt lokalt bool-namn och kombinera med `and`; använd `not` för de två ”får inte”-reglerna. Denna function ska inte minska `tickets_left`. Scenario 1 kan fortfarande bli fel eftersom operationen ännu inte frågar funktionen.

## Steg 5 – book_ticket()

**Första hint:** Var i operationen måste kontrollen ligga för att ett nekat försök ska lämna **båda** dictionaries oförändrade?

**Mer hjälp:** Tänk i två delar: fråga `can_book_ticket(...)`; vid `False`, lämna functionen direkt. Först därefter får `tickets_left` och `has_ticket` ändras. Kontrollera ett lyckat fall och ett fall med 0 biljetter.

## Steg 6A – can_enter_event(): eventets regler

**Första hint:** Vilka två frågor om eventet måste få rätt svar innan någon får gå in? Vilka keys läser ni?

**Mer hjälp:** Läs `is_event_open` och `is_cancelled`. Ett cancelled event är inte ett giltigt event att gå in på, så använd `not` för den ena regeln. Ge varje del ett eget bool-namn. Prova stängt och cancelled event på nya data, ett i taget. Funktionen ska bara läsa state.

## Steg 6B – can_enter_event(): personens regler

**Första hint:** Vilka fyra frågor gäller personen? Vilka tidigare validation functions kan återanvändas? Hur ser ni till att eventets regler från 6A finns kvar?

**Mer hjälp:** Det är samma function som i 6A – bygg vidare, skriv ingen ny. Personens regler är pass (`has_entry_pass`), ID, giltig age (`is_valid_age`) och age minst `minimum_age`. Alla krav, både 6A och 6B, måste vara sanna. Prova age 17, 18 och -1 mot minimum 18 med giltigt pass och ID, och prova sedan ett cancelled event med en i övrigt giltig person. Funktionen ska bara läsa state.

## Steg 7 – can_check_in()

**Första hint:** Vilken redan skriven function avgör inträde? Vad tillkommer för just incheckning?

**Mer hjälp:** Ett `True` från `can_enter_event(...)` räcker inte när `is_checked_in` redan är True. Kombinera inträdessvaret med en kontroll av att personen **inte** redan är incheckad. Ändra inte värdet i denna validation function.

## Steg 8 – check_in()

**Första hint:** Liknar detta skillnaden mellan `can_book_ticket()` och `book_ticket()`?

**Mer hjälp:** Fråga `can_check_in(...)` före tilldelningen. En guard clause kan lämna operationen med `False` innan någon key ändras. Vid tillåtet fall ändras bara `is_checked_in`. Kör samma person två gånger och jämför state efter båda.

## Steg 9 – cancel_event()

**Första hint:** Vilket bool-värde visar att cancellation redan har hänt? Vilka två event-keys måste ändras vid en ny cancellation?

**Mer hjälp:** Kontrollera `is_cancelled` **före** tilldelningarna. Vid ett nytt tillåtet anrop blir eventet både cancelled och stängt. Vid ett andra anrop ska inget ändras. Pröva booking med en person utan biljett mot det inställda eventet för att isolera rätt regel.

## Steg 10 – Fördjupning – valfri meny

Det här steget är valfritt. Hoppa gärna direkt till steg 11 och 12 om ni inte bygger en meny.

**Första hint:** Vilka data måste skapas **en gång** före loopen för att booking och check-in ska dela samma state?

**Mer hjälp:** Börja med `0` och `1`: avsluta respektive visa state. Lägg sedan till en operation åt gången. Varje menygren läser return-värdet från `event_system.py` och skriver ett meddelande; grenen ska inte själv ändra `tickets_left` eller `is_checked_in`. Ett okänt val ska gå tillbaka till frågan utan state-ändring.

## Steg 11 – egna scenarier

**Första hint:** Har ni både ett giltigt fall och ett nekat fall för samma operation? Använder fallen egna dictionaries?

**Mer hjälp:** `make_event()` och `make_attendee()` ger färska data. Ändra bara den key som behövs för ett scenario och skriv ner förväntat return-värde **före** anropet. Age exakt 18 och biljetter exakt 0 är bra gränser. Skriv ut state före och efter för att upptäcka mutation vid `False`. Ni behöver ingen meny – vanliga function-anrop och `print()` längst ned i `main.py` räcker.

## Steg 12 – läsbarhet och granskning

**Första hint:** Kan ni peka ut vilka functions som bara läser dictionaries och vilka som ändrar dem?

**Mer hjälp:** Läs varje operation uppifrån och ned. Finns en möjlig väg till `False` **efter** en tilldelning? Är en regel kopierad i stället för återanvänd? Be någon som inte skrev functionen förklara den och kör ett tidigare nekat scenario efter varje liten förbättring.

## När programmet inte startar

Läs sista raden i en traceback och hitta er fil och radnummer ovanför. Kontrollera stavning på function-namn och dictionary-keys, indrag efter `if`/`def`/`while`, och att terminalen står i mappen med `main.py`. Om `python` inte hittas, prova `py` eller `python3`. Ändra en sak, kör igen och skriv ner input, förväntat/faktiskt resultat och er hypotes innan ni ber om hjälp.
