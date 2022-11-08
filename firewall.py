from email.contentmanager import raw_data_manager
import sys
import random
import re

class Firewall:
    
    black_list = {}
    value_of_dict = []
      
    def add_to_black_list(self, ips: list):
        if(type(ips) == type([])):
            for ip in ips:
                if(self.is_black_listed((ip))):
                    print(f"{ip} adress is already blacklisted")
                else:
                    self.black_list[ip] = self.value_of_dict
        else:
            print(f"argument type provided is {type(ips)}. It must be a {type([])}. Ignoring it.") 
    
    def check_rule(self, rule):
        try:
            _ = self.black_list[rule]
            print(f"blocked by rule {rule}")
            return True
        except KeyError:
             return False
    
    def is_black_listed(self, ip):
        ip_blocks = ip.split('.')
        print(f"Checking ip {ip}")
        if not self.check_rule(f"{ip_blocks[0]}.*.*.*") and not self.check_rule(f"{ip_blocks[0]}.{ip_blocks[1]}.*.*") and not self.check_rule(f"{ip_blocks[0]}.{ip_blocks[1]}.{ip_blocks[2]}.*") and not self.check_rule(f"{ip_blocks[0]}.{ip_blocks[1]}.{ip_blocks[2]}.{ip_blocks[3]}"):
            print("allowed")
            return False
        return True
       
    
    def print_black_list(self):
        print("black list is:\n==============================================")
        for entry in self.black_list.keys():
            print(f"\n{entry}")
        print("\n==============================================")
    
    def print_size_of_black_list(self):
        print(f"size of the dictonary with {len(self.black_list)} entries is: {sys.getsizeof(self.black_list)}" )
        total_size = 0
        for key in self.black_list.keys():
            total_size = total_size + sys.getsizeof(self.black_list[key])
        print(f"size of the values with val={self.value_of_dict}: {total_size}")
    
firewall = Firewall()

firewall.print_size_of_black_list()

first_blocked_ip = "123.422.444.*"
firewall.add_to_black_list([first_blocked_ip])
firewall.add_to_black_list(["123.1.*.*"])

print(f"First blocked ip is: {first_blocked_ip}")

firewall.print_size_of_black_list()

blocked_list = []

for _ in range(1000):
    blocked_list.append(f"{str(random.randint(0,255))}.{str(random.randint(0,255))}.{str(random.randint(0,255))}.{str(random.randint(0,255))}")

firewall.add_to_black_list(blocked_list)

#firewall.print_black_list()
firewall.print_size_of_black_list()

#firewall.is_black_listed(first_blocked_ip)
#firewall.is_black_listed("123.422.444.1")
#firewall.is_black_listed("123.422.444.3")
#firewall.is_black_listed("123.422.444.111")
#firewall.is_black_listed("123.422.444.444")
#firewall.add_to_black_list(["123.422.444.444"])
#firewall.is_black_listed("123.422.444.5")
#firewall.is_black_listed("123.1.20.5")
#firewall.is_black_listed("123.2.220.5")