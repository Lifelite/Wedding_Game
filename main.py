import os

def introduction():
    print("""
    ###############################################################################
    #                                                                             #
    #                      You're invited to a celebration!                       #
    #                                                                             #
    ###############################################################################

                           Jeremy Huntsman and Sagan Sherlin                       
    """)
    print("""
    When:       Friday October 13th 2023
    Where:      5108 Madison Ave.
                Jacksonville AR, 72076

    Time:       Ceremony:   1 PM CDT
                Reception:  2 PM CDT            

    The ceremony is planned to be VERY small. However, it will be streamed online
    and, if feasible, will be projected on a screen outside considering the space
    cannot accommodate many.

    Reception is planned to be a glorified cookout.  Burgers, hot dogs, and sides
    will be provided, but BYOB please!  We aren't asking for gifts (seriously,
    don't even worry about it) though if you insist, we will have a QR code to a
    donation site that will go toward honeymoon expenses and other
    completely frivolous things, like giant inflatable unicorn floaties,
    useless trinkets, and probably other silly things you'd find on 
    "thisiswhyimbroke.com".           
                """)

def pretty_print(thing):
    for index in range(len(thing)):
        print(f"{index + 1}: {thing[index]}\n")

def information_input():
    print("""   Please input your information for RSVP!""")
    uInfo = {"Name": input("Name > ").title(),
             "Email": input("Email > "),
             "Discord": input("Discord Username (or N/A) > ")
             }
    pretty_print(uInfo)
    return uInfo


def rpg_character_build(info):
    toon_name = input("Name your character > ")
    print("""
    Choose your class:
    1.    Druid
    2.    Hunter
    3.     Mage
    4.     Paladin
    #     Priest
    #     Rogue
    #     Shaman
    #     Warlock
    #     Warrior
    """)
    toon_class = input("")


def n_validator(num, rang1, rang2):
    while True:
        if num in range(rang1, rang2):
            return num
        else:
            print("Invalid input")
            num = input("Try again\n\n")
            continue


introduction()
info = information_input()
