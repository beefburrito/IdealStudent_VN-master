label exams:
    show classroom2 with dis
    hide screen actions
    hide classroom
    hide tidyroom
    menu:
        "A surprise exam!"
        "Perfect Score":
            jump choice_perf
        "Pass":
            jump choice_pass
        "Fail":
            jump choice_fail

label choice_perf:

    mc "Test"
    jump choice_done

label choice_pass:

    mc "Games"

    jump choice_done

label choice_fail:
    e "Failed"
    jump choice_done

label choice_done:

    hide classroom2
    $ chance = renpy.random.randint(1,10)
    jump free_time
