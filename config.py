# t.me/Just_The_Test_Bot
# Run -> Edit Configurations и добавьте в окне Environment Variables переменную с именем BOT_TOKEN ,
# WEATHER_API_KEY и значением токена.

from os import getenv
from sys import exit

bot_token = getenv("BOT_TOKEN")
if not bot_token:
    exit("No Token")

WEATHER_API_KEY = getenv("WEATHER_API_KEY")
if not WEATHER_API_KEY:
    exit("No WEATHER_API_KEY")

CURRENT_WEATHER_API_CALL = (
        'https://api.openweathermap.org/data/2.5/weather?'
        'lat={latitude}&lon={longitude}&'
        'appid=' + WEATHER_API_KEY + '&units=metric'
)

# !!! не взлетает !!!!

# class Settings(BaseSettings):
#     bot_token: SecretStr
#
#     class Config:
#         env_file = '.env'
#         env_file_encoding = 'utf-8'
#         case_sensitive = True
# type = value_error.missing


# config = Settings()
