
import random
class Hat:  
    def __init__(self, **data):
        self.contents = []
        self.drawn = []
        for key, value in data.items():
            #print(f"{key}= {value}")
            for i in range(value):
                (self.contents).append(f"{key}")
        #print(self.contents)

    def draw(self, number):
        #delete = set(random.sample(range(len(self.contents)), number))
        #return [x for i, x in enumerate(self.contents) if not i in delete]
        drawn_now = []
        if number > len(self.contents):
            for x in self.drawn:
                self.contents.append(x)
            print(self.contents)            
            return
        else:
            drawn_now = random.sample(self.contents, number)
            for x in drawn_now:                
                self.contents.remove(x)
                self.drawn.append(x)
            print(drawn_now)
            #print(self.contents)
            return

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    gotit = 0
    number = 0
    for x in range (num_experiments):
        i = random.sample(hat.contents, num_balls_drawn)
        for key, value in expected_balls.items():
            if i.count(f'{key}') >= int(f'{value}'):
                #print(i)
                #print(i.count(f'{key}'), int(f'{value}'))
                number += 1
                #print(number)
        if number == len(expected_balls):
            gotit += 1
            number = 0
            #print(i)    
        else:
            number = 0

    print(gotit/num_experiments)

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat, expected_balls={"red":2,"green":1}, num_balls_drawn=5, num_experiments=2000)