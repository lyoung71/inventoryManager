landons_inventory = {
    "gold": 500, "mana potion": 3, "health potion": 2,
    "leather loincloth": 1, "daedric greatsword": 1
}

new_stuff = [
    "fire staff", "gold", "gold", "deadly poison", "steel arrow"
]

stuff_to_drop = [
    "gold", "mana potion", "health potion"
    ]


def display_inventory(inventory):
    total_items = 0
    print("Inventory: ")
    for k, v in inventory.items():
        print(v, k)
        total_items += v
    print("Total number of items: " + str(total_items))


def add_to_inventory(inventory, new_loot):
    for item in new_loot:
        if item not in inventory:
            inventory[item] = 1
        else:
            inventory[item] += 1
    display_inventory(inventory)


def drop_item(inventory, dropped_items):
    for item in dropped_items:
        inventory[item] -= 1
    display_inventory(inventory)


display_inventory(landons_inventory)


add_to_inventory(landons_inventory, new_stuff)


drop_item(landons_inventory, stuff_to_drop)
