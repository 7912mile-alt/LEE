"""
로또 추첨 프로그램
- 1~45 중 중복 없이 6개 번호 추첨
- 보너스 번호 1개 추가 추첨
- 여러 게임 생성 가능
"""

import random


def draw_lotto():
    """로또 번호 1세트(6개 + 보너스 1개)를 추첨합니다."""
    numbers = random.sample(range(1, 46), 7)
    main = sorted(numbers[:6])
    bonus = numbers[6]
    return main, bonus


def print_result(game_num, main, bonus):
    """추첨 결과를 출력합니다."""
    main_str = " ".join(f"{n:2d}" for n in main)
    print(f"  게임 {game_num}: [ {main_str} ] + 보너스: {bonus}")


def check_result(my_numbers, winning, bonus):
    """당첨 결과를 확인합니다."""
    matched = set(my_numbers) & set(winning)
    match_count = len(matched)
    bonus_match = bonus in my_numbers

    rank_map = {
        6: "1등 (6개 일치)",
        5: "2등 (5개 + 보너스)" if bonus_match else "3등 (5개 일치)",
        4: "4등 (4개 일치)",
        3: "5등 (3개 일치)",
    }
    rank = rank_map.get(match_count, "낙첨")
    return match_count, bonus_match, rank


def main():
    print("=" * 50)
    print("        로또 6/45 추첨 프로그램")
    print("=" * 50)

    while True:
        print("\n[메뉴]")
        print("  1. 로또 번호 자동 생성")
        print("  2. 당첨 번호 추첨 및 결과 확인")
        print("  3. 종료")
        choice = input("\n선택: ").strip()

        if choice == "1":
            try:
                count = int(input("생성할 게임 수 (1~10): "))
                count = max(1, min(count, 10))
            except ValueError:
                count = 1

            print(f"\n--- 자동 생성 ({count}게임) ---")
            for i in range(1, count + 1):
                nums, bonus = draw_lotto()
                print_result(i, nums, bonus)

        elif choice == "2":
            print("\n--- 당첨 번호 추첨 ---")
            winning, bonus = draw_lotto()
            winning_str = " ".join(f"{n:2d}" for n in winning)
            print(f"  당첨 번호: [ {winning_str} ] + 보너스: {bonus}")

            try:
                count = int(input("\n내 게임 수 (1~10): "))
                count = max(1, min(count, 10))
            except ValueError:
                count = 1

            print(f"\n--- 내 번호 ({count}게임) ---")
            for i in range(1, count + 1):
                my_nums, _ = draw_lotto()
                match_count, bonus_match, rank = check_result(
                    my_nums, winning, bonus
                )
                my_str = " ".join(f"{n:2d}" for n in my_nums)
                print(f"  게임 {i}: [ {my_str} ] -> {match_count}개 일치 => {rank}")

        elif choice == "3":
            print("\n프로그램을 종료합니다.")
            break
        else:
            print("1, 2, 3 중에서 선택해주세요.")


if __name__ == "__main__":
    main()
