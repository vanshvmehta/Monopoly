import pygame
import lists
from classes import PlayerClass, Button, board, builtList, boughtList
from random import randint
import trade

chars = [pygame.image.load('Images//Character//p1.png'), pygame.image.load('Images//Character//p2.png'),
         pygame.image.load('Images//Character//p3.png'), pygame.image.load('Images//Character//p4.png')]
game_bg = pygame.image.load('Images//board//game.jpg')
home_bg = pygame.image.load('Images//board//home.jpg')
page2_bg = pygame.image.load('Images//board//NoOfPlayer.jpg')
trade_bg = pygame.image.load('Images//Trade//bg.jpg')
house = pygame.image.load('Images//Houses//house.png')
hotel = pygame.image.load('Images//Houses//hotel.png')
pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Monopoly')
dice_list = lists.dice_list
card_list = lists.card_list
chance_card = lists.chance_list
comm_card = lists.comm_list

board = board
rolled = 0
nop = 0
roll = diceCount = times = 0
dice1, dice2 = 1, 2
isEnd = endTurn = isPay = isRoll = isBank = False
isSpin = isChance = isComm = True
players = [None] * 4
playerButton = []
turn = 0
isTrade = True
isBuild = isMort = isUnmort = False
isBuilding = isTrading = isMorting = isUnmorting = False
clock = pygame.time.Clock()

startButton = Button((0, 0, 255), 250, 375, 100, 50, 35, 'START')
twoButton = Button((0, 0, 255), 133.75, 400, 75, 40, 30, 'TWO')
threeButton = Button((0, 0, 255), 262.5, 400, 75, 40, 30, 'THREE')
fourButton = Button((0, 0, 255), 391.25, 400, 75, 40, 30, 'FOUR')
tradeButton = Button((255, 255, 0), 88, 90, 100, 30, 20, 'TRADE')
buildButton = Button((255, 255, 0), 196, 90, 100, 30, 20, 'BUILD')
mortButton = Button((255, 255, 0), 304, 90, 100, 30, 20, 'MORTGAGE')
unmortButton = Button((255, 255, 0), 412, 90, 100, 30, 20, 'UNMORTGAGE')
doneButton = Button((0, 0, 255), 410, 480, 100, 30, 30, 'DONE')
spinButton = Button((0, 0, 255), 250, 375, 100, 50, 35, 'SPIN')
spinAgainButton = Button((0, 0, 255), 250, 375, 100, 50, 25, 'SPIN AGAIN')
buyButton = Button((0, 0, 255), 150, 350, 125, 35, 25, 'BUY FOR ')
ignoreButton = Button((0, 0, 255), 150, 400, 125, 35, 25, 'IGNORE')
endTurnButton = Button((0, 0, 255), 415, 490, 100, 25, 25, 'END TURN')
rollJailButton = Button((0, 0, 255), 238, 400, 125, 35, 25, 'ROLL')
payJailButton = Button((0, 0, 255), 238, 450, 125, 35, 25, 'PAY 100 M')
bankruptcyButton = Button((0, 0, 255), 200, 375, 200, 50, 25, 'DECLARE BANKRUPTCY')

deck = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


def shuffleDeck():
    p = []
    for i in range(16):
        r = randint(0, len(deck) - 1)
        p.append(deck[r])
        deck.remove(deck[r])
    return p


chance_deck = shuffleDeck()
comm_deck = chance_deck.copy()
empty_chance = []
empty_comm = []
print(chance_deck)


def home_loop(pos):
    global home, page2

    if event.type == pygame.MOUSEBUTTONDOWN:
        if startButton.isOver(pos):
            home = False
            page2 = True
            pygame.time.delay(1000)

    if event.type == pygame.MOUSEMOTION:
        if startButton.isOver(pos):
            startButton.colour = (0, 255, 0)
        else:
            startButton.colour = (0, 0, 255)


def createPlayers():
    colours = [(255, 0, 0), (0, 0, 255), (0, 255, 0), (255, 255, 0)]
    for i in range(nop):
        players[i] = PlayerClass('Player ' + str(i + 1), colours[i], chars[i])


def redrawHome():
    win.blit(home_bg, (0, 0))
    startButton.draw(win, (0, 0, 0))


def page2_loop(pos):
    global nop, page2, game
    if event.type == pygame.MOUSEBUTTONDOWN:
        if twoButton.isOver(pos):
            nop = 2
            page2 = False
            game = True
            pygame.time.delay(1000)

        elif threeButton.isOver(pos):
            nop = 3
            page2 = False
            game = True
            pygame.time.delay(1000)

        elif fourButton.isOver(pos):
            nop = 4
            page2 = False
            game = True
            pygame.time.delay(1000)

        createPlayers()

    if event.type == pygame.MOUSEMOTION:
        if twoButton.isOver(pos):
            twoButton.colour = (0, 255, 0)
        else:
            twoButton.colour = (0, 0, 255)

        if threeButton.isOver(pos):
            threeButton.colour = (0, 255, 0)
        else:
            threeButton.colour = (0, 0, 255)

        if fourButton.isOver(pos):
            fourButton.colour = (0, 255, 0)
        else:
            fourButton.colour = (0, 0, 255)


def redrawPage2():
    win.blit(page2_bg, (0, 0))
    twoButton.draw(win, (0, 0, 0))
    threeButton.draw(win, (0, 0, 0))
    fourButton.draw(win, (0, 0, 0))


def drawPlayerButton():
    playerButton = []

    playerButton.append(Button((255, 0, 0), 95, 200, 200, 35, 30, 'PLAYER 1: ' + str(players[0].balance)))
    playerButton.append(Button((255, 0, 0), 305, 200, 200, 35, 30, 'PLAYER 2: ' + str(players[1].balance)))

    if nop == 3:
        playerButton.append(Button((255, 0, 0), 200, 240, 200, 35, 30, 'PLAYER 3: ' + str(players[2].balance)))
    elif nop == 4:
        playerButton.append(Button((255, 0, 0), 95, 240, 200, 35, 30, 'PLAYER 3: ' + str(players[2].balance)))
        playerButton.append(Button((255, 0, 0), 305, 240, 200, 35, 30, 'PLAYER 4: ' + str(players[3].balance)))

    playerButton[turn].colour = (0, 255, 0)

    black = pygame.Surface((200, 35))
    black.set_alpha(200)
    black.fill((0, 0, 0))

    for i in playerButton:
        i.draw(win, (0, 0, 0))

    for i in range(nop):
        players[i].drawButton(win, (playerButton[i].x, playerButton[i].y))

    for i in range(nop):
        if players[i].bankrupt:
            win.blit(black, (playerButton[i].x, playerButton[i].y))


def chanceExecute(player):
    global roll, isChance, chance_deck, isEnd
    if isChance:
        black = pygame.Surface((600, 600))
        black.set_alpha(200)
        win.blit(black, (0, 0))
        win.blit(chance_card[chance_deck[-1]], (150, 210))

    else:
        if len(chance_deck) == 0:
            chance_deck = empty_chance[-1::-1]

        if chance_deck[-1] == 0:
            roll = 40 - player.pos

        elif chance_deck[-1] == 1:
            player.pos = 30
            player.x = 20
            player.y = 25
            isEnd = True

        elif chance_deck[-1] == 2:
            if player.pos < 11:
                roll = 11 - player.pos
            else:
                roll = 51 - player.pos

        elif chance_deck[-1] == 3:
            if player.pos < 15:
                roll = 15 - player.pos
            else:
                roll = 55 - player.pos

        elif chance_deck[-1] == 4:
            if player.pos < 24:
                roll = 24 - player.pos
            else:
                roll = 64 - player.pos

        elif chance_deck[-1] == 5:
            roll = 39 - player.pos

        elif chance_deck[-1] == 6:
            roll = -3

        elif chance_deck[-1] == 7:
            player.balance -= player.house * 25
            player.balance -= player.hotel * 100

        elif chance_deck[-1] == 8:
            player.balance -= player.house * 40
            player.balance -= player.hotel * 115

        elif chance_deck[-1] == 9:
            player.balance -= 150

        elif chance_deck[-1] == 10:
            player.balance -= 20

        elif chance_deck[-1] == 11:
            player.balance -= 15

        elif chance_deck[-1] == 12:
            player.balance += 150

        elif chance_deck[-1] == 13:
            player.balance += 100

        elif chance_deck[-1] == 14:
            player.balance += 50

        empty_chance.append(chance_deck[-1])
        chance_deck.remove(chance_deck[-1])


def commExecute(player):
    global roll, isComm, comm_deck, isEnd

    if isComm:
        black = pygame.Surface((600, 600))
        black.set_alpha(200)
        win.blit(black, (0, 0))
        win.blit(comm_card[comm_deck[-1]], (150, 210))

    else:
        if len(comm_deck) == 0:
            comm_deck = empty_comm[-1::-1]

        if comm_deck[-1] == 0:
            roll = 40 - player.pos

        elif comm_deck[-1] == 1:
            roll = 1 - player.pos

        elif comm_deck[-1] == 2:
            player.pos = 30
            player.x = 20
            player.y = 25
            isEnd = True

        elif comm_deck[-1] == 3:
            player.balance -= 100
            board[20].cost += 100

        elif comm_deck[-1] == 4:
            player.balance -= 50
            board[20].cost += 50

        elif comm_deck[-1] == 5:
            player.balance -= 50
            board[20].cost += 50

        elif comm_deck[-1] == 6:
            player.balance += 200

        elif comm_deck[-1] == 7:
            player.balance += 100

        elif comm_deck[-1] == 8:
            player.balance += 100

        elif comm_deck[-1] == 9:
            player.balance += 50

        elif comm_deck[-1] == 10:
            player.balance += 25

        elif comm_deck[-1] == 11:
            player.balance += 20

        elif comm_deck[-1] == 12:
            player.balance += 10

        elif comm_deck[-1] == 13:
            for i in range(nop):
                if players[i].name == player.name:
                    player.balance += 10 * nop
                else:
                    players[i].balance -= 10

        elif comm_deck[-1] == 14:
            player.balance -= 100

        empty_comm.append(comm_deck[-1])
        comm_deck.remove(comm_deck[-1])


def topButtons(player):
    global isBuild, isMort, isUnmort

    black = pygame.Surface((100, 30))
    black.set_alpha(200)
    black.fill((0, 0, 0))

    if len(player.unmort):
        isUnmort = True
    else:
        isUnmort = False

    if len(player.mort):
        isMort = True
    else:
        isMort = False

    for i in player.propcolour:
        if player.propcolour[i] == 0:
            isBuild = True
            break
        else:
            isBuild = False

    tradeButton.draw(win, (0, 0, 0))
    buildButton.draw(win, (0, 0, 0))
    mortButton.draw(win, (0, 0, 0))
    unmortButton.draw(win, (0, 0, 0))

    if not isBuild:
        win.blit(black, (196, 90))

    if not isMort:
        win.blit(black, (304, 90))

    if not isUnmort:
        win.blit(black, (412, 90))


def drawHouses(win):
    for i in builtList:
        for j in range(i.noh):
            if 10 > i.pos > 0:
                if i.noh in (1, 2, 3, 4):
                    win.blit(house, (62, i.start_y + j * (i.end_y - i.start_y) // 4))
                elif i.noh == 5:
                    win.blit(hotel, (62, (i.end_y + i.start_y) // 2 - 10))

            elif 20 > i.pos > 10:
                if i.noh in (1, 2, 3, 4):
                    win.blit(house, (i.start_x + j * (i.end_x - i.start_x) // 4, 62))
                elif i.noh == 5:
                    win.blit(hotel, ((i.end_x + i.start_x) // 2 - 10, 62))

            elif 30 > i.pos > 20:
                if i.noh in (1, 2, 3, 4):
                    win.blit(house, (522, i.start_y + j * (i.end_y - i.start_y) // 4))
                elif i.noh == 5:
                    win.blit(hotel, (522, (i.end_y + i.start_y) // 2 - 10))

            elif 40 > i.pos > 30:
                if i.noh in (1, 2, 3, 4):
                    win.blit(house, (i.start_x + j * (i.end_x - i.start_x) // 4, 522))
                elif i.noh == 5:
                    win.blit(hotel, ((i.end_x + i.start_x) // 2 - 10, 522))


def drawBoughtChars():
    colour = [(255, 165, 0), (255, 255, 0), (255, 0, 0), (0, 255, 0)]
    for city in boughtList:
        if 0 < city.pos < 10:
            pygame.draw.rect(win, colour[players.index(city.bought[1])], (city.start_x, city.end_y - 10, 10, 10))
        elif 10 < city.pos < 20:
            pygame.draw.rect(win, colour[players.index(city.bought[1])], (city.start_x, city.start_y, 10, 10))
        elif 20 < city.pos < 30:
            pygame.draw.rect(win, colour[players.index(city.bought[1])], (city.end_x - 10, city.start_y, 10, 10))
        elif 30 < city.pos < 40:
            pygame.draw.rect(win, colour[players.index(city.bought[1])], (city.end_x - 10, city.end_y - 10, 10, 10))


def dice(player):
    global roll, diceCount, times, dice1, dice2, isSpin, rolled
    if diceCount == 75:
        if dice1 == dice2:
            times += 1
        if times == 3:
            if dice1 == dice2:
                player.pos = 30
        if player.pos != 30:
            rolled = roll = dice1 + dice2
        diceCount = 76

    elif diceCount < 75:
        diceCount += 1
        dice1 = randint(1, 6)
        dice2 = randint(1, 6)

        win.blit(dice_list[dice1 - 1], (235, 375))
        win.blit(dice_list[dice2 - 1], (300, 375))

    if diceCount == 76:
        if roll < 0:
            #            pygame.time.delay(500)
            player.pos -= 1
            player.move()
            roll += 1

        elif roll > 0:
            #           pygame.time.delay(500)
            player.pos += 1
            if player.pos == 40:
                player.pos = 0
                player.balance += 200
            player.move()
            roll -= 1

            win.blit(dice_list[dice1 - 1], (235, 375))
            win.blit(dice_list[dice2 - 1], (300, 375))

        else:
            if player.pos == 30:
                player.x = 20
                player.y = 25
            else:
                player.move()

            if nop in (1, 2):
                win.blit(dice_list[dice1 - 1], (100, 250))
                win.blit(dice_list[dice2 - 1], (160, 250))

            elif nop in (3, 4):
                win.blit(dice_list[dice1 - 1], (100, 285))
                win.blit(dice_list[dice2 - 1], (160, 285))

            output(players[turn])


def output(player):
    global isEnd, roll, times, isMorting, isMort, isBank
    pos = player.pos
    city = board[pos]

    if pos == 30:
        times = 3

    elif city.bought[0]:
        if city.bought[1].name != player.name and not isBank:
            if player.balance >= 0:
                city.rent_cal(rolled)
                player.balance -= city.rent
                city.bought[1].balance += city.rent
            if player.balance < 0:
                pass
            else:
                print(player.name, city.bought[1].name)
                isEnd = True
        else:
            isEnd = True

    else:
        if pos not in (0, 2, 4, 5, 7, 10, 15, 17, 20, 22, 25, 30, 33, 35, 36, 38):
            buyButton.draw(win, (0, 0, 0))
            ignoreButton.draw(win, (0, 0, 0))
            win.blit(card_list[pos], (350, 300))
            buyButton.text = 'BUY FOR ' + str(city.cost)

        elif pos in (5, 15, 25, 35):
            buyButton.draw(win, (0, 0, 0))
            ignoreButton.draw(win, (0, 0, 0))
            buyButton.text = 'BUY FOR ' + str(city.cost)

        elif pos in (7, 22, 36):
            if roll == 0:
                chanceExecute(player)
            if not isChance and roll == 0:
                isEnd = True

        elif pos in (2, 17, 33):
            if roll == 0:
                commExecute(player)
            if not isComm and roll == 0:
                isEnd = True

        elif pos == 4:
            player.balance -= 200
            board[2].cost += 200
            isEnd = True

        elif pos == 38:
            player.balance -= 100
            board[20].cost += 100
            isEnd = True

        elif pos == 20:
            player.balance += board[20].cost
            board[20].cost = 0
            isEnd = True

        elif pos in (0, 10):
            pygame.time.delay(500)
            isEnd = True

    if player.balance < 0:
        bankruptcyButton.draw(win, (0, 0, 0))
        isEnd = False
        isBank = True
    if isBank and player.balance > 0:
        isEnd = True
        isBank = False


def outputButtons(pos, player):
    global isEnd, nop, run, isBank

    if event.type == pygame.MOUSEBUTTONDOWN:
        if buyButton.isOver(pos):
            if player.balance - board[player.pos].cost >= 0:
                player.buycity()
                isEnd = True

        if ignoreButton.isOver(pos):
            isEnd = True

    if event.type == pygame.MOUSEMOTION:
        if buyButton.isOver(pos):
            buyButton.colour = (0, 255, 0)
        else:
            buyButton.colour = (0, 0, 255)

        if ignoreButton.isOver(pos):
            ignoreButton.colour = (0, 255, 0)
        else:
            ignoreButton.colour = (0, 0, 255)

    if player.balance < 0:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if bankruptcyButton.isOver(pos):
                player.bankrupt = True
                for i in player.prop:
                    i.bought = [False, None]
                    i.noh = 0
                    i.ifmort = False
                isEnd = True
                isBank = False

        if event.type == pygame.MOUSEMOTION:
            if bankruptcyButton.isOver(pos):
                bankruptcyButton.colour = (255, 0, 0)
            else:
                bankruptcyButton.colour = (0, 0, 255)


def jail(player):
    global isPay, isRoll, dice1, dice2, isEnd, diceCount, roll, rolled, isSpin, times

    if player.pos == 30 and player.bail != 0 and not isPay and not isRoll and not isEnd:
        payJailButton.draw(win, (0, 0, 0))
        rollJailButton.draw(win, (0, 0, 0))

    if isPay:
        player.pos = 10
        player.balance -= 100
        player.bail = 3
        isPay = False

    if isRoll:
        if diceCount < 75:
            diceCount += 1
            dice1 = randint(1, 6)
            dice2 = randint(1, 6)

            win.blit(dice_list[dice1 - 1], (235, 375))
            win.blit(dice_list[dice2 - 1], (300, 375))
        elif diceCount == 75:
            if dice1 == dice2:
                print('Equal')
                player.pos = 10
                player.balance -= 100
                player.bail = 3
                diceCount = 76
                roll = rolled = dice1 + dice2
                isSpin = False
            elif player.bail == 1:
                isPay = True
                print(player.bail)
            else:
                player.bail -= 1
                isEnd = True
                print(player.bail)

            isRoll = False


def turnButtons():
    if isEnd and dice1 != dice2 or times == 3 or (times == 0 and dice1 == dice2 and isEnd):
        endTurnButton.draw(win, (0, 0, 0))
        if nop in (1, 2):
            win.blit(dice_list[dice1 - 1], (100, 250))
            win.blit(dice_list[dice2 - 1], (160, 250))

        elif nop in (3, 4):
            win.blit(dice_list[dice1 - 1], (100, 285))
            win.blit(dice_list[dice2 - 1], (160, 285))

    if players[turn].pos != 30:
        if times in (1, 2) and isEnd and dice1 == dice2:
            spinAgainButton.draw(win, (0, 0, 0))

        elif times == 0 and isSpin:
            spinButton.draw(win, (0, 0, 0))


def topButtonsExecute(pos, player):
    global isBuilding, isTrading, isMorting, isUnmorting

    if isTrade and not isMorting and not isBuilding and not isUnmorting:
        if not isTrading:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if tradeButton.isOver(pos):
                    isTrading = True

            if event.type == pygame.MOUSEMOTION:
                if tradeButton.isOver(pos):
                    tradeButton.colour = (0, 255, 0)
                else:
                    tradeButton.colour = (255, 255, 0)

        if isTrading:
            if nop > 2 and trade.player_2 == '':
                trade.tradePage1(event, pos, nop, turn, win, players)
            else:
                if trade.player_2 == 1:
                    isTrading = False
                    trade.player_2 = ''
                elif not trade.offered:
                    if nop == 2:
                        if turn == 0:
                            trade.player_2 = players[1]
                            trade.tradePage2(players[0], players[1], win, event, pos)
                        else:
                            trade.player_2 = players[0]
                            trade.tradePage2(players[1], players[0], win, event, pos)
                    else:
                        trade.tradePage2(players[turn], trade.player_2, win, event, pos)
                else:
                    trade.tradePage3(players[turn], trade.player_2, win, event, pos)

    if isBuild and not isMorting and not isTrading and not isUnmorting:
        if not isBuilding:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if buildButton.isOver(pos):
                    isBuilding = True

            if event.type == pygame.MOUSEMOTION:
                if buildButton.isOver(pos):
                    buildButton.colour = (0, 255, 0)
                else:
                    buildButton.colour = (255, 255, 0)

        if isBuilding:
            player.build(pos, win, event)

    if isMort and not isBuilding and not isTrading and not isUnmorting:
        if not isMorting:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mortButton.isOver(pos):
                    isMorting = True

            if event.type == pygame.MOUSEMOTION:
                if mortButton.isOver(pos):
                    mortButton.colour = (0, 255, 0)
                else:
                    mortButton.colour = (255, 255, 0)

        if isMorting:
            player.mortgage(pos, win, event)

    if isUnmort and not isBuilding and not isTrading and not isMorting:
        if not isUnmorting:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if unmortButton.isOver(pos):
                    isUnmorting = True

            if event.type == pygame.MOUSEMOTION:
                if unmortButton.isOver(pos):
                    unmortButton.colour = (0, 255, 0)
                else:
                    unmortButton.colour = (255, 255, 0)

        if isUnmorting:
            player.unmortgage(pos, win, event)

    if isUnmorting or isBuilding or isMorting:
        doneButton.draw(win, (0, 0, 0))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if doneButton.isOver(pos):
                isBuilding = isTrading = isMorting = isUnmorting = False
        if event.type == pygame.MOUSEMOTION:
            if doneButton.isOver(pos):
                doneButton.colour = (0, 255, 0)
            else:
                doneButton.colour = (0, 0, 255)


def spin(pos, player):
    global diceCount, isSpin, isEnd, endTurn, isChance, isComm, isPay, isRoll

    if player.pos != 30:
        if times == 0:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if spinButton.isOver(pos):
                    isSpin = endTurn = False
                    isChance = isComm = True

            if event.type == pygame.MOUSEMOTION:
                if spinButton.isOver(pos):
                    spinButton.colour = (0, 255, 0)
                else:
                    spinButton.colour = (0, 0, 255)

        if times in (1, 2):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if spinAgainButton.isOver(pos):
                    diceCount = 0
                    isEnd = False
                    isChance = isComm = True

            if event.type == pygame.MOUSEMOTION:
                if spinAgainButton.isOver(pos):
                    spinAgainButton.colour = (0, 255, 0)
                else:
                    spinAgainButton.colour = (0, 0, 255)

    else:
        if not isEnd:
            jail(players[turn])
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rollJailButton.isOver(pos):
                    isRoll = True
                if payJailButton.isOver(pos):
                    isPay = True

            if event.type == pygame.MOUSEMOTION:
                if rollJailButton.isOver(pos):
                    rollJailButton.colour = (0, 255, 0)
                else:
                    rollJailButton.colour = (0, 0, 255)

                if payJailButton.isOver(pos):
                    payJailButton.colour = (0, 255, 0)
                else:
                    payJailButton.colour = (0, 0, 255)


def game_loop(pos, player):
    global isSpin, endTurn, times, turn, isEnd, isChance, isComm, isPay, isRoll, diceCount

    if isSpin or (times in (1, 2) and isEnd):
        spin(pos, player)
    topButtonsExecute(pos, player)

    if not isEnd:
        outputButtons(pos, player)

    if isEnd and dice1 != dice2 or times == 3 or (times == 0 and dice1 == dice2 and isEnd):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if endTurnButton.isOver(pos):
                endTurn = isSpin = True
                isEnd = isPay = isRoll = False
                times = 0
                diceCount = 0
                if turn == nop - 1:
                    turn = 0
                else:
                    turn += 1
                if players[turn].bankrupt:
                    if turn == nop - 1:
                        turn = 0
                    else:
                        turn += 1

        if event.type == pygame.MOUSEMOTION:
            if endTurnButton.isOver(pos):
                endTurnButton.colour = (0, 255, 0)
            else:
                endTurnButton.colour = (0, 0, 255)

    if isChance and player.pos in (7, 22, 36):
        if event.type == pygame.MOUSEBUTTONDOWN:
            isChance = False

    if isComm and player.pos in (2, 17, 33):
        if event.type == pygame.MOUSEBUTTONDOWN:
            isComm = False


def redrawGame():
    win.blit(game_bg, (0, 0))
    if not isBuilding and not isMorting and not isTrading and not isUnmorting:
        drawPlayerButton()
        topButtons(players[turn])
        turnButtons()
        drawBoughtChars()
        for i in range(nop):
            players[i].draw(win)
    if not isEnd and not isSpin:
        dice(players[turn])
    drawHouses(win)


home = True
page2 = False
game = False
run = True
while run:
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()

        if event.type == pygame.QUIT:
            run = False

    if home:
        redrawHome()
        home_loop(pos)

    elif page2:
        page2_loop(pos)
        redrawPage2()

    elif game:
        t = nop
        for i in range(nop):
            if players[i].bankrupt:
                t -= 1
        if t == 1:
            run = False
        redrawGame()
        game_loop(pos, players[turn])

    pygame.display.update()

pygame.quit()
