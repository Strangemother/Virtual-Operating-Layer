import os

def CONFIGURE():
    print('CONFIGURE')
    if os.path.exists('CONF'):
        puts('discovered configure CONF')

CONFIGURE()
