import random
import logging
import sys

# Configure logging
logging.basicConfig(level=logging.INFO, stream=sys.stdout, format='%(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)

# Comment this line to see prints of the logger
logger.setLevel(logging.WARNING)

"""
The Weights Round Rubin Algorithm:
1. initialize: every player gets 0
2. while there are still objects:
    - for every player compute: his right / his current number of objects + y  
    - the player that his portion is the highest gets to choose his favorite object
"""


def get_choosing_player(num_players, players_chosen_objects, rights, y):
    max_portion = 0
    choosing_player = None

    # Computing the portion for each player
    for player in range(num_players):
        portion = rights[player] / (players_chosen_objects[player] + y)
        logger.info(f"Player {player} with portion: {portion}")

        # Find the player with the highest portion
        if portion > max_portion:
            max_portion = portion
            choosing_player = player

    return choosing_player


def get_chosen_object(valuations, choosing_player):
    # The player with the highest portion choose from the remaining objects the object that he wants the most
    max_value = float('-inf')
    chosen_object = None
    for i, value in enumerate(valuations[choosing_player]):
        if value > max_value:
            max_value = value
            chosen_object = i
    return chosen_object


def weighted_round_rubin(rights, valuations, y):
    num_players = len(rights)
    num_objects = len(valuations[0])
    remaining_objects = set(range(num_objects))

    logger.info(f"Remaining objects: {remaining_objects}")
    logger.info(f"Valuations: {valuations}")

    # List of how much objects each player took - at the beginning every player get 0
    players_chosen_objects = [0 for _ in range(num_players)]

    while remaining_objects:

        # Get the player with the highest portion to choose his favorite object
        choosing_player = get_choosing_player(num_players, players_chosen_objects, rights, y)

        # Get the favorite object of the player with the highest portion
        chosen_object = get_chosen_object(valuations, choosing_player)

        # Update the player's number of objects
        players_chosen_objects[choosing_player] += 1

        # Remove the chosen object
        remaining_objects.remove(chosen_object)
        logger.info(f"Remaining objects: {remaining_objects}")

        print(
            f"Player {choosing_player} takes item {chosen_object} with value {valuations[choosing_player][chosen_object]}",
            flush=True)

        # Remove the chosen value at the chosen_object index from each player's valuation
        for player in range(num_players):
            valuations[player][chosen_object] = 0

        logger.info(f"Valuations: {valuations}")
        logger.info(f"Players chosen objects: {players_chosen_objects}")

    print("\n")


# Test cases
if __name__ == "__main__":
    """
    1. Different objects with different rights
    Inputs: 
        rights = [1, 2, 4]
        valuations = [[11, 11, 22, 33, 44], [11, 22, 44, 55, 66], [11, 33, 22, 11, 66]]
        y = 0.5
    Expected Output:     
        - Player 0 takes item 2
        - Player 1 takes item 3
        - Player 2 takes items 0,1,4
    """
    print("Different objects with different rights: ", flush=True)
    weighted_round_rubin([1, 2, 4], [[11, 11, 22, 33, 44], [11, 22, 44, 55, 66], [11, 33, 22, 11, 66]], 0.5)

    """
    2. Same objects with equal rights
    Inputs: 
        rights = [1, 1, 1]
        valuations = [[10, 10, 10], [10, 10, 10], [10, 10, 10]]
        y = 1
    Expected Output:     
         - Player 0 takes item 0
         - Player 1 takes item 1
         - Player 2 takes item 2    
    """
    print("Same objects with equal rights: ", flush=True)
    weighted_round_rubin([1, 1, 1], [[10, 10, 10], [10, 10, 10], [10, 10, 10]], 1)

    """
    3. Same objects with different rights
    Inputs: 
        rights = [[1, 2, 3]]
        valuations = [[10, 10, 10, 10, 10], [10, 10, 10, 10, 10], [10, 10, 10, 10, 10]]
        y = 0.5
    Expected Output:     
         - Player 0 takes item 2
         - Player 1 takes items 1,4
         - Player 2 takes items 0,3 
    """
    print("Same objects with different rights: ", flush=True)
    weighted_round_rubin([1, 2, 3], [[10, 10, 10, 10, 10], [10, 10, 10, 10, 10], [10, 10, 10, 10, 10]], 0.5)

    """
    4. Same objects with different rights - floats
    """
    print("Same objects with different rights: floats", flush=True)
    weighted_round_rubin([1.5, 1.5, 4], [[11.1, 11.1, 22, 33.5], [11.5, 22, 44, 55], [11.6, 33, 22.6, 11]], 0.2)

    """
    5. Same objects with different rights - Random numbers
    """
    random_rights = [random.uniform(1.0, 10.0) for _ in range(4)]
    print(f"Random rights: {random_rights} ", flush=True)
    random_valuations = [[random.uniform(1.0, 50.0) for _ in range(3)] for _ in range(4)]
    print(f"Random valuations: {random_valuations}", flush=True)
    random_y = random.uniform(0.0, 1.0)
    print(f"Random y: {random_y} ", flush=True)

    print("Same objects with different rights - Random numbers", flush=True)
    weighted_round_rubin(random_rights, random_valuations, random_y)
