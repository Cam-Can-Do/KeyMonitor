import sys
from keymon import keyMon

def main(argc, argv):
    log = keyMon()

    if argc > 1:
        for arg in argv[1:]:
            if arg == 'r':
                log.run()
            else:
                log.import_file(arg)

    menu = True
    while menu:
        print("""
        ==================================================================
        KEYMON MENU
           1 - run, 2 - input trigger, 3 - input triggers from txt file   
                      p - print active triggers, q - quit
        ==================================================================
        """)
        choice = input()
        if choice == "1":
            menu = False
            log.run()
        elif choice == "2":
            log.add_trigger((input("trigger: ").lower()).strip())
        elif choice == "3":
            log.import_file(input("input file path: "))
        elif choice == "p":
            log.print_triggers()
        elif choice == "q":
            menu = False
        else:
            print("Invalid input.")

    print("End!")


if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
