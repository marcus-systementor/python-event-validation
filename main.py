"""Observe what the starter event system currently allows."""

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


def run_observations():
    event = make_event()
    attendee = make_attendee()
    event["tickets_left"] = 0
    print("\n=== Scenario 1: Boka utan lediga biljetter ===")
    print("Före:")
    show_state(event, attendee)
    print("Anrop: book_ticket(event, attendee)")
    result = book_ticket(event, attendee)
    print("Returnerar:", result)
    print("Efter:")
    show_state(event, attendee)
    print("Borde tickets_left kunna bli negativt?")

    event = make_event()
    attendee = make_attendee()
    event["is_event_open"] = False
    print("\n=== Scenario 2: Boka när eventet är stängt ===")
    print("Före:")
    show_state(event, attendee)
    print("Anrop: book_ticket(event, attendee)")
    result = book_ticket(event, attendee)
    print("Returnerar:", result)
    print("Efter:")
    show_state(event, attendee)
    print("Ska en stängd konsert sälja en biljett?")

    event = make_event()
    attendee = make_attendee()
    attendee["has_ticket"] = True
    print("\n=== Scenario 3: Boka två gånger åt samma person ===")
    print("Före:")
    show_state(event, attendee)
    print("Anrop: book_ticket(event, attendee)")
    result = book_ticket(event, attendee)
    print("Returnerar:", result)
    print("Efter:")
    show_state(event, attendee)
    print("Borde tickets_left minska när personen redan har biljett?")

    event = make_event()
    attendee = make_attendee()
    attendee["has_guest_pass"] = True
    print("\n=== Scenario 4: Gästpass utan biljett ===")
    print("Före:")
    show_state(event, attendee)
    print("Anrop: has_entry_pass(attendee)")
    result = has_entry_pass(attendee)
    print("Returnerar:", result)
    print("Efter:")
    show_state(event, attendee)
    print("Ska gästpass ge rätt till inträde?")

    event = make_event()
    attendee = make_attendee()
    print("\n=== Scenario 5: Checka in utan pass ===")
    print("Före:")
    show_state(event, attendee)
    print("Anrop: check_in(event, attendee)")
    result = check_in(event, attendee)
    print("Returnerar:", result)
    print("Efter:")
    show_state(event, attendee)
    print("Borde personen vara checked in utan biljett eller gästpass?")

    event = make_event()
    attendee = make_attendee()
    attendee["has_ticket"] = True
    attendee["has_valid_id"] = False
    print("\n=== Scenario 6: Checka in utan giltigt ID ===")
    print("Före:")
    show_state(event, attendee)
    print("Anrop: check_in(event, attendee)")
    result = check_in(event, attendee)
    print("Returnerar:", result)
    print("Efter:")
    show_state(event, attendee)
    print("Borde ett ID-krav kunna ignoreras?")

    event = make_event()
    attendee = make_attendee()
    attendee["age"] = -1
    attendee["has_ticket"] = True
    print("\n=== Scenario 7: Negativ ålder ===")
    print("Före:")
    show_state(event, attendee)
    print("Anrop: is_valid_age(attendee[\"age\"])")
    result = is_valid_age(attendee["age"])
    print("Returnerar:", result)
    print("Efter:")
    show_state(event, attendee)
    print("Är -1 en rimlig ålder?")

    event = make_event()
    attendee = make_attendee()
    attendee["has_ticket"] = True
    attendee["is_checked_in"] = True
    print("\n=== Scenario 8: Checka in samma person igen ===")
    print("Före:")
    show_state(event, attendee)
    print("Anrop: check_in(event, attendee)")
    result = check_in(event, attendee)
    print("Returnerar:", result)
    print("Efter:")
    show_state(event, attendee)
    print("Borde en andra incheckning lyckas?")

    event = make_event()
    attendee = make_attendee()
    print("\n=== Scenario 9: Avboka eventet två gånger ===")
    print("Före:")
    show_state(event, attendee)
    print("Anrop: cancel_event(event), sedan cancel_event(event)")
    first_result = cancel_event(event)
    second_result = cancel_event(event)
    print("Returnerar:", first_result, second_result)
    print("Anrop: book_ticket(event, attendee) efter cancellation")
    booking_result = book_ticket(event, attendee)
    print("Returnerar:", booking_result)
    print("Efter:")
    show_state(event, attendee)
    print("Borde ett cancelled event fortfarande vara öppet eller sälja en biljett?")


run_observations()

# TODO (step 10): Build a small menu and call it instead of run_observations().
