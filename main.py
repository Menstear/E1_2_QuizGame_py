class Quiz :
    #question : 문제, choices : 4개의 선택지 리스트, answer : 정답 번호, 1~4
    def __init__(self, question, choices, answer) :
        self.question = question
        self.choices = choices
        self.answer = answer

    def show_question(self) :
        print(self.question)
        for idx, choice in enumerate(self.choices, start = 1) :
            print(f"{idx}. {choice}")

    def check_answer(self, user_answer) :
        return self.answer == user_answer


quizzes = [
    Quiz(
        "대한민국의 수도는?",
        ["오사카", "서울", "파리", "오타와"],
        2
    ),
    Quiz(
        "일본의 수도는?",
        ["서울", "토론토", "도쿄", "시드니"],
        3
    ),
    Quiz(
            "프랑스의 수도는?",
            ["캔버라", "몬트리올", "마르세유", "파리"],
            4
    ),
    Quiz(
            "캐나다의 수도는?",
            ["오타와", "브리즈번", "멜버른", "벤쿠버"],
            1
    ),
    Quiz(
        "호주의 수도는?",
        ["보고타", "로마", "워싱턴 D.C", "캔버라"],
        4
    )
]

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
            print(f"입력값이 비어 있습니다. 1-5 사이의 숫자를 입력하세요.")
            continue

        try :
            choice = int(choice)
        except ValueError :
            print(f"잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.")
            continue

        if 1 <= choice <= 5 :
            return choice

        print(f"잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.")

def input_number(prompt) :
    while True :
        value = input(prompt).strip()

        if value == "" :
            print("입력값이 비어 있습니다. 1-4 사이의 숫자를 입력하세요.")
            continue

        try :
            num = int(value)

        except ValueError :
            print(f"잘못된 입력입니다. 1-4 사이의 숫자를 입력하세요.")
            continue

        if 1 <= num <= 4 :
            return num

        print(f"잘못된 입력입니다. 1-4 사이의 숫자를 입력하세요.")

def input_text(prompt) :
    while True :
        text = input(prompt).strip()

        if text == "" :
            print("빈 값은 입력할 수 없습니다.")
            continue

        return text

def play_quiz() :
    if len(quizzes) == 0:
        print("등록된 퀴즈가 없습니다.")
        return

    score = 0

    print()
    print(f"퀴즈를 시작합니다! 총 {len(quizzes)}문제입니다.\n")

    for idx, quiz in enumerate(quizzes, start = 1) :
        print("========================================\n")
        print(f"[문제 {idx}]")
        quiz.show_question()

        user_answer = input_number("정답 입력 : ")

        if quiz.check_answer(user_answer) :
            print("정답입니다!\n")
            score += 1

        else :
            print(f"오답입니다. 정답은 {quiz.answer}번입니다.\n")

    print("========================================")
    print(f"결과 : {len(quizzes)}문제 중 {score}문제 정답!")
    print("========================================")

def add_quiz() :
    print()
    print("새로운 퀴즈를 추가합니다.")

    question = input_text("문제를 입력하세요: ")

    choices = []
    for idx in range(1, 5) :
        choice = input_text(f"선택지 {idx}: ")
        choices.append(choice)

    answer = input_number("정답 번호 (1~4) : ")

    new_quiz = Quiz(question, choices, answer)
    quizzes.append(new_quiz)

    print("퀴즈가 추가되었습니다.")

def main() :
    while True :
        show_board()
        choice = choice_board()

        if choice == 1:
            play_quiz()
        elif choice == 2:
            add_quiz()
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
                