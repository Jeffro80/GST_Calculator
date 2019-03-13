# Author name: Jeff Mitchell
# Date: 13 March 2015
# Version 0.4
# Quick Desc: Program for calculating GST values

# To fix:
# Need to check for bugs - try breaking it


# set the GST rate
gst_rate = 0.15

# calculate the total including GST from a GST exclusive total
def total_incl_gst(amount): 
    gst_incl = amount + (amount * gst_rate)
    gst_component = gst_value_from_exclusive(amount)
    return gst_incl, gst_component

# calculate the total excluding GST from a GST inclusive total
def total_excl_gst(amount): 
    gst_excl = amount - (amount * (3/23))
    gst_component = gst_value_from_inclusive(amount)
    return gst_excl, gst_component

# calculate the GST component from a GST inclusive total
def gst_value_from_inclusive(amount): 
    gst_value = amount * (3/23)
    return gst_value

# calculate the GST component from a GST exclusive total
def gst_value_from_exclusive(amount): 
    gst_value = amount * gst_rate
    return gst_value

# display options to user
def options_list():
    print("""
What would you like to do:\n
1. Calculate from a GST exclusive amount
2. Calculate from a GST inclusive amount """)
    print("3. I'd like to set the GST amount (currently %.2f%%)" %(gst_rate*100))
    print("4. Quit\n")
    
# get user selection
def user_selection():
    correct = False
    while correct == False:
        while True: # check that a number is entered
            try:
                local_selection = int(input("What would you like to do? Please press either '1'. '2', '3' or '4' "))
            except ValueError:
                print("\nSorry I cannot understand that. Please enter a number.\n")
                continue
            else:
                break

        if local_selection < 0 or local_selection > 4:
            print("\nThat is not a valid selection. Please try again.\n")
            correct = False
        else:
            correct = True
    return local_selection

# check if user wants to repeat
def user_repeat(selection):
    local_selection = selection
    repeat = input("\nWould you like to calculate another total y/n? ")
    repeat = repeat.lower()
    if repeat == "n":
        local_selection = False
    elif repeat == "y":
        print("")
        options_list()
        local_selection = user_selection()
    else:
        print("\nThat is not a valid selection. Please try again")
        user_repeat(local_selection)
    return local_selection

print("\t\t\tGST Calculator")
print("Version 0.4")
print("By Jeff Mitchell, March 2015")

options_list()
selection = user_selection()

while user_selection !=4: 
    if selection == 1:
        if selection == 4:
            break
        while True:
            try:
                start_amount = float(input("\nWhat is your starting amount (excluding GST)? "))
            except ValueError:
                print("\nSorry, I cannot understand that. Please enter a number.\n")
                continue
            else:
                break
        gst_incl_total, gst_component = total_incl_gst(start_amount)
        print("\nGST excusive price: %.2f" %start_amount)
        print("GST component: %.2f" %gst_component)
        print("\nYour total including GST is %.2f" %gst_incl_total)
        
        # Check if they want to repeat with a new total
        selection = user_repeat(selection)
    elif selection == 2:
        if selection == 4:
            break
        while True:
            try:
                start_amount = float(input("\nWhat is your starting amount (including GST)? "))
            except ValueError:
                print("\nSorry, I cannot understand that. Please enter a number.")
                continue
            else:
                break
        gst_excl_total, gst_component = total_excl_gst(start_amount)
        print("\nGST inclusive price: %.2f" %start_amount)
        print("GST component: %.2f" %gst_component)
        print("\nYour total excluding GST is %.2f" %gst_excl_total)

        # Check if they want to repeat with a new total
        selection = user_repeat(selection)
    elif selection == 3:
        if selection == 4:
            break
        while True:
            try:
                gst_rate = float(input("\nWhat is the GST rate (to three decimal places e.g. for 15% type 0.150)? "))
            except ValueError:
                print("\nSorry, I cannot understand that. Please enter a number.")
                continue
            else:
                break
        print("The new GST rate is %.3f\n" %gst_rate)
        options_list()
        selection = user_selection()
    else:
        print("\nOk, goodbye\n")
        break
   
input("\nPress enter to exit")    

