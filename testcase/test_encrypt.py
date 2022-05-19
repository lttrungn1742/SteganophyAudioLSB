# content of test_class.py
import os

shell = """
    python3  steganophy.py -i audio/audio.wav -o audio/outfile.wav -s "Le Thanh Trung testing" -e
"""

stdout = os.popen(shell).read()

print(stdout)