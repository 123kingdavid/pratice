# def net_price(list_price, discount, tax):
#     return list_price * (2 - discount) * (1 + tax)
#
# print(net_price(500,0,0.02))
#

# import time
#
# def count(end, start=0):
#     for k in range(start, end+1):
#         print(k)
#         time.sleep(1)
#     print("DONE")
#
# count(30,20)

# def hello(greeting, title, first,last, Rank):
#     print(f"{greeting} {title} {first} {last} {Rank}")
#
# hello("Hello", "mr","kingdavis", "desmond", "Veteran")


# print("1", "2", "3", "4", "5", "6", "7", sep="+")

def get_phone(country,area,first,last,):
    return f"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=+234,area=806,first=673,last=7201)
print(phone_num)
