import os
from dotenv import load_dotenv

load_dotenv()

def get_db_config() -> dict:
    return {
        "db_host": os.getenv("DB_HOST"),
        "db_user": os.getenv("DB_USER"),
        "db_password": os.getenv("DB_PASSWORD"),
        "db_port": os.getenv("DB_PORT"),
        "debug": os.getenv("DEBUG"),
    }

if __name__ == "__main__":
    cfg = get_db_config()
    print(cfg)
    print(type(cfg["db_port"]), repr(cfg["db_port"]))  # 输出类型，注意从环境变量中获取的值都是字符串