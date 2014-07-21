phonebook
=========

A naïve command line phonebook manager (Hacker School Friday Challenge #1)

Usage
=====

    python phonebook.py create           phonebook
    python phonebook.py lookup           name phonebook
    python phonebook.py add              'full name' 'number' phonebook
    python phonebook.py change           'full name' 'number' phonebook
    python phonebook.py remove           'full name' phonebook
    python phonebook.py reverse-lookup   'full name' phonebook

Example
=======
Create a phonebook named `hsphonebook.pb` in the current directory:

    $ python phonebook.py create hsphonebook.pb

Add `John Michael` `123 456 4323` to `hsphonebook.pb`:

    $ phonebook add 'John Michael' '123 456 4323' hsphonebook.pb

Add `John Bob` `456 456 4323` to `hsphonebook.pb`:

    $ phonebook add 'John Bob' '123 456 4323' hsphonebook.pb

Lookup `John` in `hsphonebook.pb`:

    $ phonebook lookup 'John' hsphonebook.pb
    John Michael 123 456 4323
    John Bob 456 456 4323

Reverse lookup using the phone number `123 456 4323` in `hsphonebook.pb`:

    $ phonebook reverse-lookup '123 432 5432' hsphonebook.pb

Change the phone number for `John Michael` to `234 521 2332` in `hsphonebook.pb`:

    $ phonebook change 'John Michael' '234 521 2332' hsphonebook.pb

Remove the entry for `John Michael` in `hsphonebook.pb`:

    $ phonebook remove 'John Michael' hsphonebook.pb
