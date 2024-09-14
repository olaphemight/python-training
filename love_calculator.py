print('''   __  __
       ,-'  `'  \         _---``--
      /    _  _  ;      __        `.
     /    / `' \;        /`-----    )
    /  .-/    ,(         ),     \-. ;
    |  \(       \       /        )/;
    |   -      _5       `7       -;
   /    (  ___-'         `-____    |
  (   ___`-_                 \ ____|
   \ /   `,/ \     _(\__      /    \
    \      ;  \  .' /'  `i.  /      |
     |      \ _-'( _\__-/  `-       |
     |       `   ,`     `_          |
     ''')





 

print("Welcome To Love Calculator")
name1 = input("What is your name?: ").lower()
name2 = input("What is your crush's name?: ").lower()
combined_name = name1 + name2
# true = combined_name.count("T") + combined_name.count("r") + combined_name.count("u") + combined_name.count("e")
t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")
# love = combined_name.count("L") + combined_name.count("o") + combined_name.count("v") + combined_name.count("e")
true = t + r + u + e
# print(true)

l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")

love = l + o + v + e

true_love = ""
# print(true_love)

if love > 9:
    love_str = str(love)
    l1 = love_str[0]
    l2 = love_str[1]
    love_add = true + int(l1)
    love_score = str(love_add) + str(l2)
    true_love = int(love_score)
    print(true_love)
else:
    love_score = str(true) + str(love)
    true_love = int(love_score)
    print(true_love)


if true_love > 85 and true_love <= 95:
    print(f'your score is {true_love}, you go together like coke and mentors.')

if true_love >= 25 and true_love <= 45:
    print(f'your score is {true_love}, There is hope, keep pushing')

if true_love > 45 and true_love <= 85:
    print(f'your score is {true_love}, you look alright')

if true_love > 10 and true_love < 25:
    print(f'your score is {true_love}, look elsewhere!!!')

if true_love == 0 or true_love >= 100:
    print(f"your score is {true_love}, It's too real to be true")