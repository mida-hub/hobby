#!/virtual/watomatoma/.pyenv/versions/3.7.0/bin/python

from wsgiref.handlers import CGIHandler
from main import app
CGIHandler().run(app)