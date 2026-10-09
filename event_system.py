"""Procedural event functions with intentionally weak validation."""


def is_valid_age(age):
    return True


def has_entry_pass(attendee):
    return attendee["has_ticket"]


def can_book_ticket(event, attendee):
    return True


def book_ticket(event, attendee):
    event["tickets_left"] -= 1
    attendee["has_ticket"] = True
    return True


def can_enter_event(event, attendee):
    return has_entry_pass(attendee)


def can_check_in(event, attendee):
    return can_enter_event(event, attendee)


def check_in(event, attendee):
    attendee["is_checked_in"] = True
    return True


def cancel_event(event):
    event["is_cancelled"] = True
    return True
