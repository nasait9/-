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

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box

console = Console()

# Общие данные для всех модулей
music_recommendations = {
    "радость": ["Pharrell Williams - Happy", "The Beatles - Here Comes the Sun", "ABBA - Dancing Queen"],
    "грусть": ["Billie Eilish - When the Party's Over", "Radiohead - No Surprises", "Lana Del Rey - Summertime Sadness"],
    "злость": ["Rage Against the Machine - Killing in the Name", "Slipknot - Duality", "Eminem - The Way I Am"],
    "спокойствие": ["Enigma - Return to Innocence", "Enya - Only Time", "Sigur Rós - Svefn-g-englar"]
}

communities = {
    "радость": "https://vk.com/happy_people - Сообщество позитивных людей",
    "грусть": "https://vk.com/support_group - Группа поддержки",
    "злость": "https://vk.com/anger_management - Управление гневом",
    "спокойствие": "https://vk.com/meditation_time - Медитация и релакс"
}

merch_items = {
    1: {"name": "🎵 Футболка с логотипом", "price": 999},
    2: {"name": "☕ Кружка музыкальная", "price": 499},
    3: {"name": "🎧 Значок наушники", "price": 199},
    4: {"name": "📻 Плакат ретро-радио", "price": 299}
}

def show_panel(title, content, color="blue"):
    console.print(Panel.fit(
        content,
        title=title,
        border_style=color
    ))

def show_table(title, items):
    table = Table(title=title, box=box.ROUNDED)
    table.add_column("№", style="cyan")
    table.add_column("Описание", style="magenta")
    for num, item in items.items():
        table.add_row(str(num), item["name"])
    console.print(table)