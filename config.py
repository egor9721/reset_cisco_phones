LOGIN = 'login' # login for ssh connect
PASSWORD = 'password' # password for ssh connect

'''
description of the parameters of telephone models (MODELS):
model - telephone model
login - login on telephone
pwd - password on telephone
reset_all - command for reset telephone
reset_cert - command for reset certificates on telephone
reboot - command for reboot telephone
port - phnoe port
'''

MODELS = [
    {
        'model': 'Cisco 7821',
        'login': 'debug',
        'pwd': 'debug',
        'reset_all': 'reset factory',
        'reset_cert': None,
        'reboot': None,
        'port': 22
    },
    {
        'model': 'Cisco 6941',
        'login': 'admin',
        'pwd': '',
        'reset_all': 'reset',
        'reset_cert': 'sec erase',
        'reboot': 'reboot',
        'port': 22
    },
    {
        'model': 'Cisco 7962',
        'login': 'debug',
        'pwd': 'debug',
        'reset_all': None,
        'reset_cert': None,
        'reboot': None,
        'port': 22
    },
    {
        'model': 'Cisco 7960',
        'login': None,
        'pwd': None,
        'reset_all': None,
        'reset_cert': None,
        'reboot': None,
        'port': 22
    },
    {
        'model': 'Cisco 7811',
        'login': 'debug',
        'pwd': 'debug',
        'reset_all': 'erase all settings',
        'reset_cert': None,
        'reboot': None,
        'port': 22
    },
    {
        'model': 'Cisco 6901',
        'login': '',  
        'pwd': '',  
        'reset_all': 'utils system factory_reset',
        'reset_cert': 'utils security ctl erase',
        'reboot': None,
        'port': 22
    },
    {
        'model': 'Cisco 3905',
        'login': None,
        'pwd': None,
        'reset_all': None,
        'reset_cert': None,
        'reboot': None,
        'port': 23  # telnet
    },
    {
        'model': 'Cisco 7911',
        'login': 'debug',
        'pwd': 'debug',
        'reset_all': None,
        'reset_cert': None,
        'reboot': None,
        'port': 22
    }
]
