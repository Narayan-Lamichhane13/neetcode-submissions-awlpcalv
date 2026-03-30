class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s and t
        # return true if s and t have the same number of letters

        if len(s) != len(t):
            return False


        '''
        s {
            'r' : 2
            'a' : 2
            't' : 1
        }

        t {
            'r' : 2
            'a' : 2
            't' : 1
        }
        '''
        s_dict, t_dict = {}, {}

        for i in range(len(s)):
            #Add s[i], index char in the string to the dictionary as a key
            s_dict[s[i]] = 1 + s_dict.get(s[i], 0) # get will return 0 if s[i] is not found in the dictionary
            t_dict[t[i]] = 1 + t_dict.get(t[i], 0)
            

        return s_dict == t_dict