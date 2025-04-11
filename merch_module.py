from data import console, show_panel, show_table, merch_items
from rich.prompt import Confirm, IntPrompt

def shop_merch():
    show_table("🎁 Магазин музыкального мерча", merch_items)

    cart = []
    total = 0

    while True:
        choice = IntPrompt.ask(
            "Выберите товар (0 для завершения)",
            choices=["0", "1", "2", "3", "4"]
        )

        if choice == 0:
            break

        item = merch_items[choice]
        cart.append(item)
        total += item["price"]
        console.print(f"Добавлено: {item['name']} - {item['price']}₽")

    if cart:
        show_panel(
            "Ваш заказ",
            "\n".join(f"{item['name']} - {item['price']}₽" for item in cart) +
            f"\n\n[b]Итого: {total}₽[/b]",
            "green"
        )
    else:
        show_panel("Информация", "Корзина пуста", "yellow")

    input("\nНажмите Enter чтобы продолжить...")