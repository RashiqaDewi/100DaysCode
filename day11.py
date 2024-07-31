# bisa draw
import random
cards = { "AS" :1,
    "AS": 11,
    "jack": 10,
    "queen": 10,
    "king": 10,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10
}

"""fungsi untuk menghitung score"""

def calculate_score(x):
    score = 0
    for kartu in x:
        score += cards[kartu] 
    return score


while True :
    ask = str(input("Do you want to play blackjack? y/n"))
    if ask == "y" :
        list_card = list(cards.keys())
        kartu_user =  random.sample(list_card,2)
        kartu_comp = random.sample(list_card,1)
        print(f"kartu computer : {kartu_comp}\nkartu user :{kartu_user}")
        if "AS" in kartu_user :
            ask_value = int(input("You got ACE in your cards, which value you want it to be? 11/1?"))
            if ask_value == 1 :
                cards["AS"] = 1  # Mengubah nilai AS menjadi 1
                list_card2 = list(cards.keys())
            elif ask_value == 11 :
                list_card = list(cards.keys())
            else :
                print("hanya bisa input nilai 1 atau 11")
            score_user = calculate_score(kartu_user)
            score_comp = calculate_score(kartu_comp) 
            print(f"kartu komputer {kartu_comp} dengan score: {score_comp}")
            print(f"kartu user {kartu_user} dengan score: {score_user}")
        else :
            score_comp = calculate_score(kartu_comp)
            score_user = calculate_score(kartu_user)
            score_user = calculate_score(kartu_user)
            score_comp = calculate_score(kartu_comp) 
            print(f"kartu komputer {kartu_comp} dengan score: {score_comp}")
            print(f"kartu user {kartu_user} dengan score: {score_user}")

        hit_stay = str(input("Mau hit or stay?"))
         # pengecekan hit/stay
        if hit_stay == "hit" :
            kartu_user.append(random.choice(list_card))
            kartu_comp.extend(random.sample(list_card, 2)) 
            score_comp = calculate_score(kartu_comp)
            score_user = calculate_score(kartu_user)
        elif hit_stay == "stay" :
            kartu_comp.append(random.choice(list_card))
            score_comp = calculate_score(kartu_comp)
            score_user = calculate_score(kartu_user)

        #pengecekan score
        if score_comp < score_user < 21 or score_user > score_comp:
            print(f"kartu komputer {kartu_comp} dengan score: {score_comp}")
            print(f"kartu user {kartu_user} dengan score: {score_user}\nYou won!")
        elif score_user == score_comp :
            print(f"kartu komputer {kartu_comp} dengan score: {score_comp}")
            print(f"kartu user {kartu_user} dengan score: {score_user}\nIt's a draw!")
        elif score_user > 21 :
            print(f"kartu komputer {kartu_comp} dengan score: {score_comp}")
            print(f"kartu user {kartu_user} dengan score: {score_user}\n You went over! Loser!")
        elif score_comp > 21 :
            print(f"kartu komputer {kartu_comp} dengan score: {score_comp}\Computer went over! You Won!")
            print(f"kartu user {kartu_user} dengan score: {score_user}")
        else :
            print(f"kartu komputer {kartu_comp} dengan score: {score_comp}")
            print(f"kartu user {kartu_user} dengan score: {score_user}\nYou lose!")
        break
    else :
        break

#gangerti aturannya gimana 