<<<<<<< HEAD
import sys
sys.path.insert(0, '/var/www/project')

"""
=======
>>>>>>> 5e83fba3cd3a02b149107d52c0dd8aca0927122b
activate_this = '/var/www/flask/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))
"""

from run import app as application
