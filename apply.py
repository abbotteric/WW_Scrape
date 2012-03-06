import sys

fat = int(sys.argv[1])
carbs = int(sys.argv[2])
protein = int(sys.argv[3])
fiber = int(sys.argv[4])

pp = 0.255018619583*fat + 0.119532905297*carbs + 0.0859900481541*protein + -0.079267094703*fiber

print pp
print round(pp) 
