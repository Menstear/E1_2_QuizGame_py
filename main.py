def show_board() :
    print("========================================")
    print("          🎯 나만의 퀴즈 게임 🎯")
    print("========================================")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("========================================")

def choice_board() :
    while True :
        choice = input("선택: ").strip()

        if choice == "" :
            print("입력값이 비어 있습니다. 1-5 사이의 숫자를 입력하세요.")
            continue

        try :
            choice = int(choice)
        except ValueError :
            print("잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.")
            continue

        if 1 <= choice <= 5 :
            return choice

        print("잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.")


def main() :
    while True :
        show_board()
        choice = choice_board()

        if choice == 1:
            print("퀴즈 풀기")
        elif choice == 2:
            print("퀴즈 추가")
        elif choice == 3:
            print("퀴즈 목록")
        elif choice == 4:
            print("점수 확인")
        elif choice == 5:
            print("종료")
            break

        print()

if __name__ == "__main__" :
    try :
        main()
    except KeyboardInterrupt :
        print("프로그램 종료")
    except EOFError :
        print("프로그램 종료")
                