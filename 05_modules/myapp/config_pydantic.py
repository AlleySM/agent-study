from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")  # 指定.env文件路径，并忽略未在Settings中定义的环境变量
    db_host: str
    db_user: str
    db_password: str
    db_port: int
    debug: bool = False  # 设置默认值为False，如果在.env文件中没有设置DEBUG，则使用默认值


if __name__ == "__main__":
    s = Settings()
    print(s)
    print(type(s.db_port), s.db_port)  # 输出类型，注意从环境变量中获取的值都是字符串)
    print(type(s.debug), s.debug)  # 输出类型，注意从环境变量中获取的值都是字符串