class IP4Addres(object):
    def __init__(self,addres):
        self.addres = addres
    def getnetwork(self):
        t = list(self.addres)
        net = t[0]
        return net
    def getmask(self):
        u = list(self.addres)
        intmask = u[1]
        tempbin = ['0' for i in range(32)]
        for i in range(intmask):
            tempbin[i]='1'
        tempmask = [''.join(tempbin[i*8:i*8+8]) for i in range(4)]
        tempmask = [str(int(s,2)) for s in tempmask]
        return '.'.join(tempmask)
    def getaddress(self):
        ipadd = str(self.getnetwork())
        submask = self.getmask()
        address = [ipadd,submask]
        return address
if __name__=='__main__':
    ipv4 = IP4Addres(([10,0,1,7],25))
print(ipv4.getmask())
