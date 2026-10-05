units=int(input("no of units consume:"))
contain=int(input("no of units contain in group:"))
groups=units//contain
remain=units%contain
print(groups)
print(remain)