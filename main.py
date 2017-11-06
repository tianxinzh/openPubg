#!/usr/bin/python3

import os
import sys
import threading

from openPubgShell import openPubgShell
from roomManager import RoomManager
from textManager import TextManager


def main():
    # Initiate the text manager
    tManager = TextManager()
    if not tManager.emailLogin():
        return
    # Initiate the room manager
    rManager = RoomManager(tManager)
    # Pass the room manager to text manager
    tManager.setRoomManager(rManager)

    # Initiate shell
    shell = openPubgShell()
    shell.setRoomManager(rManager)
    shell.setTextManager(tManager)

    # Start multithreading
    shellThread = threading.Thread(target=shell.cmdloop)
    textThread = threading.Thread(target=tManager.run)
    textThread.daemon = True

    shellThread.start()
    textThread.start()

    # Block til shell end
    shellThread.join()


if __name__ == '__main__':
    main()
