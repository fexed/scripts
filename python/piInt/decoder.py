#!/bin/python

"""
Original idea: Sarats on Discord
"I came up with the worst number format in coding. You store two
numbers - a stard and end index.
And the value of the number is the digits of pi between those indexes
 3 = (0, 1)
 14 = (1, 3)
 69 = (41, 43)
 420 = (701, 704)
"""

from mpmath import mp
import sys

start = int(sys.argv[1])
end = int(sys.argv[2])

mp.dps = 10000

pistr = mp.nstr(mp.pi, n = 10000).replace(".", "")
print(pistr[start:end])
