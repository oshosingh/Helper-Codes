
class Matcher:
    def __init__(self, text, pat):
        self.text = text
        self.pat = pat

    def KMPAlgo(self):
        n = len(self.text)
        m = len(self.pat)
        
        def constructLPS():
            leng = 0
            i = 1
            while i<m:
                if self.pat[i]==self.pat[leng]:
                    leng += 1
                    lps[i] = leng
                    i += 1
                else:
                    if leng!=0:
                        leng = lps[leng-1]
                    else:
                        lps[i] = 0
                        i += 1
                        
        lps = [0]*m
        constructLPS()
        i = 0; j = 0
        indices = []

        while i<n:
            if self.text[i]==self.pat[j]:
                i += 1
                j += 1
            if j==m:
                indices.append(i-j)
                j = lps[j-1]
            elif (i<n and self.pat[j]!=self.text[i]):
                    if j!=0:
                        j = lps[j-1]
                    else:
                        i += 1
        return indices

                        
