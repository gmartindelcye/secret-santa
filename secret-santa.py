from random import shuffle

persons = ['Barney', 'Vilma', 'Fred', 'Betty', 'Pebbles', 'Bam-Bam']

def go(persons: list):
    if len(persons) < 2:
        return []

    givers = persons.copy()
    receivers = persons.copy()
    shuffle(receivers)

    gift_list = []
    for i in range(len(persons)):
        giver = givers[i]
        receiver = receivers[i]

        while receiver == giver:
            shuffle(receivers)
            receiver = receivers[i]

        gift_list.append([giver, receiver])

    return gift_list

print(go(persons))