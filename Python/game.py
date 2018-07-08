#-------------------------------------
# Base Inputs
#-------------------------------------

#Imports-----------------------------
import warnings
import pandas
import os
import sys
import numpy as np
import pandas as pd
from time import sleep
#------------------------------------

#Functions--------------------------

#-----------------------------------

message = 'Base Inputs Loaded'
print message
#-------------------------------------
# End of Base Inputs
#-------------------------------------
#-------------------------------------
# Escape Room Program
#-------------------------------------
'''
This program is a simple escape room
It takes a few inputs 'look', 'use'
The goal is to find the key to escape the room
'''

#function to try and escape to room
def escape_room():
  acceptable_choices = ['search','examine','use','stop']
  inventory = []
  look_general = ['door','table','bookcase','emergency axe cabinet']
  #all possible searches
  search_dict = {
    'door':'lock'
    ,'table':'complicated puzzles'
    ,'suspicious dictionary':'key'
    ,'emergency axe cabinet':'axe'
    ,'bookcase':'suspicious dictionary'
  }
  #examine should have a list of all possible inventory and look_general items
  examine_dict= {
    'table':'A normal wooden table.  It looks quite old'
    ,'door': 'A strudy wooden door.  It looks new'
    ,'lock':'A shiny lock in the door.  You will need to find the key'
    ,'key':'A shiny golden key.  You found it!  Now open the door'
    ,'axe':'A fire axe...this isn\'t part of the game.  It must be for emergencies...what are you thinking of doing....'
    ,'bookcase':'A sturdy wooden bookcase, contains a bunch of dictionaries, and one suspicious book on the history of escape rooms'
    ,'suspicious dictionary':'Volume E: This dictionary is slightly open like there\'s something obviously inside it'
    ,'complicated puzzles':'A bunch of complex puzzles...it looks like you could try working on them at the table'
  }
  possible_inventory_items = ['key','axe','complicated puzzles']
  easy_ending = '''
  The door is unlocked
  You made it out the easy way
  '''
  hard_ending = '''
  CONGRATULATIONS!!!!!!!

  You have unlocked the door!
  '''
  door_unlocked = False
  print '''

  #############################################################
  Welcome to the Escape Room!
  You're testing out our new escape room game for us.
  I've locked the door, you're goal is to find the key
  Say stop when prompted and I'll open the door early for you
  #############################################################

  '''
  sleep(5)
  print'''
  #####################################################
  Oh! One more thing...there's an axe in the room...
  It's not part of the game...we haven't gotten around
  to taking it out yet. So just avoid it for now!
  I'll check on you in a bit to see how youre doing
  Good luch!
  ######################################################

  '''
  first_miss = 0
  while door_unlocked == False:
    sleep(1)
    print ' '
    print ' '
    print "You can the see: "
    for i in look_general:
      print i
    if len(inventory)>0:
      print 'You are holding: '+'/'.join(inventory)
    if first_miss == 1:
      print "Your options are : " + '/'.join(acceptable_choices)
    choice = raw_input('What do you want to do? ')
    #wrong choice restarts loop
    if choice not in acceptable_choices:
      print ' '
      sleep(1)
      if first_miss == 0:
        first_miss +=1
        print'''
###############################################
Oh! I forgot to mention...
You can only: %s
My bad! Try again!
##############################################
        '''%('/'.join(acceptable_choices))
        sleep(1)
      elif first_miss==1:
        print'''
###############################################
Remember!
You can only: %s
Try again!
##############################################
        ''' %('/'.join(acceptable_choices))
        sleep(1)
    #user decides to end the loop
    elif choice == 'stop':
      print ' '
      sleep(1)
      print 'Ok ok...I\'ll open the door for you'
      sleep(1)
      door_open = True
      print easy_ending

    #user searches
    elif choice == 'search':
      print ' '
      print 'You can see the following: '
      for i in look_general:
        print i
      search_choice = raw_input('What do you want to search? ')
      if search_choice not in look_general:
        print "You don\'t see that"
      else:
        if search_choice not in search_dict.keys():
          print "You don\'t find anything new"
        else:
          discovery = search_dict[search_choice]
          del search_dict[search_choice]
          print "You can now see the following: " + discovery
          look_general.append(discovery)
          if discovery in possible_inventory_items:
            inventory.append(discovery)
            print "You have picked up the " + discovery

    #user examines
    elif choice == 'examine':
      print ' '
      print 'You can see the following: '
      for i in look_general:
        print i
      if len(inventory)>0:
        print 'You are holding the following: '+'/'.join(inventory)
      examine_choice = raw_input('What would you like to examine? ')
      if examine_choice not in look_general and examine_choice not in inventory:
        print 'You couldn\'t find that'
      else:
        print 'You take a moment to examine it'
        sleep(1)
        print examine_dict[examine_choice]

    #user chooses to use
    elif choice == 'use':
      print ' '
      if len(inventory)==0:
        print "You don\'t have anything to use yet"
      else:
        print 'You have the following: '+'/'.join(inventory)
        inv_choice = raw_input('What would you like to use? ')
        if inv_choice not in inventory:
          print "Sorry, you don\'t have that to use"
        else:
          print ' '
          print 'You can see the following: '
          for i in look_general:
            print i
          use_choice = raw_input("What would you like to use the " + inv_choice + " on? ")
          if use_choice not in look_general:
            print "Sorry, you don\'t see that"
          else:
            if inv_choice == 'key' and use_choice == 'lock':
              door_unlocked = True
              sleep(1)
              print 'The lock turns...'
              sleep(1)
              print hard_ending
            elif inv_choice == 'key' and use_choice in ['door','severely damaged door']:
              print "Hm...maybe if you tried the lock?"
            elif inv_choice == 'axe' and use_choice == 'table':
              print "You have successfully...destroyed the table"
              look_general.remove('table')
              look_general.append('table remains')
              examine_dict['table remains'] = 'The table is just a pile of wood...might be worth searching...'
              if 'key' not in inventory:
                search_dict['table remains'] = 'key'
              print "You can now see the remains of the table..."
            elif inv_choice == 'axe' and use_choice == 'bookcase':
              print "You have successfully...destroyed the bookcase"
              look_general.remove('bookcase')
              look_general.append('bookcase remains')
              examine_dict['bookcase remains'] = 'The table is just a pile of wood...might be worth searching...'
              search_dict['bookcase remains'] = ['suspicious dictionary']
              print "You can now see the remains of the bookcase..."
            elif inv_choice == 'axe' and use_choice == 'suspicious dictionary':
              print "You have successfully...destroyed the suspicious looking Volume E dictionary"
              look_general.remove('suspicious dictionary')
              if 'key' not in inventory:
                del search_dict[use_choice]
                look_general.append('key')
                print "You have found the "+ 'key'
                inventory.append(discovery)
                print "You have picked up the " + discovery

              print "You can now see the remains of the bookcase..."
            elif inv_choice == 'axe' and use_choice == 'door':
              print "The door is damaged"
              look_general.remove('door')
              look_general.append('damaged door')
              examine_dict['damaged door'] = 'This door has a massive hole where the axe just landed...'
              search_dict['damaged door'] = 'lock'
            elif inv_choice == 'complicated puzzles' and use_choice != 'table':
              print "Trying using the puzzles at the table"
            elif inv_choice == 'complicated puzzles' and use_choice == 'table':
              print "After working at the puzzles for just under an hour, they seem to want you to look up the word \'Escape\' in a dictionary"
            elif inv_choice == 'axe' and use_choice == 'damaged door':
              print "The door is REALLY damaged"
              sleep(1)
              print"""

##############################################################
Ok look, I'm not supposed to do this but....
the key is in the book, ok...just...
put away the axe, get the key from the book, and we can forget
about this whole "destroying the door with an axe" business
##############################################################

              """
              look_general.remove('damaged door')
              look_general.append('severely damaged door')
              examine_dict['severely damaged door'] = 'This door...if one could still consider if a door, is damaged beyond repair'
              search_dict['severely damaged door'] = 'lock'
            elif inv_choice == 'axe' and use_choice == 'lock':
              print "Doesn\'t make a dent in the lock...I guess you could always try the door...wait...hold on..."
            elif inv_choice == 'axe' and use_choice == 'severely damaged door':
              door_unlocked = True
              sleep(1)
              print '''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Despite the pleas from the game developer you continue to swing at the door
You hack at the last remaining bits of wood which impetuously stand between you your goal
With every stroke you laugh heartily at your ability to subvert the game developer's wishes
What little is the left standing of the door finally crumbles before might of your will
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
              '''
              sleep(1)
              print '...ya...sure...ya that works...'
              sleep(1)
              print ' '
              print hard_ending
            elif inv_choice == 'axe' and use_choice == 'emergency axe cabinet':
              print 'That\'s probably for the best..what were you going to use it on anyway..the door?'
              search_dict['emergency axe cabinet']='axe'
            else:
              print "That doesn\'t seem to do anything"

escape_room()
