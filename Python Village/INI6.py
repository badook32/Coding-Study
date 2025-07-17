"""
최대 10,000글자로 이루어진 문자열 s이 주어진다.
문자열 s에서 각 단어가 등장한 횟수를 세어라.
단어들은 공백(스페이스)로 구분되어 있으며, 대소문자를 구분(case-sensitive)한다.
출력 결과에서 각 줄의 순서는 아무 순서나 상관없다.
"""

sample_txt = "We tried list and we tried dicts also we tried Zen"

split_txt = sample_txt.split()

word_counts = {}

for word in split_txt:
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1

for word, count in word_counts.items():
    print(f"{word} {count}")
