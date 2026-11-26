data = input("Enter the data: ")

flag = 'F'
esc = 'E'

stuffed_data = ""

for ch in data:
    if ch == flag or ch == esc:
        stuffed_data += esc

    stuffed_data += ch

frame = flag + stuffed_data + flag

print("Original Data:", data)
print("Stuffed Data:", stuffed_data)
print("Transmitted Frame:", frame)
