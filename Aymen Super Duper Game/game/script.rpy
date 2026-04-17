define N = Character("Narrator")
default player = "Aymen"
define P = Character("[player]")
default studied = False
default worked = False

image bg room = "images/BG.png"

init python:
    import random
    bgm_tracks = [
        "song1.mp3"
    ]

screen arrow_minigame():
    key "K_UP" action Return("up")
    key "K_DOWN" action Return("down")
    key "K_LEFT" action Return("left")
    key "K_RIGHT" action Return("right")

    frame:
        xalign 0.5
        yalign 0.5
        text "[display_arrow]" size 100


label start:
    scene bg room
    $ selected_bgm = random.choice(bgm_tracks)
    play music selected_bgm fadein 1.0

    N "You signed up for Hack Club Resolution,\nBut exams and procrastination got in the way."
    N "Now you only have 1.5 hours left to ship something."

    $ player = renpy.input("What is your name? (default is Aymen)", length=32)
    $ player = player.strip().title()
    if player == "":
        $ player = "Aymen"

    N "[player], nice name."

    N "1:30:00 Left"
    P "I should really start working..."

    menu:
        "What should I do?"
        "Start studying":
            call study_game
            if _return:
                $ studied = True
            else:
                $ studied = False
                jump bad_ending_study
            jump studying1

        "Start working on the game":
            jump working1

        "Play Clash Royale":
            call arrow_game
            if _return:
                if studied:
                    jump secret_ending
                else:
                    jump bad_ending_clash
            else:
                jump bad_ending_clash


label studying1:

    N "For some divine reason you get the idea to start studying."

    N "1:15:00 Left"

    menu:
        "Now what?"
        "Start working on the game":
            jump working1
        "Play Clash Royale":
            call arrow_game
            if _return:
                jump secret_ending
            else:
                jump bad_ending_clash

label working1:

    $ worked = True

    N "You start working on the game."
    N "The basic mechanics are coming together."
    N "1:00:00 Left"

    menu:
        "Next step"
        "Keep working":
            call code_game
            if _return:
                jump working2
            else:
                jump bad_ending_code

        "Play Clash Royale":
            call arrow_game
            jump bad_ending_clash


label working2:

    N "You keep coding."
    N "Menus, enemies, and UI are starting to work."
    N "0:30:00 Left"

    menu:
        "Final decision"
        "Finish the game":
            jump ending_check
        "Play Clash Royale":
            call arrow_game
            jump bad_ending_clash


label arrow_game:

    $ arrows = ["up", "down", "left", "right"]
    $ score = 0
    $ rounds = 5

    N "Focus mode activated. Hit the correct arrows."

    while rounds > 0:

        $ current_arrow = renpy.random.choice(arrows)

        if current_arrow == "up":
            $ display_arrow = "↑"
        elif current_arrow == "down":
            $ display_arrow = "↓"
        elif current_arrow == "left":
            $ display_arrow = "←"
        else:
            $ display_arrow = "→"

        call screen arrow_minigame
        $ result = _return

        if result == current_arrow:
            $ score += 1

        $ rounds -= 1

    if score >= 3:
        return True
    else:
        return False


label study_game:

    $ score = 0
    $ rounds = 5

    N "Study session started. Answer correctly."

    while rounds > 0:

        $ q = renpy.random.choice([
            ("2 + 2 =", "4"),
            ("Capital of France?", "paris"),
            ("5 * 3 =", "15"),
            ("Unity is a ___ engine?", "game"),
            ("10 / 2 =", "5")
        ])

        N "[q[0]]"

        $ answer = renpy.input("Answer:").strip().lower()

        if answer == q[1]:
            N "Correct."
            $ score += 1
        else:
            N "Wrong."

        $ rounds -= 1

    if score >= 3:
        return True
    else:
        return False


label code_game:

    $ score = 0
    $ rounds = 5

    N "You start coding..."

    while rounds > 0:

        $ word = renpy.random.choice([
            "function", "variable", "update", "player", "collision", "render"
        ])

        N "Type this:"
        N "[word]"

        $ answer = renpy.input(">").strip().lower()

        if answer == word:
            N "Correct."
            $ score += 1
        else:
            N "Bug introduced."

        $ rounds -= 1

    if score >= 3:
        return True
    else:
        return False


label ending_check:
    if studied and worked:
        jump best_ending
    else:
        jump good_ending


label best_ending:
    N "Because you studied earlier, your mind is clear."
    N "You code efficiently and finish the game just before the deadline."
    N "BEST ENDING: Game Completed AND Exams Saved"
    return


label good_ending:
    N "You finish the game just before the deadline."
    N "But your exams tomorrow might be rough. (You're cooked, lil bro.)"
    N "GOOD ENDING: Game Completed"
    return


label bad_ending_clash:
    N "You start playing Clash Royale."
    N "One match becomes ten."
    N "You look at the clock..."
    N "Time is up."
    N "BAD ENDING: Procrastination Wins"
    return

label bad_ending_study:
    N "You tried to study, but nothing sticks."
    N "Time slips away while you're stuck on questions."
    N "Time is up."
    N "BAD ENDING: Unprepared"
    return

label bad_ending_code:
    N "You keep debugging..."
    N "Nothing seems to work."
    N "Time is up."
    N "BAD ENDING: Broken Build"
    return

label secret_ending:
    N "You start playing Clash Royale."
    N "One match becomes ten."
    N "You look at the clock..."
    N "Time is up."
    N "But thanks to your extra intelligence, you get a great idea."
    N "You email the organizer asking for an extension."
    N "Somehow... they actually say yes."
    N "You now have time for both exams and your game."
    N "SECRET ENDING: EXTENSION OBTAINED"
    return