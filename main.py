import webbrowser
import time

print("""\
     ▄██████▄   ▄█       ████████▄     ▄████████  ▄████████    ▄█    █▄     ▄██████▄   ▄██████▄   ▄█
    ███    ███ ███       ███   ▀███   ███    ███ ███    ███   ███    ███   ███    ███ ███    ███ ███
    ███    ███ ███       ███    ███   ███    █▀  ███    █▀    ███    ███   ███    ███ ███    ███ ███
    ███    ███ ███       ███    ███   ███        ███         ▄███▄▄▄▄███▄▄ ███    ███ ███    ███ ███
    ███    ███ ███       ███    ███ ▀███████████ ███        ▀▀███▀▀▀▀███▀  ███    ███ ███    ███ ███
    ███    ███ ███       ███    ███          ███ ███    █▄    ███    ███   ███    ███ ███    ███ ███
    ███    ███ ███▌    ▄ ███   ▄███    ▄█    ███ ███    ███   ███    ███   ███    ███ ███    ███ ███▌    ▄
     ▀██████▀  █████▄▄██ ████████▀   ▄████████▀  ████████▀    ███    █▀     ▀██████▀   ▀██████▀  █████▄▄██
               ▀                                                                                 ▀
                      ▄████████ ███    █▄  ███▄▄▄▄      ▄████████    ▄████████  ▄████████    ▄████████    ▄███████▄    ▄████████
                     ███    ███ ███    ███ ███▀▀▀██▄   ███    ███   ███    ███ ███    ███   ███    ███   ███    ███   ███    ███
                     ███    ███ ███    ███ ███   ███   ███    █▀    ███    █▀  ███    █▀    ███    ███   ███    ███   ███    █▀
                    ▄███▄▄▄▄██▀ ███    ███ ███   ███  ▄███▄▄▄       ███        ███          ███    ███   ███    ███  ▄███▄▄▄
                   ▀▀███▀▀▀▀▀   ███    ███ ███   ███ ▀▀███▀▀▀     ▀███████████ ███        ▀███████████ ▀█████████▀  ▀▀███▀▀▀
                   ▀███████████ ███    ███ ███   ███   ███    █▄           ███ ███    █▄    ███    ███   ███          ███    █▄
                     ███    ███ ███    ███ ███   ███   ███    ███    ▄█    ███ ███    ███   ███    ███   ███          ███    ███
                     ███    ███ ████████▀   ▀█   █▀    ██████████  ▄████████▀  ████████▀    ███    █▀   ▄████▀        ██████████
                     ███    ███
       ▄██████▄     ▄████████    ▄████████ ███▄▄▄▄   ████████▄          ▄████████ ▀████    ▐████▀  ▄████████    ▄█    █▄       ▄████████ ███▄▄▄▄      ▄██████▄     ▄████████
      ███    ███   ███    ███   ███    ███ ███▀▀▀██▄ ███   ▀███        ███    ███   ███▌   ████▀  ███    ███   ███    ███     ███    ███ ███▀▀▀██▄   ███    ███   ███    ███
      ███    █▀    ███    ███   ███    ███ ███   ███ ███    ███        ███    █▀     ███  ▐███    ███    █▀    ███    ███     ███    ███ ███   ███   ███    █▀    ███    █▀
     ▄███         ▄███▄▄▄▄██▀   ███    ███ ███   ███ ███    ███       ▄███▄▄▄        ▀███▄███▀    ███         ▄███▄▄▄▄███▄▄   ███    ███ ███   ███  ▄███         ▄███▄▄▄
    ▀▀███ ████▄  ▀▀███▀▀▀▀▀   ▀███████████ ███   ███ ███    ███      ▀▀███▀▀▀        ████▀██▄     ███        ▀▀███▀▀▀▀███▀  ▀███████████ ███   ███ ▀▀███ ████▄  ▀▀███▀▀▀
      ███    ███ ▀███████████   ███    ███ ███   ███ ███    ███        ███    █▄    ▐███  ▀███    ███    █▄    ███    ███     ███    ███ ███   ███   ███    ███   ███    █▄
      ███    ███   ███    ███   ███    ███ ███   ███ ███   ▄███        ███    ███  ▄███     ███▄  ███    ███   ███    ███     ███    ███ ███   ███   ███    ███   ███    ███
      ████████▀    ███    ███   ███    █▀   ▀█   █▀  ████████▀         ██████████ ████       ███▄ ████████▀    ███    █▀      ███    █▀   ▀█   █▀    ████████▀    ██████████
                   ███    ███
            ▄███████▄  ▄██████▄     ▄████████     ███        ▄████████  ▄█
           ███    ███ ███    ███   ███    ███ ▀█████████▄   ███    ███ ███
           ███    ███ ███    ███   ███    ███    ▀███▀▀██   ███    ███ ███
           ███    ███ ███    ███  ▄███▄▄▄▄██▀     ███   ▀   ███    ███ ███
         ▀█████████▀  ███    ███ ▀▀███▀▀▀▀▀       ███     ▀███████████ ███
           ███        ███    ███ ▀███████████     ███       ███    ███ ███
           ███        ███    ███   ███    ███     ███       ███    ███ ███▌    ▄
          ▄████▀       ▀██████▀    ███    ███    ▄████▀     ███    █▀  █████▄▄██
                                   ███    ███                          ▀
                                                            created by Nico Davis, 2023
""")

print("Welcome to the OldSchool RuneScape Exchange Portal!\n")

already_exited = False

while not already_exited:
    item_name = input("Please enter an item to search or type 'Exit' to quit: ")

    if item_name.lower() == "exit":
        if already_exited:
            break
        else:
            already_exited = True
            print("Thank you for using the OldSchool RuneScape Exchange Portal!")
            continue

    print(f"\nSearching for {item_name}...\n")

    # Open the wiki page for the item
    url = f"https://oldschool.runescape.wiki/w/{item_name}"

    while True:
        print(f"{item_name}:\n")

        show_info = input("Do you wish to see more info about item? Enter Y/N: ")

        if show_info.lower() == "y":
            print(f"\nOpening {url}...\n")
            webbrowser.open(url)

            search_again = input("Please enter another item to search or type 'Exit' to quit: ")

            if search_again.lower() == "exit":
                if already_exited:
                    break
                else:
                    already_exited = True
                    print("Thank you for using the OldSchool RuneScape Exchange Portal!")
                    break
            else:
                item_name = search_again
                url = f"https://oldschool.runescape.wiki/w/{item_name}"
                print("\n")
                continue
        elif show_info.lower() == "n":
            search_again = input("Do you wish to search another item? Enter Y/N: ")

            if search_again.lower() == "y":
                item_name = input("Please enter item: ")
                url = f"https://oldschool.runescape.wiki/w/{item_name}"
                print("\n")
                break
            elif search_again.lower() == "n":
                if already_exited:
                    break
                else:
                    already_exited = True
                    print("Thank you for using the OldSchool RuneScape Exchange Portal!")
                    break
        else:
            print("Invalid input. Please enter 'Y' or 'N'.\n")
            continue
