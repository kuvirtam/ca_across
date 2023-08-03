from random import randint
from copy import deepcopy
from math import sqrt

def makeEnemys(population, size, radius):
	enemys = []
	center = [int(size[0]/2), int(size[1]/2)]
	i = 0
	while i < population:
		x = randint(center[0]-radius, center[0]+radius)
		y = randint(center[1]-radius, center[1]+radius)
		enemy = [x, y]
		enemys.append(deepcopy(enemy))
		i += 1
	return enemys

def updateEnemys(SEED, enemys):
	enemys_new = []
	for enemy in enemys:
		x, y = enemy[0], enemy[1]
		across = []
		for that in enemys:
			if that[0] == x or that[1] == y:
				across.append(deepcopy(that))
		tx, ty = 0, 0 
		for that in across:
			if that[0] < y: ty -= 1
			elif that[0] > y: ty += 1
			if that[1] < x: tx -= 1
			elif that[1] > x: tx += 1
		if not SEED["multiply"]:
			if tx > 0: tx = 1
			elif tx < 0: tx = -1
			if ty > 0: ty = 1
			elif ty < 0: ty = -1
		enemys_new.append([x+tx, y+ty])
	return enemys_new