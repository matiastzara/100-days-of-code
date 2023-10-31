lottery_numbers = {13, 21, 22, 5, 8}

players = [
    {
        'name': 'Matías', 
        'numbers': {1, 2, 3, 4, 5}
     }, 
    {
        'name': 'Amandine',
        'numbers': {13, 11, 5, 25, 8}
        }
    ]

matias = len(players[0]['numbers'].intersection(lottery_numbers))
amandine = len(players[1]['numbers'].intersection(lottery_numbers))

print(f"Player Matías got {matias} numbers right.")
print(f"Player Amandine got {amandine} numbers right.")