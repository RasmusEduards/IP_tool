import ipaddress

cidr1 = input("Enter CIDR range 1: ")

cidr2 = input("Enter CIDR range 2: ")


n1 = ipaddress.ip_network(cidr1)
n2 = ipaddress.ip_network(cidr2)

if n1.overlaps(n2) == True:
	print("CIDRs are overlapping!")
else:
	print("CIDRs are NOT overlapping!")

