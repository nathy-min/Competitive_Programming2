class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if not (coordinates[1][0] - coordinates[0][0]):
            slop = float('inf')
        else:
            slop = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
        for i in range(2, len(coordinates)):
            if slop == float('inf'):
                if (coordinates[i][0] - coordinates[i - 1][0]):
                    return False
            elif not (coordinates[i][0] - coordinates[i - 1][0]):
                return False
            elif (coordinates[i][1] - coordinates[i - 1][1]) / (coordinates[i][0] - coordinates[i - 1][0]) != slop:
                return False

        return True        