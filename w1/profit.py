cost = float(input("ต้นทุน (บาท) : "))
sell = float(input("ราคาขาย (บาท) : "))

profit = sell - cost
is_profit = profit > 0    # ตัวแปร boolean

print("กำไร/ขาดทุน :", profit, "บาท")

if profit > 0:
    print("ผลลัพธ์ : กำไร")
elif profit < 0:
    print("ผลลัพธ์ : ขาดทุน")
else:
    print("ผลลัพธ์ : เท่าทุน")

print("มีกำไรหรือไม่ :", is_profit)
