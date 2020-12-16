# Day 16 exercise 1

import day16

fields, ticket, other_tickets = day16.read_input("input//input.txt")

result_cache, result = day16.check_valid_tickets(fields, other_tickets, dict())

# print(fields)
# print(ticket)
# print(other_tickets)
# print(result_cache)
# result = calculate_scanning_error_rate(result_cache)
print(result)
