**SRN:** PES2UG24CS011

# Issues Found in theater_system.py

Line numbers refer to the original file. Ordered high severity first.

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| Weak MD5 hash (Bandit B324, High) | Security | 25 | `hashlib.md5` is used without declaring that it is not for security. MD5 is a broken hash. | Pass `usedforsecurity=False` because the value is only a short ticket label and not a security token. The ticket code stays the same. |
| Overly permissive file permissions (Bandit B103, High) | Security | 55 | `os.chmod("seats.json", 0o777)` lets every user on the machine read, write and execute the seating file. | Changed the mode to `0o600` so only the owner can read and write it. |
| Mutable default argument (Pylint W0102) | Bug | 9 | `system_logs=[]` is created once and shared across every call, so log messages from unrelated calls pile up. | Changed the default to `None` and create a new list inside the function. |
| Bare except with pass (Bandit B110, Pylint W0702, Flake8 E722) | Bug | 21-22 | `except: pass` hides every error, including typos and Ctrl+C, and `release_seat` never tells the caller whether anything was released. | Catch only `KeyError` and `ValueError`, and return `False` on failure and `True` on success. |
| No seat validation (found by running the program, not flagged by any tool) | Bug | 9-16 | Seats `-1`, `"A7"` and `25` (SHOW-1 has only 20 seats) are accepted and appear in the booked list. This also lowers the free-seat count wrongly. | Reject unknown shows, non-integer seats, and seats outside `1..seats`. Log the reason and return `False`. |
| Seat typed in as a string (found by running the program) | Bug | 50-51 | `input()` returns text, so the default seat is stored as `'4'` while other seats are ints. `'4'` and `4` would not be seen as the same seat, so double booking is possible. | Convert the input with `int()` and print a message if it is not a number. |
| Files opened without `with` or encoding (Pylint R1732, W1514) | Bug | 28, 33 | Files are never closed explicitly and the encoding depends on the system. | Use `with open(..., encoding="utf-8")`. |
| Global statement (Pylint W0603) | Quality | 32 | `global shows` rebinds module state inside a function. | Update the existing dictionary with `shows.clear()` and `shows.update(...)`. |
| Function naming (Pylint C0103) | Style | 37 | `printSeatingSummary` is not snake_case. | Renamed to `print_seating_summary` and updated the call. |
| Missing docstrings (Pylint C0114, C0116) | Style | 1, 9, 18, 24, 27, 31, 37, 42 | The module and every function have no docstring. | Added a short docstring to the module and each function. |
| Old-style string formatting (Pylint C0209) | Style | 12, 15, 40 | `%` formatting and `+` concatenation are used to build strings. | Replaced them with f-strings. |
| Line too long (Pylint C0301, Flake8 E501) | Style | 12, 40 | Lines are longer than 79 characters. | Wrapped the long lines. |
| Blank lines between definitions (Flake8 E302, E305) | Style | 9, 18, 24, 27, 31, 37, 42, 57 | Only one blank line is used around top-level functions and the final `main()` call. | Used two blank lines. |

## Results after the fixes

| Tool | Before | After |
|------|--------|-------|
| Pylint | 5.87/10 | 10.00/10 |
| Bandit | 2 High, 1 Low | No issues identified |
| Flake8 | 11 warnings | 0 warnings |
