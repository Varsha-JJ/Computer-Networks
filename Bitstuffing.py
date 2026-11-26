
data = input("Enter the binary data: ")

stuffed_data = ""
count = 0

for bit in data:
    stuffed_data += bit

    if bit == '1':
        count += 1
    else:
        count = 0

    if count == 5:
        stuffed_data += '0'
        count = 0

flag = "01111110"

frame = flag + stuffed_data + flag

print("Original Data:", data)
print("Stuffed Data:", stuffed_data)
print("Transmitted Frame:", frame)
