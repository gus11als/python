# 리스트 삭제 이상:미만:간격
a = ["빅즈히", "잠수", "문재성"]
a[0:2] = []
# del a[0] 명령어도 있음
print(a)

#리스트 추가
b = [1,4,3]
b.append("시우버")
print(b)

# 정렬 숫자는 크기순 문자는 가나다순으로 정렬
c = [1,4,3]
c.sort()
print(c)

#뒤집기
d = [1,5,3]
d.reverse()
print(d)
print(d.index(5))
#index는 위치를 알려주는것

#insert는 0번째 위치에 4를 넣는것
e = [1,5,3]
e.insert(0,4)
print(e)

#remove 는 말그대로 삭제 1쓰면 1을 지워라임
#1이 여러개면 맨처음꺼 하나만 없어짐
f = [1,5,3]
f.remove(1)
print(f)