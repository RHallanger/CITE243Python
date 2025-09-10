import math

ipList = None
subList = None
option = ''
skipBits = 0
networkBits = -1
maskList = [0, 0, 0, 0]

############### Functions

def addDisplay(varList): #just converts the list into your typical IPv4 format
    varDisplay = ''
    for i in range(len(varList)):
        if i == 0:
            varDisplay = str(varList[i])
        else:
            varDisplay = varDisplay + '.' + str(varList[i])
    return varDisplay

def addBuilder(varList): #Loop function to assemble an IPv4 address
    varList = [0, 0, 0, 0]
    varDisplay = ''
    for i in range(4):
        var = -1
        while (int(var) < 0) or (int(var) >= 256):
            print(f'\n\nPlease enter a value for octet {str(i+1)}:')
            varDisplay = addDisplay(varList)
            print(varDisplay)

            try:
                var = int(input('> '))
            except:
                print('\n\nERROR: Data type not accepted, please use integers.')

        varList[i] = var
    return varList

def subBuilder(networkBits): #Similar to the addBuilder, but with tweaks for subnet mask... Doesn't actually make sandwhichs, sorry.
    varList = [0, 0, 0, 0]
    acceptedSubValues = [0, 128, 192, 224, 240, 248, 252, 254, 255]
    varDisplay = ''
    networkBits = 0
    for i in range(4):
        var = 999
        while var not in acceptedSubValues:
            print(f'\n\nPlease enter a value for octet {str(i+1)}:')
            varDisplay = addDisplay(varList)
            print(varDisplay)

            try:
                var = int(input('> '))
            except:
                print('Data type not accepted, please use integers.')

            if var not in acceptedSubValues:
                print('\n\nERROR: Not a subnet value.')

        varList[i] = var #For display

        match var: #Convert var into network bits
            case 128:
                var = 1
            case 192:
                var = 2
            case 224:
                var = 3
            case 240:
                var = 4
            case 248:
                var = 5
            case 252:
                var = 6
            case 254:
                var = 7
            case 255:
                var = 8

        networkBits += var
        if var < 8:
            break
    return networkBits

############# Start of the program

print('This is a basic Subnet Calculator.')
print('To use this program, you will enter an IP address.\nSelect whether you are using CIDR or subnet mask and enter those values.\n\nThe information returned will be\nNetwork ID:\nFirst Usable Host:\nLast Usable Host:\nBroadcast IP:\nTotal Hosts:\nSubnet Mask:\nCIDR:')
input('\n\nWhen you are ready...\nPress any button to continue...')
ipList = addBuilder(ipList)
print('\n'*100)
print('Your IP address is: ' + addDisplay(ipList))
while option not in ['subnet', 'cidr']:
    print('\nWhat notation is your network in? Use "SUBNET" or "CIDR" to respond.')
    option = input('> ')
    option = option.lower()

if option == 'cidr':
    while (networkBits < 0) or (networkBits > 32):
        print('Please input a CIDR digit.')
        try:
            networkBits = int(input('> '))
        except:
            print('Data type not accepted, please use integers.')

else:
    networkBits = subBuilder(networkBits)


showBits = networkBits #Saving this for later so that I can show them CIDR and Subnet Mask
while networkBits >= 8: #See what octets we can skip and which one is split between host and subnet bits
    networkBits -= 8
    skipBits += 1

networkBits = 8 - networkBits #It was doing the subnet bits rather than host down below...
octetIP = ipList[skipBits] #This is our working subnet
networkBits = 2 ** networkBits
ipList[skipBits] = (math.floor(octetIP/networkBits)*networkBits)

for i in range((skipBits+1), len(ipList)): #This will convert all other octets after to 0
    ipList[i] = 0

print('\n' * 100)
print('Network ID: ' + addDisplay(ipList))
ipList[-1] += 1
print('First Host: ' + addDisplay(ipList))
ipList[-1] -= 1

ipList[skipBits] = (ipList[skipBits] + networkBits) -1 #This is technically the broadcast, but too lazy to make a var and move it lower...

for i in range((skipBits+1), len(ipList)): #This will convert all octets with 0 subnet bits to 255
    ipList[i] = 255

ipList[-1] -= 1 #Simple, subtract 1 to the last octet's host...
print('Last Host: ' + addDisplay(ipList))

ipList[-1] += 1
print('Broadcast IP: ' + addDisplay(ipList))

print('Total Hosts: ' + str((2**(32 - showBits))-2))
print('CIDR: ' + str(showBits))

for i in range(skipBits): #This will convert all other octets after to 255
    showBits -= 8
    maskList[i] = 255

match showBits: #Revert networkBits into binary digits...
    case 7:
        maskList[skipBits] = 254
    case 6:
        maskList[skipBits] = 252
    case 5:
        maskList[skipBits] = 248
    case 4:
        maskList[skipBits] = 240
    case 3:
        maskList[skipBits] = 224
    case 2:
        maskList[skipBits] = 192
    case 1:
        maskList[skipBits] = 128

print('Subnet Mask: ' + addDisplay(maskList))
input('\nPress any button to continue...')