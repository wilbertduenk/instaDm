from InstagramAPI import InstagramAPI

# Authenticate with Instagram API
api = InstagramAPI("your_username", "your_password")
api.login()

# Send a message to the user with the username "target_username"
api.send_direct_item("target_username", "Hello! This is a message sent using the InstagramAPI library.")
