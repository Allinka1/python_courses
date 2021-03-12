class Oxygen:
    t_melting = - 218
    t_fumes = - 182

    def convertation_scale(self, t, s):
        s = s.upper()
        if s == 'F':
            t = (t - 32) * (5/9)
            return t
        elif s == 'K':
            t = t - 273.15
            return t
        elif s == 'C':
            return t


    def agg_state(self, t, s):
        t = self.convertation_scale(t, s)

        print(t)

        if t >= self.t_melting and t < self.t_fumes:
            return 'I am liquid'
        elif t < self.t_melting:
            return 'I am solid'
        elif t > self.t_fumes:
            return 'I am steam'

number = Oxygen()
print(number.agg_state(-217, 'K'))