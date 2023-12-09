from logic import *


def main():
    """
    Runs application and loads window
    """
    application = QApplication([])
    window = Stickman()
    window.show()
    application.exec()


if __name__ == '__main__':
    main()
