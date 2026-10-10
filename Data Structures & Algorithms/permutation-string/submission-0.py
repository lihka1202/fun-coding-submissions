class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        L, R = 0, len(s1)-1
        dct_orig = {}
        for i in range(len(s1)):
            dct_orig[s1[i]]= 1 + dct_orig.get(s1[i],0)
        
        print(dct_orig)

        dct = {}
        for i in range(L, R + 1):
            dct[s2[i]] = 1 + dct.get(s2[i],0)
        print(dct)

        if dct == dct_orig:
            return True
        while R < len(s2) - 1:
            # Move the window 
            R += 1

            # Move L up
            if dct[s2[L]] == 1:
                del dct[s2[L]]
            else:
                dct[s2[L]] -= 1
            L += 1
            
            ## Add the R related ones
            dct[s2[R]] = 1 + dct.get(s2[R], 0)
            print("Orig: ",dct_orig)
            print("New: ",dct)
            ## Compare the DCT
            if dct == dct_orig :
                return True
        
        return False