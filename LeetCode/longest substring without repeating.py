def lengthOfLongestSubstring(s: str) -> int:
        sub={}
        current_substring_start=0
        current_lenth=0
        longest_sub=0
        
        for index,letter in enumerate(s):
            if letter in sub and sub[letter]>=current_substring_start:
                current_substring_start=sub[letter]+1
                current_lenth=index-sub[letter]
                sub[letter]=index
                
            else:
                sub[letter]=index
                current_lenth+=1
                if current_lenth>longest_sub:
                    longest_sub=current_lenth
        return (longest_sub)
                
s='pwwkew'          
lengthOfLongestSubstring(s)
