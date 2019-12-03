from string import Template


def convert_templated(src_path, dest_path=None, kwargs=None):
    """Convert a given tpy file to a standard py file. If the dest path
    is None, the src_path is used resulting in a tpy/py in the same directory
    """

    print('\nConverting tpy file')
    content = ''
    with open(src_path, 'r') as stream:
        for line in stream:
            content += line

    data = kwargs or SETTINGS
    if dest_path is None:
        dirn, filen = os.path.split(src_path)
        dest_path = os.path.join(dirn, filen)
        print('writing to "{}"'.format(dest_path))

    with open(dest_path, 'w') as stream:
        stream.write(Template(content).safe_substitute(data))


def template_str(content, data):
    return Template(content).safe_substitute(data)
