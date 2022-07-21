#공백을 넣는 방법 10을 넣으면 앞에 10칸이 띄어쓰기가됨
#-10이면 반대로 뒤에서 띄어쓰기 10번됨 
c = "%10s" % "hi"
d = "%-10smin" % "hi"
print(c)
print(d)

#소수점 짜르기
e = "%0.2f" % 3.142321312
print(e)

#카운트 몇갠지 찾아주는것
f = "hobby"
print(f.count("b"))
#find는 어딨는지 찾아줌 맨처음 b를 찾아줌
g = "hobby"
print(g.find("b"))
print(g.find("x"))

#뒤에 10은 시작점을 나타냄 10이면 맨뒤에 16출력 2로하면 앞쪽 8출력
#print(j.index('찾을워드',시작위치,끝낼위치))
j = "Life is too short"
print(j.index('t',10))

#하나씩 포함해줌
a = ",".join("abcd")
print(a)

#대문자로 변환
b = "hi"
print(b.upper())
#소문자로 변환
h = "HI"
print(h.lower())
#공백 제거해줌
i = "      hi       "
print(i.strip())
