import pygame
import map_generator, Model, Parser

bicycle = Model.Bicycle()
parser = Parser.Info('a')


pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False
t = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))

    t_r = t % parser.get_count()
    centerLine = parser.get_centerLine(t_r)
    for i in range(len(centerLine) - 1):
        pygame.draw.line(screen, (0, 0, 0), centerLine[i], centerLine[i + 1], 1)

    carPose = parser.get_carPose(t_r)
    yaw = parser.get_yaw(t_r)
    front_axle, rear_axle = bicycle.update(carPose, yaw)
    pygame.draw.line(screen, (0, 0, 0), rear_axle, front_axle, 1)

    pygame.display.flip()
    t += 1
    pygame.time.delay(int(1000))