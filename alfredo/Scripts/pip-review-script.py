#!"c:\users\alfre\onedrive\documentos\projetos em py\projeto 1\alfredo\scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'pip-review==1.3.0','console_scripts','pip-review'
__requires__ = 'pip-review==1.3.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pip-review==1.3.0', 'console_scripts', 'pip-review')()
    )
