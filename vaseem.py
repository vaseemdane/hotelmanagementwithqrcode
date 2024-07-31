import qrcode as qrc
import voicerecognizer


voicerecognizer.greetme()
print("Welcome to vaseem Hotels")
voicerecognizer.speak("welcome to speak Hotels")
class Hotel:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        self.items.append(item)

    def generate_qr_code(self):
        menu_data = "\n".join(self.items)
        qr = qrc.QRCode(
            version=10,
            error_correction=qrc.constants.ERROR_CORRECT_M,
            box_size=10,
            border=4
        )
        qr.add_data(menu_data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save("menucard.png")
        img.show()


hotel_menu = Hotel()


hotel_menu.add_item("Idli - 50rs")
hotel_menu.add_item("Dosa - 80rs")
hotel_menu.add_item("Poha - 60rs")
hotel_menu.add_item("vadapav - 60rs")
hotel_menu.add_item("pullava - 60rs")
hotel_menu.add_item("uttappa - 60rs")
hotel_menu.add_item("misal pav - 60rs")

hotel_menu.generate_qr_code()
voicerecognizer.speak("what yo want me to order in this menu")
if __name__ == '__main__':
   # query=voicerecognizer.takecommands().lower()
   # voicerecognizer.speak(f"ok i got it , i should order {query}")
   while True:
       query=voicerecognizer.takecommands().lower()
       # query = voicerecognizer.takecommands().lower()
       voicerecognizer.speak(f"ok i got it , i should order {query}")
       if 'ok bye' in query:
        print("bye bye have  a nice day ahead")
        voicerecognizer.speak("bye bye have  a nice day ahead")
        exit()
       else:
        print(query)


