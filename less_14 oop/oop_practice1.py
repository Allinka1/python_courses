class Element:

    def __init__(self, t_melting, t_fumes, scale):
        self.t_melting = t_melting
        self.t_fumes = t_fumes
        self.scale = scale


    def convertation_scale(self, t):
        s = self.scale.upper()
        if s == 'F':
            t = (t - 32) * (5/9)
            return t
        elif s == 'K':
            t = t - 273.15
            return t
        elif s == 'C':
            return t


    def agg_state(self, t):
        t = self.convertation_scale(t)

        print(t)

        if t >= self.t_melting and t < self.t_fumes:
            return 'I am liquid'
        elif t < self.t_melting:
            return 'I am solid'
        elif t > self.t_fumes:
            return 'I am steam'



class Oxygen(Element):
    pass


result1 = Oxygen(-218, -182, 'C')
print(result1.agg_state(-217, 'K'))
