import requests

'''
Client ID
ValrO45-TQP7OBibpPQ8Jg

API Key
ny-THejHpAR1ts_t2VWdRgz2tuwRFGFlU6QXEp5vHPZlLkugeGeT0n2rEttMyKU2Mbyyz4vV9AJIk3apgCzmJHGvuH2ty-CWwq6tHgnfys1UtcZBSw1ROrGT01t-Y3Yx
'''

api_key = "ny-THejHpAR1ts_t2VWdRgz2tuwRFGFlU6QXEp5vHPZlLkugeGeT0n2rEttMyKU2Mbyyz4vV9AJIk3apgCzmJHGvuH2ty-CWwq6tHgnfys1UtcZBSw1ROrGT01t-Y3Yx"
headers = {"Authorization": "Bearer %s" % api_key}
#user menu to iterate through different search options
def userMenu():
    while True:
        #try-except block in case user enters letter
        try:
            userInput = int(input("\n1:Business search \n2:Business review search(requires business id) \n3:Phone Search \n4:Business Match Search \n\nWhich option would you like to choose? "))
            if(userInput > 0 and userInput < 5):
                break
            else:
                print("\nMust enter a number between 1-4. Try again.")
                continue
        except ValueError:
            print("\nMust enter a number between 1-4. Try again.")
            continue
    return userInput
#use a while loop on this entire chain of code in case user wants to do multiple searches
while True:
    userInput = userMenu()
    if userInput == 1:
        #keep it in a while loop in case user input isn't in the correct format
        while True:
            term = input("\nWhat kind of cuisine/business are you interested in? ")
            location = input("\nIn which city? ")
            #term and location search
            url = "https://api.yelp.com/v3/businesses/search"
            #in the dictionary, term can take values like food, cafes, or businesses like McDonalds
            params = {"term":term, "location": location}
            #make an API call and store the response
            r = requests.get(url, params=params, headers=headers)
            #only continue if the request pull came back correct
            if(r.status_code == 200):
                #store API response in a variable
                businesses_dict = r.json()
                #examine businesses key and its values
                businesses = businesses_dict["businesses"]
                #print out the name of all the restaurants that match the term and location the user put in
                print("\nList of " + term.title() + " cuisine in " + location.title() + ": ")
                for business in businesses:
                    print("\t" + business["name"] + "(State: " + business["location"]["state"] + ")")
                #break while loop
                break
            else:
                print("\nThe cuisine type or location you entered was invalid. Try again.")
                continue
    #business reviews
    elif userInput == 2:
        #use a while loop in case id entered is invalid
        while True:
            #explain how to get a business id
            print("\nTo get a business id, you must go the Yelp website and find the business in question. Copy the business id from the url. \nFor example: \n\n\t -The Yelp url for SFT Construction is 'https://www.yelp.com/biz/sft-construction-san-francisco-7' \n\n\t -The business id is everything after 'biz/' \n\n\t -Therefore, it would be 'sft-construction-san-francisco-7'")
            id = input("\nEnter in business id: ")
            url = "https://api.yelp.com/v3/businesses/" + id + "/reviews" #user input
            r = requests.get(url, headers=headers)
            #if r.status_code is not 200, alarm the user that their id is invalid and ask for business id again
            if(r.status_code != 200):
                print("\nInvalid id. Please try again.")
                continue
            else:
                break
        reviews = r.json()
        #print the three reviews that the api provides
        try:
            reviews = reviews["reviews"]
            counter = 1
            print("\nHere are the 3 most recent reviews for this business:")
            for review in reviews:
                print("\nReview #" + str(counter) + ": ")
                print("\n-Rating: " + str(review["rating"]))
                print("\n-Comment: " +  review["text"] + "\n")
                counter += 1
       #KeyError is thrown if there aren't enough reviews, so have an error message ready in case this happens
        except KeyError:
            print("\nThis business doesn't have enough reviews. Please try another one.")
    #8mlpC1pRQpmCH3S5z6rzSg

    #phone search
    elif userInput == 3:
        active = True
        #use a while loop to ask for phone number, in case user input is Invalid
        while active:
            while True:
                phoneNum = input("\nWhat is the phone number of the business(Ex: +19287755612)? ")
                url = "https://api.yelp.com/v3/businesses/search/phone"
                params = {"phone":phoneNum} #user input
                r = requests.get(url, params=params, headers=headers)
                #if status_code == 200, break. Else, continue the loop until a valid phone number is entered
                if(r.status_code != 200):
                    print("\nError. Could not retriew reviews. Please try again")
                    continue
                else:
                    break
            #display valuable info from the keys and values from r.json() like name, address, rating, etc.
            business = r.json()
            '''
        this block of code takes a variable that equals request.json() and prints out info about the business

                EXPLORATION CODE
            counter = 0
            for details in business.values():
                for detail in details:
                    for key in detail:
                        print(counter, key)
                        counter += 1
                    RESULT FROM CODE ABOVE
            indexes:
                0 id
                1 alias
                2 name
                3 image_url
                4 is_closed
                5 url
                6 review_count
                7 categories
                8 rating
                9 coordinates
                10 transactions
                11 price
                12 location
                13 phone
                14 display_phone
            '''
            for details in business.values():
                #used a try-except block because the output was what I wanted pluse a TypeError print at the end I wanted to erase
                try:
                    for detail in details:
                        print("\nName: " + detail["name"])
                        print("\nPrice: " + detail["price"])
                        print("\nRating: " + str(detail["rating"]) + "(" + str(detail["review_count"]) + " reviews)")
                        print("\nCity: " + detail["location"]["city"] + " " + detail["location"]["state"])
                        #every time i enter a valid phone number, the first address is readible and legible, but anything beyond that is always funky. So that's why I'm only print address1
                        print("\nAddress: " + detail["location"]["address1"])
                except TypeError:
                    pass
                else:
                    #if phone number is invalid, details list will have zero elements
                    if(len(details) == 0):
                        print("\nPhone number is invalid. Please try again.")
                        continue
                    else:
                        #break the loop
                        active = False
    #+19286427505
    #+19287724724
    #+16029789799

    #business match search
    else:
        url = "https://api.yelp.com/v3/businesses/matches"
        #use while loop until all user input is verified to be correct
        while True:
            name = input("\nWhat's the name of the business? ")
            address = input("\nWhat's the address? ")
            city = input("\nCity? ")
            state = input("\nState?(AZ, IL, IN, etc.): ")
            zip_code = input("\nZip Code? ")
            params = {"name": name,
            "address1": address,
            "city": city,
            "state": state,
            "zip_code": zip_code,
            "country": "US"} #user input
            r = requests.get(url, params=params, headers=headers)
            if(r.status_code != 200):
                print("\nIt doesn't exist")
                break
            else:
                print("\nIt exists!")
                searchAgain = input("\nDo you want to search another business(y/n)? ")
                if searchAgain == "y":
                    continue
                else:
                    break
    goAgain = input("\nDo you want to do another search?(y/n) ")
    if(goAgain == "y"):
        continue
    else:
        break
