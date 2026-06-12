class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import deque
        words = set(wordList)
        if endWord not in words:
            return 0
        
        que = deque([(beginWord, 1)])
        visited = set([beginWord])

        while que:
            current_word, steps = que.popleft()
            if current_word == endWord:
                return steps
            
            for i in range(len(current_word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c == current_word[i]:
                        continue
                    new_word = current_word[:i] + c + current_word[i+1:]

                    if new_word in words and new_word not in visited:
                        visited.add(new_word)
                        que.append((new_word, steps + 1))
        return 0