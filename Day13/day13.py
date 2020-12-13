# Day 13 common

def calculate_bus_timestamps(bus_dict, bus_key, target):
    timestamp = 0
    bus_dict[bus_key].append(timestamp)
    while timestamp < target:
        timestamp += bus_key
        bus_dict[bus_key].append(timestamp)
    return bus_dict
