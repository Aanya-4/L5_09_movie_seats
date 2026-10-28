**SRN:** PES2UG24CS011

# Reflection

**1. Which issues were the easiest and the hardest to fix?**

The style issues were the easiest. Flake8's blank-line and line-length warnings and Pylint's docstring and f-string messages each have an obvious mechanical fix. The hardest were the ones that needed a decision about behaviour. For the bare `except: pass`, I had to decide which errors to catch and what `release_seat` should return. For the missing seat checks, I had to decide what counts as a valid seat. Pylint only reported the mutable default, so I also had to think about how the log list should work after the fix.

**2. Did the tools report anything that was a false positive or not worth fixing? Did they miss anything?**

None of the reports was clearly wrong, but some were low value for this script. Bandit's MD5 warning is a fair warning in general, but here the hash is only a ticket label, so `usedforsecurity=False` was the correct fix and not a stronger hash. The tools missed real bugs that I only saw by running the program. Seats `-1`, `"A7"` and `25` were accepted, and the default seat was stored as the string `'4'` while other seats were ints. No tool can know the business rule that a seat must be an integer inside the show's capacity.

**3. How would you use static analysis in a real project workflow?**

I would run Flake8, Pylint and Bandit automatically on every pull request and in a pre-commit hook, so style and security problems are caught before review. Bandit findings of high severity would block a merge, and the others would be fixed or explicitly suppressed with a reason. That leaves human reviewers free to look at design and logic.

**4. How did static analysis improve code quality and maintainability?**

The Pylint score went from 5.87 to 10.00, Bandit went from three findings to none, and Flake8 went from eleven warnings to none. The code is safer because the file permissions are no longer open to everyone and errors are no longer silently swallowed. It is easier to read because every function has a docstring, names follow one style, and files are closed properly. The tools are not enough on their own, though. Running the program and testing real inputs was needed to find the logic bugs.
