#! /usr/bin/env python3

import hardrock
import sys
import xboxdrv

xboxdrv.keyboard = True

class AccBot(hardrock.Player):
    def __init__(self, suffix):
        super().__init__("Oz" + suffix)
        xboxdrv.init()

    def connect(self):
        super().connect("Katarina Lyons", "Airblade")

    def tick(self):
        for thing in xboxdrv.events():
            self.do(thing)
            break

AccBot(sys.argv[1] if len(sys.argv) > 1 else "").connect()
