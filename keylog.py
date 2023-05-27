from pynput import keyboard
from pynput.keyboard import Controller, Key

class keylog():
    
    current_word = ""

    controller = Controller()

    ban_list = ["hello"]

    def trigger(self):
        self.controller.type("TRIGGERED")
        #print("TRIGGERED")
        with self.controller.pressed(Key.ctrl):
            self.controller.press("w")
            self.controller.release("w")
        '''
        with self.controller.pressed(Key.alt):
            self.controller.press(Key.f4)
            self.controller.release(Key.f4)
        '''

    def on_press(self, key):
        try:
            print(key.char)
            self.current_word += key.char
        except AttributeError:
            #print('special key {0} pressed'.format(key))
            for token in self.ban_list:
                if self.current_word == token:
                    self.trigger()

            self.current_word = ""

    def input_bword(self, word):
        self.ban_list.append(word)

    #def input_bwords_file(self, file_path):
        



    def run(self):
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()
