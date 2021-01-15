import re
new_text = []

print("Welcome to Mad Libs Game")
print("Here you have to think of words and they will be automatically assigned in the text")
print("There are few different scenarios to choose from: ")
print("1) Day at the zoo")
print("2) The Fun Park")
print("3) At the arcade")
print("4) The first day of School")
print("5) In the Jungle")
print("6) Make me a video game")
print()
game = int(input("\nPlease type in the number of the scenario: "))

if game == 1:
    path = '/home/dizont/pyth/Projects/Mad Libs Generator/day.txt'
elif game ==2:
    path = '/home/dizont/pyth/Projects/Mad Libs Generator/funpark.txt'
elif game == 3:
    path = '/home/dizont/pyth/Projects/Mad Libs Generator/arcade.txt'
elif game == 4:
    path = '/home/dizont/pyth/Projects/Mad Libs Generator/firstday.txt'
elif game == 5:
    path = '/home/dizont/pyth/Projects/Mad Libs Generator/jungle.txt'
elif game == 6:
    path = '/home/dizont/pyth/Projects/Mad Libs Generator/video.txt'

with open(path,'r') as f:
    for line in f:
        wordlist = []
        index = 0
        actionlist=[]
        string = ''.join(line.split('_')) #remove ____ 
        l = re.findall('\((.*?)\)',string) # find all things in the ()
        for el in l:
            if el != 'n' and el != '': #skip (n) or () if any
                new_word = input('Please enter one '+ el +': ')
                wordlist.append(new_word)
                actionlist.append(el)
                string = string.replace('(%s)'%actionlist[index],'%s'%wordlist[index])
                index += 1
        new_text.append(string)
    print('\n\n\n Here is your Story! \n\n')
    print(' '.join(new_text))




        
    
    

    


