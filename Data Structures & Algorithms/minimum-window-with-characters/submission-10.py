
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        idea scrapped
        #Creating a set so that we can use it for faster verification before all values are put in

        # tset = set(t)

        """
        # tdict is a counter variable with the number of characters in t   to match when we hit the required variables
        tdict = dict()

        # sdict will allow you to track t values
        sdict = dict()

        def check(td,sd):
            #Function to check if sd has all or more than check
            
            for i in td:
                if sd[i] < td[i] :
                    return False

            return True
            
        for i in t:
            if i in tdict: 
                tdict[i] +=1
            else:
                tdict[i] = 1
        
        for i in tdict:
            sdict[i] = 0

        m = (0,100000000000000)
        l = 0
        for i in range(len(s)):
            if s[i] in tdict:
                l = i
                break

        have = 0
        need = len(tdict)        

        i = 0
        l=0
        for l in range(len(s)):
            if s[l] in tdict:
                break
        while i < len(s) :
            
            while i< len(s) and s[i] not in tdict:
                i+=1    
            
            if i>=len(s):
                break
            
            
            sdict[s[i]]+=1
            if sdict[s[i]] ==1:
                have+=1

            while have>=need and check(tdict,sdict):
                if i-l < (m[1] - m[0]):
                    m = (l,i)


                sdict[s[l]] -=1
                if sdict[s[l]] ==0:
                    have -=1
                l+=1

                while l<i and s[l] not in tdict:
                    l+=1
            i+=1
        if m[1] == 100000000000000 :
            return ""
        return s[m[0]:m[1]+1]


             





        


        

        


