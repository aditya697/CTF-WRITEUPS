lst = [65639, 65645, 65632, 65638, 65658, 65653, 65609, 65584, 65650, 65630, 65640, 65634, 65586, 65630, 65634, 65651, 65586, 65589, 65644, 65630, 65640, 65588, 65630, 65618, 65646, 65630, 65607, 65651, 65646, 65627, 65586, 65647, 65630, 65640, 65571, 65612, 65630, 65649, 65651, 65586, 65653, 65621, 65656, 65630, 65618, 65652, 65651, 65636, 65630, 65640, 65621, 65574, 65650, 65630, 65589, 65634, 65653, 65652, 65632, 65584, 65645, 65656, 65630, 65635, 65586, 65647, 65605, 65640, 65647, 65606, 65630, 65644, 65624, 65630, 65588, 65649, 65585, 65614, 65647, 65660]
x = 65537
for i in range(0,len(lst)):
    lst[i]=lst[i]^x
for i in lst:
    print(chr(i),end='')
