with open('test.hi') as f:
    lines = f.readlines()


with open('count_hi_test.txt', 'w') as f:
    for index, value in enumerate(lines):
        number_of_words = len(value.split())        
        f.write('{}\n'.format(number_of_words))



with open('train.hi') as f:
    lines = f.readlines()


with open('count_hi_train.txt', 'w') as f:
    for index, value in enumerate(lines):
        number_of_words = len(value.split())        
        f.write('{}\n'.format(number_of_words))



with open('tune.hi') as f:
    lines = f.readlines()


with open('count_hi_tune.txt', 'w') as f:
    for index, value in enumerate(lines):
        number_of_words = len(value.split())        
        f.write('{}\n'.format(number_of_words))







#Marathi

with open('test.mr') as f:
    lines = f.readlines()


with open('count_mr_test.txt', 'w') as f:
    for index, value in enumerate(lines):
        number_of_words = len(value.split())        
        f.write('{}\n'.format(number_of_words))



with open('train.mr') as f:
    lines = f.readlines()


with open('count_mr_train.txt', 'w') as f:
    for index, value in enumerate(lines):
        number_of_words = len(value.split())        
        f.write('{}\n'.format(number_of_words))



with open('tune.mr') as f:
    lines = f.readlines()


with open('count_mr_tune.txt', 'w') as f:
    for index, value in enumerate(lines):
        number_of_words = len(value.split())        
        f.write('{}\n'.format(number_of_words))
