from icmplib import ping


def fnTestConnectivity(siteAddress):
    objHost = ping(address=siteAddress, count=1)
    
    if objHost.is_alive:
        return "Site can be reached"
    else:
        return "No connection to site"

print("Please enter an address (just domain name)")
print(fnTestConnectivity(input("")))