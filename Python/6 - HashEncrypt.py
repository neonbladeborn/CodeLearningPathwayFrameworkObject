import base64


chosenVariable = "yeet" # initialising a variable

inBase64_First = base64.b64encode(chosenVariable.encode('utf-8')) #encoding a varialbe
outBase64_First = base64.b64decode(inBase64_First) #decoding a variable

inBase64_Second = base64.b64encode(b'somethingIDK') #encoding a string, the "b" converts it into correct format first
outBase64_Second = base64.b64decode(b'c29tZXRoaW5nSURL') #decoding a string

print("base64 is bellow")
print(inBase64_First)
print(outBase64_First)
print("")
print(inBase64_Second)
print(outBase64_Second)



