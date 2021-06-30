import hashlib
import os
import sys


def CalcSha1(filepath):
    with open(filepath, 'rb') as f:
        sha1obj = hashlib.sha1()
        sha1obj.update(f.read())
        hashVal = sha1obj.hexdigest()
        print(hashVal)
        return hashVal


if __name__ == "__main__":
    filename = sys.argv[1]
    if os.path.exists(filename):
        CalcSha1(filename)
    else:
        print("cannot found file")
# raw_input("pause")
