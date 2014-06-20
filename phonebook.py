import os
import sys

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
        print 'Sucessfully created %s.' % phonebook

def lookup(args):
    name = args[1]
    phonebook = args[2]

    try:
        with open(phonebook) as f:
            for line in f:
                if line.index(name) >= 0:
                    print line,
    except IOError:
        print 'Error: no such phonebook.'
        return 1
    except ValueError:
        print 'Error: %s not found.' % name
        return 1

def add(args):
    name = args[1]
    number = args[2]
    phonebook = args[3]

    with open(phonebook, 'a') as f:
        f.write('%(name)s %(number)s\n' % {'name': name, 'number': number})

def change(args):
    name = args[1]
    number = args[2]
    phonebook = args[3]

    try:
        changed = False
        os.rename(phonebook, 'temp.pb')

        with open('temp.pb') as f_in, open(phonebook, 'w') as f_out:
            for line in f_in:
                if line.index(name) >= 0:
                    f_out.write(('%s %s\n' % (name, number)))
                    changed = True
                else:
                    f_out.write(line)
        os.remove('temp.pb')
    
        if changed:
            print 'Successfully changed the entry for %s.' % name
        else:
            print 'Error: %s not found.' % name
            return 1
    except OSError:
        print 'Error: no such phonebook.'
        return 1

def remove(args):
    name = args[1]
    phonebook = args[2]
    
    try:
        removed = False
        os.rename(phonebook, 'temp.pb')

        with open('temp.pb') as f_in, open(phonebook, 'w') as f_out:
            for line in f_in:
                if line.index(name) >= 0:
                    removed = True
                else:
                    f_out.write(line)

        os.remove('temp.pb')

        if removed:
            print 'Successfully removed the entry for %s.' % name
        else:
            print 'Error: %s not found.' % name
    except OSError:
        print 'Error: no such phonebook.'
        return 1

def reverse_lookup(args):
    number = args[1]
    phonebook = args[2]

    try:
        with open(phonebook) as f:
            for line in f:
                if line.index(number):
                    print line,
    except IOError:
        print 'Error: no such phonebook.'
        return 1
    except ValueError:
        print 'Error: %s not found.' % number
        return 1

def validate_args(args):
    command = args[0]
    args_length = len(args) - 1

    return VALID_COMMANDS[command] == args_length

def validate_command(command):
    return command in VALID_COMMANDS.keys()

def main(args=sys.argv[1:]):
    # Command line processing
    if len(args) == 0:
        print 'Error: no arguments passed.'
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
        'change': change,
        'remove': remove,
        'reverse-lookup': reverse_lookup
    }

    # Call appropriate function
    commands[command](args)

    return 0

if __name__ == '__main__':
    status = main()
    sys.exit(status)
