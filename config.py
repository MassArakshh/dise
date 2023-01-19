# t.me/Just_The_Test_Bot

# Run -> Edit Configurations и добавьте в окне Environment Variables переменную с именем BOT_TOKEN и значением токена.
# from pydantic import BaseSettings, SecretStr

# import logging
# from aiogram import Bot, Dispatcher, executor, types
from os import getenv
from sys import exit

bot_token = getenv("BOT_TOKEN")
if not bot_token:
    exit("No Token")

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

# Token = '5902008345:AAGIlskH44DFh3ghOEwt72E2dyt_3-gM9lM'
