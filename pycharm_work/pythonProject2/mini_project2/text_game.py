import random
import sys
import time
import os


def game_start():
    os.system('cls')
    print("""

    ⢀⣠⣴⣿⣿⣿⣿⣦⡄⠀⠀⠀⠀⠀
⠀⠀⠀⣴⣿⣿⣾⣿⣿⣿⣾⣿⣿⣆⠀⠀⠀⠀
⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀
⠀⣾⣿⣿⣿⣿⣿⣿⠟⢿⣿⣿⣿⣿⣿⣧⠀⠀
⢰⣿⣿⣿⣿⣿⣿⠃⠀⠈⢻⣿⣿⣿⣿⣿⡆⠀
⣼⣿⣿⣿⣿⣿⡏⠀⠀⠀⠘⣿⣿⣿⣿⣿⡇⠀
⣿⣿⣿⣿⣿⣿⡇⢠⣶⣦⡀⣿⣿⣿⣿⣿⣿⠀
⣿⣿⣿⣿⣿⣿⡇⠸⠿⠟⠀⣿⣿⣿⣿⣿⣿⡄
⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣷⠀⢀⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣗
⣿⣿⣿⣿⠏⢻⣿⣿⣿⣿⣿⣿⣿⡟⢹⣿⣿⣿
⣿⣿⣿⡿⠀⢸⣿⣿⣿⣿⣿⣿⣿⠃⠀⣿⣿⣿
⣿⣿⣿⠇⠀⢸⣿⣿⣿⣿⣿⣿⣿⠀⠀⢻⣿⣿
⢹⣿⣿⠀⠀⢸⣿⣿⣿⣿⣿⣿⡟⠀⠀⠈⢿⣏
⢸⣿⡇⠀⠀⠀⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⢸⡧
⠸⣿⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠁
⠀⠃⠀⠀⠀⠀⢸⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⠂⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⡟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀
""")


print("당신의 이름은 무엇입니까?")
i = input()

print(f"달콤한 꿈 속으로 오신 것을 환영합니다.{i}님.\n{i}(은)는 희미하게 들리는 목소리에 정신이 들었다.")

# 전투시 실제 적용되는 요소
hp = 75  # 체력
dfs = 0  # 방어력
atk = 0  # 공격력

# 스탯 - 전투력: 공격력, 체력 상승 / 정신력: 방어력, 스킬 증뎀 / 운: 도주 확률 증가
cop = 0  # 전투력: 공격력, 체력 상승
mty = 0  # 정신력: 방어력, 스킬 증뎀
luk = 0  # 운: 도주 확률 증가

# 부가요소 - 기: 스킬 사용을 위한 수치(기를 2번 모아야 스킬 발동, 스킬은 2번쨰 기력 모은 턴에 바로 발동.) / 도주: 도망
energy = 0  # 기력
getaway = 0  # 도망

# 랜덤 능력치
while 1:
    cop = random.randrange(5, 11)
    hp = hp + cop * 1
    atk = cop
    mty = random.randrange(1, 6)
    luk = random.randrange(1, 6)
    print(f"전투력 = {cop}, 정신 = {mty}, 운 = {luk}")
    print("능력치를 다시 결정 하시겠습니까?: a = yes, b = no")
    A = input()
    if A == "a":
        continue
    if A == "b":
        print("\n정말 선택하겠습니까?: a = yes, b = no")
        B = input()
        if B == "b":
            continue
        elif B == "a":
            print("\n능력치가 결정 되었습니다.")
            print(f"""
        [staus]
        이름 = {i}
        클래스 = 뱀파이어
        체력 = {hp}
        전투력 = {cop}
        정신 = {mty}
        운 = {luk}""")
            break

game_start()

# 게임 시작


input(f"\n{i}: 여긴... 어디지?")
input(f"\n사역마: 깨어나셨군요 마이 로드.")
input(f"\n{i}: 우왓! 깜짝이야!? 너는...!?")
input(f"\n사역마: 저는 당신의 충실한 종, 사역마입니다.")
input(f"\n{i}: 사역마..!?")
input(f"\n사역마: 네...로드꼐선 마을의 용사들에 의해 6666년 동안 봉인되셨습니다.")
input(f"\n{i}: 봉인..? 어쨰서?")
input(f"\n사역마: 이 세상에서 가장 힘을 지닌 뱀파이어가 바로 당신이니까요")
input(f"\n{i}: 내가...!? 크읏... 그러고 보니 뭔가 어지러운 것 같기도 하고...")
input(" >> 갑자기 어지러움과 심한 갈증이 느껴진다.")
input(f"\n사역마: 로드께서는 지금 기력이 많이 약해지신 상태입니다. 어서 마을로 내려가 인간들의 피를 흡혈하셔야 합니다.")
input(f"\n{i}: 인간들의 피...")
input(f"\n사역마: 로드시여...어서 인간들의 피를 빼앗으시고 로드를 봉인한 마을의 용사들에게 복수를 하셔야 합니다!")
input(f"\n{i}: 나를 봉인한 어리석은 용사들...반드시 복수하겠노라... ")
input(" >> 본능적으로 피의 갈증을 느낀 나는 복수심을 가득 안은채, 성벽 너머 불빛이 가득한 곳으로 발걸음을 옮겼다.")
input(f"\n사역마: 우선은 누워계신 동안 전투감각을 모두 잃으셨을테니 저기 있는 인간과 모의 전투를 해보시죠.")

# 야생의 인간 초기 능력치
h_hp = 50
h_dfs = 0
h_atk = 7
h_energy = 0
h_mty = 0

print("\n<야생의 인간>: 누구냐! 으힉!? 넌 뱀파이어!? 분명 용사님들이 봉인 했을텐데!?")
print(f"{i}: 하찮은 인간이여...얌전히 내 식량이 되거라...")
print('\n[시스템 알림]\n<야생의 인간>이 덤벼옵니다! 전투 시작!')

# 튜토리얼 모의전투
print(f"\n{i}(은)는의 체력: {hp}")

hp1 = hp

# 주인공의 행동 패턴, 적이 패배할 경우

while 1:
    # 주인공의 행동 패턴
    print(f"\n{i}(은)는의 차례!")
    time.sleep(1)
    N = input("q)공격, w)방어, e)스킬, r)도망\n")
    if N == "q":
        print(f"{i}(은)는 긴 손톱으로 할퀴었다.")
        atk1 = atk + random.choice([1, 2, 3, 5, 8])
        if atk1 - h_dfs <= 0:
            print("공격이 막혀버렸다...")
            h_dfs -= atk1
        else:
            h_hp -= (atk1 - h_dfs)
            print(f"<야생의 인간>의 남은 체력 = {h_hp}")
            h_dfs = 0
    elif N == "w":
        dfs += 5 + mty
        print(f'{i}(은)는 망토로 방어 자세를 취했다. 방어력이 {dfs}!')
    elif N == "e":
        energy += 1
        print(f"{i}(은)는기를 모았다.")
        if energy == 2:
            print(f"{i}(은)는의 박쥐공격!")
            h_hp -= mty + random.choice([10, 15, 20, 25, 30])
            print(f"<야생의 인간>의 남은 체력 = {h_hp}")
            energy = 0
    elif N == "r":
        escape = random.random()
        if escape < luk / 10:
            print(f"{i}(은)는 황급히 도망쳤다... \n인간에게서 도망가는 뱀파이어라니...")
            getaway += 1
            break
        else:
            print("도망에 실패했다...")
    if h_hp <= 0:
        print(f"{i}: 휴...해치웠나?;;;")
        break

    # 인간측 행동 패턴
    N = random.randrange(1, 4)
    print(f"<야생의 인간>의 차례!")
    time.sleep(1)
    if N == 1:
        h_atk1 = h_atk + random.choice([1, 2, 3, 5, 8])
        if h_atk1 - dfs <= 0:
            print("그런 약해 빠진 공격은 안 통한단다^^")
            dfs -= h_atk1
        else:
            print("<야생의 인간>은 검을 휘둘렀다.")
            hp -= (h_atk1 - dfs)
            print(f"{i}(은)는의 남은 체력 = {hp}")
            dfs = 0
    elif N == 2:
        h_dfs += 5 + h_mty
        print(f"<야셍의 인간>은 방패를 들었다.. 방어력이 {h_dfs}!")
    elif N == 3:
        h_energy += 1
        print("전집중호흡!'인간(은)는 기를 모았다.'")
        if h_energy == 2:
            print("<야생의 인간>의 스킬공격 - 번개의 호흡: 제1형 벽력일섬!")
            hp -= h_mty + random.choice([10, 15, 20, 25, 30])
            print(f"{i}(은)는의 남은 체력 = {hp}")
            h_energy = 0
    if hp <= 0:
        print("눈앞이 깜깜해졌다...")
        print("\ntip: 머리좀 굴려라 멍청아!")
        Count = input("다시 도전하시겠습니까? q: 다시 도전한다. w: 다시 도전한다. e: 다시 도전한다.\n... ")
        if Count != "무엇일까?":
            t = 4
            while t >= 1:
                t = t - 1
                time.sleep(1)
                print(f"로딩까지 {t}초")
                hp - hp1
                h_hp = 50
                h_dfs = 0
                dfs = 0
                continue

hp = hp1
dfs = 0  # 방어력
sp = 3  # 스킬 포인트

# 스킬 포인트 획득 및 분배
while sp > 0:
    print('\n[시스템 알림] \n스킬 포인트가 3만큼 올랐습니다. 능력치를 강화하세요! \nq: 전투력(공격력 상승 / 체력 상승) w: 정신력(방어력 상승 / 스킬 뎀증) 운(도망 확률 증가)')
    N = input('당신의 선택은? ... ')
    if N == "q":
        cop1 = cop
        hp1 = hp
        cop += random.choice([1, 2, 3])
        atk = cop
        hp += (cop - cop1) * 5
        print(f"\n전투력이 {cop - cop1} 만큼 올라 {cop}(이/가)되었다. 체력이 {hp - hp1}만큼 올라 {hp}(이/가)되었다.")
        sp -= 1
    elif N == "w":
        mty1 = mty
        mty += random.choice([1, 2, 3])
        print(f"\n정신력이 {mty - mty1}만큼 올라 {mty}(이/가)되었다.")
        sp -= 1
    elif N == "e":
        luk1 = luk
        luk += random.choice([1, 2, 3])
        print(f"운이 {luk - luk1}만큼 올라 {luk}(이/가)가 되었다.")
        sp -= 1

print("\n사역마: 로드시여! 인간놈을 잡아내셨군요! 축하드립니다!")
print(f"\n{i}: 헉헉...아직은 힘이 모자르다...더욱 많은 피가 필요해..!!!")
print("\n사역마: ...!? 로드시여, 이 근방에 범상치 않은 기운이 느껴집니다. 아마 용사일 것 같군요...")
print(f"\n{i}: 후후후.. 그 용사 녀석의 힘을 빼앗으면 단숨에 많은 기력이 모이겠어.")
print("\n[잠시 후]")
print("\n<???>: 웬 놈이냐!?")
print("\n'활을 든 용사가 활시위를 겨누며 말했다.'")
print(f"\n<활의 용사>: 너는!? 설마...우리 선조꼐서 666666년 전에 봉인 하셨던 뱀파이어 {i}!?")
print(f"\n{i}: 흥! 나약해 빠진 용사놈들...이미 죽어 사라졌단 말인가?")
print("\n<활의 용사>: 닥쳐라! 네 녀석은 내 대에서 반드시 재봉인 시키겠다! 그러기 위해 단련한 활이란 말이다!")
print(f"\n{i}: 가소로운 녀석, 그래 어디 그 하찮은 실력 보여 보거라! 선대 용사들은 이미 다 죽은 모양이니 네 녀석이라도 씹어 먹어 버려야겠다!")
print('\n[시스템 알림] \n<활의 용사>가 공격해 옵니다! 전투 시작!')

# <활의 용사> 초기 능력치
h1_hp = 100
h1_dfs = 2
h1_atk = 10
h1_energy = 2
h1_mty = 2

# <활의 용사>와의 전투
while 2:
    # 주인공의 행동 패턴
    print(f"\n{i}(은)는의 차례!")
    time.sleep(2)
    N = input("q)공격, w)방어, e)스킬, r)도망\n")
    if N == "q":
        print(f"{i}(은)는 긴 손톱으로 할퀴었다.")
        atk1 = atk + random.choice([1, 2, 3, 5, 8])
        if atk1 - h1_dfs <= 0:
            print("공격이 막혀버렸다...")
            h1_dfs -= atk1
        else:
            h1_hp -= (atk1 - h1_dfs)
            print(f"<활의 용사>의 남은 체력 = {h1_hp}")
            h1_dfs = 0
    elif N == "w":
        dfs += 5 + mty
        print(f'{i}(은)는 망토로 방어 자세를 취했다. 방어력이 {dfs}!')
    elif N == "e":
        energy += 1
        print(f"{i}(은)는기를 모았다.")
        if energy == 2:
            print(f"{i}(은)는의 스킬발동 - FullMoon!")
            h1_hp -= mty + random.choice([10, 15, 20, 25, 30])
            print(f"<활의 용사>의 남은 체력 = {h1_hp}")
            energy = 0
    elif N == "r":
        escape = random.random()
        if escape < luk / 10:
            print(f"{i}(은)는 황급히 도망쳤다... \n용사에게서 도망가는 뱀파이어라니...")
            getaway += 1
            break
        else:
            print("도망에 실패했다...")
    if h1_hp <= 0:
        print(f"{i}: 크크크...크하하하하하! 어리석은 용사녀석...")
        break

    # <활의 용사> 행동 패턴
    N = random.randrange(1, 4)
    print(f"<활의 용사>의 차례!")
    time.sleep(2)
    if N == 1:
        h1_atk1 = h1_atk + random.choice([1, 2, 3, 5, 8])
        if h1_atk1 - dfs <= 0:
            print("그런 약해빠진 공격은 안 통한단다^^")
            dfs -= h1_atk1
        else:
            print("<활의 용사>는 화살을 쏘았다.")
            hp -= (h1_atk1 - dfs)
            print(f"{i}(은)는의 남은 체력 = {hp}")
            dfs = 0
    elif N == 2:
        h1_dfs += 5 + h1_mty
        print(f"<활의 용사>는 수호의 주문을 외웠다.. 방어력이 {h1_dfs}!")
    elif N == 3:
        h1_energy += 1
        print("하아앗!'<활의 용사>는 활 시위를 당기며 기를 모았다.'")
        if h1_energy == 2:
            print("<활의 용사>의 스킬발동! - wind piercing!")
            hp -= h1_mty + random.choice([10, 15, 20, 25, 30])
            print(f"{i}(은)는의 남은 체력 = {hp}")
            h1_energy = 0
    if hp <= 0:
        print("눈앞이 깜깜해졌다...")
        print("\ntip: 잘 좀 해봐 멍청아...")
        Count = input("다시 도전하시겠습니까? q: 다시 도전한다. w: 다시 도전한다. e: 다시 도전한다.\n... ")
        if Count != "무엇일까?":
            t = 4
            while t >= 1:
                t = t - 1
                time.sleep(1)
                print(f"로딩까지 {t}초")
                hp - hp1
                h1_hp = 50
                h1_dfs = 0
                dfs = 0
                continue

hp = hp1
dfs = 0  # 방어력
sp = 3  # 스킬 포인트

# 스킬 포인트 획득 및 분배
while sp > 0:
    print('\n[시스템 알림] \n스킬 포인트가 3만큼 올랐습니다. 능력치를 강화하세요! \nq: 전투력(공격력 상승 / 체력 상승) w: 정신력(방어력 상승 / 스킬 뎀증) 운(도망 확률 증가)')
    N = input('당신의 선택은? ... ')
    if N == "q":
        cop1 = cop
        hp1 = hp
        cop += random.choice([1, 2, 3])
        atk = cop
        hp += (cop - cop1) * 5
        print(f"\n전투력이 {cop - cop1} 만큼 올라 {cop}(이/가)되었다. 체력이 {hp - hp1}만큼 올라 {hp}(이/가)되었다.")
        sp -= 1
    elif N == "w":
        mty1 = mty
        mty += random.choice([1, 2, 3])
        print(f"\n정신력이 {mty - mty1}만큼 올라 {mty}(이/가)되었다.")
        sp -= 1
    elif N == "e":
        luk1 = luk
        luk += random.choice([1, 2, 3])
        print(f"운이 {luk - luk1}만큼 올라 {luk}(이/가)가 되었다.")
        sp -= 1

# chapter 1 END
print(f"\n{i}: 역시..날 봉인한 용사의 자손 답게 썩 쉽진 않았군.. ")
print("\n사역마: 로드시여 드디어 용사놈 1명을 잡아내는데 성공하셨군요! 7명의 용사중 1명을 흡수 하셨습니다!")
print(f"\n{i}: 이 시대의 용사들은 총 7명이란 말인가...")
print("\n사역마: 첫 번째 난이도의 용사라 그런지 쉽게 잡으셨습니다만 남아 있는 용사들은 상당히 강력한 인물들입니다.")
print(f"\n{i}: 걱정 말거라. 내가 원래의 모든 힘을 되찾으면 그런 미물들 따윈 감히 넘볼 수 없을테니")
print("\n사역마: 아유~ 암 그렇구 말고요! 우리 로드께서 얼마나 전지전능 하신데 키키키...")
print("\n'순간, 녀석의 말에 나는 문득 떠오른 것이 있었다. \n내가 봉인된 동안 지금 시대를 이끈 인물은 과연 누구인 것인가?\n그리고 이 녀석은 과연 누구지? 과거 내게 사역마가 있었던가?")
print("\n'의문들을 뒤로 한 채 나는 새로운 용사가 있는 마을로 발걸음을 내딛기 시작했다.'")
print("\nchapter1 끝!")

sys.exit(0)


