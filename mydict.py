class Dict(dict):
    '''
     Simple dict but also support access as x.y style
     
     >>> d1=Dict()
     >>> d1['x']=100
     >>> d1.x
     100
     >>> d1.y=200
     >>> d1['y']
     200
     >>> d2=Dict(a=1,b=2,c='3')
     >>> d2.c
     '3'
    '''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(r"'Dick is ' %s" % item)

    def __setattr__(self, key, value):
        self[key] = value


if __name__ == '__main__':
    import doctest
    doctest.testmod()
