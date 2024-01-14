import pygame
import sys
import math

# Pygame initialization
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RADIUS = 5

# Initial positions
H = 200
X = 800
x, y = WIDTH // 2, HEIGHT // 2
L1 = 150
L2 = 150

# Pygame window setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Simulation")


# Function to draw points and lines
def draw_objects():
    screen.fill(WHITE)
    pygame.draw.circle(screen, BLACK, (0, H), RADIUS)  # M1
    pygame.draw.circle(screen, BLACK, (X, H), RADIUS)  # M2
    pygame.draw.line(screen, BLACK, (0, H), (X, H), 2)  # Horizontal line (M1 to M2)
    pygame.draw.circle(screen, BLACK, (int(x), int(y)), RADIUS)  # P
    pygame.draw.line(screen, BLACK, (0, H), (x, y), 2)  # L1
    pygame.draw.line(screen, BLACK, (X, H), (x, y), 2)  # L2

    # Display lengths
    font = pygame.font.Font(None, 36)
    text_l1 = font.render(f"L1: {L1:.2f}", True, BLACK)
    text_l2 = font.render(f"L2: {L2:.2f}", True, BLACK)
    screen.blit(text_l1, (10, 10))
    screen.blit(text_l2, (X - 100, 10))


# Main game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    # Update P position based on arrow key controls
    if keys[pygame.K_LEFT]:
        x -= 5
    if keys[pygame.K_RIGHT]:
        x += 5
    if keys[pygame.K_UP]:
        y -= 5
    if keys[pygame.K_DOWN]:
        y += 5

    # Recalculate lengths
    L1 = math.sqrt((x - 0) ** 2 + (y - H) ** 2)
    L2 = math.sqrt((x - X) ** 2 + (y - H) ** 2)

    print(f"Point P coordinates: ({x:.2f}, {y:.2f})")

    # Draw objects
    draw_objects()

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)
