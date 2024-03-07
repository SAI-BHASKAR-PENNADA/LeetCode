class Solution:

    def predictPartyVictory(self, senate: str) -> str:
        deleted = set()
        r = []
        d = []

        for i in range(len(senate)):
            if senate[i] == 'R':
                r.append(i)
            else:
                d.append(i)
        
        while True:
            for i in range(len(senate)):
                if i not in deleted and senate[i] == 'R':
                    if not d:
                        return "Radiant"

                    found = False
                    for j in range(len(d)):
                        if d[j] > i:
                            found = True
                            deleted.add(d.pop(j))
                            break
                    if not found:
                        deleted.add(d.pop(0))
                    

                elif i not in deleted and senate[i] == 'D':
                    if not r:
                        return "Dire"

                    found = False
                    for j in range(len(r)):
                        if r[j] > i:
                            found = True
                            deleted.add(r.pop(j))
                            break
                    if not found:
                        deleted.add(r.pop(0))