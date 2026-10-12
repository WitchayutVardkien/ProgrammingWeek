scores = [72, 95, 60, 88, 51]

biggest = scores[0]          # จ.3 ตัวแทนต้องมาจากในอะเรย์ ห้ามใช้ 0
total = 0
pos = -1                     # จ.3 ค้นหา : ถ้าไม่เจอให้เป็น -1
i = 0                        # จ.2 init
while i < len(scores):       # จ.2 condition ใช้ < ไม่ใช่ <=
    if scores[i] > biggest:  # จ.3 หาค่าสูงสุด
        biggest = scores[i]
    if scores[i] == 88:      # จ.3 ค้นหาค่า
        pos = i
    total = total + scores[i]
    i = i + 1                # จ.2 update ลืมบรรทัดนี้ลูปจะค้าง

print("max =", biggest)
print("avg =", total / len(scores))
if pos == -1:                # จ.4 ต้องเช็คก่อน เพราะ scores[-1] ไม่ฟ้อง Error
    print("not found")
else:
    print("found 88 at index", pos)