from icmplib import ping


def fnTestConnectivity(siteAddress):
    objHost = ping(address=siteAddress, count=1)

    if objHost.is_alive:
        return "Address {}, ({}), can be reached".format(siteAddress, objHost.address)
    else:
        return "No connection to {}".format(siteAddress)

print("Please enter an address (just domain name)")
print(fnTestConnectivity(input("")))