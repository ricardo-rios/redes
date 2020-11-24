import sys
import subprocess

#Checking IP reachability
def ip_reach(list):

    for ip in list:
        ip = ip.rstrip("\n")
        
        ping_reply = subprocess.call('ping %s -c 2' % ip, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
               
        if ping_reply == 0:
            print("\n* {} is reachable :)\n".format(ip))
            continue
        
        else:
            print('\n* {} not reachable :( Check connectivity and try again.'.format(ip))
            sys.exit()



if __name__ == "__main__":

   l = ['3.237.177.207']
   ip_reach(l)



