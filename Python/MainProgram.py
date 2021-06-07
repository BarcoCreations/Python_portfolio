print("Choose program:")
print("1.Automatic order program,\n2.Buy ticket lunapark,\n3.Leap year,\n4.Love calculator,\n5.Treasure island game,\n6.Hangman,\n7.Caesar cipher,\n8.BlackJack game,\n9.Rock paper scissors game,\n10. Treasure map,\n11.Password generator,")
program = input()
if program == "1":
    import Automatic_order_program
elif program == "2":
    import Buy_ticket_lunapark
elif program == "3":
    import Leap_year
elif program == "4":
    import Love_Calculator
elif program == "5":
    import Treasure_island_game
elif program == "6":
    import Hangman_game
elif program == "7":
    import Caesar_cipher
elif program == "8":
    import BlackJack_game
elif program == "9":
    import Rock_paper_scissors_game
elif program == "10":
    import Treasure_map_game
elif program == "11":
    import Password_generator
else:
    print("End of choosing")
     