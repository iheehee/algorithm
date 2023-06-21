"""
N 명의 이름과 국어, 영어, 수학 점수가 주어진다.
정렬 조건
1. 국어 점수가 감소하는 순서
2. 국어 점수가 같으면 영어 점수가 증가하는 순서
3. 영어 점수가 같으면 수학 점수가 감소하는 순서
4. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서
"""

n = int(input())

# 학생 정보 입력
students = [input().split() for _ in range(n)]

students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in students:
    print(student[0])
