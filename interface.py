#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Влад
#
# Created:     10.04.2025
# Copyright:   (c) Влад 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from rich.prompt import IntPrompt
from data import console, show_panel

def show_welcome():
    console.clear()
    show_panel(
        "🎵 Текстовый бот-помощник",
        "Выберите режим работы\n1. Рекомендация музыки\n2. Сообщество по настроению\n3. Магазин мерча\n0. Выход",
        "magenta"
    )

def get_main_choice():
    return IntPrompt.ask("Выберите действие", choices=["0", "1", "2", "3"])

def get_mood():
    show_panel(
        "Оцените ваше настроение",
        "1. Радость 😊\n2. Грусть 😢\n3. Злость 😠\n4. Спокойствие 🧘",
        "green"
    )
    return IntPrompt.ask("Ваш выбор", choices=["1", "2", "3", "4"])