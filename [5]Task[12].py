class subnetcal(object):
    def __init__(self,ipaddress):
        self.ipaddress = ipaddress

    def calculate_all(self):
        masknumber = self.ipaddress                 # hostnumber
        t = masknumber[1]
        k = 32-t
        hostnumber = 2**k-2


        add = list(self.ipaddress)
        maskint = add[1]                                # tempmask is submask address
        tempbin = ['0' for i in range(32)]
        for i in range(maskint):
            tempbin[i]='1'
        tempmask = [''.join(tempbin[i*8:i*8+8]) for i in range(4)]
        tempmask = [int(s,2) for s in tempmask]
        # mask = '.'.join(tempmask)

        network_add = add[0]                            # t is network address
        t = []
        for i in range(4):
            twoand= network_add[i] & tempmask[i]
            t.append(twoand)


        list_to_str = [str(i) for i in t]                   # re_form is the broadcast address
        x=[]
        for i in list_to_str:
            tb = bin(int(i,10)).lstrip('0b')
            x.append(tb.zfill(8))
        x = ''.join(x)
        p = []
        p.append(x[:maskint])
        for i in range(k):
            p.append('1')
        p = ''.join(p)
        re_form = [p[i*8:i*8+8] for i in range(4)]
        re_form = [(int(s,2)) for s in re_form]

        the_first_host = []
        the_first_host.append(x[:-1])
        the_first_host.append('1')
        the_first_host = ''.join(the_first_host)
        first_host = [the_first_host[i*8:i*8+8] for i in range(4)]
        first_host = [int(s,2) for s in first_host]

        the_last_host = []
        the_last_host.append(p[:-1])
        the_last_host.append('0')
        the_last_host = ''.join(the_last_host)
        last_host = [the_last_host[i*8:i*8+8] for i in range(4)]
        last_host = [int(s,2) for s in last_host]
        print("newwork address:%s, broadcast address:%s, first host:%s, last host:%s, hosts number:%s," %(t,re_form,first_host,last_host,hostnumber))

if __name__=='__main__':
    ipv4 = subnetcal(([192,168,35,7],21))
print(ipv4.calculate_all())
