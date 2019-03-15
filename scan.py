#!/usr/bin/python2


from dnsdumpster.DNSDumpsterAPI import DNSDumpsterAPI

#  User enters the domain to query for and stores results in respective variable
results = DNSDumpsterAPI({'verbose':True}).search(raw_input('DNSdumpster > '))

#  Iterator
num = 0

#  Little print function here
print "\n" + "= " * 17
print "\t sub domains"
print "= " * 17 + '\n'

#  lists all of the returned hosts for dns records
subs = results['dns_records']['host']

#  Number how DNS records returned
x = len(subs)
print "[+] Sub-domains Found: " + str(x)


#  For each result inside the dns_records, print the domain
for e in subs:
    
    print "[" + str(num+1) + "]" + " Returned Domain "
    print "- " * 10 + "\n"
    print "[+] Domain: " + results['dns_records']['host'][num]['domain']
    print "[+] IP Address: " + results['dns_records']['host'][num]['ip']
    print "[+] Header: " +  results['dns_records']['host'][num]['header']
    print "[+] Country: " +  results['dns_records']['host'][num]['country']
    print "[+] Provider: " +  results['dns_records']['host'][num]['provider'] + "\n"

    num = num + 1

