# 1. skill_tree의 문자열의 내용에서 skill과 같은 문자가 있다면 list에 넣는다
# 2. list에 저장된 단어 순서와 skill의 순서를 비교
# 3. 같을시 answer 에 1


def solution(skill, skill_trees):
    answer = 0
    for skill_tree_text in skill_trees:
        list =[]
        for stw in skill_tree_text:
            if stw in skill:
                list.append(stw)

        #list에 저장된 단어와 skill의 순서가 다르면 break
        for j in range(len(list)):
            if list[j] != skill[j]:
                break
        #아니면 answer에 +1 해준다
        else:
            answer += 1
    return answer
