def to_camel_case(text):
    for i in text:
        if i == '_':
            word = text.split('_')
            output = [word[0].lower()] + [w.capitalize() for w in word[1:]]
            answer = ''.join(output)
        return answer
    
        if i == '-':
            word = text.split('_')
            output = [word[0].capitalize()] + [w.capitalize() for w in word[1:]]
            answer = ''.join(output)
        return answer

text = "TheStealthWarrior"
res = to_camel_case(text)
print(res)

