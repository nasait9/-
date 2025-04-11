from data import console, show_panel, music_recommendations
from interface import get_mood

def recommend_music():
    mood_map = {
        1: "радость",
        2: "грусть",
        3: "злость",
        4: "спокойствие"
    }

    mood_choice = get_mood()
    mood = mood_map[mood_choice]

    show_panel(
        f"Музыка для настроения: {mood}",
        "\n".join(music_recommendations[mood]),
        "yellow"
    )
    input("\nНажмите Enter чтобы продолжить...")