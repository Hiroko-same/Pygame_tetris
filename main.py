# -*- coding:utf-8 -*-

# -- Random movement in Tetris game --
# Use the Pygame library system.
# Use my custom modules.
# Initialize Pygame.

import pygame
import sys
import random 

import ingredents
import functions

pygame.init()

# -- Grid setup --

cols = 10     
rows = 20       
cell_size = 30  

WIDTH = cols * cell_size
HEIGHT = rows * cell_size
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)

# -- Window creation --
# Create a margin on the right side of the Tetris screen.

SIDE_WIDTH = 150 
screen = pygame.display.set_mode((WIDTH + SIDE_WIDTH, HEIGHT))
pygame.display.set_caption("TetriS")

font = pygame.font.SysFont(None, 36)

# -- Initial block position --

block_x = 4   
block_y = 0     

# -- Time management & game variables --
# Use a loop function to simulate time progression.

clock = pygame.time.Clock()
fall_speed = 500    
last_fall_time = pygame.time.get_ticks()
score = 0
game_over = False

# -- Field (ground: 0 = empty) --
# Create 10 columns filled with 0, repeated for 20 rows.
# Fill the entire field with 0 to represent empty space.

field = [[0 for _ in range(cols)] for _ in range(rows)] 

current_block = functions.new_block(cols)
next_block = functions.new_block(cols)
shape = current_block['shape']

# -- Main loop --
# Call can_move() with current_block['x'], current_block['y'], and new_shape.
# If rotation is triggered, keep the position fixed (dx = 0, dy = 0) and rotate current_block by 90Åã using rotate().
# Then assign the rotated new_shape to current_block['shape'].
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_LEFT and functions.can_move(current_block, -1, 0, cols, rows, field):
                current_block['x'] -= 1        
            elif event.key == pygame.K_RIGHT and functions.can_move(current_block, 1, 0, cols, rows, field):
                current_block['x'] += 1
            elif event.key == pygame.K_DOWN and functions.can_move(current_block, 0, 1, cols, rows, field):
                current_block['y'] += 1
            elif event.key == pygame.K_r:
                new_shape = functions.rotate(current_block)
                if functions.can_move({'x':current_block['x'], 'y':current_block['y'], 'shape': new_shape}, 0, 0, cols, rows, field):
                    current_block['shape'] = new_shape

# -- When the game is not over --
# Enable automatic falling of blocks.
# Assign current_time to the current game time in milliseconds (using tick()).

    if not game_over:
        current_time = pygame.time.get_ticks()
        if current_time - last_fall_time > fall_speed:
            if functions.can_move(current_block, 0, 1, cols, rows, field):
                current_block['y'] += 1
                score += 1    
            else:
                functions.lock_block(current_block, cols, rows, field)
                field, score = functions.clear_lines(field, score, cols, rows)
                if functions.is_game_over(field, cols):
                    game_over = True
                else:
                    current_block = next_block
                    next_block = functions.new_block(cols)
            last_fall_time = current_time

# -- During the game (main display loop) --
# If the game is not over, call draw_block(current_block) to display the current falling block.
# Use an f-string (f"{variable}") to embed Python expressions directly in strings.
# Show the NEXT block beside the main field by calling draw_next_block().   
    screen.fill(BLACK) 
    functions.draw_grid(screen, cols, rows, cell_size, GRAY)    
    functions.draw_field(rows, cols, cell_size, CYAN, field, screen)
    if not game_over:
        functions.draw_block(current_block, screen, cols, rows, cell_size, CYAN)

    score_text = font.render(f"Score:{score}", True, WHITE)
    screen.blit(score_text, (WIDTH + 20, HEIGHT - 50))

    functions.draw_next_block(next_block, font, screen, WIDTH, WHITE,cell_size, CYAN)

# -- Game Over display --
# When the game is over, display the text: ÅgGAME OVERÅh in white.

    if game_over:
        over_text = font.render("Game Over", True, WHITE)
        screen.blit(over_text, (WIDTH // 2 - 80, HEIGHT // 2 -20))

# -- Screen update during the game --
# Use pygame.display.flip() to refresh the entire screen created by pygame.display.set_mode().
# Limit the screen refresh rate to a maximum of 60 frames per second.

    pygame.display.flip()  

    clock.tick(60)    