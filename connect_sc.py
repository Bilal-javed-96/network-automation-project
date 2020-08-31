from netmiko import ConnectHandler

def connect_sc():
    host_a = input("Enter the IP of device : ")
    user_a = input("Enter the username of device : ")
    pass_a = input("Enter the password of device : ")
    conf_file = input("Enter the name of config file : ")
    cisco_ios1={
        'device_type':'cisco_ios',
        'host':host_a,
        'username':user_a,
        'password':pass_a
    }
    print("Connecting to " + host_a)
    net_connect = ConnectHandler(**cisco_ios1)
    config_commands = conf_file + ".txt"

    output = net_connect.send_config_from_file(config_commands)
    print(output)

    output = net_connect.send_command('sh ip int brief')
    print(output) 
