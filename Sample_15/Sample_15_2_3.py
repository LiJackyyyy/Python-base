number_of_voters = 121
number_of_agree = 70
number_of_disargree = 20
vote_rate = (number_of_agree + number_of_disargree) / number_of_voters * 100

info = {'number_of_voters': number_of_voters,
        'number_of_agree': number_of_agree,
        'vote_rate':  vote_rate}

ans = '投票人數:{number_of_voters},' \
      '同意人數{number_of_agree},' \
      '投票率{vote_rate}'.format(**info)
print(ans)
