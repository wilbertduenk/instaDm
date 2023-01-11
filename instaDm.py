from instabot import Bot

bot = Bot()
bot.login(username="your_username", password="your_password")

# Send a message to the user with the username "target_username"
message = "Hello! This is a message sent using the instabot library."
bot.direct_message(target_username, message)