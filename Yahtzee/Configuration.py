from Dice import *

class Configuration:
    configs = ["Category", "Ones", "Twos", "Threes", "Fours", "Fives", "Sixes",
               "Upper Scores", "Upper Bonus(35)", "Three of a kind", "Four of a kind", "Full House(25)",
               "Small Straight(30)", "Large Straight(40)", "Yahtzee(50)", "Chance", "Lower Scores", "Total"]

    def getConfigs():  # 정적 메소드: 객체생성 없이 사용 가능
        return Configuration.configs

    def score(row, d):  # 정적 메소드: 객체생성 없이 사용 가능
        #row에 따라 주사위 점수를 계산 반환. 예를 들어, row가 0이면 "Ones"가 채점되어야 함을
        #의미합니다. row가 2이면, "Threes"가 득점되어야 함을 의미합니다. row가 득점 (scored)하지
        #않아야 하는 버튼 (즉, UpperScore, UpperBonus, LowerScore, Total 등)을 나타내는 경우
        # -1을 반환합니다.
        if (row >= 0 and row <= 6):
            return Configuration.scoreUpper(d, row + 1)
        elif (row == 8):
            return Configuration.scoreThreeOfAKind(d)
        elif (row == 9):
            return Configuration.scoreFourOfAKind(d)
        elif (row == 10):
            return Configuration.scoreFullHouse(d)
        elif (row == 11):
            return Configuration.scoreSmallStraight(d)
        elif (row == 12):
            return Configuration.scoreLargeStraight(d)
        elif (row == 13):
            return Configuration.scoreYahtzee(d)
        elif (row == 14):
            return Configuration.sumDie(d)

    #수정필요들
    def scoreUpper(d, num):  # 정적 메소드: 객체생성 없이 사용 가능
    # Upper Section 구성 (Ones, Twos, Threes, ...)에 대해 주사위 점수를 매 깁니다. 예를 들어,
    # num이 1이면 "Ones"구성의 주사위 점수를 반환합니다.
        sum=0
        for i in range(5):
            if num ==d[i].getRoll():
                sum += num
        return sum


    def scoreThreeOfAKind(d):
        num=[]
        sum=0
        for i in range(5):
            num.append(d[i].getRoll())
            sum += num[i]
        num.sort()
        for i in range(1,6+1):
            if num.count(i) == 3:
                return sum
        return 0

    def scoreFourOfAKind(d):
        num = []
        sum=0
        for i in range(5):
            num.append(d[i].getRoll())
            sum += num[i]
        num.sort()
        for i in range(1, 6 + 1):
            if num.count(i) == 4:
                return sum
        return 0

    def scoreFullHouse(d):
        num=[]
        two=False
        three=False
        for i in range(5):
            num.append(d[i].getRoll())
        num.sort()
        for i in range(1, 6 + 1):
            if num.count(i) == 2:
                two=True
            elif num.count(i) ==3:
                three=True
        if two is True and three is True:
            return 25
        return 0

    def scoreSmallStraight(d):
        # 1 2 3 4 혹은 2 3 4 5 혹은 3 4 5 6 검사
        # 1 2 2 3 4, 1 2 3 4 6, 1 3 4 5 6, 2 3 4 4 5
        num=[]
        for i in range(5):
            num.append(d[i].getRoll())
        num.sort()
        num=list(set(num))
        if len(num)>=4:
            for i in range(len(num)-3):
                if num[i+3]-num[i] ==3:
                    return 30
        return 0

    def scoreLargeStraight(d):
        # 1 2 3 4 5 혹은 2 3 4 5 6 검사
        num = []
        for i in range(5):
            num.append(d[i].getRoll())
        num.sort()
        num = list(set(num))
        if len(num) >= 5:
            for i in range(len(num) - 4):
                if num[i + 4] - num[i] == 4:
                    return 40
        return 0

    def scoreYahtzee(d):
        num = []
        for i in range(5):
            num.append(d[i].getRoll())
        num.sort()
        for i in range(1, 6 + 1):
            if num.count(i) == 5:
                return 50
        return 0

    def sumDie(d):
        sum = 0
        for i in range(5):
                sum += d[i].getRoll()
        return sum
