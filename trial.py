import scroller
import PySimpleGUI as sg
import time


def main():
    """
    Builds the GUI, initializes the scroller, and uses different presets to determine speed.
    """
    running = True
    sg.theme('Dark Grey 13')
    # Build layout of GUI
    layout = [[sg.Text('Input Scroll Speed')],

              [sg.Input(key="input_speed")],
              [sg.OK(), sg.Cancel()]]

    window = sg.Window("MangaScrolls", layout, icon="scroll.ico")
    event, values = window.read()
    speed = int(values['input_speed']) * -1

    window.minimize()
    time.sleep(1)

    while running:
        scroller.scroll(speed)

    window.close()


if __name__ == "__main__":
    main()

