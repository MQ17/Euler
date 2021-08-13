f = open("p059_cipher.txt")
string = bytes(''.join([chr(int(number)) for number in f.read().split(',')]), "ascii")

# print(string)
# def is_english(a,b,c):
#     key = bytes(1455 * (chr(a) + chr(b) + chr(c)), "ascii")
#     decrypted = ""
#     for g, k in zip(string, key):
#         char = g ^ k
#         # print(g)
#         # print(k)
#         # print(char)
#         if char > 127 or char<32:
#             return False
#         decrypted += chr(char)
#     if decrypted.find("the") != -1 and decrypted.find("and") != -1:
#         print(a, b, c, decrypted)


# for a in range(97, 123):
#     for b in range(97, 123):
#         for c in range(97, 123):
#             is_english(a,b,c)
a = 101
b = 120
c = 112
key = bytes(1455 * (chr(a) + chr(b) + chr(c)), "ascii")
decrypted = sum(g^k for g, k in zip(string, key))

print(decrypted)

