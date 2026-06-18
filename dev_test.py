from order_manager import place_limit_buy
response = place_limit_buy(
    market="BTCINR",
    quantity=0.00001,
    price=4000000
)

print(response)