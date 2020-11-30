import sys

# Add the parent folder path to the sys.path list
sys.path.append('../')

# Now you can import your module
import common

common.echo("start")

with open("input\\test.txt") as file:
    line = file.readline()
    print(line)

common.echo("end")
