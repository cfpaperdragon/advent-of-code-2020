# Write a function to merge two strings in the reversed order.
# InvertedMerge( “abcdefg”, “12345” ) == “g5f4e3d2c1ba”
# InvertedMerge( “x”, “12345” ) == “x54321”
# InvertedMerge( “ABCDEF”, “z” ) == “FzEDCBA”

def inverted_merge(str1, str2):
    index = 1
    result = ""
    while(len(str1) >= index or len(str2) >= index):
        if len(str1) >= index:
            result += str1[-index]
        if len(str2) >= index:
            result += str2[-index]
        index += 1

    return result

def inverted_merge2(str1, str2):
    result = ""
    counter = 0
    # loop on the first string
    for i in range(len(str1)):
        result += str1[-i-1]
        if i < len(str2):
            result += str2[-i-1]
        counter = i
    # if second string is longer, loop the second string from the index we got in the first string
    if counter < len(str2):
        for j in range(counter+1, len(str2)):
            result += str2[-j-1]
    return result

def assert_equal(str1, str2):
    if str1 == str2:
        print("Equals:" + str1)
    else:
        print("Different:" + str1 + "!=" + str2)


assert_equal(inverted_merge2( "abcdefg", "12345" ), "g5f4e3d2c1ba")
assert_equal(inverted_merge2( "x", "12345" ), "x54321")
assert_equal(inverted_merge2( "ABCDEF", "z" ), "FzEDCBA")
