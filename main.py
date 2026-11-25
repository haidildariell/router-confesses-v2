import os

ENTRY = "I dropped the connection because the killer is the butler and I refuse to be the one who spoils it."
OUTPUT_PATH = "/output/entry.txt"


def validate_entry(text):
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be blank")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def write_entry(text, path):
    validated = validate_entry(text)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(validated)


if __name__ == "__main__":
    write_entry(ENTRY, OUTPUT_PATH)
