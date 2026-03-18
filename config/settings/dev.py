from .base import *

# -----------------------------
# DEVELOPMENT SETTINGS
# -----------------------------
DEBUG = True
ALLOWED_HOSTS = ['*']  

DATABASES['default']['NAME'] = BASE_DIR / 'db.sqlite3'