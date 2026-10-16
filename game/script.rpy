# Alexei: Primal in Japan — original adult romantic comedy.
define a = Character("Alexei", color="#e8c07a")
define y = Character("Yuna", color="#f4a9c9")
define m = Character("Mika", color="#9dd5f5")
define r = Character("Reina", color="#b6e4ae")
default yuna_points = 0
default mika_points = 0
default reina_points = 0
default day = 1

label start:
    scene bg tokyo
    centered "ALEXEI: PRIMAL IN JAPAN"
    "Tokyo. The neon flickers. A plane lands."
    a "I brought a suitcase, a steak budget, and an absolutely untested theory of romance."
    "All romantic characters are adults."
    jump crossroads

label crossroads:
    scene bg tokyo
    "Day [day]. Where should Alexei go?"
    menu:
        "Yuna's steakhouse":
            jump yuna_route
        "Mika's climbing gym":
            jump mika_route
        "Reina's bookstore café":
            jump reina_route

label yuna_route:
    scene bg restaurant
    show yuna_portrait at truecenter
    "Yuna, a 28-year-old chef, raises an eyebrow."
    y "You're the tall guy who ordered four steaks."
    a "One was emotionally important."
    menu:
        "Ask about her cooking":
            $ yuna_points += 2
            y "Finally, someone interested in the food instead of his own opinions."
        "Give a speech about the primal diet":
            $ yuna_points += 1
            y "Can your ancestors wash dishes?"
    if yuna_points >= 2:
        jump yuna_evening
    jump continue_day

label yuna_evening:
    y "Stay after closing. Help me invent something."
    "They cook together while rain taps on the windows."
    menu:
        "Tell Yuna she's more interesting than any diet":
            $ yuna_points += 2
            y "Careful. That's almost charming."
        "Challenge her to a steak competition":
            $ yuna_points += 1
            y "You're going to lose spectacularly."
    "A shared laugh becomes a lingering look."
    menu:
        "Ask if she'd like a kiss":
            y "Yes. I thought you'd never ask."
            "They kiss. The city outside grows quiet."
            "Later, the lights dim and the scene fades to black."
        "Enjoy the evening without rushing":
            y "I like that you know how to take your time."
    jump yuna_ending

label mika_route:
    scene bg gym
    show mika_portrait at truecenter
    "Mika, a 30-year-old climbing instructor, points at the wall."
    m "Height won't solve every problem."
    a "My entire worldview is under attack."
    menu:
        "Ask for a lesson":
            $ mika_points += 2
            m "Good. First rule: listen."
        "Try to impress her":
            $ mika_points += 1
            "Alexei falls harmlessly onto the padded mat."
            m "Gravity remains undefeated."
    if mika_points >= 2:
        jump mika_evening
    jump continue_day

label mika_evening:
    scene bg night
    show mika_portrait at truecenter
    "After climbing, Mika invites Alexei to a rooftop dinner."
    m "You're more fun when you're not performing."
    menu:
        "Admit she's right":
            $ mika_points += 2
            a "I can be ridiculous and sincere."
        "Insist steak is the secret":
            $ mika_points += 1
            m "I'm beginning to think steak is your legal guardian."
    "Mika steps closer under the city lights."
    menu:
        "Ask to kiss her":
            m "Only if you promise not to narrate it like a nature documentary."
            "They kiss, laughing."
            "Their evening continues privately as the screen fades to black."
        "Offer to meet again tomorrow":
            m "It's a date."
    jump mika_ending

label reina_route:
    scene bg bookstore
    show reina_portrait at truecenter
    "Reina, a 32-year-old novelist, looks up from her manuscript."
    r "Are you always this loud?"
    a "Only when my inner wolf has coffee."
    menu:
        "Ask about her novel":
            $ reina_points += 2
            r "It's about a hero who confuses confidence with wisdom."
        "Explain your diet":
            $ reina_points += 1
            r "A fascinatingly repetitive character trait."
    if reina_points >= 2:
        jump reina_evening
    jump continue_day

label reina_evening:
    scene bg night
    show reina_portrait at truecenter
    "Reina takes Alexei to a lantern-lit night market."
    r "I might write you into my next book."
    menu:
        "Ask to read her work":
            $ reina_points += 2
            r "That means more than you know."
        "Ask to be the handsome hero":
            $ reina_points += 1
            r "You can be the comic relief."
    "At her apartment door, Reina hesitates, smiling."
    menu:
        "Ask whether she'd like another hour together":
            r "I'd like that very much."
            "The door closes gently. Their private evening fades to black."
        "Wish her goodnight":
            r "Call me tomorrow."
    jump reina_ending

label continue_day:
    $ day += 1
    if day <= 4:
        "Not every encounter becomes romance. Alexei tries again."
        jump crossroads
    jump solo_ending

label yuna_ending:
    centered "YUNA ENDING — THE SECRET INGREDIENT"
    "Alexei learns that sharing a meal matters more than winning an argument."
    return

label mika_ending:
    centered "MIKA ENDING — HIGHER THAN HEIGHT"
    "Alexei discovers that trust is a different kind of strength."
    return

label reina_ending:
    centered "REINA ENDING — THE NEXT CHAPTER"
    "A man who came to Japan with all the answers finally learns to ask questions."
    return

label solo_ending:
    centered "SOLO ENDING — STEAK FOR ONE"
    a "I have learned that confidence is not a substitute for listening."
    "He orders dinner and begins a better chapter tomorrow."
    return
