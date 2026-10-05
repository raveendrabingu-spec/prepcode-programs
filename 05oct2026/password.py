password=input()
special_ch=input()
if len(password)>=8 and special_ch:
    print("valid")
else:
    print("invalid")