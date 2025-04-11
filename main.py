from interface import show_welcome, get_main_choice
from music_module import recommend_music
from community_module import find_community
from merch_module import shop_merch

def main():
    while True:
        show_welcome()
        choice = get_main_choice()

        if choice == 0:
            break
        elif choice == 1:
            recommend_music()
        elif choice == 2:
            find_community()
        elif choice == 3:
            shop_merch()

    print("До свидания! Приходите еще!")

if __name__ == "__main__":
    main()