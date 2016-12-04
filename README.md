# SI 206 Project 4 "Shoot the Fruit!"

The project I have created is a simple vertical shooter game created with Pygame.

Please make sure you have installed Pygame and any missing dependencies.

Objective: Monkey has to collect falling fruit by shooting with space bar and dodge fruit by navigating on horizontal plane using left and right arrow keys. Game will quit when monkey runs out of lives.

Features:
- Class inheritance of Player 1, Fruit, and Bullet from sprite class
- Horizontal player movement constrained to screen width
- Collision detection using Circular Bounding Box
- Observable score using draw module. Score accumulating by 10 for each time Player1 hits mob
- Sound effects as mixers used to denote sprite collisions
- Background music played on inifinite loop while game is running

Extras:
- Key module used
- Game over screen when player runs out of lives
- Random range for speed of mob class

I used the following resources:
- Pygame v1.9.2 documentation (http://www.pygame.org/docs/) for draw, joystick, key, mixer, music, Rect, sprite, and surface modules
- Kids Can Code (https://www.youtube.com/watch?v=vvgWfNLgK9c) to create a bar representing the number of available lives
- OpenGameArt (http://opengameart.org/) for player and mob animation
- Discovery Playground (http://www.discoveryplayground.com/computer-programming-for-kids/rgb-colors/) for RGB background color
- Payne, B. (2015). Teach your kids to code: A parent-friendly guide to Python programming. San Francisco: No Starch Press.

