import base64
import cryptography
import os
import sys

print(" ------------------------ BITLOCK ------------------------\n\n")

if "-h" in sys.argv:
    print("Usage of Bitlock:\n")
    print("-e <password>:\tEncrypt the password given.\n")
    print("-d <password>:\tDecrypt the password given.\n")