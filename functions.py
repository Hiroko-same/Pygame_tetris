# -*- coding: utf-8 -*-
import pygame
import random
import ingredents

# -- Initialize Tetromino position and selection --
# Randomly spawn a new Tetromino.

def new_block(cols):      
    t = random.choice(list(ingredents.shapes.keys()))
    return {
        'type': t,
        'shape': ingredents.shapes[t],
        'x': cols // 2 - 2,
        'y': 0
    }


# -- Function to draw the grid (lines of the field) --
# Draw rectangles of the specified cell size at the intersection of rows and columns.

def draw_grid(screen, cols, rows, cell_size, GRAY):
    for y in range(rows):
        for x in range(cols):
            rect = pygame.Rect(x * cell_size, y * cell_size,
cell_size, cell_size)
            pygame.draw.rect(screen, GRAY, rect, 1) 


# -- Draw the current block --
# Calculate the current position of current_block using dx and dy (because the block keeps moving).

def draw_block(current_block, screen, cols, rows, cell_size, CYAN):   
    for dx, dy in current_block['shape']: 
        x = current_block['x'] + dx  
        y = current_block['y'] + dy
        if 0 <= x < cols and 0 <= y < rows:
            rect = pygame.Rect(x * cell_size, y * cell_size, cell_size,
cell_size)
        pygame.draw.rect(screen, CYAN, rect)


# -- Draw the field (grounded blocks) --
# For each cell that is non-zero, draw a rectangle in that position.
# Fill the block with CYAN color.

def draw_field(rows, cols, cell_size, CYAN, field, screen):      
    for y in range(rows):
        for x in range(cols):
            if field[y][x]: 
                rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, 
cell_size)
                pygame.draw.rect(screen, CYAN, rect)


# -- Check if the block can move --
# Calculate the new position (px, py) of the block after moving to (dx, dy).
# If False is returned, the can_move() function stops.

def can_move(current_block, dx, dy, cols, rows, field):  
    for px, py in current_block['shape']:
        x = current_block['x'] + px + dx     
        y = current_block['y'] + py + dy
        if x < 0 or x >= cols or y >= rows: 
            return False
        if y >= 0 and field[y][x]: 
            return False
    return True


# -- Function for rotation --
# The O-shaped Tetromino does not rotate.
# Rotate the block 90° clockwise.
# Adjust the x-position by ±1 to prevent wall collision.

def rotate(current_block):
    if current_block['type'] == 'O':
        return current_block['shape']
    return [(-py, px) for px, py in current_block['shape']]


# -- Lock the block on the field --
# If the block’s position is within the game field, fill that cell with 1.
# This makes the block become part of the grounded field.

def lock_block(current_block, cols, rows, field):
    for dx, dy in current_block['shape']:  
        x = current_block['x'] + dx
        y = current_block['y'] + dy
        if 0 <= x < cols and 0 <= y < rows:
            field[y][x] = 1


# -- Erase completed lines --
# For each row:
#   If any cell is 0, keep the row as is.
# Otherwise, it’s considered a completed line.

def clear_lines(field, score, cols, rows):     
    new_field = [row for row in field if any(cell == 0 
for cell in row)]
    lines_cleared = rows - len(new_field)
    score += lines_cleared * 100
    for _ in range(lines_cleared):
        new_field.insert(0, [0] * cols)
    return new_field, score


# -- Game over condition --
# Check the top row (field[0][x]).
# If any of the 10 cells in the top row are non-zero, return a Game Over state.

def is_game_over(field, cols):
    return any(field[0][x] != 0 for x in range(cols))


# -- Display the next block text --

def draw_next_block(block, font, screen, WIDTH, WHITE,cell_size, CYAN):
    next_text = font.render("NEXT", True, WHITE)
    screen.blit(next_text, (WIDTH + 20, 20))
    for dx, dy in block['shape']:
        x = WIDTH + 40 + dx * cell_size
        y = 60 + dy * cell_size
        rect = pygame.Rect(x, y, cell_size, cell_size)
        pygame.draw.rect(screen, CYAN, rect)
