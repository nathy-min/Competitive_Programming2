class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        ptr1 = ptr2 = 0
        max_matching = 0

        while ptr1 < len(players) and ptr2 < len(trainers):

            while ptr2 < len(trainers) and trainers[ptr2] < players[ptr1]:
                ptr2 += 1

            print(ptr1, ptr2)
            if ptr1 < len(players) and ptr2 < len(trainers) and trainers[ptr2] >= players[ptr1]:
                max_matching += 1 
            ptr1 += 1 
            ptr2 += 1
            
              

        return max_matching