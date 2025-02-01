import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman!!!!")

FONT = pygame.font.Font(None, 50)

words = ["apple", "banana", "orange", "time", "way", "year", "work", "government", "day", "man",
         "world", "life", "part", "house", "course", "case", "system", "place", "end", "group",
         "company", "party", "information", "school", "fact", "money", "point", "example", "state",
         "business", "night", "area", "water", "thing", "family", "head", "hand", "order", "side",
         "home", "development", "week", "power", "country", "council", "use", "service", "room",
         "market", "problem", "court", "police", "interest", "car", "law", "road", "form", "face",
         "education", "policy", "research"]

word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6

def draw_hangman(attempts):
    if attempts <= 5:  # Head
        pygame.draw.circle(screen, BLACK, (400, 200), 40, 3)
    if attempts <= 4:  # Body
        pygame.draw.line(screen, BLACK, (400, 240), (400, 350), 3)
    if attempts <= 3:  # Left Arm
        pygame.draw.line(screen, BLACK, (400, 270), (350, 320), 3)
    if attempts <= 2:  # Right Arm
        pygame.draw.line(screen, BLACK, (400, 270), (450, 320), 3)
    if attempts <= 1:  # Left Leg
        pygame.draw.line(screen, BLACK, (400, 350), (350, 420), 3)
    if attempts == 0:  # Right Leg
        pygame.draw.line(screen, BLACK, (400, 350), (450, 420), 3)

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            guess = event.unicode.lower()
            if guess.isalpha():
                if guess in word:
                    for i, letter in enumerate(word):
                        if letter == guess:
                            guessed[i] = guess
                else:
                    attempts -= 1

    text = FONT.render(" ".join(guessed), True, BLACK)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 100))

    if "_" not in guessed:
        text = FONT.render(f"You Won! Word: {word}", True, BLACK)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 300))
        pygame.display.flip()
        pygame.time.delay(3000)
        running = False

    elif attempts == 0:
        text = FONT.render(f"You Lost! Word: {word}", True, BLACK)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 300))
        pygame.display.flip()
        pygame.time.delay(3000)
        running = False

    draw_hangman(attempts)
    pygame.display.flip()
