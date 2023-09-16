import os
from dotenv import load_dotenv

env = 'development'
env_file_mapping = {
    'development': '.env.development',
    'test': '.env.test',
    'homolog': '.env.stage',
    'production': '.env.production',
}
env_file = f'.env.{env}' 

if os.path.exists(env_file):
    message = 'Crie um arquivo .env.development seguindo os passos do arquivo README.md' if env == 'development' else f"Não existe um arquivo {env_file}"
    raise FileNotFoundError(message)

load_dotenv(env_file)

class Config():
    DATABASE_URL=os.getenv('DATABASE_URL')
    SECRET_KEY=os.getenv('SECRET_KEY')


class Development(Config):
    DEBUG = True


class Test(Config):
    DEBUG = True


class Homolog(Config):
    DEBUG = False


class Production(Config):
    DEBUG = False


def get_config():
    if env == 'development':
        return Development()
    elif env == 'test':
        return Test()
    elif env == 'homolog':
        return Homolog()
    elif env == 'production':
        return Production()