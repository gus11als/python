
https://wikidocs.net/42526
#1
a = 80
b = 75
c = 55

print((a+b+c)/3)

#2 %를 통해 홀수 짝수 구별 0이면 짟수 1이면 홀수
print(13%2)

#3 이상:미만:간격
a ="881120-1068234"
year = a[0:6]
print(year)
etc = a[7:14]
print(etc)

#남호쿤꺼 빼끼기
#b = input('주민번호를 입력하세요 % - 포함 :')
#b = b.replace("-","").strip()
#print(b[0:6])
#print(b[6:13])

#4
c = "881120-2068234"
print(c[7])

#5
d = "a:b:c:d"
e = d.replace(":","#").strip()
print(e)

#6
f = [1,3,5,4,2]
f.sort()
f.reverse()
print(f)

#7
g = ['Life','is','too','short']
h = " ".join(g)
print(h)
