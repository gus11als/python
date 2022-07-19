from platform import python_branch


a = "Life is too short, you need python"
print(a[0:9:2])
#a[이상:미만:간격:] 간격에 -2 넣으면 뒤로 두칸씩

b = "20171505rainy"
date = b[:8]
print(date)

c = "I eat %d apples." % 7
d = "I eat " + str(3) + " apples"  #위에가 좀더 현명함
print(c)
print(d)

number = 10
day = "there"
e = "I ate %d apples , so I was sick for %s days" %(number , day)  #10 은 s로 해도 에러는 안남 %에 여러개를 사용시 괄호는 필수
print(e)