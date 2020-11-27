
def rotate_chr(c):
    rot_by = 3
    c = c.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # Keep punctuation and whitespace
    if c not in alphabet:
        return c
    rotated_pos = ord(c) + rot_by
    # If the rotation is inside the alphabet
    if rotated_pos <= ord(alphabet[-1]):
        return chr(rotated_pos)
    # If the rotation goes beyond the alphabet
    return chr(rotated_pos - len(alphabet))

# cypher_text = "".join(map(rotate_chr, "My secret message goes here."))
# print(cypher_text)

print("Enter the text need to be cypher")
original_text = input()
cypher_text = "".join(map(rotate_chr, original_text))
print("cypher text is : {}".format(cypher_text))