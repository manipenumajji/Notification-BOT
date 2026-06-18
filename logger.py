from datetime import datetime
def log_message(message):

    current_time = datetime.now()

    with open("bot.log", "a") as file:

        file.write(
            f"{current_time} | {message}\n"
        )