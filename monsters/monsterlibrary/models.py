from __future__ import unicode_literals

from django.db import models

# Create your models here.

define Monster(models.Model)
	name = models.CharField()
	# Size should be its own table
	# Type comes from a table
	# Alignment is going to come from a table
	# Armor Class : Haven't decided how this works
	# Hit Points are derived
	hit_dice = models.IntegerField() # May not be correct class callable
	# Speed has its own table too
	strength = models.IntegerField()
	dexterity = models.IntegerField()
	constitution = models.IntegerField()
	intelligence = models.IntegerField()
	wisdom = models.IntegerField()
	charisma = models.IntegerField()
	# damage_resistances
	# damage_immunities
	# condition_immunities
	# senses
	# languages
	# skills
	# challenge = derived
	# POWERS = class
	# ACTIONS
	# LEGENDARY ACTIONS
	# LAIR ACTIONS
	
	