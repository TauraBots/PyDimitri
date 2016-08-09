import pickle

TIME = 0

class Motion(object):
    def __init__(self):
        self.keyframes = []
        self.allframes = []
        self.period = 0.050
    def generate(self):
        self.allframes = []
        for i in range(len(self.keyframes)-1):
            self.allframes.append(self.keyframes[i])
            steps = int(self.keyframes[i][TIME] / self.period)
            for j in range(steps):
                frame = {}
                for joint_id in self.keyframes[i].keys():
                    frame[joint_id] = self.interpolate(\
                            self.keyframes[i][joint_id], self.keyframes[i+1][joint_id],
                            steps, j)
                self.allframes.append(frame)
        self.allframes.append(self.keyframes[-1])
        self.allframes[-1][TIME] = self.period

        #gambiarra period fix
        for frame in self.allframes:
            frame[TIME] = self.period

    def interpolate(self, start, end, steps, i):
        step = (end - start) / steps
        return start + step*i
    def save(self, filename):
        thefile = open(filename, 'w')
        pickle.dump(self.keyframes, thefile)
        thefile.close()
    def read(self, filename):
        thefile = open(filename, 'r')
        self.keyframes = pickle.load(thefile)
        thefile.close()
