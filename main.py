import numpy as np



class Game:

    def __init__(self,dict_path):
    
        words = []
        with open(dict_path,'r') as f:
            
            content = f.read()

        self.words = content.split('\n')
        
        self.game_loop()
        
    def game_loop(self):

        first_enter = True
        while True:
            print('New game!')
            self.new_game()

            while self.step() or first_enter:
                first_enter = False
                continue

            



    def step(self):

        print('Guess a letter')
        
        letter = input()
        
        if len(letter) == 0 or len(letter) > 1:
            print('Input just one letter!')
            return True

        am_user_right = letter in self.current_word

        if am_user_right:
            print('Hit!')
            self.update_avail(letter)

        else:
            self.mistakes += 1
            print('Missed, mistake {} out of 5'.format(self.mistakes))
            
        print('The word: {}'.format(self.current_avail))
        #print(self.current_avail, self.current_word)
        need_step = True

        if self.mistakes == 5:
            print('You lost!')
            need_step = False
        if self.current_avail == self.current_word:
            print('You won!')
            need_step = False

        return need_step


    def update_avail(self,letter):
        
        indexes = [i for i,x in enumerate(self.current_word) if x == letter]

        l = list(self.current_avail)

        for idx in indexes:
            l[idx] = letter

        self.current_avail = ''.join(l)

    def new_game(self):

        self.current_word = np.random.choice(self.words)
        self.current_avail = '*'*len(self.current_word)
        self.mistakes = 0

        


    



        




a = Game('dict.txt')






