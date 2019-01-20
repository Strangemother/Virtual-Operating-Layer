
class Config:

    def find(self, name):
        if os.path.exists(name):
            puts('discovered configure {}'.format(name))
            data = self.read(name)
            return data

    def write(self, value, name):
        vv=compile('{}\n'.format(value), name, 'eval')
        ff=open(name, 'wb')
        marshal.dump(vv, ff)
        ff.close()

    def read(self, name):
        stream = open(name, 'rb')
        br = b''
        for line in stream.readlines():
            br += line
        result = eval(marshal.loads(br))
        stream.close()
        return result
