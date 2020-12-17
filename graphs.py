from file_importer0 import australia, brunei, cambodia, china, indonesia, japan, lao, malaysia, myanmar, new_zeland, philipines, singapore, thailand, vietnam
import matplotlib.pyplot as plt


list = [australia, brunei, cambodia, china, indonesia, japan, lao, malaysia, myanmar, new_zeland, philipines, singapore, thailand, vietnam]
names = ['Australia', 'Brunei', 'Cambodia', 'China', 'Indonesia', 'Japan', 'Lao', 'Malaysia', 'Myanmar', 'New Zealand', 'Philippines', 'Singapore', 'Thailand', 'Vietnam']

def plot_creator(ls, x):
    for v, y in zip(ls, names):
        plt.plot(australia['Year'], v[x], label= y)
    plt.title('%s vs Years'%(x))
    plt.legend(loc='best')
    plt.show()



#Here, write in the second variable the variable that you want to plot for. To know what variables are available, please check the ER diegram, specificallly the columns of the tables from the countries in the SQL database.
plot_creator(list, 'Account_Balance')
