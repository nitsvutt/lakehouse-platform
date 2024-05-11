from datetime import datetime
import pytz

from core.config import TIMEZONE, DATE_FORMAT, DATETIME_FORMAT

def current_sysdate():
    return datetime.now(pytz.timezone(TIMEZONE)).strftime(DATE_FORMAT)

def current_systime():
    return datetime.now(pytz.timezone(TIMEZONE)).strftime(DATETIME_FORMAT)