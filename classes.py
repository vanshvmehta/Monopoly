import pygame

builtList = []
boughtList = []

class CityClass:
    def __init__(self, name, pos, cost, colour, start_x, end_x, start_y, end_y):
        self.name = name
        self.cost = cost
        self.colour = colour
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.pos = pos
        self.bought = [False, None]
        self.noh = 0
        self.ifmort = False
        self.cost_x = 125
        self.rent = 0
        self.house = self.house_cal()

    def house_cal(self):
        if self.pos < 10:
            house = 50
        elif 20 > self.pos > 10:
            house = 100
        elif 30 > self.pos > 20:
            house = 150
        elif 40 > self.pos > 30:
            house = 200
        else:
            house = 0

        return house

    def rent_cal(self, roll):
        if self.pos in (5, 15, 25, 35) and self.bought[0] == 'Y':
            rent = int(25 * self.bought[1].stations)

        elif self.pos in (12, 28) and self.bought[0] == 'Y':
            if self.bought[1].works == 1:
                rent = int(4 * roll)
            else:
                rent = int(10 * roll)

        else:
            if self.noh == 0:
                rent = int((self.cost / 10 - 4))
            else:
                rent = int((self.cost // 2 - 20) * (1 + 2 * (self.noh - 1)))

        self.rent = rent

    def isOver(self, pos):
        if self.start_x < pos[0] < self.end_x:
            if self.start_y < pos[1] < self.end_y:
                return True

        return False


board = [
    CityClass('GO', 0, 0, None, 0, 80, 520, 600),
    CityClass('Old Kent Road', 1, 60, 'Br', 0, 80, 470, 520),
    CityClass('Community Chest', 2, 0, None, 0, 80, 420, 470),
    CityClass('White Chappel Road', 3, 60, 'Br', 0, 80, 373, 420),
    CityClass('Income Tax', 4, 0, None, 0, 80, 324, 373),
    CityClass("King's Cross Station", 5, 200, 'St', 0, 80, 274, 324),
    CityClass('The Angel, Islington', 6, 100, 'LB', 0, 80, 226, 274),
    CityClass('Chance', 7, 0, None, 0, 80, 177, 226),
    CityClass('Euton Road', 8, 100, 'LB', 0, 80, 130, 177),
    CityClass('Pentonville Road', 9, 120, 'LB', 0, 80, 80, 130),
    CityClass('Jail', 10, 0, None, 0, 80, 0, 80),
    CityClass('Pall Mall', 11, 140, 'P', 80, 128, 0, 80),
    CityClass('Electric Company', 12, 150, 'V', 128, 176, 0, 80),
    CityClass('White Hall', 13, 140, 'P', 176, 226, 0, 80),
    CityClass("Northumrl'd Avenue", 14, 160, 'P', 226, 274, 0, 80),
    CityClass('Marylebone Station', 15, 200, None, 274, 324, 0, 80),
    CityClass('Bow Street', 16, 180, 'O', 324, 374, 0, 80),
    CityClass('Community Chest', 17, 0, None, 374, 422, 0, 80),
    CityClass('Marleborough Street', 18, 180, 'O', 422, 472, 0, 80),
    CityClass('Vine Street', 19, 200, 'O', 472, 521, 0, 80),
    CityClass('Free Parking', 20, 0, None, 520, 600, 0, 80),
    CityClass('Strand', 21, 220, 'R', 520, 600, 80, 130),
    CityClass('Chance', 22, 0, None, 520, 600, 130, 177),
    CityClass('Fleet Street', 23, 240, 'R', 520, 600, 177, 226),
    CityClass('Trafalgar Square', 24, 240, 'R', 520, 600, 226, 274),
    CityClass('Fenchurch St. Station', 25, 200, None, 520, 600, 274, 324),
    CityClass('Leicester Square', 26, 260, 'Y', 520, 600, 324, 373),
    CityClass('Coventry Street', 27, 260, 'Y', 520, 600, 373, 420),
    CityClass('Water Works', 28, 100, 'V', 520, 600, 420, 470),
    CityClass('Picadilly', 29, 280, 'Y', 520, 600, 470, 520),
    CityClass('Go to jail', 30, 0, None, 520, 600, 520, 600),
    CityClass('Regent Street', 31, 300, 'G', 472, 520, 520, 600),
    CityClass('Oxford Street', 32, 320, 'G', 422, 472, 520, 600),
    CityClass('Community Chest', 33, 0, None, 374, 422, 520, 600),
    CityClass('Bond Street', 34, 340, 'G', 324, 374, 520, 600),
    CityClass('Liverpool St. Station', 35, 200, None, 274, 324, 520, 600),
    CityClass('Chance', 36, 0, None, 226, 274, 520, 600),
    CityClass('Park Lane', 37, 380, 'DB', 176, 226, 520, 600),
    CityClass('Super Tax', 38, 0, None, 128, 176, 520, 600),
    CityClass('Mayfair', 39, 400, 'DB', 80, 128, 520, 600)
]


class PlayerClass:
    def __init__(self, name, colour, image):
        self.name = name
        self.x = 20
        self.y = 550
        self.pos = 0
        self.image = image
        self.balance = 1500
        self.prop = []
        self.propcolour = {'Br': 2, 'LB': 3, 'P': 3, 'O': 3, 'R': 3, 'Y': 3, 'G': 3, 'DB': 2}
        self.bail = 3
        self.stations = 0
        self.works = 0
        self.colour = colour
        self.mort = []
        self.unmort = []
        self.house = 0
        self.hotel = 0
        self.bankrupt = False

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

    def drawButton(self, win, pos):
        win.blit(self.image, pos)

    def move(self):
        pos = self.pos

        if (self.x == 20 or self.x == 30) and self.y > 30:
            self.y = (board[pos].start_y + board[pos].end_y) // 2 - 15
            self.x = 20

        elif (self.y == 10 or self.y == 25) and self.x < 550:
            self.x = (board[pos].start_x + board[pos].end_x) // 2 - 10
            self.y = 10

        elif (self.x == 560 or self.x == 550) and self.y < 545:
            self.y = (board[pos].start_y + board[pos].end_y) // 2 - 15
            self.x = 560

        elif (self.y == 550 or self.y == 545) and self.x > 30:
            self.x = (board[pos].start_x + board[pos].end_x) // 2 - 10
            self.y = 550

    def buycity(self):
        global boughtList
        city = board[self.pos]

        self.balance -= city.cost
        self.prop.append(city)
        self.mort.append(city)
        city.bought = [True, self]
        boughtList += [city]

        if city.colour == 'St':
            self.stations += 1

        elif city.colour == 'V':
            self.works += 1

        for i in self.propcolour:
            if i == city.colour:
                self.propcolour[i] -= 1

    def build(self, pos, win, event):
        global builtList
        col, buildlist = [], []

        black_mid = pygame.Surface((440, 440))
        black_mid.set_alpha(200)
        black_mid.fill((0, 0, 0))

        win.blit(black_mid, (80, 80))

        for i in board:
            for j in self.propcolour:
                if self.propcolour[j] == 0:
                    if i.colour != j:
                        black_card = pygame.Surface((i.end_x - i.start_x, i.end_y - i.start_y))
                        black_card.set_alpha(200)
                        black_card.fill((0, 0, 0))
                        win.blit(black_card, (i.start_x, i.start_y))

                    else:
                        buildlist += [i]

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in buildlist:
                for j in buildlist:
                    if i.noh > j.noh:
                        break
                else:
                    if i.isOver(pos):
                        if self.balance - i.house > 0:
                            if i.noh != 5:
                                if i.noh < 4:
                                    self.house += 1
                                else:
                                    self.hotel += 1
                                    self.house -= 4
                                self.balance -= i.house
                                i.noh += 1
                                builtList += [i]
                                pygame.time.delay(100)
                            print(i.name, i.noh)

    def mortgage(self, pos, win, event):
        black_mid = pygame.Surface((440, 440))
        black_mid.set_alpha(200)
        black_mid.fill((0, 0, 0))

        win.blit(black_mid, (80, 80))

        for i in self.unmort:
            red_card = pygame.Surface((i.end_x - i.start_x, i.end_y - i.start_y))
            red_card.set_alpha(150)
            red_card.fill((255, 0, 0))
            win.blit(red_card, (i.start_x, i.start_y))

        for i in board:
            for j in self.prop:
                if i.name == j.name:
                    break
            else:
                black_card = pygame.Surface((i.end_x - i.start_x, i.end_y - i.start_y))
                black_card.set_alpha(200)
                black_card.fill((0, 0, 0))
                win.blit(black_card, (i.start_x, i.start_y))

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in self.mort:
                if i.isOver(pos):
                    if i.noh > 0:
                        l = []
                        for j in self.mort:
                            if i.colour == j.colour:
                                l += [j]
                        mort = True
                        for j in l:
                            if i.noh < j.noh:
                                mort = False
                        if mort:
                            if i.noh == 5:
                                self.hotel -= 1
                                self.hotel += 4
                            else:
                                self.house -= 1
                            i.noh -= 1
                            self.balance += i.house // 2
                            pygame.time.delay(100)
                            print(i.name, i.noh)

                    else:
                        i.ifmort = True
                        self.propcolour[i.colour] += 1
                        self.balance += i.cost // 2
                        self.unmort += [i]
                        self.mort.remove(i)
                        pygame.time.delay(100)
                        print(i.name, i.ifmort)

    def unmortgage(self, pos, win, event):
        black_mid = pygame.Surface((440, 440))
        black_mid.set_alpha(200)
        black_mid.fill((0, 0, 0))

        win.blit(black_mid, (80, 80))

        for i in self.unmort:
            red_card = pygame.Surface((i.end_x - i.start_x, i.end_y - i.start_y))
            red_card.set_alpha(150)
            red_card.fill((255, 0, 0))
            win.blit(red_card, (i.start_x, i.start_y))

        for i in board:
            for j in self.prop:
                if i.name == j.name:
                    break
            else:
                black_card = pygame.Surface((i.end_x - i.start_x, i.end_y - i.start_y))
                black_card.set_alpha(200)
                black_card.fill((0, 0, 0))
                win.blit(black_card, (i.start_x, i.start_y))

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in self.unmort:
                if i.isOver(pos):
                    i.ifmort = False
                    self.propcolour[i.colour] -= 1
                    self.balance -= i.cost // 2
                    self.mort += [i]
                    self.unmort.remove(i)
                    pygame.time.delay(100)
                    print(i.name, i.ifmort)


class Button:
    def __init__(self, colour, x, y, width, height, size, text = ''):
        self.colour = colour
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.text_size = size

    def draw(self, win, outline=None):
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.colour, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comics', self.text_size)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (
                self.x + (self.width // 2 - text.get_width() // 2), self.y + (self.height // 2 - text.get_height() // 2)))

    def isOver(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True

        return False
