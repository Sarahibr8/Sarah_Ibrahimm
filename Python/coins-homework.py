# Home work :

total = 287
coin_100 = total // 100 # // كم مره يدخل الرقم بدون كسور مثال : كم 100 داخل ال287 الي عندنا بتكون 2 
left = total % 100 # % كم الباقي بعد القسمه 

coin_50 = left // 50
left = left % 50

coin_25 = left // 25
left = left % 25

coin_10 = left // 10
left = left % 10 

coin_5 = left // 5
left = left % 5
coin_1 = left // 1 
print(f"Total halalas: {total}\n") # \n for line after total .

print(f"100-halala coins: {coin_100}")
print(f"50-halala coins: {coin_50}")
print(f"25-halala coins: {coin_25}")
print(f"10-halala coins: {coin_10}")
print(f"5-halala coins: {coin_5}")
print(f"1-halala coins: {coin_1}")