# War Card Game Simulation

## Overview
This project simulates the classic card game of War, where two players draw cards from their decks, and the player with the higher card wins both cards. In case of a tie (war), additional cards are drawn as stakes until one player wins. The game continues until one player wins all the cards or the game reaches a predefined condition to prevent infinite loops.

## Challenge: Infinite Game Loops
During the development and testing phase, I encountered a significant challenge with the game entering infinite loops under certain conditions. This was primarily due to the nature of the game mechanics and the random distribution of the cards. Infinite loops occurred when the sequence of wins, losses, and ties caused the game to continue without progressing towards a conclusion.

## Solution and Implementation
To address the infinite loop issue, I introduced a shuffle mechanism during "wars" where cards are drawn in case of a tie. This randomization helped in breaking potential patterns that could lead to an endless game. Additionally, I set up a limit on the number of rounds to ensure that the game would forcibly conclude if it reached an unusually high number of iterations, further preventing the possibility of an infinite loop.

## Simulations and Results
After implementing the solution, I ran multiple simulations to test the effectiveness of my approach and to gather statistics on the game's behavior. I performed 100 simulations, which provided insights into the average number of rounds and wars per game:

- **Average Rounds:** The simulations showed a wide range of outcomes, with some games concluding in fewer than 100 rounds, while others extended beyond several hundred rounds. This variability highlights the significant impact of card shuffling and the random nature of the game.
- **Average Wars:** Wars are a critical aspect of the game, representing tied rounds that require additional cards to resolve. The simulations indicated an average number of wars per game, illustrating how common ties are and their role in extending the game duration.

## Conclusion
The War Card Game Simulation project provided valuable insights into game design, probability, and the challenges of simulating traditional card games. By addressing the infinite loop challenge, I enhanced the reliability and realism of our simulation. The project underscores the importance of incorporating randomness and setting practical limits to ensure a balanced and enjoyable game experience.

## How to Run
To run the simulation, ensure you have Python installed on your system. Download the project files, navigate to the project directory in your terminal, and execute the `python3 war.py` command. Follow the prompts to start the game simulation.

## Contributions
I welcome contributions from the community. Whether you have suggestions for improving the simulation, ideas for new features, or fixes for bugs, your input is valuable. Please feel free to fork the repository, make your changes, and submit a pull request.

## Acknowledgments
Special thanks to all contributors and testers who participated in the development and refinement of this simulation. Your feedback and insights were instrumental in overcoming challenges and improving the project.
