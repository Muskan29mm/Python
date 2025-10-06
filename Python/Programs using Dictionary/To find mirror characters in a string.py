# Program to find mirror characters in a string

mirror_chars = set("AHIMOTUVWXY018")

def check_mirror_characters(input_str):
    mirror = []
    non_mirror = []

    for char in input_str.upper():  # Convert to uppercase for uniformity
        if char in mirror_chars:
            mirror.append(char)
        else:
            non_mirror.append(char)

    print("Input String:", input_str)
    print("Mirror Characters:", ''.join(mirror))
    print("Non-Mirror Characters:", ''.join(non_mirror))

# Example usage
input_str = "HELLO123"
check_mirror_characters(input_str)

