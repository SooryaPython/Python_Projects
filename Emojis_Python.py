""" 
Date: 4th May 2022
Name: S. Soorya
File description: About emojis in Python
"""
# Before proceeding, in the terminal window, type "pip install emoji". Then only it will work properly
# Visit https://www.getemoji.com/ to get emojis. Visit https://www.pypi.org/ to see the Python packaging manager
# Printing emoji:
import emoji
print(emoji.emojize(":disappointed_face:")) # 😞
print(emoji.emojize(":slightly_smiling_face:")) # 🙂
print(emoji.emojize(":smiling_face_with_sunglasses:")) # 😎
print(emoji.emojize(":star-struck:")) # 🤩
print(emoji.emojize(":cold_face:")) # 🥶
# Sometimes, we can't find the names of emojis such as ":disappointed_face:". So, for that we can use: print(emoji.demojize(""))
print(emoji.demojize("😞")) # :disappointed_face:
print(emoji.demojize("🙂")) # :slightly_smiling_face:
print(emoji.demojize("😎")) # :smiling_face_with_sunglasses:
print(emoji.demojize("🤩")) # :star-struck:
print(emoji.demojize("🥶")) # :cold_face:

# Program Finished