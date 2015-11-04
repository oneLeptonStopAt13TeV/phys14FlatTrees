import os

############################################
# Print all the subdirectoris in dpm
# starting from a base-directory
############################################


rfcommand = "/usr/bin/rfdir "
dpm_prefix = "/dpm/in2p3.fr/home/cms/phedex/store/user/"
user = os.popen("echo $USER").read().rstrip('\n')
#user = "kskovpen"
# New value can be changed here
#dpm_main_dir = "FlatTrees/MantaRay-patch7-pfcand"
#dpm_main_dir = "FlatTree/MantaRay-patch8-v20151025"
dpm_main_dir = "FlatTrees/test-ak10"


# From a list of directory, create a new list containing all subdirectories
# Return False if no subdirectories are found

def subdirlist(list, newlist):
    foundAtLeastOne = False
    for d in list:
       command = rfcommand + " "+ d
       out = os.popen(command).read()
       found = False
       for i in out.split('\n'):
		#print "i = ", i
		a = i.split(" ")
		type = a[0].split()
		isDir = False
		if len(type)>0 and len(type[0].split())>0 and type[0][0]=='d': 
			#print "type", type
			#print type[0]
			isDir = True
		#print a[0]
		if(a[-1] != "" and isDir) : 
			newlist.append(d+"/"+a[-1])
			found = True
			
       if not found: newlist.append(d)
       else: foundAtLeastOne = True

    return foundAtLeastOne



base_dir = dpm_prefix+user+"/"+dpm_main_dir+"/"

print "Dear", user, "the script will look the subdirectories of ", base_dir
print " .. It can up take few minutes if the disks are busy and if therer are many subdir ..."

command = rfcommand + " " + base_dir
print base_dir
#out = os.popen(command).read()
#print out

list = [base_dir]
needed = True
while(needed):
    newlist = []
    needed = subdirlist(list,newlist)
    list = newlist
    #print needed
    #print list


print "List of subdirectoris"
for i in list:
    print i



