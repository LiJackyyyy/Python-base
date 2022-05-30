number_of_voters = 121
number_of_agree = 70
number_of_disargree = 20
vote_rate = (number_of_agree + number_of_disargree) / number_of_voters * 100
ans = '投票人數:{0:^5}同意人數{1:<5},不同意人數:{2:>},投票率{3:10}'\
    .format(number_of_voters, number_of_agree, number_of_disargree, vote_rate)
print(ans)

