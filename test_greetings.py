import greetings  # Εισαγωγή του κώδικα από το αρχείο greetings.py

def test_greeting_variable():
    # Έλεγχος αν η μεταβλητή greeting υπάρχει και περιέχει την τιμή 'Hello, World!'
    assert hasattr(main, 'greeting'), "Η μεταβλητή 'greeting' δεν υπάρχει στο greetings.py"
    assert main.greeting == 'Καλημέρα Python', "Η μεταβλητή 'greeting' δεν έχει την τιμή 'Καλημέρα Python'"

def test_print_output(capsys):
    # Εκτελεί το πρόγραμμα και ελέγχει την έξοδο του print
    main_output = greetings  # Εισαγωγή του αρχείου για να τρέξει το πρόγραμμα
    captured = capsys.readouterr()  # Capture output
    assert captured.out == 'Καλημέρα Python\n', "Το πρόγραμμα δεν εκτύπωσε 'Καλημέρα Python'"
