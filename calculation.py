from balldontlie import balldontlie, player, stats
from matplotlib import pyplot as plt

'''This function gets more information about the player by inputting 
their name and dataset to search'''
def getplayer(firstname, lastname, datalist):
        for players in datalist:
            for info in players.data:
                if info['first_name'] == firstname and info['last_name'] == lastname:
                    return player(info['first_name'], info['last_name'], info['id'])

def main():
    totalpages = range(1, 34)
    kobeyears = range(1996,2016)
    kobestatlist = []
    kobeperlist = []
    datalist = []
    for page in totalpages:
        datalist.append(balldontlie('https://www.balldontlie.io/api/v1/players?page=' + str(page)))
    kobe = getplayer('Kobe', 'Bryant', datalist)
    for year in kobeyears:
        kobestatlist.append(kobe.getstats(kobe,year))
    for stat in kobestatlist:
        kobeperlist.append(stat.calculate_PER(stat))
    plt.plot(kobeyears, kobeperlist, label= "Kobe Bryant's Player Efficiency Rating", 
    color='yellow')
    plt.xlabel('Season')
    plt.xticks(kobeyears)
    plt.ylabel('Player Efficiency Rating')
    plt.title('Change in PER Over Time')
    ax = plt.gca()
    ax.set_facecolor('purple')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()

