from icmplib import traceroute, ping


def fnTestRoute(siteAddress):
    objHost = ping(address=siteAddress, count=1)
    objRoute = traceroute(address=siteAddress)

    if objHost.is_alive:
        print('Distance (ttl)    Address    Average round-trip time')
        intDistance = 0
        for hop in objRoute:
            if intDistance + 1 != hop.distance:
                print(f"{intDistance + 1}       Hop ({hop.address}) isn't responding")
            print(f'{hop.distance}       {hop.address}        {hop.avg_rtt} ms')
            intDistance = hop.distance
    else:
        print(f"No connection to {siteAddress}")

print("Please enter an address (just domain name)")
fnTestRoute(input(""))
