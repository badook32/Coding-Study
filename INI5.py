"""
최대 1000줄로 이루어진 파일 하나가 주어진다.
원본 파일에서 줄 번호가 짝수인 줄만 포함된 새로운 파일을 반환하라.
(줄 번호는 1부터 시작하는 것(1-based numbering)으로 가정한다)
"""

sample_txt = """Bravely bold Sir Robin rode forth from Camelot
Yes, brave Sir Robin turned about
He was not afraid to die, O brave Sir Robin
And gallantly he chickened out
He was not at all afraid to be killed in nasty ways
Bravely talking to his feet
Brave, brave, brave, brave Sir Robin
He beat a very brave retreat"""

lines = sample_txt.strip().split("\n")

for i, line in enumerate(lines):
    if (i + 1) % 2 == 0:
        print(line)
