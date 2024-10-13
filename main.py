
def on_on_chat():
    blocks.fill(SLIME_BLOCK, pos(-20, 0, -20), pos(20, 0, 20), FillOperation.REPLACE)
player.on_chat("slime", on_on_chat)
def on_travelled_bounce():
 mobs.spawn(PIG, randpos(pos(-10, 20, -10), pos(10, 20, 10)))
player.on_travelled(BOUNCE, on_travelled_bounce)