from hashlib import sha256

# prints the sha256 hash for different substrings of the string "hash"
if __name__ == "__main__":
    # [example]
    example = bytes("hash", "utf-8")
    for i in range(1, len(example) + 1):
        substring = example[:i]
        hash = sha256(substring).hexdigest()
        print(f"{substring}\n{hash}")
    # [/example]
