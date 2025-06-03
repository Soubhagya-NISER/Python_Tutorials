'''info = {
    'Name':'John',
    'Age': 30,
    'Gender': 'Male'
}
info['hi'] = 'SD' 
print(info.get('hi', 'go'))
print(info['Age'])
print(info)

p = input('Enter your phone no.: ')
dm = {
    '1' : 'One',
    '2' : 'Two',
    '3' : 'Three',
    '4' : 'Four'
}
o = ''
for i in p:
    o += dm.get(i,'!')+" "
print(o)
'''

message = input('>')
word = message.split()
print (word)
o = ''
emojis = {
    ":)" : "🙂",
    ":(" : "😞"
}
for i in word:
    o += emojis.get(i,i)+" "
print(o)