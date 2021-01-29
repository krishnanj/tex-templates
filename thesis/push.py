##
## push.py
## lazy push to repo

import subprocess as sp

sp.call("git add *; git commit -m 'revise thesis'; git push", shell=True)