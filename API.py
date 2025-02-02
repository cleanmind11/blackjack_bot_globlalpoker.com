import requests
import time
import random
from datetime import datetime
# Global variable
all_response = ''
REQUEST_HEADER = ''
REQUEST_URL = 'https://api.gap.vgwgames.com/play'
# REQUEST_HEADER = {
#     'Authorization': "Bearer eyJraWQiOiJhbGlhcy9nYXAtZ2FzLXNpZ25pbmcta2V5IiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYifQ.eyJhdWQiOiJHQVMiLCJzdWIiOiIzNzUyNTI2IiwiaXNTdGFmZiI6ZmFsc2UsImNvaW5UeXBlSWQiOiJHQyIsImlzcyI6ImdhcCIsImxhdW5jaE1vZGUiOjEsImV4cCI6MTczODMxMzk0NCwib3BlcmF0b3JDb2RlIjoiUE9LIiwianRpIjoiNDgyYmQ3Y2EtNGJhYS00ZjNiLThiZTgtMzJlYjUzZDRhYjdkIn0.J5xn7FtT5KI0-QnzDobKBgA6s1Bz1qna7GRkwNgXhdeKnMnwJAsCbf_rUABCkxwWvMudj0n-bfuUXQtd7tI0SD-wSZGqS9vmRJiMQZlHdQ07PlZzLLSsDPwtM51iiovqUBa5bPvOZWEB9sVWFGyCua8u9p6AZJ3ZNLOSmFVi-fQUzE72EvX7Sedh_LMnHpX_JReSnorcc6eHiNAV4q-p756rvOBQ-RQYrnKsmGu15wmSNIa9Jbeddnrm18jvidRZ03peBgDYDV2CkrF9pGCO5EnZGK_2TOlIpXiz1BdCeg_mNWNAxYO9Uu7YRN4fsNS9cWaoxTozVxGud4-CoP6ZTg",
# }

def getToken(auth):
    headers = {
        'Authorization':"Bearer " + auth,
    }
    tokenResponse = requests.get('https://slots-server-external.globalpoker.com/gap/player/launch?coinType=GC&gameId=blackjack-classic&gameProviderId=gas&isMobile=false',headers=headers)
    if tokenResponse.status_code == 200:
        tokenResponseData = tokenResponse.json()
        auth = str(tokenResponseData.get("launchUrl"))
        print("--------------------------------------------------------------")
        print(auth)
        auth = auth[137:-39]
        body = {"gameId":"blackjack-classic"}
        time.sleep(5)
        tokenResponse = requests.post("https://player-account-web-api.globalpoker.com/recently-played/3752526",headers=headers, json=body)
        global REQUEST_HEADER
        REQUEST_HEADER = {
            'Token': "Bearer " + auth,
        }
        time.sleep(5)
        print(REQUEST_HEADER)
        tokenResponse = requests.get('https://api.gap.vgwgames.com/public/v2/game/start',headers = REQUEST_HEADER)
        print(tokenResponse)
        if tokenResponse.status_code == 200:
            tokenResponseData = tokenResponse.json()
            auth = str(tokenResponseData.get("launchUrl"))
            print("--------------------------------------------------------------")
            print(auth)
            auth = auth[58:-131]
            REQUEST_HEADER = {
                'Authorization': "Bearer " + auth,
            }
        else :
            print("token error")
    else:
        print('Failed to get Token:', tokenResponse.status_code) 
def even_play(roundId):
    body = {
        "roundId":roundId,
        "gameInstanceId":"blackjack-classic-pok",
        "gameRequest":{"type":"accept-even-play"}}
    # print(body)
    global all_response
    all_response = all_response + str(body) + "\n" 
    with open('result.txt', 'w', encoding='utf-8') as file:
        file.write(all_response)
    response = requests.post(REQUEST_URL, headers = REQUEST_HEADER, json=body)
    if response.status_code == 200:
       response_data = response.json()
       print(response_data)
       return response_data
    else :
        getToken(authorization)
        response = requests.post(REQUEST_URL, headers = REQUEST_HEADER, json=body)
        if response.status_code == 200:
            response_data = response.json()
            print(response_data)
            return response_data
        else :
            response_data = even_play(roundId)
            response = requests.post(REQUEST_URL, headers = REQUEST_HEADER, json=body)
            response_data = response.json()
            print(response_data)
            return response_data
def start(amount):
    body = {
    "roundId": None,
    "gameInstanceId": "blackjack-classic-pok",
        "gameRequest": {
            "type": "start-game",
            "playAmount": amount
        }
    }
    # print(body)
    global all_response
    all_response = all_response + str(body) + "\n" 
    with open('result.txt', 'w', encoding='utf-8') as file:
        file.write(all_response)
    print("Request URL:",REQUEST_URL)
    print("header:",REQUEST_HEADER)
    print(body)
    response = requests.post(REQUEST_URL, headers = REQUEST_HEADER, json=body)
    print(response)
    if response.status_code == 200:
       response_data = response.json()
       print(response_data)
       return response_data
    else :
        getToken(authorization)
        response = requests.post(REQUEST_URL, headers = REQUEST_HEADER, json=body)
        if response.status_code == 200:
            response_data = response.json()
            print(response_data)
            return response_data
        # else :
        #     response_data = even_play(roundId)
        #     response = requests.post(REQUEST_URL, headers = REQUEST_HEADER, json=body)
        #     response_data = response.json()
        #     print(response_data)
        #     return response_data
def hit(roundId,handleIndex):
    body = {
        "roundId":roundId,
        "gameInstanceId":"blackjack-classic-pok",
            "gameRequest":{
                "type":"hit-hand",
                "handIndex":handleIndex
            }
    }
    global all_response
    all_response = all_response + str(body) + "\n" 
    with open('result.txt', 'w', encoding='utf-8') as file:
        file.write(all_response)
    # print(body)
    response = requests.post(REQUEST_URL, headers = REQUEST_HEADER, json=body)
    if response.status_code == 200:
       response_data = response.json()
       print(response_data)
       return response_data
    else :
        getToken(authorization)
        response = requests.post(REQUEST_URL, headers = REQUEST_HEADER, json=body)
        if response.status_code == 200:
            response_data = response.json()
            print(response_data)
            return response_data
        else :
            response_data = even_play(roundId)
            response = requests.post(REQUEST_URL, headers = REQUEST_HEADER, json=body)
            response_data = response.json()
            print(response_data)
            return response_data
def stand(roundId,handleIndex):
    body = {
        "roundId":roundId,
        "gameInstanceId":"blackjack-classic-pok",
        "gameRequest":{
            "type":"stand-hand",
            "handIndex":handleIndex
        }
    }
    # print(body)
    global all_response
    all_response = all_response + str(body) + "\n" 
    with open('result.txt', 'w', encoding='utf-8') as file:
        file.write(all_response)
    response = requests.post(REQUEST_URL, headers = REQUEST_HEADER, json=body)
    if response.status_code == 200:
       response_data = response.json()
       print(response_data)
       return response_data
    else :
        getToken(authorization)
        response = requests.post(REQUEST_URL, headers = REQUEST_HEADER, json=body)
        if response.status_code == 200:
            response_data = response.json()
            print(response_data)
            return response_data
        else :
            response_data = even_play(roundId)
            response = requests.post(REQUEST_URL, headers = REQUEST_HEADER, json=body)
            response_data = response.json()
            print(response_data)
            return response_data
def split(roundId):
    body = {
        "roundId":roundId,
        "gameInstanceId":"blackjack-classic-pok",
        "gameRequest":{"type":"split-hand"}
    }
    # print(body)
    global all_response
    all_response = all_response + str(body) + "\n" 
    with open('result.txt', 'w', encoding='utf-8') as file:
        file.write(all_response)
    response = requests.post(REQUEST_URL, headers = REQUEST_HEADER, json=body)
    if response.status_code == 200:
       response_data = response.json()
       print(response_data)
       return response_data
    else :
        getToken(authorization)
        response = requests.post(REQUEST_URL, headers = REQUEST_HEADER, json=body)
        if response.status_code == 200:
            response_data = response.json()
            print(response_data)
            return response_data
        else :
            response_data = even_play(roundId)
            response = requests.post(REQUEST_URL, headers = REQUEST_HEADER, json=body)
            response_data = response.json()
            print(response_data)
            return response_data
def double(roundId, handleIndex):
    body = {
        "roundId":roundId,
        "gameInstanceId":"blackjack-classic-pok",
        "gameRequest":{
            "type":"double-hand",
            "handIndex":handleIndex
        }
    }
    global all_response
    all_response = all_response + str(body) + "\n" 
    with open('result.txt', 'w', encoding='utf-8') as file:
        file.write(all_response)
    # print(body)
    response = requests.post(REQUEST_URL, headers = REQUEST_HEADER, json=body)
    if response.status_code == 200:
       response_data = response.json()
       print(response_data)
       return response_data
    else :
        getToken(authorization)
        response = requests.post(REQUEST_URL, headers = REQUEST_HEADER, json=body)
        if response.status_code == 200:
            response_data = response.json()
            print(response_data)
            return response_data
        else :
            response_data = even_play(roundId)
            response = requests.post(REQUEST_URL, headers = REQUEST_HEADER, json=body)
            response_data = response.json()
            print(response_data)
            return response_data
def decline_insurance(roundId):
    body = {
        "roundId":roundId,
        "gameInstanceId":"blackjack-classic-pok",
        "gameRequest":{"type":"decline-insurance"}}
    # print(body)
    global all_response
    all_response = all_response + str(body) + "\n" 
    with open('result.txt', 'w', encoding='utf-8') as file:
        file.write(all_response)
    response = requests.post(REQUEST_URL, headers = REQUEST_HEADER, json=body)
    if response.status_code == 200:
       response_data = response.json()
       print(response_data)
       return response_data
    else :
        getToken(authorization)
        response = requests.post(REQUEST_URL, headers = REQUEST_HEADER, json=body)
        if response.status_code == 200:
            response_data = response.json()
            print(response_data)
            return response_data
        else :
            response_data = even_play(roundId)
            response = requests.post(REQUEST_URL, headers = REQUEST_HEADER, json=body)
            response_data = response.json()
            print(response_data)
            return response_data
def calcuation(dealer_value, player_cards, player_value,hand_index):
    print(f"----------------------{allowed_hand_actions.get("canSplit")}")
    if player_cards[hand_index][0][0] == player_cards[hand_index][1][0] and allowed_hand_actions.get("canSplit") == True:
        if player_cards[hand_index][0][0] == 'J' or player_cards[hand_index][0][0] == 'K' or player_cards[hand_index][0][0] == 'Q' or player_cards[hand_index][0][0] == 'T':
            return "stand"
        elif player_cards[hand_index][0][0] == 'A':
            return "split"
        elif player_cards[hand_index][0][0] == '9':
            if dealer_value == 7 or dealer_value == 11 or dealer_value == 10:
                return "stand"
            else:
                return "split"
        elif player_cards[hand_index][0][0] == '8':
            if dealer_value == 10 or dealer_value == 11:
                return "hit"
            else:
                return "split"
        elif player_cards[hand_index][0][0] == '7':
            if dealer_value==8 or dealer_value == 9 or dealer_value == 10 or dealer_value == 11:
                return "hit"
            else:
                return "split"
        elif player_cards[hand_index][0][0] == '6':
            if dealer_value == 7 or dealer_value == 8 or dealer_value == 9 or dealer_value == 10 or dealer_value == 11:
                return "hit"
            else:
                return "split"
        elif player_cards[hand_index][0][0] == '5':
            if dealer_value == 10 or dealer_value == 11:
                return "hit"
            else:
                return "double"
        elif player_cards[hand_index][0][0] == '4':
            if dealer_value == 5 or dealer_value == 6:
                return "split"
            else :
                return "hit"
        elif player_cards[hand_index][0][0] == '3':
            if dealer_value == 8 or dealer_value == 9 or dealer_value == 10 or dealer_value == 11:
                return "hit"
            else :
                return "split"
        elif player_cards[hand_index][0][0] == '2':
            if dealer_value == 8 or dealer_value == 9 or dealer_value == 10 or dealer_value == 11:
                return "hit"
            else :
                return "split"   
    sumA = 0
    for card in player_cards[hand_index]:
        if card == 'AS' or card == 'AD' or card == 'AC' or card == 'AH':
            sumA = sumA + 1
    if sumA > 0:
        if player_value[hand_index] == 13:
            if (dealer_value == 5 or dealer_value == 6 ) and allowed_hand_actions.get("canDouble") == True:
                return "double"
            else :
                return "hit"
        elif player_value[hand_index] == 14:
            if (dealer_value == 5 or dealer_value == 6) and allowed_hand_actions.get("canDouble") == True:
                return "double"
            else :
                return "hit"    
        elif player_value[hand_index] == 15:
            if (dealer_value == 4 or dealer_value == 5 or dealer_value == 6) and allowed_hand_actions.get("canDouble") == True:
                return "double"
            else :
                return "hit"  
        elif player_value[hand_index] == 16:
            if (dealer_value == 4 or dealer_value == 5 or dealer_value == 6) and allowed_hand_actions.get("canDouble") == True:
                return "double"
            else :
                return "hit"  
        elif player_value[hand_index] == 17:
            if (dealer_value == 3 or dealer_value == 4 or dealer_value == 5 or dealer_value == 6) and allowed_hand_actions.get("canDouble") == True:
                return "double"
            else :
                return "hit"  
        elif player_value[hand_index] == 18:
            if (dealer_value == 3 or dealer_value == 4 or dealer_value == 5 or dealer_value == 6) and allowed_hand_actions.get("canDouble") == True:
                return "double"
            elif dealer_value == 9 or dealer_value == 10 or dealer_value == 11:
                return "hit"
            else :
                return "stand"
        else :
            return "stand"
    else :
        if player_value[hand_index] >= 5 and player_value[hand_index] <= 8:
            return "hit"
        elif player_value[hand_index] == 9:
            if dealer_value >= 3 and dealer_value <= 6 and allowed_hand_actions.get("canDouble") == True:
                return "double"
            else :
                return "hit"
        elif player_value[hand_index] == 10:
            if dealer_value == 10 or dealer_value == 11:
                return "hit"
            elif allowed_hand_actions.get("canDouble") == True :
                return "double"
            else :
                return "hit"
        elif player_value[hand_index] == 11:
            if dealer_value == 11:
                return "hit"
            elif allowed_hand_actions.get("canDouble") == True :
                return "double"
            else :
                return "hit"
        elif player_value[hand_index] == 12:
            if dealer_value >= 4 and dealer_value <= 6:
                return "stand"
            else :
                return "hit"
        elif player_value[hand_index] >= 13 and player_value[hand_index] <= 16:
            if dealer_value >= 2 and dealer_value <= 6:
                return "stand"
            else :
                return "hit"
        else :
            return "stand"
def request(calculation_result, roundId, handelindex):
    match calculation_result:
        case "stand":
            return stand(roundId,handelindex)
        case "hit":
            return hit(roundId,handelindex)
        case "double":
            return double(roundId,handelindex)
        case "split":
            return split(roundId)
        case "decline_insurance":
            return decline_insurance(roundId)
        case "even-play":
            return even_play(roundId)
authorization = input("Enter authorization:")
REQUEST_HEADER = {
    'Authorization': "Bearer ",
}
getToken(authorization)

amount = input("Enter amount:")
token = amount
if int(amount) < 1000 :
    amount = input("Please input 1000~100000:")
roundnumber = int(input ("How many rounds would you like?:")) 
RTPsum = 0
RTPmy = 0
now = datetime.now()
starttime = now.strftime("%H:%M:%S")
for i in range(roundnumber) :
    all_response = all_response + "Round "+ str(i) + "\n"
    all_response = all_response + "----------------------------------------------------------------" + "\n"
    time.sleep(20)
    print("Round",i)
    response_data = start(amount)
    all_response = all_response + str(response_data) + "\n"
    # print(response_data)
    RTPmy = RTPmy + int(amount)
    delay = random.uniform(1.5, 5.5)
    time.sleep(delay)
    game_response = response_data.get('gameResponse', {})
    messages = game_response.get('messages', [])
    game_history_play = game_response.get('gameHistoryPlay', {})
    game_history_overview = game_response.get('gameHistoryOverview', {})
    balance = response_data.get('balance')
    round_id = response_data.get('roundId')
    round_completed = response_data.get('roundCompleted')
    insurance_flag = 0
    if i == 0 :
        startingBalance = int(balance) + int(amount)
    for message in messages:
        message_type = message.get('type')
        if message_type == 'game-start':
            initial_play_amount = message.get('initialPlayAmount')
            # print(f"Game Start - Initial Play Amount: {initial_play_amount}")
        elif message_type == 'cards-dealt':
            player_cards = message.get('playerCards', [])
            
            player_initial_hand_value = message.get('playerInitialHandValue')
            is_player_hand_blackjack = message.get('isPlayerHandBlackjack')
            dealer_card = message.get('dealerCard', {})
            
            # print(f"Cards Dealt - Player Cards: {player_cards}")
            # print(f"Player Initial Hand Value: {player_initial_hand_value}")
            # print(f"Is Player Hand Blackjack: {is_player_hand_blackjack}")
            # print(f"Dealer Card: {dealer_card}")
        elif message_type == 'player-action-requested':
            allowed_hand_actions = message.get('allowedHandActions', {})
            hand_index = int(message.get('handIndex'))
            
            # print(f"Player Action Requested - Allowed Hand Actions: {allowed_hand_actions}")
            # print(f"Hand Index: {hand_index}")
        elif message_type == "insurance-offered":
            response_data = request("decline_insurance", round_id, 0)
            insurance_flag = 1
            break
        elif message_type == 'even-play-offered':
            response_data = request("even-play", round_id, 0)
            insurance_flag = 1
            break
    if insurance_flag == 1:
        game_response = response_data.get('gameResponse', {})
        messages = game_response.get('messages', [])
        game_history_play = game_response.get('gameHistoryPlay', {})
        game_history_overview = game_response.get('gameHistoryOverview', {})
        balance = response_data.get('balance')
        round_id = response_data.get('roundId')
        round_completed = response_data.get('roundCompleted')
        insurance_flag = 0
        hand_index = 0
    action = game_history_play.get('action')
    hand = game_history_play.get('hand', {})
    value = game_history_play.get('value', {})
    result = game_history_play.get('result', {})
    
    print(f"Game History Play - Action: {action}")
    print(f"Hand - Dealer: {hand.get('dealer')}")
    print(f"Hand - Player: {hand.get('player')}")
    print(f"Value - Dealer: {value.get('dealer')}")
    print(f"Value - Player: {value.get('player')[0]}")
    # print(f"Result - Dealer: {result.get('dealer')}")
    print(f"Result - Player: {result.get('player')[0]}")

    is_insured = game_history_overview.get('isInsured')
    total_play_amount = game_history_overview.get('totalPlayAmount')
    total_win_amount = game_history_overview.get('totalWinAmount')

    # print(f"Game History Overview - Is Insured: {is_insured}")
    # print(f"Total Play Amount: {total_play_amount}")
    # print(f"Total Win Amount: {total_win_amount}")

    # Extracting other values
    # print(f"Balance: {balance}")
    # print(f"Round ID: {round_id}")
    # print(f"Round Completed: {round_completed}")
    if result.get('player')[0] == '-':
        while result.get('player')[hand_index] == '-':
            calcuation_result = calcuation(value.get('dealer'),hand.get('player'),value.get('player'),int(hand_index))
            print("Calculation:", calcuation_result)
            delay = random.uniform(1.5, 5.5)
            time.sleep(delay)
            response_data = request(calcuation_result, round_id, hand_index)
            all_response = all_response + str(response_data) + "\n"
            with open('result.txt', 'w', encoding='utf-8') as file:
                file.write(all_response)
            # print(response_data)
            game_response = response_data.get('gameResponse', {})
            messages = game_response.get('messages', [])
            game_history_play = game_response.get('gameHistoryPlay', {})
            game_history_overview = game_response.get('gameHistoryOverview', {})
            balance = response_data.get('balance')
            round_id = response_data.get('roundId')
            round_completed = response_data.get('roundCompleted')
            for message in messages:
                message_type = message.get('type')
                if message_type == 'game-start':
                    initial_play_amount = message.get('initialPlayAmount')
                    print(f"Game Start - Initial Play Amount: {initial_play_amount}")
                elif message_type == 'cards-dealt':
                    player_cards = message.get('playerCards', [])
                    player_initial_hand_value = message.get('playerInitialHandValue')
                    is_player_hand_blackjack = message.get('isPlayerHandBlackjack')
                    dealer_card = message.get('dealerCard', {})
                    
                    # print(f"Cards Dealt - Player Cards: {player_cards}")
                    # print(f"Player Initial Hand Value: {player_initial_hand_value}")
                    # print(f"Is Player Hand Blackjack: {is_player_hand_blackjack}")
                    # print(f"Dealer Card: {dealer_card}")
                elif message_type == 'player-action-requested':
                    allowed_hand_actions = message.get('allowedHandActions', {})
                    hand_index = message.get('handIndex')
                elif message_type == 'even-play-offered':
                    response_data = request("even-play", round_id, 0)
                    insurance_flag = 1
                    break
                    # print(f"Player Action Requested - Allowed Hand Actions: {allowed_hand_actions}")
                    # print(f"Hand Index: {hand_index}")
            action = game_history_play.get('action')
            hand = game_history_play.get('hand', {})
            value = game_history_play.get('value', {})
            result = game_history_play.get('result', {})
                
            print(f"Game History Play - Action: {action}")
            print(f"Hand - Dealer: {hand.get('dealer')}")
            print(f"Hand - Player: {hand.get('player')}")
            print(f"Value - Dealer: {value.get('dealer')}")
            print(f"Value - Player: {value.get('player')}")
            # print(f"Result - Dealer: {result.get('dealer')}")
            print(f"Result - Player: {result.get('player')}")

            is_insured = game_history_overview.get('isInsured')
            total_play_amount = game_history_overview.get('totalPlayAmount')
            total_win_amount = game_history_overview.get('totalWinAmount')

            # print(f"Game History Overview - Is Insured: {is_insured}")
            print(f"Total Play Amount: {total_play_amount}")
            print(f"Total Win Amount: {total_win_amount}")

            # Extracting other values
            print(f"Balance: {balance}")
    RTPsum = RTPsum + total_win_amount
    # print(f"Round {i}: RTPsum:{RTPsum}")   
    # print(f"Round {i}: RTPmy:{RTPmy}")
    percent = int(RTPsum / RTPmy * 100)
    # print(f"{percent}%")
endingBalance = int(balance)
percent = endingBalance / startingBalance * 100
print("Finished washing")
print(f"Starting Balance was {startingBalance}")
print(f"Ending Balance is {endingBalance}")
print(f"RTP is {percent}%")
now = datetime.now()
endtime = now.strftime("%H:%M:%S")
print("Start Time = ", starttime)
print("End time = ", endtime)