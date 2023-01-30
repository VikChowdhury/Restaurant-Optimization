import pandas as pd
chickIng = [['chicken',.25],['bread',1],['cheese',.1]]
beefIng = [['beef',.25],['bread',1],['cheese',.1]]
porkIng = [['pork',.25],['bread',1],['cheese',.1]]
#example market for restaurant
exGroc = [['chicken',5],['beef',8],['pork',6],['cheese',4],['bread',.5]]

class Market:
    def __init__(self,datframe = None):
        self.mark = {}
        if datframe!= None:
            for i in datframe:
                self.mark.update({i[0]:i[1]})
    def access(self,name):
        return self.mark[name]
    def refresh(self, datframe):
        for i in datframe:
            self.mark.update({i[0],i[1]})
class Dish:
    def __init__(self,name, ing, hard, time, price, market):
        self.name = name #name of dish
        self.ing = ing #list of ingredients. Each ingredient is a list ["Name",quantity]
        self.hard = hard #difficulty in making dish rated 1-10
        self.time = time #time needed to make the dish in minutes
        self.price = price #price dish is sold for
        self.market = market #market
    
    def labour(self):
        wage = self.hard * 5 + 10
        return (self.time/60) * wage

    def cost(self):
        cost = 0
        for i in self.ing:
            cost += i[1]*self.market.access(i[0])
        cost+=self.labour()
        return cost

    def profit(self):
        return self.price-self.cost()
    def refresh(self):
        self.market.refresh()

class Menu:
    def __init__(self, more = None):
        if more == None:
            self.all = []
        else:
            self.all = []
            for i in more:
                self.all.append(i)
    def add(self, dish):
        self.all.append(dish)
    def addmany(self,dishes): #input list of dishes
        for i in dishes:
            self.all.append(i)
    def getDish(self,ind):
        return self.all[ind]
    
menu1 = Menu()
#dataframe1 = pd.read_excel('C:\\Users\\duket\\OneDrive\\Documents\\rest-Market.xlsx')
#store = Market(dataframe1)
grocery = Market(exGroc)
men = Menu()
men.add(Dish('Chicken Melt',chickIng,3,15,12,grocery))
men.add(Dish('Beef Melt', beefIng,3,15,12,grocery))
men.add(Dish('Pulled Pork Melt', porkIng,3,15,12,grocery))
print(men.getDish(1).profit()) #profit for the beef melt
