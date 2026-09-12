
# 4b pydantic-settings
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    db_host: str
    db_user: str
    db_password: str
    db_port: int
    debug: bool = False  # 设置默认值为False，如果在.env文件中没有设置DEBUG，则使用默认值

settings = Settings()