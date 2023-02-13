import dishes
import pandas as pd

dishesobj= dishes.dishesclass();
dishdf= dishesobj.getdishesdf();

def srchkeywrd(kywrd):
  dshnme= dishdf["dish_name"];
  srch= list();
  srchnum= list();
  srchdic= dict();
  if type(kywrd) == 'int':
    dish= dishdf.loc[kywrd];
    srchdic[kywrd]= dish;
  else:
    for indx,dishnm in dshnme.items():
      if kywrd in dishnm:
        srch.append(dishnm);
        srchnum.append(indx);
  srchdict= dict(zip(srchnum, srch));


  return srchdict;

def calcnutri(dishlst,dshqtylst):
    mealdf= pd.DataFrame();
    mealdf= dishdf.loc[dishlst];
   # for indx in dishlst:
    #  el= dishdf.loc[indx];
     # mealdf = pd.concat([mealdf, pd.DataFrame(el)], axis=1, ignore_index=False);
    mealdf.insert(loc=10, column='usrqty', value= dshqtylst );
    mealdf["Calories"] =  mealdf["Calories"]* mealdf["usrqty"]*0.01; mealdf["Carbohydrate_g"]= mealdf["Carbohydrate_g"]* mealdf["usrqty"]*0.01;
    mealdf["Protein_g"]= mealdf["Protein_g"]* mealdf["usrqty"]*0.01; mealdf["Fat_g"]= mealdf["Fat_g"]* mealdf["usrqty"]*0.01;
    calories = mealdf["Calories"].sum();
    carb = mealdf["Carbohydrate_g"].sum();
    prot = mealdf["Protein_g"].sum();
    fat = mealdf['Fat_g'].sum();
    calreq = 1200;  carbreq= 147;  protreq= 88;  fatreq= 26;
    nutridict = {"Calories":[calories,calreq],"Carbohydrate_g": [carb,carbreq], "Protein_g": [prot,protreq], "Fat_g": [fat,fatreq]};
    return nutridict;

