class HighScores(object):
    def __init__(self, scores):
        self.scores = scores


    def latest(self):
        """Last added score to the scores list"""
        del self.scores[:len(self.scores)-1]
        return self.scores[0]

    def personal_top(self):
        """top 3 scores"""
        if len(self.scores) <= 3:
            self.scores = sorted(self.scores ,key=int, reverse=True)
            return self.scores
        else :
            self.scores = sorted(self.scores , key = int , reverse=True)
            del self.scores[3:]
            return self.scores

    def personal_best(self):
        """Highest score"""
        return max(self.scores)
    
    def report(self):
        """The diffrence between last added score and highest score"""
        differ = self.personal_best() - self.latest()
        if differ == 0:
            return "Your latest score was {}. That's your personal best!".format(self.latest())
        else:
            return "Your latest score was {}. That's {} short of your personal best!".format(self.latest() , differ)
