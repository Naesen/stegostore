'''

This file will take in the path of any file on the machine
convert it to base 64
encrypt this base 64 string
append it with a "start" and "end" byte
create a "whitespace" counter until the sum of the filesize, the bookend bytes, and the whitespace tokens %3=0
Determine if this sum, when divided by three, is square, if so, use an equal height and width value
if not square, factorize the thirded sum. If the thirded sum is prime, add 3 to the whitespaces counter and refactor.
If it is not prime, take the two closest (central) factors to produce the image.

Take the height, width, whitespace counter, and total encrypted filestring,
use PIL to put it in to an image (starting with the whitespace counter, essentially values which will be skipped over in
the decryption process), then providing that image as output


Idea: have it use argparse in a command line style fashion.
Allow for user to specify -e for encrypt, -d for decrypt -f for filepath, -m for message, -p for password, -o for output destination.
look up how to pipe this output to other processes.

the -m option will simply take in a string, encode it in to a message inside the image.
'''

import base64
import math
import numpy
import random
import os
import sys


def encodefile(filepath):
    encodedstring=""
    with open(filepath, "rb") as myfile:
        encodedstring=base64.b64encode(myfile.read())
    return encodedstring

def encodemessage(message):
    encodedstring=""
    encodedstring=b64encode(message)
    return encodedstring



