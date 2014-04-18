#!/usr/bin/python
import os
os.environ['DJANGO_SETTINGS_MODULE'] = "pleft.settings"

import sys
#
path = '/home/ubuntu/pleft_env/pleft'

if path not in sys.path:
   sys.path.append(path)
sys.path.append(sys.path[0] + '/..')
from django.core.mail import * 
#from settings import *

send_mail(subject='subject',
		  message='message',
		  from_email='jc@blim.net',
		  recipient_list=['joconsol@gmail.com'],
		 # EMAIL_HOST = 'SMTP-RELAY.GMAIL.COM',
		  fail_silently=False)


