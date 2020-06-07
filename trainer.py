import random
import sc2
from sc2.ids.ability_id import AbilityId
from sc2.constants import *
'''
This class carried out build orders previously, variables are still used.

'''


class Trainer:

	def __init__(self):
		self.allow_voidrays = False
		self.allow_tempests = False
		self.allow_phoenix = False
		self.allow_zealots = True
		self.allow_stalkers = True
		self.allow_immortals = True
		self.allow_warpprisms = False
		self.allow_sentrys = False
		self.allow_observers = False
		self.allow_colossus = False
		self.allow_adepts = True
		self.allow_hightemplars = False
		self.allow_disruptors = False
		self.allow_carriers = False
		self.allow_mothership = False

