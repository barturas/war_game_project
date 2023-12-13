def play_war(deck1, deck2):
    rounds = 0
    wars = 0
    game = True
    while deck1 and deck2 and game:
        rounds += 1
        war_cards = []

        while True:
            # Check if either player has run out of cards
            if len(deck1) == 0 or len(deck2) == 0:
                break

            card1 = deck1.pop(0)
            card2 = deck2.pop(0)
            war_cards.extend([card1, card2])
            random.shuffle(war_cards)

            if card1.rank > card2.rank:
                deck1.extend(war_cards)
                break
            elif card1.rank < card2.rank:
                deck2.extend(war_cards)
                break
            else:
                wars += 1
                # Check if either player has enough cards for another war
                if len(deck1) < 4 or len(deck2) < 4:
                    game = False
                    break  
                war_cards.extend(deck1[:3] + deck2[:3])
                random.shuffle(war_cards)
                deck1 = deck1[3:]
                deck2 = deck2[3:]
        # os.system('cls' if os.name == 'nt' else 'clear') 
        # print(f"Move: {card1} Player 1 deck: {deck1}\n")
        # print(f"Move: {card2} Player 2 deck: {deck2}\n")

    winner = "Player 1" if deck1 else "Player 2"
    return winner, rounds, wars