# pallindrom is comparestr and reverse of astring if both are equal str is a pallindrom


str =input("enter a str")
rev_str=""
for char in str:
     rev_str=char+rev_str


if str==rev_str:
    print("pallindrom")
else:
    print("not a pallindrom")
