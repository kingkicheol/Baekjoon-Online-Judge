N = int(input())
score = list(map(int, input().split()))
highscore = max(score)
new_score = [s/highscore*100 for s in score]
print(sum(new_score)/N)