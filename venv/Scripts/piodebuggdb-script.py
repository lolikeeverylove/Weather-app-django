#!C:\Users\lolike\PycharmProjects\untitled2\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'platformio==4.0.3','console_scripts','piodebuggdb'
__requires__ = 'platformio==4.0.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('platformio==4.0.3', 'console_scripts', 'piodebuggdb')()
    )
