from datetime import datetime

from core.config import DATETIME_FORMAT

def current_systime():
    return datetime.now().strftime(DATETIME_FORMAT)
