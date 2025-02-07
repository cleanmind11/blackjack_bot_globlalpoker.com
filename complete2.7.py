import requests
import time
import random
import json
from datetime import datetime
all_response = ''
REQUEST_HEADER = ''
REQUEST_URL = 'https://api.gap.vgwgames.com/play'
webhook_url = 'https://discord.com/api/webhooks/1336732522100424814/fDE9DAh0glvwFJxZUqBRCv5VZ5UlyNX-KWcszAviflebQ9WWPP2DB1xeNIsJLUl-nOqM'  
def send_webhook_notification(content):  
    # Create a payload with the content you want to send  
    data = {  
        "content": content,  
        "username": "BlackJack Bot",  # You can change the username here  
        "avatar_url": "https://example.com/avatar.png"  # Optional avatar URL  
    }  

    # Send a POST request to the Discord webhook URL  
    response = requests.post(webhook_url, data=json.dumps(data), headers={"Content-Type": "application/json"})  

    # Check if the request was successful  
    if response.status_code == 204:  
        print("Notification sent successfully!")  
    else:  
        print(f"Failed to send notification: {response.status_code}, {response.text}")  
def getToken(auth):
    headers = {
        'Authorization':"Bearer " + auth,
    }
    tokenResponse = requests.get('https://slots-server-external.globalpoker.com/gap/player/launch?coinType=SC&gameId=blackjack-classic&gameProviderId=gas&isMobile=false',headers=headers)
    if tokenResponse.status_code == 200:
        tokenResponseData = tokenResponse.json()
        auth = str(tokenResponseData.get("launchUrl"))
        auth = auth[137:-39]
        body = {"gameId":"blackjack-classic"}
        time.sleep(5)
        tokenResponse = requests.post("https://player-account-web-api.globalpoker.com/recently-played/3752526",headers=headers, json=body)
        global REQUEST_HEADER
        REQUEST_HEADER = {
            'Token': "Bearer " + auth,
        }
        time.sleep(5)
        tokenResponse = requests.get('https://api.gap.vgwgames.com/public/v2/game/start',headers = REQUEST_HEADER)
        if tokenResponse.status_code == 200:
            tokenResponseData = tokenResponse.json()
            auth = str(tokenResponseData.get("launchUrl"))
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
        "gameRequest":{"type":"accept-even-play"}
    }
    global all_response
    all_response = all_response + str(body) + "\n" 
    with open('result.txt', 'w', encoding='utf-8') as file:
        file.write(all_response)
    response = requests.post(REQUEST_URL, headers = REQUEST_HEADER, json=body)
    if response.status_code == 200:
       response_data = response.json()
       return response_data
    else :
        getToken(authorization)
        response = requests.post(REQUEST_URL, headers = REQUEST_HEADER, json=body)
        if response.status_code == 200:
            response_data = response.json()
            return response_data
        else :
            response_data = even_play(roundId)
            response = requests.post(REQUEST_URL, headers = REQUEST_HEADER, json=body)
            response_data = response.json()
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
    global all_response
    all_response = all_response + str(body) + "\n" 
    with open('result.txt', 'w', encoding='utf-8') as file:
        file.write(all_response)
    response = requests.post(REQUEST_URL, headers = REQUEST_HEADER, json=body)
    if response.status_code == 200:
       response_data = response.json()
       return response_data
    else :
        getToken(authorization)
        response = requests.post(REQUEST_URL, headers = REQUEST_HEADER, json=body)
        if response.status_code == 200:
            response_data = response.json()
            return response_data
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
    response = requests.post(REQUEST_URL, headers = REQUEST_HEADER, json=body)
    if response.status_code == 200:
       response_data = response.json()
       return response_data
    else :
        getToken(authorization)
        response = requests.post(REQUEST_URL, headers = REQUEST_HEADER, json=body)
        if response.status_code == 200:
            response_data = response.json()
            return response_data
        else :
            response_data = even_play(roundId)
            response = requests.post(REQUEST_URL, headers = REQUEST_HEADER, json=body)
            response_data = response.json()
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
       return response_data
    else :
        getToken(authorization)
        response = requests.post(REQUEST_URL, headers = REQUEST_HEADER, json=body)
        if response.status_code == 200:
            response_data = response.json()
            return response_data
        else :
            response_data = even_play(roundId)
            response = requests.post(REQUEST_URL, headers = REQUEST_HEADER, json=body)
            response_data = response.json()
            return response_data
def split(roundId):
    body = {
        "roundId":roundId,
        "gameInstanceId":"blackjack-classic-pok",
        "gameRequest":{"type":"split-hand"}
    }
    global all_response
    all_response = all_response + str(body) + "\n" 
    with open('result.txt', 'w', encoding='utf-8') as file:
        file.write(all_response)
    response = requests.post(REQUEST_URL, headers = REQUEST_HEADER, json=body)
    if response.status_code == 200:
       response_data = response.json()
       return response_data
    else :
        getToken(authorization)
        response = requests.post(REQUEST_URL, headers = REQUEST_HEADER, json=body)
        if response.status_code == 200:
            response_data = response.json()
            return response_data
        else :
            response_data = even_play(roundId)
            response = requests.post(REQUEST_URL, headers = REQUEST_HEADER, json=body)
            response_data = response.json()
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
            return response_data
        else :
            response_data = even_play(roundId)
            response = requests.post(REQUEST_URL, headers = REQUEST_HEADER, json=body)
            response_data = response.json()
            return response_data
def decline_insurance(roundId):
    body = {
        "roundId":roundId,
        "gameInstanceId":"blackjack-classic-pok",
        "gameRequest":{"type":"decline-insurance"}}
    global all_response
    all_response = all_response + str(body) + "\n" 
    with open('result.txt', 'w', encoding='utf-8') as file:
        file.write(all_response)
    response = requests.post(REQUEST_URL, headers = REQUEST_HEADER, json=body)
    if response.status_code == 200:
       response_data = response.json()
       return response_data
    else :
        getToken(authorization)
        response = requests.post(REQUEST_URL, headers = REQUEST_HEADER, json=body)
        if response.status_code == 200:
            response_data = response.json()
            return response_data
        else :
            response_data = even_play(roundId)
            response = requests.post(REQUEST_URL, headers = REQUEST_HEADER, json=body)
            response_data = response.json()
            return response_data
def calcuation(dealer_value, player_cards, player_value,hand_index):
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
            # if dealer_value == 10 or dealer_value == 11:
            #     return "hit"
            # else:
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
            if (dealer_value == 2 or dealer_value == 3 or dealer_value == 4 or dealer_value == 5 or dealer_value == 6) and allowed_hand_actions.get("canDouble") == True:
                return "double"
            elif dealer_value == 9 or dealer_value == 10 or dealer_value == 11:
                return "hit"
            else :
                return "stand"
        elif player_value[hand_index] == 19:
            if dealer_value == 6 and allowed_hand_actions.get("canDouble") == True:
                return "double"
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
            # if dealer_value == 11:
            #     return "hit"
            if allowed_hand_actions.get("canDouble") == True :
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

amount = input("Enter amount(>0.5):")
amount = float(amount)

if amount < 0.5:
    amount = input("Please input 0,5 :")
    amount = float(amount)
amount = int(amount * 100)
token = amount
roundnumber = int(input ("How many rounds would you like?:")) 
RTPsum = 0
RTPmy = 0
now = datetime.now()
starttime = now.strftime("%H:%M:%S")
for i in range(roundnumber) :
    all_response = all_response + "----------------------------------------------------------------" + "\n"
    all_response = all_response + "Round "+ str(i) + "\n"
    delay = random.uniform(1.5, 5.5)
    time.sleep(delay)
    print("Round",i)
    now = datetime.now()    
    nowtime = now.strftime("%H:%M:%S")
    all_response = all_response + "Time: "+ str(nowtime) + "\n"
    response_data = start(amount)
    all_response = all_response + str(response_data) + "\n"
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
        elif message_type == 'cards-dealt':
            player_cards = message.get('playerCards', [])      
            player_initial_hand_value = message.get('playerInitialHandValue')
            is_player_hand_blackjack = message.get('isPlayerHandBlackjack')
            dealer_card = message.get('dealerCard', {})
        elif message_type == 'player-action-requested':
            allowed_hand_actions = message.get('allowedHandActions', {})
            hand_index = int(message.get('handIndex'))
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
    print(f"Result - Player: {result.get('player')[0]}")

    is_insured = game_history_overview.get('isInsured')
    total_play_amount = game_history_overview.get('totalPlayAmount')
    total_win_amount = game_history_overview.get('totalWinAmount')
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
                elif message_type == 'cards-dealt':
                    player_cards = message.get('playerCards', [])
                    player_initial_hand_value = message.get('playerInitialHandValue')
                    is_player_hand_blackjack = message.get('isPlayerHandBlackjack')
                    dealer_card = message.get('dealerCard', {})
                elif message_type == 'player-action-requested':
                    allowed_hand_actions = message.get('allowedHandActions', {})
                    hand_index = message.get('handIndex')
                elif message_type == 'even-play-offered':
                    response_data = request("even-play", round_id, 0)
                    insurance_flag = 1
                    break
            action = game_history_play.get('action')
            hand = game_history_play.get('hand', {})
            value = game_history_play.get('value', {})
            result = game_history_play.get('result', {})
            print(f"Game History Play - Action: {action}")
            print(f"Hand - Dealer: {hand.get('dealer')}")
            print(f"Hand - Player: {hand.get('player')}")
            print(f"Value - Dealer: {value.get('dealer')}")
            print(f"Value - Player: {value.get('player')}")
            print(f"Result - Player: {result.get('player')}")

            is_insured = game_history_overview.get('isInsured')
            total_play_amount = game_history_overview.get('totalPlayAmount')
            total_win_amount = game_history_overview.get('totalWinAmount')

            print(f"Total Play Amount: {total_play_amount}")
            print(f"Total Win Amount: {total_win_amount}")

            # Extracting other values
            print(f"Balance: {balance}")
    RTPsum = RTPsum + total_win_amount
    percent = int(RTPsum / RTPmy * 100)
    discord_balance = float(balance)/100
    webhook_result = "Round: " + str(i) + "\n" + "Balance: " + str(discord_balance) + "\n" + "Result: " + str(result.get('player')) + "\n"
    send_webhook_notification(webhook_result)
endingBalance = float(balance) / 100
startingBalance = float(startingBalance) / 100
percent = endingBalance / startingBalance * 100
print("Finished washing")
print(f"Starting Balance was {startingBalance}")
print(f"Ending Balance is {endingBalance}")
print(f"RTP is {percent}%")
now = datetime.now()
endtime = now.strftime("%H:%M:%S")
print("Start Time = ", starttime)
print("End time = ", endtime)