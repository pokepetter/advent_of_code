with open('9_input.txt', 'r') as f:
    all_lines = f.read().strip().split('\n')
#     all_lines = '''R 4
# U 4
# L 3
# D 1
# R 4
# D 1
# L 5
# R 2'''.split('\n')    # 13
#     all_lines = '''R 5
# U 8
# L 8
# D 3
# R 17
# D 10
# L 25
# U 20'''.split('\n')    # 13

from ursina import *
app = Ursina()
window.color = color.black
window.size *= .5
# Entity(model='quad', texture='white_cube', origin=[-.5,-.5], texture_scale=Vec2(8))
par = Entity()
parts = [Button(parent=par, scale=.75, color=hsv(i*20,1,1), prev_pos=[0,0]) for i in range(2)]
head = parts[0]
tail = parts[-1]
# head = Button(parent=par, text='head')
# tail = Button(parent=par, scale=.75, text='tail')
EditorCamera()

app.i = 0
visited = [(tail.X,tail.Y), ]

def move(dir):
    head.prev_pos = head.position
    head.position += dir

    for i in range(len(parts)-1):
        lead = parts[i]
        follower = parts[i+1]

        if follower.x < lead.x-1 or follower.x > lead.x+1 or follower.y < lead.y-1 or follower.y > lead.y+1:
            # invoke(setattr, follower, 'position', lead.prev_pos, delay=.1*i)
            follower.position = lead.prev_pos

            # catch up
            # if lead.x != follower.x or lead.y != follower.y:        # move diagonally
            #     if lead.x

            # if lead.x == follower.x or lead.y == follower.y:
            #     follower.position += dir
            # else:


        if lead != head:
            lead.prev_pos = lead.position

    if not (tail.X,tail.Y) in visited:
        visited.append((tail.X,tail.Y))
        # Entity(parent=par, model='circle', position=tail.position, z=.1)


def step_next(animate=False, override_direction=False):
    if not override_direction:
        l = all_lines[app.i]
        # print_on_screen(app.i, position=(0,.45))
        dir, num = l[0], int(l[2:])
    else:
        dir = override_direction
        num = 1

    dir = {'R' : Vec2(1,0), 'L' : Vec2(-1,0), 'U' : Vec2(0,1), 'D' : Vec2(0,-1)}[dir]

    for i in range(num):
        move(dir)


    app.i += 1

def input(key):
    if key == 'space' or key == 'space hold':
        step_next(animate=False)

    if key == 'enter':
        for e in all_lines:
            step_next()

        print(len(visited))

    if key == 'w': step_next(override_direction='U')
    if key == 'a': step_next(override_direction='L')
    if key == 's': step_next(override_direction='D')
    if key == 'd': step_next(override_direction='R')
    # print()

app.run()
