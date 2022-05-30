score = float(input('Please enter operator score:'))
print('Your score is', score)
if score >= 60:
    print('Pass')
elif 0 < score < 60:
    print('Fail')
elif score == 0.0:
    print('0.0')
else:
    print('正確以上條件')
