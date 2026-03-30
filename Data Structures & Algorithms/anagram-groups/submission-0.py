class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List(str)]:

        # dictionary we will group/pair the anagram words
        group_dict = defaultdict(list)

        for string in strs:
            # an array of 26 0s
            buffer = [0] * 26

            for char in string:
                # the letter we encounter will be subtracted by ascii 'a'
                # then that will align/map a as index 0, b as index 1, c as...
                # then that representative spot will be turned to a 1
                # each word will have a 1 in the corresponding spot to the letter it has
                buffer[ord(char) - ord('a')] += 1
            
            
            group_dict[tuple(buffer)].append(string)

        return list(group_dict.values())





