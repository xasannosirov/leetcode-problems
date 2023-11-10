class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        if int(coordinates[1])%2==0 and ord(coordinates[0]) % 2 == 1:
            return True
        elif int(coordinates[1])%2==1 and ord(coordinates[0]) % 2 == 0:
            return True
        return False
