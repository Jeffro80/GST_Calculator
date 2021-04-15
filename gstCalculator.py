# Author name: Jeff Mitchell
# Date: 28 March 2019
# Version 0.5
# Quick Desc: Program for calculating GST values


import admintools as ad
import sys


def calc_from_gst_excl(gst_rate, records_dict):
    """Get gst_incl_total and gst_component and display.
    
    Calculates the GST inclusive amount and the GST component from a GST
    exlusive amount. Displays the totals to the user.
    
    Args:
        gst_rate (float): GST rate to apply.
    """
    while True:
        try:
            start_amount = float(input('\nWhat is your starting amount '
                                       '(excluding GST)? '))
        except ValueError:
            print('\nSorry, I cannot understand that. Please enter a number '
                  '.\n')
            continue
        else:
            break
    gst_incl_total, gst_component = total_incl_gst(start_amount, gst_rate)
    print('\nGST-exclusive price: ${:.2f}'.format(start_amount))
    display_gst_rate(gst_rate)
    print('GST component: ${:.2f}'.format(gst_component))
    print('Your total including GST is ${:.2f}'.format(gst_incl_total))
    # Add check if want to add item to records_dict


def calc_from_gst_incl(gst_rate, records_dict):
    """Get gst_excl_total and gst_component and display.
    
    Calculates the GST exlusive amount and the GST component from a GST
    inclusive amount. Displays the totals to the user.
    
    Args:
        gst_rate (float): GST rate to apply.
    """
    while True:
        try:
            start_amount = float(input('\nWhat is your starting amount '
                                       '(including GST)? '))
        except ValueError:
            print('\nSorry, I cannot understand that. Please enter a '
                  'number.')
            continue
        else:
            break
    gst_excl_total, gst_component = total_excl_gst(start_amount, gst_rate)
    print('\nGST-inclusive price: ${:.2f}'.format(start_amount))
    display_gst_rate(gst_rate)
    print('GST component: ${:.2f}'.format(gst_component))
    print('Your total excluding GST is ${:.2f}'.format(gst_excl_total))
    # Add check if want to add item to records_dict


def display_gst_rate(gst_rate):
    """Displays the GST rate to the screen.
    
    Args:
        gst_rate (float): Current GST rate.
    """
    percent = gst_rate * 100
    print('Current GST rate: {:.2f}, ({:.2f}%)'.format(gst_rate, percent))


def gst_value_from_inclusive(amount, gst_rate):
    """Calculate GST component from a GST inclusive total.
    
    GST amount calculated as amount - (1 + gst_rate)).
    
    Args:
        amount (float): GST inclusive amount
        gst_rate (float): GST rate to apply.
        
    Returns:
        gst_component (float): Calculated GST component.
    """          
    return amount - (amount / (1 + gst_rate))


def help_menu():
    """Display the requested help information."""
    repeat = True
    low = 1
    high = 5
    while repeat:
        try_again = False
        help_menu_message()
        try:
            action = int(input('\nPlease enter the number for your '
                               'selection --> '))
        except ValueError:
            print('Please enter a number between {} and {}.'.format(low, high))
            try_again = True
        else:
            if action < low or action > high:
                print('\nPlease select from the available options ({} - {})'
                      .format(low, high))
                try_again = True
            elif action == low:
                pass # To Be Written
            elif action == 2:
                pass # To Be Written
            elif action == 3:
                pass # To Be Written
            elif action == 5:
                pass # To Be Written
            elif action == high:
                repeat = False
        if not try_again:
            repeat = ad.check_repeat_help()


def help_menu_message():
    """Display the help menu options."""
    print('\nPlease enter the number for the item you would like help on:\n')
    print('1: <TBC>')
    print('2: <TBC>')
    print('3: <TBC>')
    print('4: <TBC>')
    print('5: Exit Help Menu')


def item_constructor():
    """Create an empty dict for storing record_dict item values.
    
    Returns:
        item (dict): Empty dict with required keys.
    """
    item = {}
    item['gst_exlusive_total'] = 0
    item['gst_inclusive_total'] = 0
    item['gst_rate'] = 0
    item['gst_component'] = 0
    item['item_desc'] = ''
    return item    


def main():
	# Initialise GST rate
    gst_rate = 0.15
    # Initialise records_dict
    records_dict = {}
    repeat = True
    low = 0
    high = 8
    while repeat:
        try_again = False
        main_message()
        try:
            action = int(input('\nPlease enter the number for your '
                               'selection --> '))
        except ValueError:
            print('Please enter a number between {} and {}.'.format(low, high))
            try_again = True
        else:
            if action < low or action > high:
                print('\nPlease select from the available options ({} - {})'
                      .format(low, high))
                try_again = True
            elif action == low:
                help_menu()
            elif action == 2:
                calc_from_gst_excl(gst_rate, records_dict)
            elif action == 3:
                calc_from_gst_incl(gst_rate, records_dict)
            elif action == 4:
                display_gst_rate(gst_rate)
                try_again = True
            elif action == 5:
                gst_rate = set_gst_rate(gst_rate)
                try_again = True
            elif action == 6:
                pass # Function to view all items
            elif action == 7:
                pass # Function to view individual item
            elif action == high:
                print('\nIf you have generated any files, please find them '
                      'saved to disk. Goodbye.')
                sys.exit()
            if not try_again:
                repeat = ad.check_repeat()
    input("\nPress enter to exit")


def main_message():
    """Display menu of options."""
    print('\n\n*************==========================*****************')
    print('\nGST Calculator version 0.5')
    print('Created by Jeff Mitchell, 2019')
    print('\nOptions:')
    print('\n1. Help Menu')
    print('2. Calculate from a GST-exclusive amount')
    print('3. Calculate from a GST-inclusive amount')
    print('4. Display GST rate')
    print('5. Set GST rate')
    print('6. View all saved items')
    print('7. View item in saved items')
    print('8. Quit\n')


def set_gst_rate(gst_rate):
    """Set the GST rate.
    
    Args:
        gst_rate (float): Current GST rate.
        
    Returns:
        gst_rate (float): New GST rate.
    """
    while True:
        try:
            gst_rate = float(input('\nWhat is the GST rate (to three decimal '
                                    'places e.g. for 15% type 0.150)? '))
        except ValueError:
            print('\nSorry, I cannot understand that. Please enter a number.')
            continue
        else:
            break
    display_gst_rate(gst_rate)
    return(gst_rate)


def total_excl_gst(amount, gst_rate):
    """Calculate total excluding GST.
    
    Calculates total exluding GST and returns the GST exlusive amount and the
    gst_component amount.
    
    Args:
        amount (float): GST inclusive amount
        gst_rate (float): GST rate to apply.
        
    Returns:
        gst_excl (float): GST exclusive total
        gst_component (float): GST component of total.
    """
    gst_component = gst_value_from_inclusive(amount, gst_rate)
    gst_excl = amount - gst_component
    return gst_excl, gst_component    


def total_incl_gst(amount, gst_rate): 
    """Calculate total including GST.
    
    Calculates total including GST and returns the GST inclusive amount and the
    gst_component amount.
    
    Args:
        amount (float): GST exlusive amount
        gst_rate (float): GST rate to apply.
        
    Returns:
        gst_incl (float): GST inclusive total
        gst_component (float): GST component of total.
    """
    gst_component = amount * gst_rate
    gst_incl = amount + (gst_component)
    return gst_incl, gst_component


if __name__ == '__main__':
    main()