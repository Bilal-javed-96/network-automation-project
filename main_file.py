from info_inp import info_inp
from config_file import config_file
from connect_sc import connect_sc
import webbrowser



while True:
    print("-----------------------------------------------------")
    print("----------------ZEUS AUTOMATION TOOL-----------------")
    print("----------------------------------------------------- " + '\n')
    print( "Press A or a to make a device info file " '\n' 
       "Press B or b to make a device configuration file " '\n'
       "Press C or c to connect to a device "'\n'
       "Press H or h for help "'\n'
       "Press Q or q to exit ")
    var_a = input("Enter  : ")
    if (var_a == 'A' or var_a =='a'):
        info_inp()
    elif (var_a == 'B' or var_a == 'b'):
        config_file()
    elif (var_a == 'C' or var_a == 'c'):
        connect_sc()
    elif (var_a == 'Q' or var_a == 'q'):
        break
    elif (var_a == 'H' or var_a == 'h'):
        webbrowser.open('https://blogs.cisco.com/developer/network-configuration-template', new=2)
        print("Opening tutorial")
    else:
        print("Enter valid option")


