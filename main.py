from price_fetcher import get_price
from alert import check_alert
from notification import play_alert
target = 63000
price = get_price()
print("current price:",price)
triggred=check_alert(price, target)
if triggred:
    play_alert()
    print("ALERT TRIGGRED")
else:
    print("Waiting....")    
