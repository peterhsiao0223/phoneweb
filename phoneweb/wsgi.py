"""
WSGI config for phoneweb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

# import os
# import sys
# from os.path import dirname, abspath
# from django.core.wsgi import get_wsgi_application

# PROJECT_DIR = dirname(dirname(abspath(__file__)))                                                                                                             
# sys.path.insert(0, PROJECT_DIR) 
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "phoneweb.settings")

# application = get_wsgi_application()

import os
import sys
from os.path import dirname, abspath



PROJECT_DIR = dirname(dirname(abspath(__file__)))
# sys.path.append('/var/www/html/lost_taiwan/')
sys.path.insert(0, PROJECT_DIR)
sys.path.append('/var/www/html/phoneweb')  

# sys.path.append('/usr/local/lib/python3.5/dist-packages')  
# sys.path.append('/usr/local/lib/python3.5/dist-packages') 
from django.core.wsgi import get_wsgi_application
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lost_taiwan.settings")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "phoneweb.settings")

application = get_wsgi_application()