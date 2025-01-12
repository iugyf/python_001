from random import choice, randrange, seed

articles = ['a', 'an', 'the']       # 冠词

nouns = ['apple', 'banana', 'car', 'book', 'computer', 'table', 'chair', 'phone', 'camera', 'bicycle', 'coffee', 'tea', 'house', 'city', 'country', 'ocean', 'mountain', 'river', 'sun', 'moon', 'star', 'animal', 'plant', 'music', 'movie', 'painting', 'science', 'history', 'mathematics', 'physics', 'chemistry', 'biology', 'geography', 'language', 'culture', 'art', 'sports', 'exercise', 'football', 'basketball', 'tennis', 'swimming', 'running', 'jumping', 'walking', 'reading', 'writing', 'programming', 'design', 'architecture', 'engineering', 'medicine', 'law', 'economics', 'politics', 'philosophy']

verbs = ['run', 'walk', 'jump', 'swim', 'read', 'write', 'speak', 'listen', 'eat', 'drink', 
         'sleep', 'wake', 'drive', 'fly', 'cook', 'eat', 'dance', 'sing', 'play', 'work', 
         'study', 'learn', 'teach', 'help', 'build', 'create', 'destroy', 'open', 'close', 
         'start', 'stop', 'move', 'stay', 'find', 'lose', 'buy', 'sell', 'give', 'take', 
         'send', 'receive', 'love', 'hate', 'like', 'dislike', 'laugh', 'cry', 'smile', 
         'frown', 'think', 'dream', 'remember', 'forget', 'solve', 'ask', 'answer', 'wait', 
         'hurry', 'push', 'pull', 'carry', 'lift', 'drop', 'throw', 'catch', 'hit', 'kick', 
         'touch', 'see', 'hear', 'smell', 'taste', 'feel', 'breathe', 'live', 'die', 'grow', 
         'shrink', 'increase', 'decrease', 'win', 'lose', 'win', 'fail', 'try', 'succeed', 'fail', 
         'begin', 'end', 'continue', 'pause', 'resume', 'change', 'stay', 'become', 'remain', 'appear', 
         'disappear', 'arrive', 'leave', 'enter', 'exit', 'join', 'quit', 'accept', 'refuse', 'agree', 
         'disagree', 'love', 'hate', 'like', 'dislike', 'enjoy', 'hate', 'prefer', 'choose', 'decide', 'plan', 
         'organize', 'prepare', 'execute', 'complete', 'finish', 'start', 'stop', 'continue', 'pause', 'resume', 
         'repeat', 'practice', 'improve', 'develop', 'design', 'build', 'construct', 'destroy', 'break', 'fix', 
         'repair', 'clean', 'wash', 'cook', 'bake', 'grill', 'fry', 'boil', 'steam', 'roast', 'microwave', 'freeze', 
         'thaw', 'mix', 'stir', 'blend', 'cut', 'slice', 'chop', 'peel', 'skin', 'shred', 'grate', 'crush', 'mash', 
         'spread', 'pour', 'sprinkle', 'splash', 'drip', 'flow', 'run', 'rush', 'stream', 'trickle', 'gush', 'bubble', 
         'boil', 'simmer', 'fizz', 'sparkle', 'shine', 'glow', 'twinkle', 'blink', 'flash', 'light', 'darken', 'brighten', 
         'dim', 'fade', 'vanish', 'disappear', 'reappear', 'show', 'hide', 'cover', 'uncover', 'reveal', 'conceal', 'expose', 
         'protect', 'defend', 'attack', 'fight', 'argue', 'debate', 'discuss', 'talk', 'chat', 'whisper', 'shout', 'yell', 
         'scream', 'laugh', 'giggle', 'chuckle', 'snicker', 'sob', 'cry', 'weep', 'wail', 'moan', 'groan', 'sigh', 'yawn', 
         'cough', 'sneeze', 'blow', 'breathe', 'inhale', 'exhale', 'suck', 'blow', 'spit', 'lick', 'kiss', 'bite', 'chew', 
         'swallow', 'vomit', 'cough', 'sneeze', 'yawn', 'stretch', 'flex', 'bend', 'twist', 'turn', 'spin', 'rotate', 'flip', 
         'roll', 'jump', 'hop', 'skip', 'step', 'stride', 'pace', 'tiptoe', 'stomp', 'walk', 'run', 'jog', 'sprint', 
         'dash', 'race', 'crawl', 'creep', 'slither', 'slide', 'glide', 'skate', 'ski', 'surf', 'swim', 'dive', 'float', 
         'sink', 'fly', 'soar', 'glide', 'hover', 'land', 'take off', 'ascend', 'descend', 'climb', 'descend', 'scale', 
         'climb up', 'climb down', 'jump over', 'jump off', 'jump into', 'jump out of', 'jump across', 'jump through', 
         'jump around', 'jump up and down', 'jump for joy', 'jump with excitement', 'jump in surprise', 'jump in fear', 
         'jump in anger', 'jump in frustration', 'jump in delight', 'jump in anticipation', 'jump in celebration', 
         'jump in victory', 'jump in defeat', 'jump in despair', 'jump in hope', 'jump in love', 'jump in hate', 
         'jump in joy', 'jump in sorrow', 'jump in pain', 'jump in pleasure', 'jump in surprise', 'jump in fear', 
         'jump in anger', 'jump in frustration', 'jump in delight', 'jump in anticipation', 'jump in celebration', 
         'jump in victory', 'jump in defeat', 'jump in despair', 'jump in hope', 'jump in love', 'jump in hate', 
         'jump in joy', 'jump in sorrow', 'jump in pain', 'jump in pleasure']

# 构建句子
def sentence():
    return noun_phrase() + verb_phrase() 


# 生成名词
def noun_phrase():
    return [choice(articles), choice(nouns)]


# 生成动词
def verb_phrase():
    vp = [choice(verbs)]
    if randrange(3)>0:
        vp.extend(noun_phrase()) 
    return vp


# 生成随机种子
seed()


# 输出句子
for i in range(10):
    print(" ".join(sentence()))     # .join 每个词后面加空格





##########################################
print("--------------------------------")
print("以下关于randrange的用法展示")
for i in range(10):
    print(randrange(3))