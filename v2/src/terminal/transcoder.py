"""
decoder, encoder utilites for text streams through the CLI/CMD.
Given is a string to convert to a readable format for the interface to digest.
"""
def from_cli(key_object, process, session):

    result = key_object.decode(session['decode'])

    res = ()
    for char in result:
        res += ((char, process_stream(session, char), ), )

    return res


def to_cli(value, name):
    """Encode the value from the UI to a terminal cli value.
    The return value should be a string like entity.
    """
    if isinstance(value, dict):
        result = value['key']
        if result == 'Enter':
            return '\r\n'
        return result

    return value

SEQ = (

    )


def process_stream(session, char):
    """
        Receive a value from the input stream. Perform data detection
        and any pseudo responsibilities.
        Return a result for the view. through send_to_view
    """
    print('F',char, char.encode('utf').hex())

    return char
