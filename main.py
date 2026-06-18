import time
from price_fetcher import get_price
from alert import check_alert
from notification import play_alert , show_notification
target = float(input("enter target price:"))
alert_sent=False
while True:
    price=get_price()
    print("current price:",price) 
    if check_alert(price,target) and not alert_sent:
        show_notification(price, target)
        play_alert()
        print("Alert Triggred")
        alert_sent=True
    time.sleep(10)    



