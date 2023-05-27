from keylog import keylog

def main():
    log = keylog()

    menu = True
    while menu:
        print("keykiller menu options || 1 - run, 2 - input banword, 3 - input banwords from txt file, q - quit ||")
        choice = input()
        if choice == "q":
            menu = False
        elif choice == "1":
            menu = False
            log.run()
        elif choice == "2":
            log.input_bword(input())
        elif choice == "3":
            file_path = input("input file path: ")
            with open(file_path, 'r', encoding="utf-8") as file:
                read_data = file.read()

        else:
            print("Invalid input.")

    print("End!")


if __name__ == "__main__":
    main()
