import random
import turtle

import pygame #pip install pygame

# Initialize pygame mixer
pygame.mixer.init()

# Load the click sound
click_sound = pygame.mixer.Sound("fire.wav")

# Set up the main screen
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("DVD Loading Animation")
screen.setup(width=800, height=600)

# Create the turtle for the DVD logo
dvd_logo = turtle.Turtle()
dvd_logo.shape("square")
dvd_logo.shapesize(stretch_wid=2, stretch_len=4)
dvd_logo.penup()
dvd_logo.speed(0)

# Define the boundary for the DVD logo to bounce within
boundary_x = screen.window_width() // 2 - 40
boundary_y = screen.window_height() // 2 - 40

# Set initial movement speed
x_speed = 3
y_speed = 3

# Initialize score and click count
score = 0
click_count = 0
remaining_time = 60  # Time left in seconds for the current minute

# Create turtles to display the score, timer, and remaining time
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.color("black")
score_display.goto(0, screen.window_height() // 2 - 30)

timer_display = turtle.Turtle()
timer_display.hideturtle()
timer_display.penup()
timer_display.color("black")
timer_display.goto(0, screen.window_height() // 2 - 60)

time_display = turtle.Turtle()
time_display.hideturtle()
time_display.penup()
time_display.color("black")
time_display.goto(0, screen.window_height() // 2 - 90)


# Function to get a random color
def random_color():
    return (random.random(), random.random(), random.random())


# Function to get a random shape
def random_shape():
    return random.choice(["square", "triangle", "circle"])


# Update the displays
def update_displays():
    score_display.clear()
    score_display.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))

    timer_display.clear()
    timer_display.write(
        f"Clicks in last minute: {click_count}",
        align="center",
        font=("Arial", 24, "normal"),
    )

    time_display.clear()
    time_display.write(
        f"Time remaining: {remaining_time} s",
        align="center",
        font=("Arial", 24, "normal"),
    )


# Function to move the DVD logo
def move_logo():
    global x_speed, y_speed

    x, y = dvd_logo.position()

    # Check for collision with the boundary and bounce
    if x > boundary_x or x < -boundary_x:
        x_speed *= -1
        dvd_logo.color(random_color())  # Change to a random color on horizontal bounce
    if y > boundary_y or y < -boundary_y:
        y_speed *= -1
        dvd_logo.color(random_color())  # Change to a random color on vertical bounce

    dvd_logo.setx(x + x_speed)
    dvd_logo.sety(y + y_speed)


# Function to update the score and increase speed
def update_score(x, y):
    global score, x_speed, y_speed, click_count

    # Play click sound
    click_sound.play()

    # Increase the score and click count
    score += 1
    click_count += 1

    # Update displays
    update_displays()

    # Increase speed based on the score
    if score % 5 == 0:  # Increase speed every 5 points
        x_speed *= 1.1  # Increase speed by 10%
        y_speed *= 1.1  # Increase speed by 10%

    # Change shape randomly
    dvd_logo.shape(random_shape())


# Function to update remaining time and reset click count every minute
def update_timer():
    global remaining_time

    if remaining_time > 0:
        remaining_time -= 1
        time_display.clear()
        time_display.write(
            f"Time remaining: {remaining_time} s",
            align="center",
            font=("Arial", 24, "normal"),
        )
        screen.ontimer(update_timer, 1000)  # Schedule this function to run every second
    else:
        # When the timer reaches 0, reset the click count
        reset_click_count()


# Function to reset click count and restart timer
def reset_click_count():
    global click_count, remaining_time
    click_count = 0
    remaining_time = 60  # Reset the remaining time to 60 seconds
    update_displays()
    update_timer()  # Restart the timer


# Function to show the welcome screen
def show_welcome_screen():
    welcome_display = turtle.Turtle()
    welcome_display.hideturtle()
    welcome_display.penup()
    welcome_display.color("black")
    welcome_display.goto(0, 50)
    welcome_display.write(
        "Welcome to the DVD Game!", align="center", font=("Arial", 24, "normal")
    )

    start_button = turtle.Turtle()
    start_button.shape("square")
    start_button.shapesize(stretch_wid=2, stretch_len=4)
    start_button.color("lightgray")
    start_button.penup()
    start_button.goto(0, -50)

    def start_game(x, y):
        welcome_display.clear()
        start_button.clear()
        start_button.hideturtle()
        screen.onclick(None)  # Disable the click event for starting the game

        # Set up mouse click event to call update_score
        dvd_logo.onclick(update_score)

        # Start the timer and animation
        update_timer()
        animation_loop()

    start_button.onclick(start_game)
    screen.update()


# Function to show the developer info
def show_info():
    info_screen = turtle.Screen()
    info_screen.bgcolor("lightblue")
    info_screen.title("Developer Info")
    info_screen.setup(width=400, height=300)

    info_display = turtle.Turtle()
    info_display.hideturtle()
    info_display.penup()
    info_display.color("black")
    info_display.goto(0, 100)
    info_display.write(
        "Developer: Your Name\nContact: your.email@example.com",
        align="center",
        font=("Arial", 18, "normal"),
    )

    def close_info(x, y):
        info_screen.bye()

    close_button = turtle.Turtle()
    close_button.shape("square")
    close_button.shapesize(stretch_wid=1, stretch_len=2)
    close_button.color("lightgray")
    close_button.penup()
    close_button.goto(0, -100)
    close_button.write("Close", align="center", font=("Arial", 12, "normal"))
    close_button.onclick(close_info)

    info_screen.mainloop()


# Function to show the info button
def show_info_button():
    info_button = turtle.Turtle()
    info_button.shape("square")
    info_button.shapesize(stretch_wid=1, stretch_len=2)
    info_button.color("lightgray", "white")
    info_button.penup()
    info_button.goto(-screen.window_width() // 2 + 40, screen.window_height() // 2 - 40)
    info_button.write("Info", align="center", font=("Arial", 12, "normal"))

    def open_info(x, y):
        show_info()

    info_button.onclick(open_info)
    screen.update()


# Turn off screen updates to manually control the animation
screen.tracer(0)


# Main animation loop
def animation_loop():
    move_logo()
    screen.update()  # Update the screen manually
    screen.ontimer(animation_loop, 10)  # Call this function again after 10 ms


# Show the welcome screen and info button
show_welcome_screen()
show_info_button()

# Keep the window open
screen.mainloop()
