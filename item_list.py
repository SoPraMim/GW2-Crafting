""" Support functions for calculate_crafts """

import numpy as np
import math

class ItemList:
    def __init__(self, item_list):
        self.item_list=item_list


    def getSingleID(self,text: str):
        flag=False
        for i in range(len(self.item_list)):
            if text==self.item_list['name'][i]:
                flag=True
                break
        if flag == True:
            return self.item_list['id'][i]
        else:
            return 

    def getID(self,List:list):
        listIDs=[]
        for i in range(len(List)):
            listIDs.append(self.getSingleID(List[i]))
        return listIDs

    def getValueFromID(self,ID,Value):
        for i in range(len(self.item_list)):
            if ID==self.item_list['id'][i]:
                break
        return self.item_list[Value][i]

class RecipeList:
    def __init__(self, recipe_list):
        self.recipe_list=recipe_list

def getMaterials(OutputID, recipe_list: RecipeList, item_list: ItemList) -> list:
    out=[]
    for i in range(len(recipe_list.recipe_list)):
        if OutputID == recipe_list.recipe_list["output"][i]:
            idx=i
            break
    if not ('idx' in locals()):
        return out
    for i in range(5):
        if (not np.isnan(recipe_list.recipe_list['item_'+str(i+1)+'_id'][idx])):  # If there is a material:
            if np.isnan(item_list.getValueFromID(recipe_list.recipe_list['item_'+str(i+1)+'_id'][idx],'buy_price')):          #If it is not purchaseable in the TP, check how it can be crafted.
                crafted_materials=getMaterials(recipe_list.recipe_list['item_'+str(i+1)+'_id'][idx],recipe_list,item_list)
                for line in range(len(crafted_materials)):
                    crafted_materials[line][1]=crafted_materials[line][1]*recipe_list.recipe_list['item_'+str(i+1)+'_quantity'][idx]
                    out.append(crafted_materials[line])
            else:
                out.append([recipe_list.recipe_list['item_'+str(i+1)+'_id'][idx],recipe_list.recipe_list['item_'+str(i+1)+'_quantity'][idx]])
    return out

def ConvertToGold(Value) -> list:
    out=[]
    out.append(math.floor(Value/10000))                      #Gold
    out.append(math.floor((Value-out[0]*10000)/100))         #Silver
    out.append(math.floor((Value-out[0]*10000-out[1]*100)))  #Copper
    return out