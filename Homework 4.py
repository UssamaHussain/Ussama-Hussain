Task 1:


def insert_interval(intervals, newInterval):
    result = []
    i = 0
    # Add all intervals ending before newInterval starts
    while i < len(intervals) and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1

    # Merge overlapping intervals
    while i < len(intervals) and intervals[i][0] <= newInterval[1]:
        newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        i += 1

    result.append(newInterval)

    # Add remaining intervals
    while i < len(intervals):
        result.append(intervals[i])
        i += 1

    return result


# Test cases
intervals1 = [[1, 3], [6, 9]]
newInterval1 = [2, 5]
print(insert_interval(intervals1, newInterval1))

intervals2 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval2 = [4, 8]
print(insert_interval(intervals2, newInterval2))


Task 2:
from collections import defaultdict, deque


def findLadders(beginWord, endWord, wordList):
    if endWord not in wordList:
        return []

    wordSet = set(wordList)
    graph = defaultdict(list)
    level = {beginWord: [[beginWord]]}

    queue = deque([beginWord])

    while queue:
        new_level = defaultdict(list)
        for word in queue:
            if word == endWord:
                return level[word]
            for i in range(len(word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + char + word[i + 1:]
                    if new_word in wordSet:
                        new_level[new_word] += [path + [new_word] for path in level[word]]

        wordSet -= set(new_level.keys())
        level = new_level
        queue = deque(new_level.keys())

    return []


# Test cases
beginWord1 = "hit"
endWord1 = "cog"
wordList1 = ["hot", "dot", "dog", "lot", "log", "cog"]
print(findLadders(beginWord1, endWord1, wordList1))

beginWord2 = "hit"
endWord2 = "cog"
wordList2 = ["hot", "dot", "dog", "lot", "log"]
print(findLadders(beginWord2, endWord2, wordList2))


Task 3:

def maxProfit(prices):
    if not prices or len(prices) < 2:
        return 0

    max_profit = 0
    min_price = prices[0]

    for price in prices[1:]:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)

    return max_profit


# Test cases
prices1 = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices1))

prices2 = [7, 6, 4, 3, 1]
print(maxProfit(prices2))

Task 4:

def maxProfit(prices):
    max_profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            max_profit += prices[i] - prices[i - 1]
    return max_profit


# Test cases
prices1 = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices1))

prices2 = [1, 2, 3, 4, 5]
print(maxProfit(prices2))

prices3 = [7, 6, 4, 3, 1]
print(maxProfit(prices3))

Task 5:

def maximumGap(nums):
    if len(nums) < 2:
        return 0

    nums.sort()
    max_diff = 0
    for i in range(1, len(nums)):
        diff = nums[i] - nums[i - 1]
        max_diff = max(max_diff, diff)

    return max_diff


# Test cases
nums1 = [3, 6, 9, 1]
print(maximumGap(nums1))

nums2 = [10]
print(maximumGap(nums2)

