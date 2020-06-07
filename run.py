import sc2, sys
from __init__ import run_ladder_game
from sc2 import Race, Difficulty
from sc2.player import Bot, Computer, Human
import random


# Load bot
from additionalpylons import MyBot
bot = Bot(Race.Protoss, MyBot())
#bot = Bot(Race.Random, ExampleBot())


#allmaps = ['AutomatonLE', 'CyberForestLE', 'KairosJunctionLE', 'KingsCoveLE', 'NewRepugnancyLE', 'PortAleksanderLE', 'YearZeroLE'] # all maps
allmaps = ['EternalEmpireLE'] #, 'PortAleksanderLE', 'YearZeroLE'] # all maps

#allmaps = ['DigitalFrontier'] # test maps only

_difficulty = random.choice([Difficulty.CheatInsane, Difficulty.CheatMoney, Difficulty.CheatVision])


_realtime = True

_difficulty = Difficulty.CheatInsane #CheatInsane, CheatMoney, CheatVision
_opponent = random.choice([Race.Zerg, Race.Terran, Race.Protoss, Race.Random])
_opponent = Race.Zerg

# Start game
if __name__ == '__main__':
    if "--LadderServer" in sys.argv:
        # Ladder game started by LadderManager
        print("Starting ladder game...")
        run_ladder_game(bot)
    else:
        # Local game
        print("Starting local game...")      
        sc2.run_game(sc2.maps.get(random.choice(allmaps)), [
            Human(Race.Terran,fullscreen=True),
            Bot(Race.Protoss, MyBot())
            
        ], realtime=_realtime)