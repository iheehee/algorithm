"""
접근 방법
- querise 안의 단어를 스펠링으로 분리하여 리스트로 묶는다. 
- sort라이브러리의 활용해 정렬한다.  
- 쿼리의 첫 문장을 기준으로 내림차순 정렬
- 정렬한 단어를 기준으로 이진 탐색을 시도한다.
- 두번째 문장을 기준으로 정렬 ...  계속 정렬한다.
- 다시 이진탐색을 시도한다. 
- 문자의 길이가 같고 스펠링이 동일한 결과가 있다면 result 변수 카운트를 올린다. .
"""
from bisect import bisect_left, bisect_right

word = ["frodo", "front", "frost", "frozen", "frame", "kakao"]

queries = ["fro??", "????o", "fr???", "fro???", "pro?"]


def solution(word, queries):
    answer = []
    for query in queries:
        results = []
        # 쿼리의 길이와 단어의 길이가 같은 단어들로 데이터 재구성
        for i in word:
            if len(query) == len(i):
                results.append(i)
            else:
                continue
        for k in range(len(query)):
            if query[k] != "?":  # 물음표가 아니라면 해당 문자의 인덱스를 기준으로 정렬
                results.sort(key=lambda x: x[k])
                # bisect 라이브러리를 사용, 찾고자 하는 값의
                print(results)
                left_index = bisect_left(results, query[k])
                right_index = bisect_right(results, query[k])
                results = results[left_index : right_index + 1]
        count = len(results)  # 결과 값 카운팅하기
        answer.append(count)

    return answer


"""
- 이진탐색으로 정렬된 결과 값의 좌쪽 인덱스, 우쪽 인덱스를 찾는 함수 만들기
- 쿼리와 문장을 대조해 일치하면 카운트를 업하는 코드 구현
"""

print(solution(word, queries))
