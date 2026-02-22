import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com")
    STANDARD_USER = os.getenv("STANDARD_USER", "standard_user")
    LOCKED_USER = os.getenv("LOCKED_USER", "locked_out_user")
    PASSWORD = os.getenv("PASSWORD", "secret_sauce")
    IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", "10000"))
    HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
    BROWSER = os.getenv("BROWSER", "chromium")
    SLOW_MO = int(os.getenv("SLOW_MO", "0"))
