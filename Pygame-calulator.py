import pygame

# Set up Pygame
pygame.init()

# Set the window size and title
screen = pygame.display.set_mode((400, 680))
pygame.display.set_caption("Calculator")

# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the display area
display_font = pygame.font.Font(None, 36)
display_text = display_font.render("0", 1, WHITE)
display_rect = display_text.get_rect()
display_rect.center = (200, 50)

# Create the buttons
button_font = pygame.font.Font(None, 36)
buttons = []
for i in range(10):
    button_text = button_font.render(str(i), 1, WHITE)
    button_rect = button_text.get_rect()
    button_rect.center = (50 + (i % 3) * 100, 100 + (i // 3) * 100)
    buttons.append(("digit", button_text, button_rect, str(i)))
operations = ["+", "-", "*", "/", "=", "C"]
for i, operation in enumerate(operations):
    button_text = button_font.render(operation, 1, WHITE)
    button_rect = button_text.get_rect()
    button_rect.center = (350, 100 + i * 100)
    buttons.append(("operation", button_text, button_rect, operation))

# Create a list to store the numbers and operations
calculation = []

# Run the Pygame loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if a button was clicked
            for button_type, button_text, button_rect, button_label in buttons:
                if button_rect.collidepoint(event.pos):
                    # Handle the button click
                    if button_type == "digit":
                        # Update the display with the digit
                        display_text = display_font.render(button_label, 1, WHITE)
                        display_rect = display_text.get_rect()
                        display_rect.center = (200, 50)
                        calculation.append(int(button_label))
                    elif button_type == "operation":
                        if button_label == "=":
                            # Evaluate the calculation
                            result = 0
                            operation = None
                            for item in calculation:
                                if isinstance(item, int):
                                    if operation is None:
                                        result = item
                                    elif operation == "+":
                                        result += item
                                    elif operation == "-":
                                        result -= item
                                    elif operation == "*":
                                        result *= item
                                    elif operation == "/":
                                        result /= item
                                else:
                                    operation = item
                            # Update the display
                            display_text = display_font.render(str(result), 1, WHITE)
                            display_rect = display_text.get_rect()
                            display_rect.center = (200, 50)
                            calculation.clear()
                        elif button_label == "C":
                            # Clear the calculation
                            calculation.clear()
                            display_text = display_font.render("0", 1, WHITE)
                            display_rect = display_text.get_rect()
                            display_rect.center = (200, 50)
                        else:
                            # Update the display with the operation
                            calculation.append(button_label)
                            display_text = display_font.render("".join(map(str, calculation)), 1, WHITE)
                            display_rect = display_text.get_rect()
                            display_rect.center = (200, 50)
    
    # Draw the calculator to the screen
    screen.fill(BLACK)
    screen.blit(display_text, display_rect)
    for _, button_text, button_rect, _ in buttons:
        screen.blit(button_text, button_rect)
    pygame.display.flip()

# Quit Pygame
pygame.quit()
