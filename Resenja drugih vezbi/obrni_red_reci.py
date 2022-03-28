def solution(text):
    for line in text.split('\n'):
        return(' '.join(line.split()[::-1]))


print(solution("Pera Peric je super mega car."))
print(solution("Red reci je obrnut."))
