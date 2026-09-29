from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine=MoneyMachine()
coffee_maker=CoffeeMaker()
menu_methods=Menu()
total=0
is_on=True
while is_on:
    list_of_drinks=menu_methods.get_items()
    order=input(f"What would You like to have?({list_of_drinks}):  ")
    if order=='off':
        is_on=False
    elif order=='report':
        print(coffee_ma18:37:56.684: [/home/gokul_04/PycharmProjects/Python100D] git /usr/bin/git -c core.quotepath=false -c log.showSignature=false version
git version 2.55.0
20:22:39.496: [/home/gokul_04/PycharmProjects/Python100D] git /usr/bin/git -c credential.helper= -c core.quotepath=false -c log.showSignature=false add --ignore-errors -A --pathspec-from-file=- --pathspec-file-nul
20:22:40.003: [/home/gokul_04/PycharmProjects/Python100D] git /usr/bin/git -c credential.helper= -c core.quotepath=false -c log.showSignature=false add --ignore-errors -A -f --pathspec-from-file=- --pathspec-file-nul
20:22:40.015: [/home/gokul_04/PycharmProjects/Python100D] git /usr/bin/git -c credential.helper= -c core.quotepath=false -c log.showSignature=false commit -F /tmp/git-commit-msg-13719095531776984846.txt --
[master ad7aade] day16-oop coffe_machine
 8 files changed, 188 insertions(+), 1 deletion(-)
 create mode 100644 oop-coffee-machine-start/coffee_maker.py
 create mode 100644 oop-coffee-machine-start/main.py
 create mode 100644 oop-coffee-machine-start/menu.py
 create mode 100644 oop-coffee-machine-start/money_machine.py
 create mode 100644 oop_coffe_machine.py
20:22:44.236: [/home/gokul_04/PycharmProjects/Python100D] git /usr/bin/git -c credential.helper= -c core.quotepath=false -c log.showSignature=false push --progress --porcelain origin refs/heads/master:master
Picked up _JAVA_OPTIONS: -Dswing.defaultlaf=com.sun.java.swing.plaf.gtk.GTKLookAndFeel
Picked up _JAVA_OPTIONS: -Dswing.defaultlaf=com.sun.java.swing.plaf.gtk.GTKLookAndFeel
Enumerating objects: 15, done.
Counting objects:   6% (1/15)
Counting objects:  13% (2/15)
Counting objects:  20% (3/15)
Counting objects:  26% (4/15)
Counting objects:  33% (5/15)
Counting objects:  40% (6/15)
Counting objects:  46% (7/15)
Counting objects:  53% (8/15)
Counting objects:  60% (9/15)
Counting objects:  66% (10/15)
Counting objects:  73% (11/15)
Counting objects:  80% (12/15)
Counting objects:  86% (13/15)
Counting objects:  93% (14/15)
Counting objects: 100% (15/15)
Counting objects: 100% (15/15), done.
Delta compression using up to 16 threads
Compressing objects:  10% (1/10)
Compressing objects:  20% (2/10)
Compressing objects:  30% (3/10)
Compressing objects:  40% (4/10)
Compressing objects:  50% (5/10)
Compressing objects:  60% (6/10)
Compressing objects:  70% (7/10)
Compressing objects:  80% (8/10)
Compressing objects:  90% (9/10)
Compressing objects: 100% (10/10)
Compressing objects: 100% (10/10), done.
Writing objects:   9% (1/11)
Writing objects:  18% (2/11)
Writing objects:  27% (3/11)
Writing objects:  36% (4/11)
Writing objects:  45% (5/11)
Writing objects:  54% (6/11)
Writing objects:  63% (7/11)
Writing objects:  72% (8/11)
Writing objects:  81% (9/11)
Writing objects:  90% (10/11)
Writing objects: 100% (11/11)
Writing objects: 100% (11/11), 5.11 KiB | 5.11 MiB/s, done.
Total 11 (delta 3), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas:   0% (0/3)
remote: Resolving deltas:  33% (1/3)
remote: Resolving deltas:  66% (2/3)
remote: Resolving deltas: 100% (3/3)
remote: Resolving deltas: 100% (3/3), completed with 3 local objects.
remote: Internal Server Error
remote: Request ID D6EC:20AE18:252E01:280E22:6ABBD0C0
remote: Time 2026-09-29T14:52:48Z
error: failed to push some refs to 'https://github.com/GokulTamilarasu/Python.git'
To https://github.com/GokulTamilarasu/Python.git
!	refs/heads/master:refs/heads/master	[remote rejected] (Internal Server Error)
Done
20:23:15.111: [/home/gokul_04/PycharmProjects/Python100D] git /usr/bin/git -c credential.helper= -c core.quotepath=false -c log.showSignature=false push --progress --porcelain origin refs/heads/master:master
Picked up _JAVA_OPTIONS: -Dswing.defaultlaf=com.sun.java.swing.plaf.gtk.GTKLookAndFeel
Picked up _JAVA_OPTIONS: -Dswing.defaultlaf=com.sun.java.swing.plaf.gtk.GTKLookAndFeel
Enumerating objects: 15, done.
Counting objects:   6% (1/15)
Counting objects:  13% (2/15)
Counting objects:  20% (3/15)
Counting objects:  26% (4/15)
Counting objects:  33% (5/15)
Counting objects:  40% (6/15)
Counting objects:  46% (7/15)
Counting objects:  53% (8/15)
Counting objects:  60% (9/15)
Counting objects:  66% (10/15)
Counting objects:  73% (11/15)
Counting objects:  80% (12/15)
Counting objects:  86% (13/15)
Counting objects:  93% (14/15)
Counting objects: 100% (15/15)
Counting objects: 100% (15/15), done.
Delta compression using up to 16 threads
Compressing objects:  10% (1/10)
Compressing objects:  20% (2/10)
Compressing objects:  30% (3/10)
Compressing objects:  40% (4/10)
Compressing objects:  50% (5/10)
Compressing objects:  60% (6/10)
Compressing objects:  70% (7/10)
Compressing objects:  80% (8/10)
Compressing objects:  90% (9/10)
Compressing objects: 100% (10/10)
Compressing objects: 100% (10/10), done.
Writing objects:   9% (1/11)
Writing objects:  18% (2/11)
Writing objects:  27% (3/11)
Writing objects:  36% (4/11)
Writing objects:  45% (5/11)
Writing objects:  54% (6/11)
Writing objects:  63% (7/11)
Writing objects:  72% (8/11)
Writing objects:  81% (9/11)
Writing objects:  90% (10/11)
Writing objects: 100% (11/11)
Writing objects: 100% (11/11), 5.11 KiB | 5.11 MiB/s, done.
Total 11 (delta 3), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas:   0% (0/3)
remote: Resolving deltas:  33% (1/3)
remote: Resolving deltas:  66% (2/3)
remote: Resolving deltas: 100% (3/3)
remote: Resolving deltas: 100% (3/3), completed with 3 local objects.
To https://github.com/GokulTamilarasu/Python.git
 	refs/heads/master:refs/heads/master	00c2a64..ad7aade
Doneker.report())
    else:
        drink = menu_methods.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)



