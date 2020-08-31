from pprint import pprint
import json
def info_inp():
    interfaces=[]
    in_ee_no=int(input("Enter the number of Fast Ethernet interfaces"))
    in_fe_no=int(input("Enter the number of Fast Ethernet interfaces"))
    in_ge_no=int(input("Enter the number of Gigabit Ethernet interfaces"))
    if in_ee_no > 0:
        for i in range(in_ee_no):
            name=None
            description=None
            vlan=None
            mode=None
            max_mac=None
            violation_action=None
            name=("Ethernet " + input("Enter the number of Ethernet interface ( Example : 0/1, 1/0) : ") )
            description=input("Enter " + name + " Description : ")
            vlan=input("Enter the vlan number for " + name +" : ")
            mode=input("Enter the mode (access/trunk) for " + name +" : ")
            max_mac=input("Enter the maximum MAC allowed in case of Mac_Flooding for " + name +" : ")
            violation_action=input("Enter the action (restrict / shutdown) in case of Mac_Flooding on " + name +" : ")
            inter={ 'name':name,
                    'description':description,
                    'vlan':vlan,
                    'mode':mode,
                    'max_mac':max_mac,
                    'violation_action':violation_action
                }
            interfaces.append(inter)
    else:
        print("No Ethernet Interface")
    if in_fe_no > 0:
        for i in range(in_fe_no):
            name=None
            description=None
            vlan=None
            mode=None
            max_mac=None
            violation_action=None
            name=("FastEthernet " + input("Enter the number of FastEthernet interface ( Example : 0/1, 1/0) : ") )
            description=input("Enter " + name + " Description : ")
            vlan=input("Enter the vlan number for " + name +" : ")
            mode=input("Enter the mode (access/trunk) for " + name +" : ")
            max_mac=input("Enter the maximum MAC allowed in case of Mac_Flooding for " + name +" : ")
            violation_action=input("Enter the action (restrict / shutdown) in case of Mac_Flooding on " + name +" : ")
            inter={ 'name':name,
                    'description':description,
                    'vlan':vlan,
                    'mode':mode,
                    'max_mac':max_mac,
                    'violation_action':violation_action
                }
            interfaces.append(inter)
    else:
        print("No Fast Ethernet Interface")
    if in_ge_no > 0:
        for i in range(in_ge_no):
            name=None
            description=None
            vlan=None
            mode=None
            max_mac=None
            violation_action=None
            name=("gi" + input("Enter the number of GIgEthernet interface ( Example : 0/1, 1/0) : ") )
            description=input("Enter " + name + " Description : ")
            vlan=input("Enter the vlan number for " + name +" : ")
            mode=input("Enter the mode (access/trunk) for " + name +" : ")
            max_mac=input("Enter the maximum MAC allowed in case of Mac_Flooding for " + name +" : ")
            violation_action=input("Enter the action (restrict / shutdown) in case of Mac_Flooding on " + name +" : ")
            inter={ 'name':name,
                    'description':description,
                    'vlan':vlan,
                    'mode':mode,
                     'max_mac':max_mac,
                     'violation_action':violation_action
                }
            interfaces.append(inter)
    else:
        print("Enter Gigibit interfaces")

    f_name=input("Enter the name of info file : ")
    file_name=f_name+".txt"
    with open (file_name,'w') as f:
        f.write(json.dumps(interfaces,indent=4))
    pprint(interfaces)