import time

# Money
money = 100

# Gallery
gallery_name = None
gallery_exists = False

# Slots
slot_a = "empty"
slot_b = "empty"
slot_c = "empty"
slot_d = "empty"
slot_e = "empty"

# PRODUCTS
# Product 1
car1 = "Fiat Doblo"
car1_buy = 100
car1_sell = 150
car1_code = 53946

# Product 2
car2 = "Mercedes-Benz"
car2_buy = 150
car2_sell = 250
car2_code = 85383

def are_slots_full():
    return (
        slot_a != "empty" and
        slot_b != "empty" and
        slot_c != "empty" and
        slot_d != "empty" and
        slot_e != "empty"
    )

# GAME LOOP
while True:
    command = input("System > ")

    # CREATE GALLERY
    if command == "create":
        if gallery_exists:
            print("You already have a gallery.")
        else:
            gallery_name = input("Enter gallery name: ")
            gallery_exists = True
            print("Gallery created successfully.")

    # INFO
    elif command == "info":
        if gallery_exists:
            print(f"Gallery: {gallery_name}")
            print(f"Slot 1: {slot_a}")
            print(f"Slot 2: {slot_b}")
            print(f"Slot 3: {slot_c}")
            print(f"Slot 4: {slot_d}")
            print(f"Slot 5: {slot_e}")
        else:
            print("You don't have a gallery.")

    # BUY
    elif command == "buy":
        if not gallery_exists:
            print("You don't have a gallery.")
            continue

        if are_slots_full():
            print("All slots are full.")
            continue

        print(f"Your money: {money}")
        print(f"{car1} | Buy price: {car1_buy} | Code: {car1_code}")
        print(f"{car2} | Buy price: {car2_buy} | Code: {car2_code}")

        try:
            code = int(input("Enter product code: "))
        except ValueError:
            print("Please enter a number.")
            continue

        if code == car1_code:
            product = car1
            price = car1_buy
        elif code == car2_code:
            product = car2
            price = car2_buy
        else:
            print("Product not found.")
            continue

        if money < price:
            print("Not enough money.")
            continue

        slot = input("Choose slot (1-5): ")

        if slot == "1" and slot_a == "empty":
            slot_a = product
        elif slot == "2" and slot_b == "empty":
            slot_b = product
        elif slot == "3" and slot_c == "empty":
            slot_c = product
        elif slot == "4" and slot_d == "empty":
            slot_d = product
        elif slot == "5" and slot_e == "empty":
            slot_e = product
        else:
            print("Slot is full or invalid.")
            continue

        money -= price
        print("Purchase successful.")

    # SELL
    elif command == "sell":
        if not gallery_exists:
            print("You don't have a gallery.")
            continue

        slot = input("Choose slot (1-5): ")

        def sell(product):
            global money
            if product == car1:
                money += car1_sell
            elif product == car2:
                money += car2_sell

        if slot == "1" and slot_a != "empty":
            sell(slot_a)
            slot_a = "empty"
        elif slot == "2" and slot_b != "empty":
            sell(slot_b)
            slot_b = "empty"
        elif slot == "3" and slot_c != "empty":
            sell(slot_c)
            slot_c = "empty"
        elif slot == "4" and slot_d != "empty":
            sell(slot_d)
            slot_d = "empty"
        elif slot == "5" and slot_e != "empty":
            sell(slot_e)
            slot_e = "empty"
        else:
            print("Slot is empty or invalid.")
            continue

        print("Vehicle sold successfully.")

    # MONEY
    elif command == "money":
        print(f"Your money: {money}")

    # EXIT
    elif command == "exit":
        print("System shutting down...")
        time.sleep(1)
        break

    else:
        print("Invalid command.")
