import json
from PW_Generator_functions import passwordgenerator

### function for adding dummy data; adding to file #####
def add_data():
    fn = 'PWMGR.json'
    # data to add; account:password
    PWinfo = {'hotmail':'qwerty',
            'gmail':'qazwsx',
            'runescape':'q1w2e3r4t5',
            'google':'fdlkasdf'}

    # add data to json file
    with open(fn,'w') as jsonobj:
        json.dump(PWinfo,jsonobj)
    # load data to confirm it was added
    with open(fn) as fileobj:
        contents = json.load(fileobj)





# ## encrypting a string ##
# key1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','^','&','*','(',')','+','=','[',']','{','}','\\','|',';',':','"',"'",'<',',','>','.','?','/']
# key2 = [';','!','&','v','(','k','i','o','8','+','5','4','%','/',"'",'?','e','q',']','j','t','[','"','$','g','{','|','w','x','d','b','7','}','y','>','1','.','9','2','#','\\','p',':','*','u','c','f','=','^','h','n','m','3','z',',','@','a','0','l','<','s','6',')','r']
#
#
# password = 'qwerty123'
#
# encrypted_string = ''
# for items in password:
#     encrypting = key2.index(key2[key1.index(items)])
#     encrypted_string += key2[encrypting]
# # print(encrypted_string)




# ## adding and saving to the json
# fn = 'PWMGR.json'
# with open(fn,'r+') as f:
#     ## load json
#     contents = json.load(f)
#     ## add k,v
#     contents['work laptop'] = 'abc987'
#
# ## add to json file with json.dumps()
# with open(fn,'w') as f:
#     f.write(json.dumps(contents))









## functions




## encrypts password string using build in encryption method
def encrypt_password(password_to_encrypt):
    key1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^',
            '&', '*', '(', ')', '+', '=', '[', ']', '{', '}', '\\', '|', ';', ':', '"', "'", '<', ',', '>', '.', '?',
            '/']
    key2 = [';', '!', '&', 'v', '(', 'k', 'i', 'o', '8', '+', '5', '4', '%', '/', "'", '?', 'e', 'q', ']', 'j', 't',
            '[', '"', '$', 'g', '{', '|', 'w', 'x', 'd', 'b', '7', '}', 'y', '>', '1', '.', '9', '2', '#', '\\', 'p',
            ':', '*', 'u', 'c', 'f', '=', '^', 'h', 'n', 'm', '3', 'z', ',', '@', 'a', '0', 'l', '<', 's', '6', ')',
            'r']


    encrypted_string = ''
    for character in password_to_encrypt:
        index = key1.index(character) ## get index of character in key1
        encrypting = key2[index] ## return char in same index of key2
        encrypted_string += encrypting ## add to string
    #print(encrypted_string)
    return encrypted_string



## decrypt the password string
def decryptor(password_to_decrypt):
    key1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^',
            '&', '*', '(', ')', '+', '=', '[', ']', '{', '}', '\\', '|', ';', ':', '"', "'", '<', ',', '>', '.', '?',
            '/']
    key2 = [';', '!', '&', 'v', '(', 'k', 'i', 'o', '8', '+', '5', '4', '%', '/', "'", '?', 'e', 'q', ']', 'j', 't',
            '[', '"', '$', 'g', '{', '|', 'w', 'x', 'd', 'b', '7', '}', 'y', '>', '1', '.', '9', '2', '#', '\\', 'p',
            ':', '*', 'u', 'c', 'f', '=', '^', 'h', 'n', 'm', '3', 'z', ',', '@', 'a', '0', 'l', '<', 's', '6', ')',
            'r']


    decrypted_string = ''
    for character in password_to_decrypt:
        index = key2.index(character)
        decrypting = key1[index]
        decrypted_string += decrypting

    return decrypted_string




## adds account and password to json file
## password gets encrypted using encrypt_password()
## requires account and password input
def add_to_file(account,password):
    # fn = 'PWMGR.json'
    with open(fn, 'r+') as f:
        ## load json
        contents = json.load(f)
        ## add k,v
        contents[account] = encrypt_password(password)

    ## add to json file with json.dumps()
    with open(fn, 'w') as f:
        f.write(json.dumps(contents))






## pass the account/site you want the password from
def get_password(account):
    fn = 'PWMGR.json'

    # load data to confirm it was added
    with open(fn) as f:
        contents = json.load(f)

    password = contents[account]
    password = decryptor(password)

    return password
    #print(f"your decrypted password is: {password}")



def list_acconts(fn):
    fn = 'PWMGR.json'

    # load data to confirm it was added
    with open(fn) as f:
        contents = json.load(f)
        for k,v in contents.items():
            print(k.title())




## running it
try:
    while True:
        ## asks user what they want to do
        userInput = input('\nWhat would you like to do? Here are your options:'
                          '\n Type "q" to quit'
                          '\n Add: to add account and passwrod'
                          '\n Get: tells you password of the account'
                          '\n Update: update password for existing account'
                          '\n List: list out all stored accounts\n')
        ## quit option
        if userInput.lower() == 'q' or userInput.lower() == 'quit':
            print('=== EXISTING PROGRAM ====')
            break
        ## add new account and password pair
        elif userInput.lower() == 'add':
            accounta = input('\nwhat is the account/site'.title())
            passworda = input('what is the password'.title())
            add_to_file(accounta,passworda)

        ## retrieve password of an account
        elif userInput.lower() == 'get':
            account_to_get = input('\nwhat is the account whos password you want to get; i.e hotmail/gmail'.title())
            heres_your_password = get_password(account_to_get)

            print(f"\nyour password for {account_to_get} is {heres_your_password}".title())

        ## update a password to an existing account
        elif userInput.lower() == 'update':
            account_name = input('\nwhat accounts password do you want to update?'.title())
            new_password = input('what is the new password'.title())
            add_to_file(account_name,new_password)

        ## list out all accounts stored in the PasswordManager
        elif userInput.lower() == 'list':
            list_acconts()
except KeyboardInterrupt:
    print('\n === ENDING PROGRAM ===')
except KeyError:
    print('\nALERT: That account does not exist!'.upper())




'''
TO DO:
1 - add a forgot password and reset password option using twilio from text me with a randomly generated key from passwordgenerator


'''