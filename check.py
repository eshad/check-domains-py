#!/usr/bin/python
import pythonwhois
domains = []


available = []
unavailable = []


def getDomains():
    with open('domains.txt', 'r+') as f:
        for domainName in f.read().splitlines():
            domains.append(domainName)

def run():   
    for dom in domains:
        if dom is not None and dom != '':
            details = pythonwhois.get_whois(dom)
	    date = ""
	    try:
		date = str(details['creation_date'])
		#print type (date)
	    except:
		print ""
	    #print "\n"
	    #print "\n"
	    
            if date != "":
                unavailable.append(dom)
            else:
                available.append(dom)
            date = ""
def printAvailability():
    print "-----------------------------"
    print "Unavailable Domains: "
    print "-----------------------------"
    for un in unavailable:
        print un
    print "\n"
    print "-----------------------------"
    print "Available Domains: "
    print "-----------------------------"
    for av in available:
        print av
    

if __name__ == "__main__":
    getDomains()
    run()
    printAvailability()


