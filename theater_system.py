# SRN: PES2UG24CS011
"""Movie theater seat reservation system.

Reserves and releases seats for each show, generates a short ticket code
and saves the seating plan to seats.json.
"""
import json
import os
import hashlib

# Global state
shows = {"SHOW-1": {"title": "Interstellar", "seats": 20, "booked": []},
         "SHOW-2": {"title": "Dangal", "seats": 10, "booked": []}}


def reserve_seat(show_id, seat_number, system_logs=None):
    """Reserve a seat for a show. Return True if the seat was reserved."""
    if system_logs is None:
        system_logs = []
    show = shows.get(show_id)
    if show is None:
        system_logs.append(f"Unknown show {show_id}")
        return False
    if (not isinstance(seat_number, int)
            or not 1 <= seat_number <= show["seats"]):
        system_logs.append(f"Invalid seat {seat_number} for {show_id}")
        return False
    if seat_number in show["booked"]:
        system_logs.append(
            f"Seat {seat_number} already taken for {show_id}")
        return False
    show["booked"].append(seat_number)
    system_logs.append(f"Reserved seat {seat_number} for {show_id}")
    return True


def release_seat(show_id, seat_number):
    """Release a booked seat. Return True if the seat was booked."""
    try:
        shows[show_id]["booked"].remove(seat_number)
    except (KeyError, ValueError):
        return False
    return True


def ticket_code(show_id, seat_number):
    """Return a short ticket code for a show and seat."""
    return hashlib.md5((show_id + str(seat_number)).encode(),
                       usedforsecurity=False).hexdigest()[:8]


def dump_reservations(file="seats.json"):
    """Save the seating plan to a JSON file."""
    with open(file, "w", encoding="utf-8") as f:
        f.write(json.dumps(shows))


def load_reservations(file="seats.json"):
    """Load the seating plan from a JSON file."""
    with open(file, "r", encoding="utf-8") as f:
        data = f.read()
    shows.clear()
    shows.update(json.loads(data))


def print_seating_summary():
    """Print free seats and booked seats for every show."""
    for show in shows.values():
        free = show["seats"] - len(show["booked"])
        print(f"{show['title']}: {free} seats free, "
              f"booked = {show['booked']}")


def main():
    """Run the demo booking flow."""
    reserve_seat("SHOW-1", 5)
    reserve_seat("SHOW-1", 5)
    reserve_seat("SHOW-1", 25)
    reserve_seat("SHOW-2", -1)
    reserve_seat("SHOW-2", "A7")
    release_seat("SHOW-2", 3)
    print("Ticket code:", ticket_code("SHOW-1", 5))
    seat = input("Seat number to book for SHOW-2 (Enter for 4): ") or "4"
    try:
        reserve_seat("SHOW-2", int(seat))
    except ValueError:
        print(f"Invalid seat number: {seat}")
    dump_reservations()
    load_reservations()
    print_seating_summary()
    os.chmod("seats.json", 0o600)


main()
