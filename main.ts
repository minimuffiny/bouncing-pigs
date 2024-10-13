player.onTravelled(BOUNCE, function () {
    mobs.spawn(PIG, randpos(
    pos(-10, 20, -10),
    pos(10, 20, 10)
    ))
})
player.onChat("slime", function () {
    blocks.fill(
    SLIME_BLOCK,
    pos(-20, 0, -20),
    pos(20, 0, 20),
    FillOperation.Replace
    )
})
