import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "BAFN6r0As-zf7RjX9rV9mx-FpqRb6m1mIzW8GBFZ-0lH-rfOsyjUOLjF6AcExzhOdeaDf1CGh8ljBH2j169S3ujwrKYFSztRBg4dS2kfjJWU25M2sPC9Jk_P5l-ybuoKDYGjdt7tEVpqlrhMlCmIZ4-YNVqESuM8DeKaLXh4_PmRz0SrBWdsBkCfYnG4IogFu49e4Ej-bEZ8rQBPpvDicnIpd8JjUl6t98BDPO0mqlBUsWY54wuI534tJKln8iJvDa-HsDuHuUmOgN37EtWgI4YP5HQX1MYWQZCa1c_URR-rOKgHJJBLIsYZEL2NCoQnVTzNkH-vShLXeys3X2Aoc2ZbEpvjmAAAAAHnAcMFAA")
BOT_TOKEN = getenv("8209712439:AAH-TuZmh0ou1sUw5KtT7Ebox4Av7lQIkFg")
BOT_NAME = getenv("BOT_NAME", "Artz Music Projesi")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/cd0b87484429704c7b935.png")
THUMB_IMG = getenv("THUMB_IMG", "https://i.ibb.co/VQd4HSH/Photo-1629477903701.jpg")
AUD_IMG = getenv("AUD_IMG", "https://i.ibb.co/VQd4HSH/Photo-1629477903701.jpg")
QUE_IMG = getenv("QUE_IMG", "https://i.ibb.co/VQd4HSH/Photo-1629477903701.jpg")
admins = {}
API_ID = int(getenv("21883581"))
API_HASH = getenv("c3b4ba58d5dada9bc8ce6c66e09f3f12")
BOT_USERNAME = getenv("BOT_USERNAME", "leousertaggerbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "ramomusicasis")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Sohbetdestek")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "EfsaneMusicProject")
OWNER_NAME = getenv("OWNER_NAME", "artzfounder") # kullanıcı adınızı semboller olmadan doldurma @
DEV_NAME = getenv("DEV_NAME", "artzfounder")
PMPERMIT = getenv("PMPERMIT", None)

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "250"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
