import pygame
from classes import Button, board
from lists import trade_list

bg = pygame.image.load('Images//Trade//bg.jpg')
up = pygame.image.load('Images//Trade//up.png')
down = pygame.image.load('Images//Trade//down.png')
p1Button = Button((255, 0, 0), 150, 275, 150, 40, 30, 'PLAYER 1')
p2Button = Button((255, 0, 0), 325, 275, 150, 40, 30, 'PLAYER 2')
p3Button = Button((255, 0, 0), 150, 325, 150, 40, 30, 'PLAYER 3')
p4Button = Button((255, 0, 0), 325, 325, 150, 40, 30, 'PLAYER 4')
cancelButton = Button((0, 0, 255), 420, 470, 75, 30, 25, 'CANCEL')
cash1Button = Button((128, 128, 128), 153, 450, 75, 40, 30, '0')
cash2Button = Button((128, 128, 128), 373, 450, 75, 40, 30, '0')
offerButton = Button((0, 255, 170), 80, 495, 100, 25, 20, 'OFFER')
cancelOfferButton = Button((0, 255, 170), 420, 495, 100, 25, 20, 'CANCEL')
acceptButton = Button((0, 255, 170), 80, 495, 100, 25, 20, 'ACCEPT')
rejectButton = Button((0, 255, 170), 420, 495, 100, 25, 20, 'REJECT')

p = [p1Button, p2Button, p3Button, p4Button]
chosen = offered = False
give = []
take = []
player_2 = ''

blackSurface = pygame.Surface((600, 600))
blackSurface.set_alpha(200)
blackSurface.fill((0, 0, 0))

blackCard = pygame.Surface((150, 40))
blackCard.set_alpha(200)
blackCard.fill((0, 0, 0))


def tradePage1(event, pos, nop, turn, win, players):
    global chosen, player_2
    win.blit(blackSurface, (0, 0))
    win.blit(bg, (80, 80))
    cancelButton.draw(win, (0, 0, 0))
    font1 = pygame.font.SysFont('comic sans ms', 45)
    text = font1.render('WHICH PLAYER?', 1, (255, 0, 0))
    win.blit(text, (125, 125))

    cash1Button.text = '0'
    cash2Button.text = '0'

    for i in range(nop):
        p[i].draw(win, (0, 0, 0))
        if turn == i or players[i].bankrupt:
            win.blit(blackCard, (p[i].x, p[i].y))

    if event.type == pygame.MOUSEBUTTONDOWN:
        for i in range(nop):
            if turn != i and not players[i].bankrupt:
                if p[i].isOver(pos):
                    player_2 = players[i]

        if cancelButton.isOver(pos):
            player_2 = 1

    if event.type == pygame.MOUSEMOTION:
        for i in range(nop):
            if turn != i and not players[i].bankrupt:
                if p[i].isOver(pos):
                    p[i].colour = (0, 255, 0)
                else:
                    p[i].colour = (255, 0, 0)

        if cancelButton.isOver(pos):
            cancelButton.colour = (0, 255, 0)
        else:
            cancelButton.colour = (0, 0, 255)


def tradePage2(player1, player2, win, event, pos):
    global player_2, offered, give, take
    win.blit(blackSurface, (0, 0))
    win.blit(bg, (80, 80))
    p1Prop, p2Prop = [], []

    font = pygame.font.SysFont('comic sans ms', 28)
    text1 = font.render(player1.name, 1, (255, 0, 0))
    text2 = font.render(player2.name, 1, (255, 0, 0))
    win.blit(text1, (130, 90))
    win.blit(text2, (350, 90))
    cash1Button.draw(win)
    cash2Button.draw(win)
    win.blit(up, (110, 450))
    win.blit(down, (230, 450))
    win.blit(up, (330, 450))
    win.blit(down, (450, 450))
    offerButton.draw(win, (0, 0, 0))
    cancelOfferButton.draw(win, (0, 0, 0))

    for i in range(len(player1.prop)):
        if len(player1.prop):
            if player1.prop[i].noh == 0:
                p1Prop += [trade_list[board.index(player1.prop[i])]]

    for i in range(len(player2.prop)):
        if len(player2.prop):
            if player2.prop[i].noh == 0:
                p2Prop += [trade_list[board.index(player2.prop[i])]]

    x1, y1, x2, y2 = 100, 150, 325, 150
    for i in p1Prop:
        if len(p1Prop):
            i.x = x1
            i.y = y1
            i.draw(win, (0, 0, 0))
            x1 += 45
            if x1 > 275:
                x1 = 100
                y1 += 60

    for i in p2Prop:
        if len(p2Prop):
            i.x = x2
            i.y = y2
            i.draw(win, (0, 0, 0))
            x2 += 45
            if x2 > 500:
                x2 = 325
                y2 += 60

    if event.type == pygame.MOUSEBUTTONDOWN:
        print(pos[0], pos[1])
        if 110 < pos[0] < 140 and 450 < pos[1] < 490 and int(cash1Button.text) < player2.balance:
            cash1Button.text = str(int(cash1Button.text) + 10)
        if 230 < pos[0] < 270 and 450 < pos[1] < 490 and cash1Button.text > '0':
            cash1Button.text = str(int(cash1Button.text) - 10)
        if 330 < pos[0] < 370 and 450 < pos[1] < 490 and int(cash2Button.text) < player1.balance:
            cash2Button.text = str(int(cash2Button.text) + 10)
        if 450 < pos[0] < 490 and 450 < pos[1] < 490 and cash2Button.text > '0':
            cash2Button.text = str(int(cash2Button.text) - 10)

        if offerButton.isOver(pos):
            offered = True
        if cancelOfferButton.isOver(pos):
            player_2 = 1
            try:
                for i in trade_list:
                    i.text = str(trade_list.index(i))
            except:
                pass

        for i in p1Prop:
            if i.isOver(pos):
                i.text = ''
                print(i.text)
                give += [i]

        for i in p2Prop:
            if i.isOver(pos):
                i.text = ''
                take += [i]

        pygame.time.delay(100)

    if event.type == pygame.MOUSEMOTION:
        if offerButton.isOver(pos):
            offerButton.colour = (0, 255, 0)
        else:
            offerButton.colour = (0, 255, 170)

        if cancelOfferButton.isOver(pos):
            cancelOfferButton.colour = (0, 255, 0)
        else:
            cancelOfferButton.colour = (0, 255, 170)


def tradePage3(player1, player2, win, event, pos):
    global player_2, offered, give, take
    win.blit(blackSurface, (0, 0))
    win.blit(bg, (80, 80))

    font = pygame.font.SysFont('comic sans ms', 28)
    text1 = font.render(player1.name, 1, (255, 0, 0))
    text2 = font.render(player2.name, 1, (255, 0, 0))
    win.blit(text1, (130, 90))
    win.blit(text2, (350, 90))
    cash1Button.draw(win)
    cash2Button.draw(win)
    acceptButton.draw(win, (0, 0, 0))
    rejectButton.draw(win, (0, 0, 0))

    x1, y1, x2, y2 = 100, 150, 325, 150
    for i in give:
        if len(give):
            i.x = x1
            i.y = y1
            i.text = str(trade_list.index(i))
            i.draw(win, (0, 0, 0))
            x1 += 45
            if x1 > 275:
                x1 = 100
                y1 += 60

    for i in take:
        if len(take):
            i.x = x2
            i.y = y2
            i.text = str(trade_list.index(i))
            i.draw(win, (0, 0, 0))
            x2 += 45
            if x2 > 500:
                x2 = 325
                y2 += 60

    if event.type == pygame.MOUSEBUTTONDOWN:
        if acceptButton.isOver(pos):
            tradeThem(player1, player2)
            player_2 = 1
            offered = False
        if rejectButton.isOver(pos):
            player_2 = 1

    if event.type == pygame.MOUSEMOTION:
        if acceptButton.isOver(pos):
            acceptButton.colour = (0, 255, 0)
        else:
            acceptButton.colour = (0, 255, 170)

        if rejectButton.isOver(pos):
            rejectButton.colour = (0, 255, 0)
        else:
            rejectButton.colour = (0, 255, 170)


def tradeThem(player1, player2):
    for i in give:
        city = player1.prop.pop(player1.prop.index(board[trade_list.index(i)]))
        player2.prop += [city]
        city.bought[1] = player2
        if city.ifmort:
            player2.unmort += [city]
            player1.unmort.remove(city)
        else:
            player2.mort += [city]
            player1.mort.remove(city)
        if city.colour == 'St':
            player1.stations -= 1
            player2.stations += 1
        elif city.colour == 'V':
            player1.works -= 1
            player2.works += 1
        else:
            player1.propcolour[city.colour] += 1
            player2.propcolour[city.colour] -= 1

    for i in take:
        city = player2.prop.pop(player2.prop.index(board[trade_list.index(i)]))
        player1.prop += [city]
        city.bought[1] = player1
        if city.ifmort:
            player1.unmort += [city]
            player2.unmort.remove(city)
        else:
            player1.mort += [city]
            player2.mort.remove(city)
        if city.colour == 'St':
            player2.stations -= 1
            player1.stations += 1
        elif city.colour == 'V':
            player2.works -= 1
            player1.works += 1
        else:
            player2.propcolour[city.colour] += 1
            player1.propcolour[city.colour] -= 1

    player1.balance -= int(cash2Button.text)
    player2.balance -= int(cash1Button.text)
    player2.balance += int(cash2Button.text)
    player1.balance += int(cash1Button.text)
