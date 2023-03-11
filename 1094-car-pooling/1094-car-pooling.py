class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passengers = [0] * (1001)
        
        for no_of_passengers, start, end in trips:
            passengers[start] += no_of_passengers
            passengers[end] -= no_of_passengers
            
        max_passengers = 0
        
        for no_of_passengers in passengers:
            max_passengers +=  no_of_passengers
            if max_passengers > capacity:
                return False
        
        return True