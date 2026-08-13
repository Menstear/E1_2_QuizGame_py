import json
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

    def to_dict(self) :
        return{
            "question" : self.question,
            "choices" : self.choices,
            "answer" : self.answer
        }

class QuizGame :
    def __init__(self) :
        self.state_file = "state.json"
        self.quizzes = self.create_default_quizzes()
        self.best_score = 0
        self.best_total = 0

    def create_default_quizzes(self) :
        return [
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
                    ["오타와", "브리즈번", "멜버른", "밴쿠버"],
                    1
            ),
            Quiz(
                "호주의 수도는?",
                ["보고타", "로마", "워싱턴 D.C", "캔버라"],
                4
            )
        ]

    def save_state(self) : 
        data = {
            "quizzes" : [],
            "best_score" : self.best_score,
            "best_total" : self.best_total
        }

        for quiz in self.quizzes:
            data["quizzes"].append(quiz.to_dict())

        try :
            with open(self.state_file, "w", encoding = "utf-8") as file:
                json.dump(data, file, ensure_ascii= False, indent = 4)
        except OSError :
            print("데이터 저장 중 오류가 발생하였습니다.")

    def load_state(self) :
        try:
            with open(self.state_file, "r", encoding = "utf-8") as file :
                data = json.load(file)

            loaded_quizzes = []
            for quiz_data in data["quizzes"] :
                quiz = Quiz(
                    quiz_data["question"],
                    quiz_data["choices"],
                    quiz_data["answer"]
                )
                loaded_quizzes.append(quiz)

            self.quizzes = loaded_quizzes
            self.best_total = data.get("best_total", 0)
            self.best_score = data.get("best_score", 0)

            print(f"저장된 데이터를 불러왔습니다. 퀴즈 {len(self.quizzes)}개")

        except FileNotFoundError:
            print("저장 파일이 없어 기본 퀴즈 데이터를 사용합니다.")
        except (json.JSONDecodeError, KeyError, TypeError) :
            print("저장 파일이 손상되어 기본 퀴즈 데이터를 사용합니다.")
        except OSError :
            print("데이터 파일을 읽는 중 오류가 발생하여 기본 퀴즈 데이터를 사용합니다.")

    def show_board(self) :
        print("========================================")
        print("          🎯 나만의 퀴즈 게임 🎯")
        print("========================================")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("========================================")

    def input_number(self, prompt, min_value, max_value) :

        while True :
            value = input(prompt).strip()

            if value == "" :
                print(f"입력값이 비어 있습니다. {min_value}-{max_value} 사이의 숫자를 입력하세요.")
                continue

            try :
                num = int(value)

            except ValueError :
                print(f"잘못된 입력입니다. {min_value}-{max_value} 사이의 숫자를 입력하세요.")
                continue

            if min_value <= num <= max_value :
                return num

            print(f"잘못된 입력입니다. {min_value}-{max_value} 사이의 숫자를 입력하세요.")

    def input_text(self, prompt) :
        while True :
            text = input(prompt).strip()

            if text == "" :
                print("빈 값은 입력할 수 없습니다.")
                continue

            return text

    def play_quiz(self) :
        if len(self.quizzes) == 0:
            print("등록된 퀴즈가 없습니다.")
            return

        score = 0

        print()
        print(f"퀴즈를 시작합니다! 총 {len(self.quizzes)}문제입니다.\n")

        for idx, quiz in enumerate(self.quizzes, start = 1) :
            print("========================================\n")
            print(f"[문제 {idx}]")
            quiz.show_question()

            user_answer = self.input_number("정답 입력 : ", 1, 4)

            if quiz.check_answer(user_answer) :
                print("정답입니다!\n")
                score += 1

            else :
                print(f"오답입니다. 정답은 {quiz.answer}번입니다.\n")

        print("========================================")
        print(f"결과 : {len(self.quizzes)}문제 중 {score}문제 정답!")

        if self.best_total == 0 or score > self.best_score :
            self.best_score = score
            self.best_total = len(self.quizzes)
            print("새로운 최고 점수입니다!")
            self.save_state()

        print("========================================")

    def add_quiz(self) :
        print()
        print("새로운 퀴즈를 추가합니다.")

        question = self.input_text("문제를 입력하세요: ")

        choices = []
        for idx in range(1, 5) :
            choice = self.input_text(f"선택지 {idx}: ")
            choices.append(choice)

        answer = self.input_number("정답 번호 (1~4) : ", 1, 4)

        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)

        print("퀴즈가 추가되었습니다.")
        self.save_state()

    def show_quiz_list(self) :
        if len(self.quizzes) == 0 :
            print("등록된 퀴즈가 없습니다.")
            return

        print()
        print(f"등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print("========================================")

        for idx, quiz in enumerate(self.quizzes, start = 1) :
            print(f"[{idx}] {quiz.question}")

        print("========================================")

    def show_score(self) :
        if self.best_total == 0:
            print("아직 퀴즈를 푼 기록이 없습니다.")
            return

        score_percent = int(self.best_score / self.best_total * 100)

        print()
        print(f"최고 점수: {score_percent}점 ({self.best_total}문제 중 {self.best_score}문제 정답)")

    def run(self) :
        self.load_state()

        while True :
            self.show_board()
            choice = self.input_number("선택: ", 1, 5)

            if choice == 1:
                self.play_quiz()
            elif choice == 2:
                self.add_quiz()
            elif choice == 3:
                self.show_quiz_list()
            elif choice == 4:
                self.show_score()
            elif choice == 5:
                print("종료")
                self.save_state()
                break

            print()


if __name__ == "__main__":
    game = QuizGame()

    try :
        game.run()
    except KeyboardInterrupt :
        print("\n프로그램을 안전하게 종료합니다.")
        game.save_state()
    except EOFError :
        print("\n입력이 종료되어 프로그램을 안전하게 종료합니다.")
        game.save_state()
