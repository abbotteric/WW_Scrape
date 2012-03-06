import sys

fat = int(sys.argv[1])
carbs = int(sys.argv[2])
protein = int(sys.argv[3])
fiber = int(sys.argv[4])

pp = 0.255083527127*fat + 0.119597812842*carbs + 0.0860549556987*protein + -0.0792021871584*fiber

print pp
print round(pp) 
