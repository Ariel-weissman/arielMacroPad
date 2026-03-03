import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros
from kmk.handlers.sequences import press, release, tap

keyboard = KMKKeyboard()
keyboard.debug_enabled = True

macros = Macros()
keyboard.modules.append(macros)

PINS = [board.D11, board.D10, board.D9]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [KC.MACRO("Hello Person"), KC.MACRO(press(KC.LGUI), tap(KC.TAB), release(KC.LGUI)), KC.BSPC]
]

if __name__ == '__main__':
    keyboard.go()
