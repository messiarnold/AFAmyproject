import random 
for i in range(1):
    list_1 = ["חגי","אוריה","אביגיל","אבישי","גבריאל","יעל ד","יעל ש","ירדני","שוויקה","מנחנח","מעיין","ענאל","שמואל אלמליח","אריאל","ידידיה",""]
    list_2 = ["מיכל זילבן","איילת וולף","שמואל קויפמן","תהל","אילת","מאיר","מורדי","אפרת","רועי",""]
    while list_2 != []:
        for n in range(2):
            list_1_choice = random.choice(list_1)
            list_1.pop(list_1.index(list_1_choice))
            print(list_1_choice,end=' ')
        for i in range(2):
            list_2_choice = random.choice(list_2)
            list_2.pop(list_2.index(list_2_choice))
            print(list_2_choice,end=' ')
        print()
    print()
print("\n\n")
print(list_1)