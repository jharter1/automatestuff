def spam():
    print(eggs) #this line will error out
    eggs = 'spam local'

eggs = 'global'
spam()