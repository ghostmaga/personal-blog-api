import environ, os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '/.env'))
print(env('DB_HOST'))    