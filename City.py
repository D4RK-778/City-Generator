WORKING = True
if WORKING:
    import pygame as py
    import random as r
    py.init()

    WWIN_SZ = 909
    HWIN_SZ = 778
    window = py.display.set_mode((WWIN_SZ, HWIN_SZ))
    clock = py.time.Clock()

    class Building(py.sprite.Sprite):
        def __init__(self, image, x, y, rotation=None):
            py.sprite.Sprite.__init__(self)
            if rotation is None:
                angle = r.randint(-15, 16)
            self.image = py.transform.rotozoom(image, angle, 1)
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)

    building = py.image.load("building top.png").convert_alpha()
    city = py.sprite.Group()
    poses = []
    pop = 0
    buildings = 0
    ls = [
        "UK", "BR", "PT", "AR", "CUBA",
        "USA", "FR", "GER", "RUS", "SWE", "SING",
        "SLO", "SVK", "CHINA", "ITA", "JAP", "GRE", "NOR",
        # Easter Eggs
        "USSR", "US", "????"
    ]
    location = ""

    def cloning():
        city.empty()
        poses.clear()
        buildings = r.randint(0, 64)
        location = r.choice(ls)
        pop = 60 * buildings
        for i in range(buildings):
            nw = r.randint(120, 789)
            nh = r.randint(120, 658)
            oc_pos = False
            for pos in poses:
                if abs(pos[0] - nw) < 100 and abs(pos[1] - nh) < 100:
                    oc_pos = True
                    break
            if not oc_pos:
                poses.append((nw, nh))
                new = Building(building, nw, nh)
                city.add(new)

        print(poses, pop, buildings, location)

    cloning()

    while True:
        clock.tick(64)
        for e in py.event.get():
            if e.type == py.QUIT:
                py.quit()
            if e.type == py.KEYDOWN:
                if e.key == py.K_SPACE:
                    cloning()
        window.fill((0, 187, 0))
        city.draw(window)

        py.display.update()