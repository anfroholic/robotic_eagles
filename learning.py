
print('hello Angie')


angie = 'angie is awesome'
print(angie)


shooter_stick = 0

def shooter(joystick):
    # print(joystick)
    if joystick > 0:
        print('move up')
        move('up')
    elif joystick < 0:
        print('move down')
        move('down')
    else:
        print('stop')
        move('stop')


elevator_up = False

def move(direction):
    # print(direction)
    if direction == 'up':
        print('motor1.' + direction)
    elif direction == 'down':
        print('motor1.' + direction)
    elif direction == 'stop':
        print('motor1.' + direction)
    else:
        print('unknown')


def comparison(boat, bagel):
    house = boat
    apple = bagel
    print(house == apple)
    print(house != apple)
    print(apple > house)
    print(house == 6)
    print(house + apple)
    print(apple - house)
    print(house * apple)
    print(float(apple) / float(house))
    print(apple // house)
    print(apple % house)
    print(house ** apple)
    print(house - apple)
    print(apple ** .5)

def add_text(first, second):
    return first + second
def test():
    global shooter_stick
    shooter(shooter_stick)
    shooter_stick = 0.5
    shooter(shooter_stick)
    shooter_stick = -0.5
    shooter(shooter_stick)

if __name__ == '__main__':
    print(angie)

    print('run test')
    test()

    print('\nrun comparison')
    comparison(14, 73)