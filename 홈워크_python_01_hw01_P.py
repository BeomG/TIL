score = {
    'python': 80,
    'django': 89,
    'web': 83,
}
# 1번
score['algorithm'] = 90

# 2번
score['python'] = 85

# 3번
print(sum(score.values())/len(score))