from time import sleep
from datetime import datetime
import sys
import CoinMarketCap

class Launcher:
    # Initial Current DateTime
    date = datetime.now()
        
    # Construction
    def __init__(self, delay=1):
        # Initial Variable
        self.delay = delay # Launcher Update Delay
        self.coinMarketCap = CoinMarketCap(2) # Initial CoinMarketCap Minning Model

        # Core Process
        self.init()
        self.update()

    # Sigle Process
    def init(self):
        print('Launch...')
        self.coinMarketCap.init()

    # Repeating Process
    def update(self):
        while True:
            # <---------- Start Repeat Function ---------->
            self.updateDatetime()
            self.coinMarketCap.update(self.date.minute)
            # <---------- End Repeat Function ---------->
            sleep(self.delay)
    
    # Set current Date
    def updateDatetime(self):
        self.date = datetime.now()
        print(f"<---------- {self.date} ---------->")


sys.modules[__name__] = Launcher
