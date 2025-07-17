"""
길이가 최대 200자인 문자열 s와 네 개의 정수 a, b, c, d가 주어진다.
문자열 s에서 인덱스 a부터 b까지, 그리고 인덱스 c부터 d까지의 두 부분 문자열을 추출하여 공백을 사이에 두고 출력하라.
여기서 s[b]와 s[d]는 포함된다(슬라이스는 양쪽 끝을 포함해야 한다).
"""

sample = "HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain."

print(sample[22:28], sample[97:103])
