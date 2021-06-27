def find_winner(**kwargs):
    return max(kwargs, key=kwargs.get)

print(find_winner(Andy=17, Marry=19, Sim=45, Kae=34))