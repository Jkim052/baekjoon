sen = input()

imoticon = {}

imoticon['hap'] = sen.count(':-)')
imoticon['sad'] = sen.count(':-(')

if (imoticon['hap'] + imoticon['sad']) == 0:
    print('none')
elif imoticon['hap'] > imoticon['sad']:
    print('happy')
elif imoticon['hap'] < imoticon['sad']:
    print('sad')
else:
    print('unsure')