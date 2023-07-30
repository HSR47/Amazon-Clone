
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_HOST : str
    DB_DB : str
    DB_USER : str
    DB_PASS : str
    SECRET_KEY : str
    ALGORITHM : str
    ACCESS_TOKEN_EXPIRE_MINUTES : int
    REFRESH_TOKEN_EXPIRE_MINUTES : int
    MAIL_USERNAME : str
    MAIL_PASSWORD : str
    MAIL_FROM_NAME : str
    PASS_RESET_TOKEN_EXP_MINUTES : int
    
    class Config:
        env_file = ".env"

settings = Settings()