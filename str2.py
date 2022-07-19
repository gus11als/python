print('>>> head = "Python"')
head = "python"
tail = " is fun!"
b = "'"
print('>>> tail = " is fun!')
print(">>> head + tail")
print (b+head +tail+b)

a = "python"
print('>>> a = "python"')
print(">>> a * 2")
print(b+a * 2+b)

#b를 쓰지않고 지정해주면 가능함
d = "'%s'" % (head+tail)
print(d)