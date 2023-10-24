import random

start = True
while start is True:
    die = input("Would You Like Roll The Die (Yes/No) :")
    roll = random.randint(1,6)
    if die == 'Yes' or die == 'Y' or die == 'yes' or die == 'y':
        print("You Got A :",roll)
        if roll == 1:
            print("  .-------.")   
            print(" /   o   /|")    
            print("/_______/o|") 
            print("| o     | |") 
            print("|   o   |o/") 
            print("|     o |/")  
            print("'-------'")  
        elif roll == 2:
            print("  .-------.")   
            print(" / o   o /|")    
            print("/_______/ |") 
            print("| o   o |o|") 
            print("|       | /") 
            print("| o   o |/")  
            print("'-------'")  
        elif roll == 3:
            print("  .-------.")   
            print(" / o o o /|")    
            print("/_______/ |") 
            print("|     o |o|") 
            print("|   o   | /") 
            print("| o     |/")  
            print("'-------'")  
        elif roll == 4:
            print("  .-------.")   
            print(" / o   o /|")    
            print("/_o___o_/ |") 
            print("| o   o |o|") 
            print("| o   o | /") 
            print("| o   o |/")  
            print("'-------'")  
        elif roll == 5:
            print("   .-------.")   
            print("  / o   o /|")    
            print(" /   o   / |")
            print("/_o___o_/  |") 
            print("| o   o |o |") 
            print("| o   o | /") 
            print("| o   o |/")  
            print("'-------'") 
        elif roll == 6:
            print("  .-------.")   
            print(" / o o o /|")    
            print("/_o_o_o_/ |") 
            print("| o   o |o|") 
            print("|       | /") 
            print("| o   o |/")  
            print("'-------'")  
            
            
            

    