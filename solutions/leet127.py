# word ladder
#bfs sol
from collections import deque
def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    wordset = set(wordList)
        queue = collections.deque()
        queue.append((beginWord, 1))
        word_length = len(beginWord)
        while queue:
            word, step = queue.popleft()
            if word == endWord:
                return step
            for i in range(word_length):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i]+c+word[i+1:]
                    if newWord in wordset:
                        wordset.remove(newWord)
                        queue.append((newWord, step+1))
        return 0