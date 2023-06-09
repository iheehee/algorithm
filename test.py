from bisect import bisect_left, bisect_right

word = ["frodo", "front", "frost", "frozen", "frame", "kakao"]

queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

word.sort(key=lambda x: x[2])

print(word)

left_index = bisect_left(word, "kakao")

print(left_index)


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
