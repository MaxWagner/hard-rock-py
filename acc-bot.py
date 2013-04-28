#! /usr/bin/env python3

import hardrock
import sys

class AccBot(hardrock.Player):
    def __init__(self, suffix):
        super().__init__("acc" + suffix)

    def connect(self):
        super().connect("Cyberhawk", "Marauder")

    def tick(self):
        self.do("accelerate")

AccBot(sys.argv[1] if len(sys.argv) > 1 else "").connect()
