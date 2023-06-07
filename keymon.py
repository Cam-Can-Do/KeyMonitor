from pynput import keyboard
from pynput.keyboard import Controller, Key
import os
import platform

class keyMon(): 

    current_word = ""
    controller = Controller()
    trigger_list = []

    def trigger(self):
        system = platform.system()
        if system == 'Windows':
            os.system("shutdown /s /t 1")
        elif system == 'Linux':
            os.system("shutdown now")
        elif system == 'Darwin':  # macOS
            os.system("sudo shutdown -h now")

    def on_press(self, key):
        try:
            self.current_word += key.char
            #print(key.char)
        except AttributeError:
            for token in self.trigger_list:
                if self.current_word == token:
                    self.trigger()

            self.current_word = ""

    def add_trigger(self, word):
        if word not in self.trigger_list:
            self.trigger_list.append(word)
            #print(f"Trigger {word} added.")

    def import_file(self, file_path):
        try:
            with open(file_path, 'r', encoding="utf-8") as file:
                file_lines = file.readlines()
                for line in file_lines:
                    words = line.split(' ')
                    for word in words:
                        self.add_trigger((word.lower()).strip())
                #print("Triggers updated.")
        except IOError:
            print("An error occurred while reading file.")
        except Exception as e:
            print("An unexpected error occurred:", str(e))


    def print_triggers(self):
        print("Active triggers:")
        for trigger in self.trigger_list:
            print(trigger)

    def run(self):
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()
