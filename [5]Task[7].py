class Kangaroo(object):

    def __init__(self, name, contents=None):
        self.name = name
        self.pouch_contents = contents or []

    def __str__(self):
        t = [self.name + ' has pouch contents:']
        for i in self.pouch_contents:
            s = '' + object.__str__(i)
            t.append(s)
        return ''.join(t)

    def put_in_pouch(self, item):
        self.pouch_contents.append(item)


kanga = Kangaroo('Kanga')
roo = Kangaroo('Roo')
kanga.put_in_pouch('roo')

print(kanga)
print(roo)
