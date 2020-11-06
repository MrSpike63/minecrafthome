#!/usr/bin/env python 
import sys
import re

file_1 = sys.argv[1]
file_2 = sys.argv[2]

output_1 = re.findall(r"(?<=S: )\d{21}", open(file_1).read())
output_2 = re.findall(r"(?<=S: )\d{21}", open(file_2).read())

output_1 = sorted(list(set(output_1)))
output_2 = sorted(list(set(output_2)))

if output_1 == output_2:
    sys.exit(0)
else:
    sys.exit(1)