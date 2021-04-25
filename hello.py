def character():
    print("유저이름은", userinput)
    print("등장인물은", member)
list_array = ['포켓몬과 싸운다', '포켓몬을 잡는다', '나의 포켓몬을 회복한다', '상대포켓몬을 무시하고 도망갔다']
b = {'지우': '피카츄', '이슬이':'토게피', '웅이':'롱스톤'}
print("<<포켓몬스터 게임>>")

userinput = input("당신의 이름을 입력하세요 ")
print("==========================")
print("지우, 이슬이, 웅이")
member = input ("등장인물을 선택하세요 ")
if member == '지우':
    print("함께할 포켓몬은 아래에 표시됩니다 ")
    print(b['지우'])
elif member == '이슬이':
    print("함께할 포켓몬은 아래에 표시됩니다")
    print(b['이슬이'])
elif member == '웅이':
    print("함께할 포켓몬은 아래에 표시됩니다")
    print(b['웅이'])
else:
    print("등장인물을 잘못입력하셨습니다 게임을 다시시작해주세요")
print("==========================")
character()
print("==========================")
while True:
    print("==========================")
    print("야생 포켓몬을 발견했습니다")
    print("싸운다, 잡는다, 회복한다, 도망간다")
    numinput = input("중에 선택해주세요 어떤것을 하시겠습니까?: ")

    if numinput == '싸운다':
        print(list_array[0])
        continue
    elif numinput == '잡는다':
        print(list_array[1])
        continue
    elif numinput == '회복한다':
        print(list_array[2])
        continue
    elif numinput == '도망간다':
        print(list_array[3])
        continue
    else:
        print("잘못 입력했습니다 게임을 종료합니다")
        break
