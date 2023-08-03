from _sets import *
from _defs import *

# ===== GUI init

import pygame as pg
pg.init()
screen = pg.display.set_mode(SEED["size"])
pg.display.set_caption(SEED["title"])
clock = pg.time.Clock()

# ===== GUI functions

def drawEnemys(SEED, enemys):
	i = 0
	while i < len(enemys):
		enemy = enemys[i]
		if i != len(enemys)-1:
			pg.draw.circle(screen, SEED["color"], enemy, SEED["r"])
		else:
			pg.draw.circle(screen, SEED["checkcolor"], enemy, SEED["r"]*3)
		i += 1

def drawFrames(t):
	pg.font.init()
	tsize = int(SEED["size"][1]*0.03)
	font = pg.font.SysFont("Lucida Console", tsize)
	text_frames = font.render("{}".format(str(t)), True, SEED["textcolor"])
	screen.blit(text_frames, (SEED["size"][0]-tsize*len(str(t))*0.7, SEED["size"][1]-tsize))

def drawText(SEED):
	pg.font.init()
	tsize = int(SEED["size"][1]*0.02)
	font = pg.font.SysFont("Lucida Console", tsize)

	info = "ppl:{} | mlp:{}".format(
		str(SEED["population"]),
		str(SEED["multiply"])
		)
	text_info = font.render(info, True, SEED["textcolor"])
	screen.blit(text_info, (0, SEED["size"][1]-tsize))

def drawGrid(SEED):
	pg.font.init()
	font = pg.font.SysFont("Lucida Console", int(SEED["size"][1]*0.015))

	t = int(max(SEED["size"])/10)
	i = 0
	while i < t:
		if i%10 == 0:
			tlen = 10
			mark = font.render(str(i*10), True, SEED["gridcolor"])
			screen.blit(mark, [10, i*10])
			screen.blit(mark, [i*10, 10])
		else:
			tlen = 5

		pg.draw.line(screen, SEED["gridcolor"], [i*10, 0], [i*10, tlen])
		pg.draw.line(screen, SEED["gridcolor"], [0, i*10], [tlen, i*10])
		i += 1

	pg.draw.rect(screen, SEED["gridcolor"], [
		int((SEED["size"][0]/2)-SEED["spawn"]),
		int((SEED["size"][1]/2)-SEED["spawn"]),
		SEED["spawn"]*2, SEED["spawn"]*2
		], 1)

# ===== INIT

enemys = makeEnemys(SEED["population"], SEED["size"], SEED["spawn"])

# ===== LOOP

t = 0
run = True
while run:
	screen.fill(SEED["bgcolor"])
	# ---------- LOOP

	for e in pg.event.get():
		if e.type == pg.QUIT: run = False
		if e.type == pg.KEYDOWN:
			if e.key == pg.K_ESCAPE: run = False

	drawGrid(SEED)
	drawText(SEED)

	drawFrames(t)
	drawEnemys(SEED, enemys)

	enemys = updateEnemys(SEED, enemys)

	if SEED["video"]:
		pg.image.save(screen, "{}/f{}.png".format(SEED["path"], t))

	# ---------- LOOP end
	pg.display.update()
	clock.tick(SEED["fps"])
	t += 1
	if t >= SEED["duration"]: run = False