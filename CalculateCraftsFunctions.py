# Support functions for CalculateCrafts

import numpy as np
import math

class ItemList:
    def __init__(self, ItemList):
        self.ItemList=ItemList


    def getSingleID(self,text):
        flag=False
        for i in range(len(self.ItemList)):
            if text==self.ItemList['name'][i]:
                flag=True
                break
        if flag == True:
            return self.ItemList['id'][i]
        else:
            return 

    def getID(self,List):
        listIDs=[]
        for i in range(len(List)):
            listIDs.append(self.getSingleID(List[i]))
        return listIDs

    def getValueFromID(self,ID,Value):
        for i in range(len(self.ItemList)):
            if ID==self.ItemList['id'][i]:
                break
        return self.ItemList[Value][i]



class RecipeList:
    def __init__(self, RecipeList):
        self.RecipeList=RecipeList



def getMaterials(OutputID,RecipeList,ItemList):
    out=[]
    for i in range(len(RecipeList.RecipeList)):
        if OutputID == RecipeList.RecipeList["output"][i]:
            idx=i
            break
    if not ('idx' in locals()):
        return out
    for i in range(5):
        if (not np.isnan(RecipeList.RecipeList['item_'+str(i+1)+'_id'][idx])):  # If there is a material:
            if np.isnan(ItemList.getValueFromID(RecipeList.RecipeList['item_'+str(i+1)+'_id'][idx],'buy_price')):          #If it is not purchaseable in the TP, check how it can be crafted.
                CraftedMaterials=getMaterials(RecipeList.RecipeList['item_'+str(i+1)+'_id'][idx],RecipeList,ItemList)
                for line in range(len(CraftedMaterials)):
                    CraftedMaterials[line][1]=CraftedMaterials[line][1]*RecipeList.RecipeList['item_'+str(i+1)+'_quantity'][idx]
                    out.append(CraftedMaterials[line])
            else:
                out.append([RecipeList.RecipeList['item_'+str(i+1)+'_id'][idx],RecipeList.RecipeList['item_'+str(i+1)+'_quantity'][idx]])
    return out

def ConvertToGold(Value):
    out=[]
    out.append(math.floor(Value/10000))                      #Gold
    out.append(math.floor((Value-out[0]*10000)/100))         #Silver
    out.append(math.floor((Value-out[0]*10000-out[1]*100)))  #Copper
    return out