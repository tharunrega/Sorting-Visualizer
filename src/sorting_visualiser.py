"""
Sorting Visualiser

This project was created and implemented solely by Tharun rega.
"""
import pygame
import random

# Initialize Pygame
pygame.init()
pygame.font.init()
pygame.display.set_caption('Sorting Visualiser')

# Constants
ARRAY_SIZES = [15, 25, 50, 125, 200, 250, 500, 1000]
ARRAY_SIZE_INDEX = 2
ARRAY_SIZE = ARRAY_SIZES[ARRAY_SIZE_INDEX]
MS_DELAY = 1
WIDTH = 1000
HEIGHT = 800
MIN_VAL = 10
MAX_VAL = 450
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.SysFont('Arial', 15)
USAGE_TEXT = [
    "Usage:",
    "[g] generate new array",
    "[b] bubble sort",
    "[i] insertion sort",
    "[s] selection sort",
    "[m] merge sort",
    "[q] quick sort",
    f"[up][down] delay: {MS_DELAY}",
    f"[<][>] Size: {ARRAY_SIZE}"
]


def render_multiline_text(text_list, font, color, x, y, line_spacing=5):
    """Render multiple lines of text."""
    for line in text_list:
        line_surface = font.render(line, True, color)
        SCREEN.blit(line_surface, (x, y))
        y += line_surface.get_height() + line_spacing  # Move down for the next line


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


def check_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


def generate_array(min, max, size):
    return [random.randint(min, max) for _ in range(size)]


def draw_array(arr, sort_position=None, selection_sort_swap_position=None, pivot_position=None):
    SCREEN.fill(BLACK)
    bar_width = WIDTH // ARRAY_SIZE

    for count, height in enumerate(arr):
        if count == sort_position:
            color = RED
        elif count == selection_sort_swap_position:
            color = GREEN
        elif count == pivot_position:
            color = BLUE
        else:
            color = WHITE
        pygame.draw.rect(SCREEN, color, (count * bar_width, HEIGHT - height, bar_width, height))
    render_multiline_text(USAGE_TEXT, FONT, WHITE, 15, 15)
    pygame.display.flip()


def bubble_sort(arr):
    for pass_num in range(len(arr) - 1):
        for i in range(len(arr) - 1 - pass_num):
            if arr[i + 1] < arr[i]:
                arr[i + 1], arr[i] = arr[i], arr[i + 1]
            check_quit()
            draw_array(arr, i+1)
            pygame.time.delay(MS_DELAY)


def insertion_sort(arr):
    n = len(arr)  # Get the length of the list A
    for nn in range(1, n):  # Loop over array starting at second element
        ii = nn  # Begin the check at the current index
        while ii > 0 and arr[ii - 1] > arr[ii]:
            # The inner loop starts from the current element nn and moves backwards
            # The condition ii > 0 and A[ii - 1] > A[ii] ensures that the loop continues as long as the current
            # element is smaller than the previous element, indicating that the elements are out of order and
            # need to be swapped.

            arr[ii], arr[ii - 1] = arr[ii - 1], arr[ii]
            ii = ii - 1
            check_quit()
            draw_array(arr, ii)
            pygame.time.delay(MS_DELAY)


def selection_sort(arr):  # This sort uses tuples and a pythonic approach to swap the elements
    n = len(arr)  # Get the length of the list A
    for nn in range(n - 1):  # Loop over the array except for the last element
        min = nn  # Assume the current index nn is the smallest
        for jj in range(nn + 1, n):  # Loop through the remaining elements
            if arr[jj] < arr[min]:  # If a smaller element is found
                min = jj  # Update the index of the smallest element
            check_quit()
            draw_array(arr, jj, nn)
            pygame.time.delay(MS_DELAY)
        # Swap the found minimum element with the element at the current position nn
        arr[min], arr[nn] = arr[nn], arr[min]


def merge_sort(arr):
    merge_sort_recurse(arr, 0, len(arr) - 1)


def merge_sort_recurse(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort_recurse(arr, left, mid)
        merge_sort_recurse(arr, mid + 1, right)
        merge(arr, left, mid, right)


def merge(arr, left, mid, right):
    # Create temporary arrays
    left_arr = arr[left:mid + 1]
    right_arr = arr[mid + 1:right + 1]

    i = j = 0  # Initial indexes for left and right arrays
    k = left  # Initial index for merged array

    # Merge the temp arrays back into arr[left..right]
    while i < len(left_arr) and j < len(right_arr):
        check_quit()
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        draw_array(arr, k)  # Visualize the current step
        pygame.time.delay(MS_DELAY)
        k += 1

    # Copy remaining elements of left_arr if any
    while i < len(left_arr):
        check_quit()
        arr[k] = left_arr[i]
        draw_array(arr, k)  # Visualize the current step
        pygame.time.delay(MS_DELAY)
        i += 1
        k += 1

    # Copy remaining elements of right_arr if any
    while j < len(right_arr):
        check_quit()
        arr[k] = right_arr[j]
        draw_array(arr, k)  # Visualize the current step
        pygame.time.delay(MS_DELAY)
        j += 1
        k += 1


def quick_sort(arr):
    quickSortRecurse(arr, 0, len(arr) - 1)


def quickSortRecurse(arr, left_index, right_index):
    if (right_index > left_index):
        pivotindex = (left_index + right_index) // 2
        newPivotindex = doPartitioning(arr, left_index, right_index, pivotindex)

        quickSortRecurse(arr, left_index, newPivotindex - 1)
        quickSortRecurse(arr, newPivotindex + 1, right_index)


def doPartitioning(arr, left_index, right_index, pivot_index):
    pivotVal = arr[pivot_index]
    arr[pivot_index] = arr[right_index]
    arr[right_index] = pivotVal

    curr_index = left_index
    for ii in range(left_index, right_index + 1):
        check_quit()
        # Visualize current comparison
        draw_array(arr, ii, left_index, right_index)
        pygame.time.delay(MS_DELAY)
        if arr[ii] < pivotVal:
            arr[ii], arr[curr_index] = arr[curr_index], arr[ii]
            curr_index += 1

    new_pivot_index = curr_index
    arr[right_index] = arr[new_pivot_index]
    arr[new_pivot_index] = pivotVal
    return new_pivot_index


array = generate_array(MIN_VAL, MAX_VAL, ARRAY_SIZE)
running = True
while running:
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            running = False
        if keys[pygame.K_g]:
            array = generate_array(MIN_VAL, MAX_VAL, ARRAY_SIZE)
        elif keys[pygame.K_b]:
            bubble_sort(array)
        elif keys[pygame.K_i]:
            insertion_sort(array)
        elif keys[pygame.K_s]:
            selection_sort(array)
        elif keys[pygame.K_m]:
            merge_sort(array)
        elif keys[pygame.K_q]:
            quick_sort(array)
        elif keys[pygame.K_UP]:
            MS_DELAY += 1
            USAGE_TEXT[7] = f"[up][down] delay: {MS_DELAY}"

        elif keys[pygame.K_DOWN]:
            if MS_DELAY > 1:
                MS_DELAY -= 1
                USAGE_TEXT[7] = f"[up][down] delay: {MS_DELAY}"

        elif keys[pygame.K_RIGHT]:
            if ARRAY_SIZE_INDEX < len(ARRAY_SIZES) - 1:
                ARRAY_SIZE_INDEX += 1
                ARRAY_SIZE = ARRAY_SIZES[ARRAY_SIZE_INDEX]
                USAGE_TEXT[8] = f"[<][>] Size: {ARRAY_SIZE}"
                array = generate_array(MIN_VAL, MAX_VAL, ARRAY_SIZE)

        elif keys[pygame.K_LEFT]:
            if ARRAY_SIZE_INDEX > 0:
                ARRAY_SIZE_INDEX -= 1
                ARRAY_SIZE = ARRAY_SIZES[ARRAY_SIZE_INDEX]
                USAGE_TEXT[8] = f"[<][>] Size: {ARRAY_SIZE}"
                array = generate_array(MIN_VAL, MAX_VAL, ARRAY_SIZE)
    draw_array(array)
