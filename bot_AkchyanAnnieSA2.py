def choice(round_score, my_score, opponent_score):
    if my_score + round_score <=  opponent_score:
        return True
    elif my_score + round_score >= opponent_score or opponent_score - 7 == my_score:
        return False
