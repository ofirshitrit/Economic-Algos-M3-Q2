def weighted_round_rubin(rights, valuations, y):
    num_players = len(rights)
    num_objects = len(valuations[0])
    remaining_objects = set(range(num_objects))

    print(f"Remaining objects: {remaining_objects}")  # TODO - delete
    print(f"Valuations: {valuations}")  # TODO - delete
    print(
        "##############################################################################################")  # TODO - delete

    # List of how much objects each player took - at the beginning every player get 0
    players_chosen_objects = [0 for _ in range(num_players)]

    while remaining_objects:
        max_portion = 0
        choosing_player = None
        chosen_object = None
        max_value = float('-inf')

        for player in range(num_players):
            # Computing the portion for each player
            portion = rights[player] / (players_chosen_objects[player] + y)
            print(f"player {player} with portion: {portion}")  # TODO - delete

            # Find the player with the highest portion
            if portion > max_portion:
                max_portion = portion
                choosing_player = player

        # The player with the highest portion choose from the remaining objects the object that he wants the most
        for i, value in enumerate(valuations[choosing_player]):
            if value > max_value:
                max_value = value
                chosen_object = i

        players_chosen_objects[choosing_player] += 1
        remaining_objects.remove(chosen_object)
        print(f"Remaining objects: {remaining_objects}")  # TODO - delete

        print(
            f"Player {choosing_player} takes item {chosen_object} with value {valuations[choosing_player][chosen_object]}")

        # Remove the chosen value at the chosen_object index from each player's valuation
        for player in range(num_players):
            valuations[player][chosen_object] = 0
        print(f"Valuations: {valuations}")  # TODO - delete
        print(f"players chosen objects: {players_chosen_objects} ")  # TODO - delete
        print(
            "##############################################################################################")  # TODO - delete


# Test cases
if __name__ == "__main__":
    # Test case
    # weighted_round_rubin([1, 2, 4], [[11, 11, 22, 33, 44], [11, 22, 44, 55, 66], [11, 33, 22, 11, 66]], 0.5)

    # Additional test cases
    # A. Identical objects with equal rights
    # weighted_round_rubin([1, 1, 1], [[10, 10, 10], [10, 10, 10], [10, 10, 10]], 1)
    #
    # # B. Same objects with different rights
    weighted_round_rubin([1, 2, 3], [[10, 10, 10, 10, 10], [10, 10, 10, 10, 10], [10, 10, 10, 10, 10]], 0.5)
    #
    # # C. Different objects with different rights
    # weighted_round_rubin([1, 3, 2], [[5, 10, 15], [20, 15, 10], [10, 5, 20]], 0.5)
