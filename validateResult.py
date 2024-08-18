import sys
import hashlib
 
valid_hash = "e68874613d6e0ea140ab9050e6358f2c58a335ffad680cceab81b826ae885692"

input_data = sys.stdin.read().strip()

input_bytes = input_data.encode('utf-8')
hash_object = hashlib.sha256(input_bytes)
hash_hex = hash_object.hexdigest()

if valid_hash == hash_hex:
    print("Correct")
else:
    print("Incorrect")