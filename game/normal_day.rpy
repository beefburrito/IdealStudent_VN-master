init python:
    import random

label normal_day:
    hide screen actions
    hide classroom2
    hide classroom
    hide tidyroom
    "...."

    show classroom2 with dis

    $ rndm = random.randrange(0,4)
    if rndm == 0:
        t"Class dismissed!"
    elif rndm == 1:
        t"This is going to be in the exam!"
    elif rndm == 2:
        t"Don't forget to study we've got a surprise exam soon!"
        mc"*sigh Why can't I know when the exam is"
    else:
        mc"When is the exam?"
        "Teacher""It's called a surprise exam for a reason"
        mc"Ugh..."
    $ intelligence = intelligence + 700
    $ tm = tm + 10
    $ chance = renpy.random.randint(1,10)
    jump free_time
