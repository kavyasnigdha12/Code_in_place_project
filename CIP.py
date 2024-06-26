import random

# creating a line separator 
def separator():
    print("=" * 120)

def msg_separator():
    print("-" * 120)

# header for the game
print("\n")
separator()
print("                                     Welcome To Daily Routine Motivator                           ")
separator()
print("\n")

# mood dictionary 1
moods_dictionary = {
    "happy😊": " ", "excited😄": " ", "grateful🙏": " ", "calm🧘": " ", "energized⚡": " ", "content😌": " ",
    "inspired🌟": " ", "indifferent😐": " ", "neutral😶": " ", "reflective🤔": " ", "curious🧐": " ",
    "pensive🤔": " ", "sad😢": " ", "anxious😟": " ", "angry😠": " ", "frustrated😤": " ", "lonely😔": " ",
    "bored😐": " ", "tired😴": " ", "stressed😫": " ", "depressed😞": " ", "nostalgic🌅": " ", "ambivalent🤷": " ",
    "bittersweet😢😊": " ", "hopeful🌈": " ", "conflicted🤯": " ", "comfortable🛋️": " ", "uncomfortable😣": " "
}

# mood dictionary 2 [without Emoticons]
moods = {
    "happy": "Keep spreading the joy! Your happiness is contagious. 😊",
    "excited": "Harness that excitement and let it fuel your passions! ✨",
    "grateful": "Gratitude turns what we have into enough. Keep appreciating the little things. 🙏",
    "calm": "Embrace the peace and use it to find clarity in your thoughts. 🧘",
    "energized": "Channel that energy into something productive and watch amazing things happen. ⚡",
    "content": "Contentment is a great place to be. Enjoy this moment of satisfaction. 😌",
    "inspired": "Take that inspiration and turn it into action. Great things await you. 🌟",
    "indifferent": "It's okay to feel indifferent sometimes. Reflect on what truly matters to you. 🖊️ ",
    "neutral": "A neutral state can be a great base for mindfulness. Take a moment to breathe. 😌",
    "reflective": "Use this time of reflection to learn and grow from your experiences. 📚",
    "curious": "Curiosity is the gateway to knowledge. Keep asking questions and exploring. 🔎",
    "pensive": "Deep thoughts can lead to profound insights. Embrace this time of contemplation. ⌛",
    "sad": "It's okay to feel sad. Allow yourself to feel, and remember that brighter days are ahead. 📅",
    "anxious": "Take a deep breath. You're stronger than your anxiety, and this too shall pass. 🍀",
    "angry": "Channel your anger into positive action. Use it as a catalyst for change. 🍃",
    "frustrated": "Frustration can be a sign of progress. Keep pushing forward, you're closer than you think.  🌇",
    "lonely": "Reach out to someone you trust. Connections are just a conversation away. ☎️",
    "bored": "Boredom can spark creativity. Find a new hobby or activity to engage in.  🎨🕹️🎾⚽",
    "tired": "Rest is important. Take time to recharge and you'll come back stronger. 😴",
    "stressed": "Take a moment to relax and breathe. You've handled everything so far, you can do this. 👍",
    "depressed": "You're not alone. Reach out for support, and remember that there is hope. 😞",
    "nostalgic": "Cherish those memories, but don't forget to create new ones. 🌅",
    "ambivalent": "It's okay to have mixed feelings. Take time to understand what you truly want. 🤞 ",
    "bittersweet": "Embrace the complexity of your emotions. It's a sign of a life well-lived. 😊",
    "hopeful": "Hold onto that hope. It's a powerful force that can drive you towards your goals. 🌈",
    "conflicted": "Conflict can lead to growth. Take time to resolve your feelings and find clarity. 🔮 ",
    "comfortable": "Enjoy this comfort, but also be open to stepping out of your comfort zone for growth. 🛋️",
    "uncomfortable": "Discomfort can lead to growth. Embrace the challenge and learn from it. 🎯"
}

# Counter to keep track of position in the table
counter = 0

# Loop through the dictionary
for key, value in moods_dictionary.items():
    # Print formatted table row every 3rd element
    if counter % 3 == 0:
        print()  # New line for a new row

    # Print key and value with some padding
    print(f"{key:<15}", end="  ")

    counter += 1

# Print newline after the last row
print()

while True:
    user_mood = input("\nHey! How are you feeling today? ").strip()
    if user_mood in moods:
        print(moods[user_mood])
        break
    else:
        print("Please choose from the given Moods.")

print("\n")
separator()
separator()
print("\n")

questionnaire_dictionary = {
    "key1": "Did you engage in any physical exercise today?",
    "key2": "Did you plan your day in advance today?",
    "key3": "Did you spend some time outdoors and get some sunlight today?",
    "key4": "Did you get 6-8 hours of sleep last night?",
    "key5": "Did you spend time working towards your personal or academic goals today?",
    "key6": "Did you read any interesting content today?",
    "key7": "Did you take at least 5 minutes to relax or meditate today?",
    "key8": "Did you practice gratitude by noting down something you're thankful for today?"
}

motivation_dictionary = {
    "key1": "No worries! Even a short walk or stretching session can boost your energy and mood. \nHow about a quick workout tomorrow to kickstart the day?",
    "key2": "No problem! Planning ahead can really help streamline your day and reduce stress. \nTomorrow, let's jot down a few priorities to make things easier...As they say planned day is a productive day!",
    "key3": "It happens! Fresh air and sunlight can really rejuvenate you. \nLet's aim for a brief outdoor break tomorrow to soak in some natural energy.\nSunshine is the best medicine!",
    "key4": "Sleep is crucial for our well-being. Maybe tonight, \ntry winding down a bit earlier or creating a relaxing bedtime routine to ensure you get those hours in.\nRest is essential for success!",
    "key5": "It's okay! Every step counts, big or small. \nTomorrow, let's carve out some time to focus on what matters most to you. Progress is progress! \nSmall steps lead to big achievements!",
    "key6": "No worries! Knowledge is power, keep learning! \nAnd reading expands our minds and sparks creativity. \nHow about exploring an intriguing article or book tomorrow that piques your curiosity?",
    "key7": "Taking time for yourself is crucial! \nTaking time to unwind is essential for mental clarity. Tomorrow, let's schedule a few minutes to relax or meditate together.",
    "key8": "That's alright! Gratitude can really shift our perspective. \nTomorrow, let's make a note of something we're thankful for to start the day on a positive note.",
}

keep_it_up_dictionary = {
    "key1": "That's fantastic! Taking care of your body is a great way to boost your overall well-being.",
    "key2": "Great job! Planning ahead sets the tone for a productive and organized day.",
    "key3": "Wonderful! Getting outside and soaking in sunlight can really lift your spirits and increase vitamin D levels.",
    "key4": "Well done! Quality sleep is essential for your health and cognitive function.",
    "key5": "Awesome! Dedication to your goals shows commitment and determination.",
    "key6": "Fantastic! Reading enriches the mind and opens up new perspectives.",
    "key7": "Excellent! Taking time to relax or meditate promotes inner peace and reduces stress.",
    "key8": "That's great to hear! Practicing gratitude cultivates a positive mindset and appreciation for life's blessings."
}

done = []
not_done = []
count_yes = 0
response_dictionary = {}

def get_motivation_quote(count):
    motivational_lines = {
        0: "Every day is a new beginning 🌿🌞, Let's plan the day now, you got this! ",
        1: "That's a step towards success! You're doing amazing!\n"
           "Studies show overcoming inertia, that initial resistance to starting, is a huge hurdle.\n"
           "By taking that first step, you've activated your brain's reward system, making it easier to keep going.\n"
           "Momentum is building on your side!",
        2: "2 down, keep the fire burning!\n'The journey of a thousand miles begins with a single step.' - Lao Tzu",
        3: "Halfway there! You're unstoppable! \n'The difference between ordinary and extraordinary is that little extra.' - Jimmy Johnson",
        4: "Almost there! Remember, \n'The best way to get started is to quit talking and begin doing.' - Walt Disney",
        5: "You're on a roll! Almost done! \n'The only person you are destined to become is the person you decide to be.' - Ralph Waldo Emerson",
        6: "Nearly finished! Celebrate your progress! \n'Success is not final, failure is not fatal: it is the courage to continue that counts.' - Winston Churchill",
        7: "Amazing! You completed all your tasks! \n'The only limit to our realization of tomorrow will be our doubts of today.' - Franklin D. Roosevelt",
    }
    return motivational_lines.get(count)  # Use get to handle missing keys

# Shuffle the keys for random order
shuffled_keys = list(questionnaire_dictionary.keys())
random.shuffle(shuffled_keys)

for key in shuffled_keys:
    question = questionnaire_dictionary[key]
    while True:
        response = input(f"{question} (yes/no): ").lower()
        if response in ("yes", "no"):
            break
        else:
            print("Please answer with 'yes' or 'no'.")

    response_dictionary[key] = response
    if response == "yes":
        print(keep_it_up_dictionary[key])  # Use Keep It Up dictionary for relevant quote
        count_yes += 1
        done.append(key)
        print("\n")
    else:
        print(motivation_dictionary[key])  # Use motivation dictionary for relevant quote
        not_done.append(key)
        print("\n")

print("\nYour Responses:")
print(response_dictionary)

print("\n")
print("You did all these tasks: ", done)
#print("All the tasks you didn't do: ", not_done)
print("\n")

motivation_quote = get_motivation_quote(count_yes)
msg_separator()
print("💐___MESSAGE___💐")
if motivation_quote:
    print(motivation_quote)
else:
    print("Amazing! You got all your tasks done, you are maintaining a 1000/10 routine!")
msg_separator()

print("\n")
separator()
print("                                     Daily Routine Motivator Signing Out!                           ")
print("                                         Hope You Have A Great Time                                 ")

separator()
print("\n")
