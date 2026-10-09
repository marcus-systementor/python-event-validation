"""Teacher solution: demonstrate the completed event system.

Run from the repository root: python facit/main.py
"""

from event_system import (
    book_ticket,
    can_book_ticket,
    can_check_in,
    can_enter_event,
    cancel_event,
    check_in,
    has_entry_pass,
    is_valid_age,
)


def make_event():
    return {
        "name": "Python Live",
        "is_event_open": True,
        "is_cancelled": False,
        "minimum_age": 18,
        "tickets_left": 5,
    }


def make_attendee():
    return {
        "name": "Alex",
        "age": 20,
        "has_ticket": False,
        "has_guest_pass": False,
        "has_valid_id": True,
        "is_checked_in": False,
    }


def show_state(event, attendee):
    print(
        "Event:",
        "open=", event["is_event_open"],
        "cancelled=", event["is_cancelled"],
        "minimum_age=", event["minimum_age"],
        "tickets_left=", event["tickets_left"],
    )
    print(
        "Attendee:",
        "age=", attendee["age"],
        "ticket=", attendee["has_ticket"],
        "guest_pass=", attendee["has_guest_pass"],
        "valid_id=", attendee["has_valid_id"],
        "checked_in=", attendee["is_checked_in"],
    )


def show_result(call_text, result):
    print("Anrop:", call_text)
    print("Returnerar:", result)


def run_observations():
    # Scenario 1: no tickets left -> booking rejected, nothing changes.
    event = make_event()
    attendee = make_attendee()
    event["tickets_left"] = 0
    print("\n=== Scenario 1: Boka utan lediga biljetter ===")
    show_state(event, attendee)
    show_result("book_ticket(event, attendee)", book_ticket(event, attendee))
    show_state(event, attendee)

    # Scenario 2: successful booking.
    event = make_event()
    attendee = make_attendee()
    print("\n=== Scenario 2: Lyckad bokning ===")
    show_state(event, attendee)
    show_result("book_ticket(event, attendee)", book_ticket(event, attendee))
    show_state(event, attendee)

    # Scenario 3: repeated booking with the same dictionaries.
    print("\n=== Scenario 3: Boka igen åt samma person ===")
    show_result("book_ticket(event, attendee)", book_ticket(event, attendee))
    show_state(event, attendee)

    # Scenario 4: closed event.
    event = make_event()
    attendee = make_attendee()
    event["is_event_open"] = False
    print("\n=== Scenario 4: Boka när eventet är stängt ===")
    show_state(event, attendee)
    show_result("book_ticket(event, attendee)", book_ticket(event, attendee))
    show_state(event, attendee)

    # Scenario 5: ticket and guest pass both give entry.
    event = make_event()
    attendee = make_attendee()
    attendee["has_ticket"] = True
    print("\n=== Scenario 5a: Inträde med biljett ===")
    show_result("can_enter_event(event, attendee)", can_enter_event(event, attendee))
    event = make_event()
    attendee = make_attendee()
    attendee["has_guest_pass"] = True
    print("\n=== Scenario 5b: Inträde med gästpass (ingen biljett) ===")
    show_result("can_enter_event(event, attendee)", can_enter_event(event, attendee))
    show_state(event, attendee)

    # Scenario 6: no entry pass.
    event = make_event()
    attendee = make_attendee()
    print("\n=== Scenario 6: Checka in utan pass ===")
    show_state(event, attendee)
    show_result("check_in(event, attendee)", check_in(event, attendee))
    show_state(event, attendee)

    # Scenario 7: no valid ID.
    event = make_event()
    attendee = make_attendee()
    attendee["has_ticket"] = True
    attendee["has_valid_id"] = False
    print("\n=== Scenario 7: Checka in utan giltigt ID ===")
    show_state(event, attendee)
    show_result("check_in(event, attendee)", check_in(event, attendee))
    show_state(event, attendee)

    # Scenario 8: age rules (below minimum, negative, exactly minimum).
    print("\n=== Scenario 8: Åldersregler ===")
    for age in (17, -1, 18):
        event = make_event()
        attendee = make_attendee()
        attendee["has_ticket"] = True
        attendee["age"] = age
        print("age =", age)
        show_result("can_enter_event(event, attendee)", can_enter_event(event, attendee))
    print("is_valid_age(-1):", is_valid_age(-1), "| is_valid_age(0):", is_valid_age(0))

    # Scenario 9: successful check-in, then repeated check-in on the same dictionaries.
    event = make_event()
    attendee = make_attendee()
    attendee["has_ticket"] = True
    print("\n=== Scenario 9: Checka in två gånger ===")
    show_state(event, attendee)
    show_result("check_in(event, attendee)", check_in(event, attendee))
    show_state(event, attendee)
    show_result("check_in(event, attendee) igen", check_in(event, attendee))
    show_state(event, attendee)

    # Scenario 10: repeated cancellation, then operations after cancellation.
    event = make_event()
    attendee = make_attendee()
    print("\n=== Scenario 10: Avboka två gånger och försök sedan boka ===")
    show_state(event, attendee)
    show_result("cancel_event(event)", cancel_event(event))
    show_result("cancel_event(event) igen", cancel_event(event))
    show_result("book_ticket(event, attendee)", book_ticket(event, attendee))
    show_state(event, attendee)

    # Scenario 11: a person with ticket and ID cannot check in to a cancelled event.
    attendee = make_attendee()
    attendee["has_ticket"] = True
    print("\n=== Scenario 11: Checka in på inställt event ===")
    show_result("check_in(event, attendee)", check_in(event, attendee))
    show_state(event, attendee)


def run_menu():
    # Optional: one event and one attendee are shared by all menu choices.
    event = make_event()
    attendee = make_attendee()

    while True:
        print("\n1. Show status")
        print("2. Book ticket")
        print("3. Check in")
        print("4. Cancel event")
        print("0. Exit")
        choice = input("Choose: ")

        if choice == "0":
            print("Bye!")
            break
        elif choice == "1":
            show_state(event, attendee)
        elif choice == "2":
            if book_ticket(event, attendee):
                print("Ticket booked.")
            else:
                print("Booking denied.")
        elif choice == "3":
            if check_in(event, attendee):
                print("Checked in.")
            else:
                print("Check-in denied.")
        elif choice == "4":
            if cancel_event(event):
                print("Event cancelled.")
            else:
                print("Cancellation denied.")
        else:
            print("Unknown choice. Try 0-4.")


# Default: show the observations.
# To try the optional menu, comment out run_observations() and remove
# the # in front of run_menu().
run_observations()
# run_menu()
