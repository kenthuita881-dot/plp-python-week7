PLP Python Week 7 - Lists
list_warmup.py - creates a list of fruits and demonstrates index access, .append(), .remove() and len().
shopping_list.py - an interactive shopping list menu (add / remove / show / done) that never crashes.
list_report.py - prints a numbered list, counts names longer than 4 letters, and finds the longest name with a loop.
screenshots/ - screenshots of each program running.
Why check in before .remove()?

Calling .remove() on an item that is not in the list raises a ValueError and crashes the program. Checking with in first lets us handle the missing item gracefully, printing a friendly message instead. This keeps the program running and gives the user clear feedback