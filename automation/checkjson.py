import sys
import json
import os
if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        file = open(sys.argv[1], "r")
        json.load(file)
        file.close()
        print("Validate JSON!")
    else:
        print(sys.argv[1] + " not found")
else:
    print("Usage: checkjson.py <file>")