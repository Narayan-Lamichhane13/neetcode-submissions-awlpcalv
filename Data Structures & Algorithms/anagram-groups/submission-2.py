class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # count the number of same letters
        # uniqueness of the same letters
        # if true^ --> add to a pair list 


        # hash_map {  1 a 1 c 1 t : [].append(act, cat) }
        pair_map = defaultdict(list)

        for string in strs:

            buffer = [0] * 26 #[0,0,0,0.....]

            for char in string:
                buffer[ord(char) - ord('a')] += 1
            
            pair_map[tuple(buffer)].append(string) # [1,0,1....1...0] : [act, cat]
        

        result = list(pair_map.values())
        return result 