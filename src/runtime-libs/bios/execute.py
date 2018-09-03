
def execute_system(system, scope):
    puts(BEEP, '\n')
    if HEADER:
        puts(HEADER.get('welcome', 'New System'))
    else:
        puts("System HEADER does not exist.")
    puts('\n')

    setattr(scope, 'system', system)
