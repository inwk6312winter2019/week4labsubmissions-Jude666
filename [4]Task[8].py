import os, string
def all_files(dirf):
    musiclist = []
    for x, y, z in os.walk(dirf):
        if len(z) > 0:
            for i in z:
                if i[-4:-1] == 'mp3':
                    musiclist.append(x+'/'+i)
    return musiclist

def find_dups(musiclist):
    d = dict()
    for x in musiclist:
        x = x.replace(' ', '\ ')
        for i in "(){}[]&,';":
            x = x.replace(i,"\\"+i)
        f = os.popen('md5sum '+x)
        hashed = f.read()
        d[hashed[:32]] = d.get(hashed[:32], [])+[x]
        f.close()
        print(x)
    return d
