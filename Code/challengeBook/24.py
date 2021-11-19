#Challenge 24, structured record
#using Objects

class Results:
    total = 0
    
    def __init__(self):
        self.homeTeam = []
        self.homeTeamScore = []
        self.awayTeam = []
        self.awayTeamScore = []

    def addGame(self,homeTeam,homeTeamScore,awayTeam,awayTeamScore):
        self.homeTeam.append(homeTeam)
        self.homeTeamScore.append(homeTeamScore)
        self.awayTeam.append(awayTeam)
        self.awayTeamScore.append(awayTeamScore)

        self.total += 1
        
    def disp(self, team):
        self.found = 0
        
        for i in range(self.total):
            if team in [self.homeTeam[i],self.awayTeam[i]]:
                self.found += 1
                print("{0}-{1} to {2}-{3}".format(self.homeTeam[i], self.homeTeamScore[i], self.awayTeam[i], self.awayTeamScore[i]))

        print("{0} of {1} Games shown".format(self.found, self.total))

def main():
    struct = Results()
    while True:

        select =int(input("Would you like to add a game(1), see the games(2) or exit(3)"))
        if select == 1:
            homeInp = input("Enter the hometeam: ")
            scoreHInp = int(input("Enter the hometeam's score: "))
            awayInp = input("Enter the awayteam: ")
            scoreAInp = int(input("Enter the awayteam's score: "))

            struct.addGame(homeInp,scoreHInp,awayInp,scoreAInp)

        elif select == 2:
            search = input("Search by team name: ")
            struct.disp(search)

        elif select == 3:
            exit()

if __name__ == "__main__":
    main()
