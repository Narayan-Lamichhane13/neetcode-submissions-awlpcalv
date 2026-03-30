class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Lengths have to be valid if it is an anagram
        if len(s) != len(t):
            return False


        s_dict = {}
        t_dict = {}

        for i in range(len(s)):
            #dict[key[value index]]
            s_dict[s[i]] = 1 + s_dict.get(s[i], 0) # if s[i] is found, return that value, else return 0 if not found or the letter isn't added yet
        

        for i in range(len(t)):
            t_dict[t[i]] = 1 + t_dict.get(t[i],0 )
            
        return s_dict == t_dict