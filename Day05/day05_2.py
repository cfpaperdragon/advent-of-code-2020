# Day 05 exercise 2

import day05

boardingpass_list = day05.read_input("input//input.txt")

seat_list = list()

for boardingpass in boardingpass_list:
    row = day05.decode_boardingpass_row(boardingpass)
    column = day05.decode_boardingpass_column(boardingpass)
    seatid = row * 8 + column
    seat_list.append(seatid)

seat_list.sort()
# for seat in seat_list:
#    print(seat)

for i in range(len(seat_list) - 1):
    this_seat = seat_list[i]
    next_seat = seat_list[i+1]
    if next_seat == (this_seat + 2):
        print(this_seat + 1)
        break
