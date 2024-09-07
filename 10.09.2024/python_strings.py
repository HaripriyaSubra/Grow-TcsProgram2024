message = 'welcome to python'

sub_message = 'WELCOME'

print(len(message))

print(message.upper())

print(sub_message.lower())

print(message.title())

print(message.capitalize())

print(message.find('e'))

print(message.find('a'))

print(message.replace('python', 'introduction to python'))

print(message)

print(message.startswith('welcome'))

print(message.startswith('good'))

print(message.startswith('Welcome'))

print(message.endswith('python'))

print(message.find('welcome'))

print(message.find('python'))

print(message.count('o'))

print(message.center(50))

price_tag = 'This article costs {price:.2f} euros'

print(price_tag.format(price=56.89))

digit_string = "12345"
is_digit = digit_string.isdigit()
print(is_digit)

alpha_string = "abc"
is_alpha = alpha_string.isalpha()
print(is_alpha)

is_upper = "HELLO".isupper()
print(is_upper)

word_list = message.split()
print(word_list)

joined_string = '-'.join(word_list)
print(joined_string)

