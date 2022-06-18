class Solution:
    def carPooling(self, trips:list[list[int]], capacity: int) -> bool:
        maxOflist=max(trips)
        maxOflist.sort()
        changePassenger=[0]*(maxOflist[-1]+1)

        for t in trips:
            numberOfPassenger, start, end = t
            changePassenger[start] += numberOfPassenger
            changePassenger[end] -= numberOfPassenger
        # return changePassenger 

        currentPassengerCount=0
        for i in range(maxOflist[-1]+1):
            currentPassengerCount += changePassenger[i]
            if currentPassengerCount > capacity:
                return False
        return True    


p= Solution()
print(p.carPooling([[2,1,5],[3,3,7]],4))   