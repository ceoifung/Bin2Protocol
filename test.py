import os

def print_hex(bytes):
  l = [hex(int(i)).replace('0x', '').zfill(2) for i in bytes]
  return " ".join(l)

with open("./01.bin", "rb") as file:
    l1 = []
    for line in file:
        l1.extend(print_hex(line).split(' '))
    # print(len(l1))
    frame = len(l1) // 128
    # print(frame, len(l1)-frame*128)
    # print(l1[:100])
    # print('----------------------------------start-------------------------------------')
    for i in range(frame):
        # print('----------------------------------'+str(i) +
            #   '-------------------------------------')
        print(l1[i*128:128+i*128])
    # print('----------------------------------last-------------------------------------')
    print(l1[frame*128: len(l1)])
