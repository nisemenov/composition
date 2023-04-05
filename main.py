from math import ceil


class WinDoor:
    def __init__(self, x, y):
        self.square = x * y


class RollWallpaper:
    def __init__(self, lg, w):
        self.square = lg * w


class Room:
    def __init__(self, lg, w, h):
        self.length = lg
        self.width = w
        self.height = h
        self.wd = []

    def full_square(self):
        return 2 * self.height * (self.length + self.width)

    def add_wd(self, w, h):
        self.wd.append(WinDoor(w, h))

    def work_surface(self):
        new_square = self.full_square()
        for i in self.wd:
            new_square -= i.square
        return round(new_square, 3)

    def wallpaper(self, lg, w):
        n = self.work_surface() / RollWallpaper(lg, w).square
        return ceil(n)


l_w_h = input('Enter dimensions of the room (LxWxH): ')
l_w = input('Enter dimensions of the one wallpaper (LxW): ')

l_w_h = [float(i) for i in l_w_h.split('x')]
l_w = [float(i) for i in l_w.split('x')]

r1 = Room(l_w_h[0], l_w_h[1], l_w_h[2])

while True:
    wd = input('Enter dimensions of the window/door (LxW) or input "next": ')
    if wd != 'next':
        wd = [float(i) for i in wd.split('x')]
        r1.add_wd(wd[0], wd[1])
    else:
        break

print(f'Area will be covered by wallpaper {r1.work_surface()}')
print(f'Quantity of wallpapers: {r1.wallpaper(l_w[0], l_w[1])}')
