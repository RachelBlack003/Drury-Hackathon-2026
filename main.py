import random, math, pygame

def radians(degrees):
    """convert degrees to radians"""
    return math.pi / 180 * degrees

class Node:
    def __init__(self, x, y, speed, angle):
        """create a node"""
        self.x = x
        self.y = y
        self.speed = speed
        self.angle = angle

    def move(self):
        """move the node"""
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed

    def draw(self):
        """draw the node to the screen"""
        pygame.draw.circle(
            screen, (100, 200, 200), (int(self.x), int(self.y)), node_radius
        )

    def reflect(self):
        """reflect off a boundary of the screen"""
        if self.x > winwidth - node_radius:  # right edge
            self.x = 2 * (winwidth - node_radius) - self.x
            self.angle = -self.angle
        elif self.x < node_radius:  # left edge
            self.x = 2 * node_radius - self.x
            self.angle = -self.angle
        if self.y > winheight - node_radius:  # bottom edge
            self.y = 2 * (winheight - node_radius) - self.y
            self.angle = math.pi - self.angle
        elif self.y < node_radius:  # top edge
            self.y = 2 * node_radius - self.y
            self.angle = math.pi - self.angle

# window details
winwidth = 600  # width of window
winheight = 400  # height of window
background = (5, 5, 5)  # black

# set up node(s)
node_radius = 100
num_nodes = 1

# initialize pygame
screen = pygame.display.set_mode((winwidth, winheight))
clock = pygame.time.Clock()
pygame.init()

# create node(s)
nodes = []
for i in range(num_nodes):
    speed = 1.5
    angle = 45
    nodes.append(Node(winwidth // 2, winheight // 2, speed, angle))

# the game loop: (press q to quit)
quit_ = False
while not quit_:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_ = True
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                quit_ = True
                break
    if quit_:
        break

    screen.fill(background)

    # update the nodes
    for node in nodes:
        node.move()
        node.reflect()
        node.draw()

    clock.tick(60)
    pygame.display.flip()

pygame.quit()