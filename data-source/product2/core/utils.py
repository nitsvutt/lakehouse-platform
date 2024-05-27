from datetime import datetime
import pytz
from passlib.context import CryptContext

from core.config import TIMEZONE, DATE_FORMAT, DATETIME_FORMAT

def current_sysdate():
    return datetime.now(pytz.timezone(TIMEZONE)).strftime(DATE_FORMAT)

def current_systime():
    return datetime.now(pytz.timezone(TIMEZONE)).strftime(DATETIME_FORMAT)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class hasher():
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    def get_password(password):
        return pwd_context.hash(password)