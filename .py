class Dog:
  #class variable
  animal='Dog'
  #the init method or constructor
  def __init__(self,breed,colour):
    #Instance Variable
    self.breed=breed
    self.colour=colour
#objects of dog class
Rodger=Dog("Pug","brown")
Buzo=Dog("Bulldog","black")
print('Rodger details:')
print('Rodger is a',Rodger.animal)
print('breed:',Rodger.breed)
print('colour:',Rodger.colour)

print('\nBuzo details:')
print('Buzo is a',Buzo.animal)
print('Breed:',Buzo.breed)
print('colour:',Buzo.colour)
