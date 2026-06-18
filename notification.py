import winsound
from plyer import notification
def play_alert():
    winsound.Beep(1000,1000)
def show_notification(price,target):
     notification.notify(
        title="Crypto Alert",
        message=f"BTC Price: {price}\nTarget: {target}",
        timeout=10)

    