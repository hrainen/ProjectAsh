class DungeonGen:

    # takes in the size of board you want
    def __init__(self, size):
        self.board = [] #this will hold all of the values associated with ascii
        self.size = size
        for x in range(self.size**2):
            self.board.append("x")
        


    # takes in 2d room array [[dim of room],[coords of room]]       Could make room another class later on
    #                        [length ⬇, width ➡],[TL, TR, BR, BL] (top left, bot right, etc)
    def placeRoom(self, room): 
        start = room[1][0] # the starting location of the room in the 1d array
        for length in range(room[0][0]):
                for width in range(room[0][1]):
                        # if first row (run checks) straight wall across
                        if length == 0 or length == (room[0][0]-1):
                                self.board[start + self.size*length+width] = "#"
                        else:
                                # if its a side wall (left or right) replace with #, otherwise, its space we can walk on "_"
                                if width == 0 or width == (room[0][1] -1):
                                        self.board[start + self.size*length+width] = "#"
                                else:
                                        self.board[start + self.size*length+width] = "_"
                        """
                        if(start < len(self.board) and start >= 0):
                                self.board[start] = "#" # this creates the top wall for a room

                        if((start + self.size*(room[0][0]-1)) < len(self.board) and (start + self.size*(room[0][0]-1)) >= 0):
                                self.board[start + self.size*(room[0][0]-1)] = "#" # this creates the bottom wall for a room
                        
                        start += 1
                        """
                
        return 0

    def printBoard(self):
        for row in range(self.size):
            for col in range(self.size):
                print(self.board[row*self.size + col], end=" ")
            print("")

def main():
    board = DungeonGen(32)
    board.placeRoom([[5,5],[50]])
    board.printBoard()

main()

