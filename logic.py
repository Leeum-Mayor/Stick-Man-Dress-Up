from PyQt6.QtWidgets import *
from gui import *


class Stickman(QMainWindow, Ui_MainWindow):
    """
    Handles the logic for a stickman object
    """
    GROUPS = ['hat', 'top', 'pants', 'shoe']

    def __init__(self) -> None:
        """
        Assigns buttons and loads their features
        """
        super().__init__()
        self.setupUi(self)

        for groups in self.GROUPS:
            for i in range(6):
                button_name = getattr(self, f'{groups}{i}Button')
                button_name.toggled.connect(self.create_callback(groups, i))

        self.load_buttons()

        self.outfit1Load.clicked.connect(lambda: self.load_outfit(1))
        self.outfit2Load.clicked.connect(lambda: self.load_outfit(2))
        self.outfit3Load.clicked.connect(lambda: self.load_outfit(3))

        self.outfit1Button.clicked.connect(lambda: self.save_outfit(1))
        self.outfit2Button.clicked.connect(lambda: self.save_outfit(2))
        self.outfit3Button.clicked.connect(lambda: self.save_outfit(3))

        self.outfit1Delete.clicked.connect(lambda: self.delete_outfit(1))
        self.outfit2Delete.clicked.connect(lambda: self.delete_outfit(2))
        self.outfit3Delete.clicked.connect(lambda: self.delete_outfit(3))

    def submit(self, group: int, num: int) -> None:
        """
        Allows clothing to appear on stick-man when radio button is toggles
        :param group: Relevant clothing group
        :param num: Relevant clothing number
        """
        if group == 'shoe':
            self.shoeWearing.setPixmap(QPixmap(f'images/shoes{num}'))
        else:
            pixmap_name = getattr(self, f'{group}Wearing')
            pixmap_name.setPixmap(QPixmap(f'images/{group}{num}'))

    def create_callback(self, group: int, index: int) -> callable(int):
        """
        Loop to assign radio buttons to self.submit()
        :param group: Relevant clothing group
        :param index: Relevant clothing number
        :return: submit function with relevant clothing group and number
        """
        def callback():
            self.submit(group, index)

        return callback

    def save_outfit(self, outfit: int) -> None:
        """
        Saves outfit to correct button
        :param outfit: Which outfit number button was pressed
        """
        input_file = open('outfits.txt', 'r')
        lines = input_file.readlines()
        lines[outfit - 1] = f'{self.hatGroup.checkedId()} {self.topGroup.checkedId()} {self.pantsGroup.checkedId()} {self.shoeGroup.checkedId()}\n'
        input_file.close()

        output_file = open('outfits.txt', 'w')
        output_file.writelines(lines)
        output_file.close()

        button_save = getattr(self, f'outfit{outfit}Button')
        button_save.hide()
        button_save.setEnabled(False)

        button_load = getattr(self, f'outfit{outfit}Load')
        button_load.show()
        button_load.setEnabled(True)

        button_delete = getattr(self, f'outfit{outfit}Delete')
        button_delete.show()
        button_delete.setEnabled(True)

    def load_outfit(self, outfit: int) -> None:
        """
        Load outfit from correct button
        :param outfit: Outfit number to load
        """
        input_file = open('outfits.txt', 'r')
        lines = input_file.readlines()
        input_file.close()
        full_outfit = lines[outfit - 1].split()
        print(full_outfit)
        for group in self.GROUPS:
            pixmap_name = getattr(self, f'{group}Wearing')
            if group == 'hat' and full_outfit[0] != '-1':
                pixmap_name.setPixmap(QPixmap(f'images/{group}{full_outfit[0]}'))
                button = getattr(self, f'{group}Group').button(int(full_outfit[1]))
                button.setChecked(True)
            elif group == 'top' and full_outfit[1] != '-1':
                pixmap_name.setPixmap(QPixmap(f'images/{group}{full_outfit[1]}'))
                button = getattr(self, f'{group}Group').button(int(full_outfit[1]))
                button.setChecked(True)
            elif group == 'pants' and full_outfit[2] != '-1':
                pixmap_name.setPixmap(QPixmap(f'images/{group}{full_outfit[2]}'))
                button = getattr(self, f'{group}Group').button(int(full_outfit[2]))
                button.setChecked(True)
            elif group == 'shoe' and full_outfit[3] != '-1':
                pixmap_name.setPixmap(QPixmap(f'images/{group}s{full_outfit[3]}'))
                button = getattr(self, f'{group}Group').button(int(full_outfit[3]))
                button.setChecked(True)
            else:
                pass

    def delete_outfit(self, outfit: int) -> None:
        """
        Deletes a saved outfit
        :param outfit: Outfit number to delete
        """
        input_file = open('outfits.txt', 'r')
        lines = input_file.readlines()
        input_file.close()

        lines[outfit - 1] = 'NA\n'

        output_file = open('outfits.txt', 'w')
        output_file.writelines(lines)
        output_file.close()

        button_save = getattr(self, f'outfit{outfit}Button')
        button_save.show()
        button_save.setEnabled(True)

        button_load = getattr(self, f'outfit{outfit}Load')
        button_load.hide()
        button_load.setEnabled(False)

        button_delete = getattr(self, f'outfit{outfit}Delete')
        button_delete.hide()
        button_delete.setEnabled(False)

    def load_buttons(self) -> None:
        """
        Loads outfit buttons depending on which outfits are saved
        """
        input_file = open('outfits.txt', 'r')
        lines = input_file.readlines()

        for i in range(len(lines)):
            lines[i] = lines[i].rstrip()

        for i in range(1, 4):
            outfit_button = getattr(self, f'outfit{i}Button')
            outfit_load = getattr(self, f'outfit{i}Load')
            outfit_delete = getattr(self, f'outfit{i}Delete')

            if len(lines[i - 1]) > 2:
                print(lines[i - 1])
                outfit_button.hide()
                outfit_button.setEnabled(False)
            else:
                outfit_load.hide()
                outfit_load.setEnabled(False)
                outfit_delete.hide()
                outfit_delete.setEnabled(False)
