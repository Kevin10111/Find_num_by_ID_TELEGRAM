from telethon import TelegramClient, events, sync
from telethon.tl.types import InputPhoneContact
from telethon import functions, types
from colorama import Fore, Back, Style
print(Fore.CYAN + "Created by CR.MATIX")
print(Fore.BLUE + " :::::::::::::::::::::::::    :::::::::::: ::::    ::::::    :::  :::   :::" )
print(Fore.BLUE + "  :+:           :+:    :+:+:   :+::+:    :+::+:+:   :+::+:    :+: :+:+: :+:+:")
print(Fore.BLUE + "   +:+           +:+    :+:+:+  +:++:+    +:+:+:+:+  +:++:+    +:++:+ +:+:+ +:+")
print(Fore.BLUE + "    :#::+::#      +#+    +#+ +:+ +#++#+    +:++#+ +:+ +#++#+    +:++#+  +:+  +#+")
print(Fore.BLUE + "     +#+           +#+    +#+  +#+#+#+#+    +#++#+  +#+#+#+#+    +#++#+       +#+")
print(Fore.BLUE + "      #+#           #+#    #+#   #+#+##+#    #+##+#   #+#+##+#    #+##+#       #+#")
print(Fore.BLUE + "       ###       ##############    ############# ###    #### ######## ###       ###")
print(Fore.BLUE + 'v0.1')
def check(phone_number, usr):
    try:
        contact = InputPhoneContact(client_id = 0, phone = phone_number, first_name="__test__", last_name="__last_test__")
        contacts = client(functions.contacts.ImportContactsRequest([contact]))
        username = contacts.to_dict()['users'][0]['username']
        return username
        dell = client(functions.contacts.DeleteContactsRequest(id=[username]))
    except:
        res = "__err__"
        return res

def list_checker():
    list_file = input(Fore.GREEN + "Number List File: ")
    usr = input(Fore.GREEN + "Target Username: ")
    list = open(list_file, 'r').read().splitlines()
    for num in list:
        try:
            ress = check(num, usr)
            if ress == '__err__':
                print (Fore.GREEN + "Number: {} <{}>".format(num,Fore.GREEN + "ERROR!"))
            elif ress.lower() == usr.lower():
                f = open("hit.txt", "a")
                f.write(ress+":"+num)
                f.close()
                print ("Number: {} <{}>".format(num,Fore.GREEN + "OK:)"))
                break
            else:
                print ("Null")
        except:
            print ("Null")

if __name__ == '__main__':
    phone =input(Fore.GREEN +'Enter your Phonenumber:')
    client = TelegramClient(phone,input(Fore.GREEN + 'Enter your App api id: '), input(Fore.GREEN + 'Enter your App api hash: '))
    client.connect()
    if not client.is_user_authorized():
        client.send_code_request(phone)
        client.sign_in(phone, input(Fore.GREEN + 'Enter the code in your Account: '))
    list_checker()
    
    