## 
## Improving Your First Python Program

input('what is your name')
print('hello world')

## Variables
name = input('enter your name')
print('hello')
print(name)

## Comments
#ask user there name
name = input('enter your')

## Pseudocode
## ask user name
name = input('enter your name')
## print hello
print('hello')
## print input name
print(name)

## Further Improving Your First Python Program
name = input('enter your name')
print('hello' + name) # print('hello', name)

## Formatting Strings
name = input('enter your name')
print(f'hello ${name}')


## More on Strings
name = input('enter your name')
name = name.strip()
print(f'hello, ${name}')

## Capitalize the first letter of each word
name = name.title()

print(f'hello, ${name}')

name = name.strip().title()
print(f'hello, ${name}')

name = input('enter your name').strip().title()
print(f'hello, ${name}')

## Integers or int

