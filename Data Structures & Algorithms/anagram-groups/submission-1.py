class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        group_map = defaultdict(list)

            # [0,1,0,2,0,1...] : [cat, hat, etc]

    
        for string in strs:
            buffer = [0] * 26

            for c in string:
                buffer[ord(c) - ord('a')] += 1
            
            group_map[tuple(buffer)].append(string)
        
        result = list(group_map.values())

        return result


