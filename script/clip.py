import platform
import os




def to_clipboard(icon):
    current = platform.system()

    if current == "Linux":
        # Copy command for Linux.
        # I used to use xclip, but now I must consider Wayland support.
        ...
    elif current == "Darwin":
        os.system("printf '%s' " + icon + " | pbcopy")
        ...
    elif current == "Windows":
        ...
