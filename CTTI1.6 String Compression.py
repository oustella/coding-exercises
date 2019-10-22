# 1.6
def strCompress(user_str):
    letter = user_str[0]
    count = 1
    i = 1
    compressed = ""
    while i < len(user_str):
        print(i)
        if user_str[i] != letter:
            compressed += letter + str(count)
            letter = user_str[i]
            count = 1
        else:
            count += 1
        i += 1
    compressed += letter + str(count)
    print(compressed)
    if len(compressed) < len(user_str):
        return compressed
    else:
        return user_str


def strCompress(user_str):
    """uses .join() to combine string which is faster than string + operation."""
    count = 0
    i = 0
    compressed = []
    while i < len(user_str):
        count += 1
        if i + 1 >= len(user_str) or user_str[i] != user_str[i+1]:  # if index out of range or (absolute) current string does not equal the next string
            compressed.append(user_str[i])
            compressed.append(str(count))  # make sure to convert count integer to string
            count = 0  # return to zero for the next character
        i += 1
    compressed_string = "".join(compressed)
    # print(compressed)
    if len(compressed_string) < len(user_str):
        return compressed_string
    else:
        return user_str

strCompress("aaaaaaaabxcc")
strCompress("abxcc")
strCompress("aaaaaaaaaaaaaaAAbxcc")