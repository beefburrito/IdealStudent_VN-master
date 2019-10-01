$ finalshowdown = 0

label showdown:
    jump showdown_isabelle

label showdown_elizabeth:
    show city with dis
    "(The monster's population is increasing quite drastically)"
    "(As a result heroes such as you are present to deal with this)"
    "(One Punch is the strongest hero in the Hero Association)"
    "(Unfortunately you are the weakest hero)"
    "(To make up for it you have Hyper Focus to improve yourself)"
    "(Rumors have surfaced stating a monster overlord has been the cause
    of the monster's population increase)"
    "(Many heroes have fallen trying to fight this monster)"
    "(Currently you can train yourself)"

label showdown_isabelle:
    hide screen actions
    hide classroom2
    hide classroom
    hide tidyroom
    "Ending"
    jump endings
