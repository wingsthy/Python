alien = {}
alien['color']= 'green'
alien['points']=5
print(alien)
alien['color']='yellow'
print(alien)

favorite_language = {
    'jen':'python',
    'bob':'ruby',
    'jack':'java',
    'phil':'c',
        }
print("bob's favorite_language is " + favorite_language['bob'].title() + ".")
user = {
    'name':'baby',
    'first':'enrico',
    'last':'fermi',
        }
for key,value in user.items():
    print("\nKey: " + key)
    print("\nValue:" + value)

aliens= []

for alien_number in range(30):
    new_alien = {'color':'green', 'points':'5', 'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print(".....")

