# Day 05 exercise 1

import day05

boardingpass_list = day05.read_input("input//input.txt")
# print(boardingpass_list)

max_seatid = 0

for boardingpass in boardingpass_list:
    row = day05.decode_boardingpass_row(boardingpass)
    column = day05.decode_boardingpass_column(boardingpass)
    seatid = row * 8 + column
    if seatid > max_seatid:
        max_seatid = seatid

print(max_seatid)