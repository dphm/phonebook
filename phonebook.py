#!/usr/bin/env python

import os
import sys

USAGE = """
Usage:

    python phonebook.py create           [phonebook]
    python phonebook.py lookup           [name] [phonebook]
    python phonebook.py add             '[name]' '[number]' [phonebook]
    python phonebook.py changed         '[name]' '[number]' [phonebook]
    python phonebook.py remove          '[name]' '[number]' [phonebook]
    python phonebook.py reverse-lookup  '[number]' [phonebook]
"""

# Store valid commands and the number of arguments they take
VALID_COMMANDS = {'create': 1,
                  'lookup': 2,
                  'add': 3,
                  'change': 3,
                  'remove': 2,
                  'reverse-lookup': 2}

def create(args):
    phonebook = args[1]

    # Create empty phonebook
    with open(phonebook, 'w') as f:
        return ['Sucessfully created %s.\n' % phonebook]

def lookup(args):
    name = args[1]
    phonebook = args[2]

    try:
        with open(phonebook) as f:
            return [line for line in f if line.index(name) >= 0]
    except IOError:
        return ['Error: no such phonebook.']
    except ValueError:
        return ['Error: %s not found.' % name]

def add(args):
    name = args[1]
    number = args[2]
    phonebook = args[3]

    with open(phonebook, 'a') as f:
        f.write('%s %s\n' % (name, number))
        return ["Successfully added %s." % name]

def change_or_remove(args):
    command = args[0].lower()
    name = args[1]
    phonebook = args[-1]

    try:
        changed = False
        os.rename(phonebook, 'temp.pb')

        with open('temp.pb') as f_in, open(phonebook, 'w') as f_out:
            for line in f_in:
                if line.index(name) >= 0:
                    if command == 'change':
                        number = args[2]
                        f_out.write(('%s %s\n' % (name, number)))
                    changed = True
                else:
                    f_out.write(line)

        os.remove('temp.pb')

        if changed:
            if command == 'change':
                return ['Successfully changed %s.\n' % name]
            else:
                return ['Successfully removed %s.\n' % name]
        else:
            return ['Error: %s not found.' % name]
    except OSError:
        return ['Error: no such phonebook.']
    except ValueError:
        return ['Error: %s not found.' % name]

def validate_args(args):
    command = args[0]
    args_length = len(args) - 1

    return VALID_COMMANDS[command] == args_length

def validate_command(command):
    return command in VALID_COMMANDS.keys()

def main(args=sys.argv[1:]):
    # Command line processing
    if len(args) == 0:
        print USAGE
        return 1

    command = args[0].lower()

    # Command validation
    valid = validate_command(command)
    
    if not valid:
        print ('Error: %s is not a valid command.' % command)
        return 1

    # Argument validation
    valid = validate_args(args)

    if not valid:
        print ('Error: expected %d argument(s) for the %s command'
               % (VALID_COMMANDS[command], command))
        return 1

    commands = {
        'create': create,
        'lookup': lookup,
        'add': add,
        'change': change_or_remove,
        'remove': change_or_remove,
        'reverse-lookup': lookup
    }

    # Call appropriate function and print results
    for line in commands[command](args):
        print line,

    return 0

if __name__ == '__main__':
    status = main()
    sys.exit(status)
