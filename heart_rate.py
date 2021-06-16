"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum.
"""

print('This program will train your heart:) ')
age = float(input('Please enter your age: '))

highest_beat = (220 - age)
max_beat = highest_beat * .85
min_beat = highest_beat * .65

print(f'When you exercise to strengthen your heart, you should \nkeep your heart rate between {min_beat:.0f} and {max_beat:.0f} beats per minute. ')