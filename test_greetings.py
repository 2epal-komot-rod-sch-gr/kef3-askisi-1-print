# -*- encoding: utf-8 -*-
from cStringIO import StringIO
import sys
import greetings  # Εισαγωγή του αρχείου `greetings.py`

def test_greeting_variable():
    # Έλεγχος αν η μεταβλητή greeting υπάρχει και περιέχει την τιμή 'Hello, World!'
    assert hasattr(greetings, 'greeting'), "Variable 'greeting' doesnt exist in greetings.py"
    assert greetings.greeting == 'Hello Python', "Variable 'greeting' isnt 'Hello Python'"

def test_print_output():
    # Ανακατεύθυνση της εξόδου σε προσωρινή μνήμη
    old_stdout = sys.stdout
    sys.stdout = captured_output = StringIO()

    try:
        # Επαναφορτώνουμε το greetings για να εκτελεστεί ξανά
        reload(greetings)
    finally:
        # Επαναφορά της κανονικής εξόδου stdout
        sys.stdout = old_stdout

    # Καταγράφουμε την εκτυπωμένη έξοδο
    output = captured_output.getvalue().strip()

    # Έλεγχος της εξόδου για την επιθυμητή τιμή
    assert output == "Hello Python", "It didn't print 'Hello Python', got: '{}'".format(output)
