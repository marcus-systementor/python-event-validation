"""Teacher solution: procedural event functions with complete validation."""


def is_valid_age(age):
    # An age of 0 is allowed; only negative ages are invalid.
    return age >= 0


def has_entry_pass(attendee):
    # A ticket OR a guest pass gives the right to enter.
    return attendee["has_ticket"] or attendee["has_guest_pass"]


def can_book_ticket(event, attendee):
    # Validation only reads values. It never changes the dictionaries.
    is_open = event["is_event_open"]
    is_not_cancelled = not event["is_cancelled"]
    has_tickets_left = event["tickets_left"] > 0
    does_not_have_ticket = not attendee["has_ticket"]
    return is_open and is_not_cancelled and has_tickets_left and does_not_have_ticket


def book_ticket(event, attendee):
    # Validate first, so a rejected booking changes nothing.
    if not can_book_ticket(event, attendee):
        return False

    event["tickets_left"] -= 1
    attendee["has_ticket"] = True
    return True


def can_enter_event(event, attendee):
    # Event rules (step 6A).
    is_open = event["is_event_open"]
    is_not_cancelled = not event["is_cancelled"]
    if not (is_open and is_not_cancelled):
        return False

    # Attendee rules (step 6B).
    has_pass = has_entry_pass(attendee)
    has_valid_id = attendee["has_valid_id"]
    has_valid_age = is_valid_age(attendee["age"])
    # Age exactly at minimum_age is allowed.
    is_old_enough = has_valid_age and attendee["age"] >= event["minimum_age"]
    return has_pass and has_valid_id and is_old_enough


def can_check_in(event, attendee):
    # Reuse the entry rules, then add the "only once" rule.
    if not can_enter_event(event, attendee):
        return False
    return not attendee["is_checked_in"]


def check_in(event, attendee):
    # Validate first; only is_checked_in may change.
    if not can_check_in(event, attendee):
        return False

    attendee["is_checked_in"] = True
    return True


def cancel_event(event):
    # A second cancellation is rejected without changes.
    if event["is_cancelled"]:
        return False

    event["is_cancelled"] = True
    event["is_event_open"] = False
    return True
