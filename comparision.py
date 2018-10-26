
import re
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from scipy.misc import imread
from matplotlib.offsetbox import (TextArea, DrawingArea, OffsetImage,
                                  AnnotationBbox)
from matplotlib.cbook import get_sample_data


#create dictionay of emojis
def create_dictionary(x, emoji):
    x = x.split()
    for i in x:
        if re.search(r"^(:)", i):
            emoji[i] = 0
    
    #return emoji


def emoji_count(x, emoji):
    t = x.split()
    for k in t:
        for i in emoji:
            if k == i:
                #print("match")
                emoji[i] = emoji[i] + 1      
                       
    #return emoji



emoji = {}


data = pd.DataFrame.from_csv('processed_eagles_after.csv', encoding='utf-8', index_col= None)
data1 = pd.DataFrame.from_csv('processed_patriots_after.csv', encoding='utf-8', index_col= None)
#data = pd.DataFrame.from_csv('processed_superbowl_after.csv', encoding='utf-8', index_col= None)


#data = pd.DataFrame.from_csv('pre_bitcoin.csv', encoding='utf-8', index_col= None)

data.text = data.text.astype(str)

data.text.apply(lambda x: create_dictionary(x, emoji))

print("hello")
data.text.apply(lambda x: emoji_count(x, emoji))

#print(emoji)

#print("dictionary size is ",len(emoji))

emoji = dict(Counter(emoji).most_common(30))


length = len(data.index)

dens = {}
denss = {}

for i in emoji:
    dens[i] = (1000 * emoji[i])/length
    denss[i] = (emoji[i] + 1)/(length  + 1)


#print(emoji.keys())


# second subset 


emoji1 = {}



data1.text = data1.text.astype(str)

data1.text.apply(lambda x: create_dictionary(x, emoji1))

data1.text.apply(lambda x: emoji_count(x, emoji1))

print("----emoji1----")
#print(emoji1)

emoji1 = dict(Counter(emoji1).most_common(30))

length1 = len(data1.index)

dens1 = {}
dens1s = {}

for i in emoji1:
    dens1[i] = (1000 * emoji1[i])/length1
    dens1s[i] = (emoji1[i] + 1)/(length1  + 1)


final_emojis_set = []
final_emojis = {}
final_emojis1= {}
logor = {}
densmean = {}



import math

for i in emoji:
    for j in emoji1:
        if i == j and emoji[i]>0 and emoji1[j]>0:
            final_emojis_set = i
            final_emojis[i] = emoji[i]
            final_emojis1[j] = emoji1[j]
            logor[i] = round(math.log(denss[i]/dens1s[i]), 2)
            densmean[i] = round((dens[i] + dens1[i])/2, 2)


print(len(logor), len(densmean))

print(logor.keys(), logor.values())

print(densmean.keys(), densmean.values())

            

#plotting the distribution

#plt.figure(figsize=(10,8))

fig, ax = plt.subplots(figsize=(10,8))


#ax.set_title("Emoji")
ax.set_xlabel("Log odds ratio")
ax.set_ylabel("Frequency (per 1000 tweets)")
#ax.set_xticklabels(x_labels)




flags1 = ['eagle.png', 'american_football.png', 'face_with_tears_of_joy.png', 
          'clapping_hands.png', 'trophy.png', 'party_popper.png', 
          'medium-dark_skin_tone.png', 'medium_skin_tone.png', 'raising_hands.png',
          'fire.png', 'light_skin_tone.png', 'thumbs_up.png', 'rolling_on_the_floor_laughing.png', 
          'medium-light_skin_tone.png', 'flexed_biceps.png', 'smiling_face_with_heart-eyes.png', 
          'folded_hands.png', 'bottle_with_popping_cork.png', 'loudly_crying_face.png', 'grinning_face_with_smiling_eyes.png', 
          'smiling_face_with_smiling_eyes.png', 'smiling_face_with_sunglasses.png',
          'smiling_face_with_open_mouth.png', 'OK_hand.png', 'rugby_football.png', 'oncoming_fist.png', 
          'red_heart.png', 'thinking_face.png', 'face_blowing_a_kiss.png', 'blue_heart.png',
          'grimacing_face.png', 'crying_face.png', 'ring.png', 'eyes.png']


j=0

plt.xlim((-0.5,1.9))
plt.ylim((-10,135))

for i in logor:
    x_value = logor[i]
    y_value = densmean[i]

    arr_img = plt.imread(flags1[j])

    imagebox = OffsetImage(arr_img, zoom=0.2)
    imagebox.image.axes = ax

    ab = AnnotationBbox(imagebox, [x_value, y_value],
                        xybox=(x_value, y_value),
                        xycoords='data',
                        boxcoords="offset points",
                        pad=0.5
                        )
    ax.add_artist(ab)
    j= j+1

plt.savefig("comparision_after.png")

plt.show()

