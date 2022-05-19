# content of test_class.py
import os

shell = """
    python3 steganophy.py -i audio/outfile.wav  -d
"""

stdout = os.popen(shell).read()

print(stdout)