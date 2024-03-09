import time
from data import Data
Th = time.gmtime().tm_hour + 9
Tm = time.gmtime().tm_min
Td = time.gmtime().tm_wday

Sd = ["월","화","수","목","금"]
if Th > 24:
    Th -= 24
    Td += 1
if Td > 4:
    print("주말 일정이 등록되지 않았습니다.\n평일에 실행하세요.")
    ans = input("\nEnter로 종료...")
    while ans != "":
        ans = input("...")
    exit()
try:
    f = open("setting.txt","r")
except(Exception):
    f = open("setting.txt","w")
    f.write(input("학년(정수) >> ")+"\n")
    f.write(input("반(정수) >> ")+"\n")
    f.write(input("최소화 사용(boolean) >> "))
    f.close()
    f = open("setting.txt","r")
data = f.readlines()
g = int(data[0])
if g != 1:
    print("지원되지 않는 학년입니다.\nsetting.txt를 제거하세요")
    ans = input("\nEnter로 종료...")
    while ans != "":
        ans = input("...")
    exit()
c = int(data[1])
if c not in [1,2,3,4]:
    print("대마고는 1반부터 4반까지만 있습니다.\nsetting.txt를 제거하세요")
    ans = input("\nEnter로 종료...")
    while ans != "":
        ans = input("...")
    exit()
B1 = data[2]
f.close()
if (B1 == "true") or (B1 == "True"):
    B1 = True
else:
    B1 = False
C1 = Data()
Rd = C1.getData((int(c)))[Td]
Sl = ["담임","1교시","휴식","2교시","휴식","3교시","휴식","4교시","식사","5교시","휴식","6교시","휴식","7교시","담임","8교시","식사","9교시","휴식","10교시","일과 종료"] if Td != 4 else ["담임","1교시","휴식","2교시","휴식","3교시","휴식","4교시","식사","5교시","담임"]
St = list()
for i in Rd:
    St.append(i[1])
if not B1:
    print(f"/ {g}학년 {c}반 {Sd[Td]}요일 시간표 /", end="\n")
    count = 0
    for i in Rd:
        print(f"{Sl[count]}\t[{i[0]}] {i[1]}")
        count += 1
count = 0
Fl = list()
for i in St:
    if ((Th == int(i[:(len(i)-3)])) and (Tm >= int(i[(len(i)-2):]))) or (Th > int(i[:(len(i)-3)])):
        Fl.append(count)
    count += 1
C2 = True
if Fl[-1]+1 >= len(Rd):
    C2 = False
print(f"/ 현재 시각 : {Th}시 {Tm}분 /")
try:
    print(f"\n현재 교시 : {Rd[Fl[-1]][0]}")
except(Exception):
    print(f"\n등교 전")
    Fl = [-1]
if C2:
    Tt = Rd[Fl[-1]+1][1]
    Lh = int(Tt[:(len(Tt)-3)]) - Th
    Lm = int(Tt[(len(Tt)-2):]) - Tm
    if Lm < 0:
        Lh -= 1
        Lm += 60
        print(f"[{Rd[Fl[-1]+1][0]}] 까지 남은 시간 : ",end="")
    if Lh == 0:
        print(f"{Lm}분")
    else:
        print(f"{Lh}시 {Lm}분")
else:
    print("다음 일정 : 없음")

ans = input("\nEnter로 종료...")
while ans != "":
    ans = input("...")