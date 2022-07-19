a = "Life is too short, You need Python"
b = "'"
print('>>> a = "Life is too short, You need Python"')
print(">>> a[0]")
print(b+a[0]+b)
print(">>> a[12]")
print(b+a[12]+b)
print(">>> a[-1]")
print(b+a[-1]+b)


# 밑은 b를 사용안하고 출력한 방법
c = "'%s'" %a[0]
print(c)
d = "'%s'" %a[12]
print(d)
e = "'%s'" %a[-1]
print(e)