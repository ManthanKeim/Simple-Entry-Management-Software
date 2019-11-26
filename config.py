import os

_mail_enabled = os.environ.get("MAIL_ENABLED", default="true")
MAIL_ENABLED = _mail_enabled.lower() in {"1", "t", "true"}

SECRET_KEY = b'\xfc\xed6x\x12u\xe3\xf2\x7f07Z\\\xd6\x83\xe3'
MYSQL_HOST = 'localhost'

if not SECRET_KEY:
    raise ValueError("No SECRET_KEY set for Flask application")
