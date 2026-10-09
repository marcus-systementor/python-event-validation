# Facit / lärarmaterial

Den här mappen innehåller en komplett lösning på Event-labben. **Öppna den bara när läraren ber er göra det.** Era egna filer i rotmappen (`event_system.py` och `main.py`) är startfiler som ni själva ska förbättra – de ändras inte av facit.

## Kör lösningen

Stå i repots rotmapp och kör:

```text
python facit/main.py
```

På Windows kan `py facit/main.py` fungera; på vissa datorer `python3 facit/main.py`. Programmet kör elva observationsscenarier med state före och efter.

## Kör den valfria menyn

Menyn är **fördjupning** och inte ett krav. Öppna `facit/main.py`, längst ned: kommentera bort `run_observations()` och ta bort `#` framför `run_menu()`. Kör sedan samma kommando igen. Ett exempel på val: `1, 2, 1, 3, 1, 3, 4, 2, 0`.

## Koppling till labbens steg

| Function | Steg |
| --- | --- |
| `is_valid_age` | 2 |
| `has_entry_pass` | 3 |
| `can_book_ticket` | 4 |
| `book_ticket` | 5 |
| `can_enter_event` | 6A (eventets regler) och 6B (personens regler) |
| `can_check_in` | 7 |
| `check_in` | 8 |
| `cancel_event` | 9 |
| `run_observations()` | 1 och 11 |
| `run_menu()` | 10 (valfri) |

## Viktiga idéer

**Validation function eller operation function?** `is_valid_age`, `has_entry_pass`, `can_book_ticket`, `can_enter_event` och `can_check_in` svarar bara `True` eller `False` och ändrar aldrig `event` eller `attendee`. `book_ticket`, `check_in` och `cancel_event` utför en ändring.

**Varför validera före ändring?** Om en operation ändrar state först och upptäcker felet sedan har den redan förstört data, till exempel ett negativt `tickets_left`. Med en guard clause (`return False` tidigt) lämnas båda dictionaries orörda vid nekande.

## Jämför med er egen lösning

När läraren går igenom facit: läs era egna functions bredvid och förklara skillnaderna med egna ord. Er lösning behöver inte se likadan ut – den ska följa samma regler och samma kontrakt. Reflektionsfrågorna i `REFLECTION.md` besvarar ni själva.
