def show_menu():
    print("=" * 40)
    print("       🎯 K-Food 퀴즈 게임 🎯")
    print("=" * 40)
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("=" * 40)
def read_int(prompt, min_value, max_value):
    while True:
        text = input(prompt).strip()
        if text == "":
            print("⚠️ 입력이 비어 있습니다. 숫자를 입력하세요.")
            continue      
        try:
            number = int(text)
        except ValueError:
            print("⚠️ 숫자만 입력할 수 있습니다.")
            continue      
        if number < min_value or number > max_value:
            print(f"⚠️ {min_value}~{max_value} 사이의 숫자를 입력하세요.")
            continue
        return number



def main():
    try:
        while True:
            show_menu()
            choice = read_int("선택: ", 1, 5)

            if choice == 5:
                print("👋 프로그램을 종료합니다.")
                break
            else:
                print("🚧 준비 중인 기능입니다.")
    except (KeyboardInterrupt, EOFError):
        print("\n⚠️ 입력이 중단되어 프로그램을 안전하게 종료합니다.")


if __name__ == "__main__":
    main()