import pygame
from sys import exit
from random import randint

# import time
# import numpy as np

# Choose Algorithm
algoNum = -1

while algoNum < 1 or algoNum > 3:
    print("Enter 1 for bubble sort")
    print("Enter 2 for selection sort")
    print("Enter 3 for insertion sort")
    algoNum = int(input("Enter your value: "))

# Display Setup
WIDTH = 900
HEIGHT = 600
FRAME_RATE = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Visualizer")
clock = pygame.time.Clock()

# Game Setup
nums = [randint(0, HEIGHT) for _ in range(WIDTH)]
# nums = np.random.randint(0, HEIGHT, WIDTH)
i, j = 0, 0
if algoNum == 3:
    i = 1
run_display = True
run_sort = True
algoDuration = -1
begin_time = pygame.time.get_ticks()
while run_display:
    # Clock Speed
    clock.tick(FRAME_RATE)

    # Algorithms
    if algoNum == 1 and run_sort:  # BUBBLE SORT
        if i < len(nums):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]  # swap elements
            i += 1
        else:
            algo_duration = pygame.time.get_ticks() - begin_time
            print(f"\nTime taken to complete sort: {algo_duration / 1000} seconds")
            run_sort = False
    elif algoNum == 2 and run_sort:  # SELECTION SORT
        if i < len(nums):
            select_val = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[select_val]:
                    select_val = j
            nums[i], nums[select_val] = nums[select_val], nums[i]
            i += 1
        else:
            algo_duration = pygame.time.get_ticks() - begin_time
            print(f"\nSorting finished in {algo_duration / 1000} seconds")
            run_sort = False
    elif algoNum == 3 and run_sort:  # INSERTION SORT
        if i < len(nums):
            insert_val = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > insert_val:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = insert_val
            i += 1
        else:
            algo_duration = pygame.time.get_ticks() - begin_time
            print(f"\nSorting finished in {algo_duration / 1000} seconds")
            run_sort = False

    # handle exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_display = False

    # show background and bars
    screen.fill(BLACK)
    for n in range(len(nums)):
        pygame.draw.line(screen, WHITE, (n, HEIGHT), (n, HEIGHT - nums[n]))
    pygame.display.flip()  # update display

pygame.quit()
exit()
