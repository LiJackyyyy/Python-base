score_f = float(input('Please enter your score:'))
# ....if 條件式   else ..... ， 如果是條件是正確會出現 if左邊的結果 ，如果是錯誤會出現 if 右邊的結果
score = int(score_f)if score_f == int(score_f) else score_f
result = 'Pass' if score >= 60 else 'fail'
print(result)
print('Your score is:', score)
