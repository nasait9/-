from data import console, show_panel, communities
from interface import get_mood

def find_community():
    mood_map = {
        1: "радость",
        2: "грусть",
        3: "злость",
        4: "спокойствие"
    }

    mood_choice = get_mood()
    mood = mood_map[mood_choice]

    show_panel(
        f"Сообщества для вашего настроения ({mood})",
        communities[mood],
        "cyan"
    )
    input("\nНажмите Enter чтобы продолжить...")