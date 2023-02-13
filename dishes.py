import pandas as pd
import xldata

class dishesclass:
    def __init__(self):
        self.dishdf= pd.DataFrame();

    def getdishesdf(self):
        self.dishdf = xldata.xltodf("static/database/dishnutri.xlsx");
        return self.dishdf;

    def dishsbyCond(self, col, cond, limit, dishdf= " ", condidf=" "):
        if dishdf == " ":
            dishdf= self.dishdf;
        if cond == '<':
            df = dishdf[dishdf[col] < limit];
        if cond == '>':
            df = dishdf[dishdf[col] > limit];
        if cond == '=':
            df = dishdf[dishdf[col] == limit];
            return df;

class nutrireq:
    def __init__(self):
        self.dishmethfrqreqdf = pd.DataFrame();
        self.nutrireqdf= pd.DataFrame();
        self.fooditemfrq = pd.DataFrame();
        self.dishtype = pd.DataFrame();
        self.nutridf = pd.DataFrame();
        self.foodclassdf = pd.DataFrame();
        print("dishes py");
    def getdefaltnutrireq(self, df):
        if self.dishmethfrqreqdf.equals(df):
            {}# self.dishmethfrqreqdf = xldata.xltodf("static/database/dishmethfrqreq.xlsx");
        if self.nutrireqdf.equals(df):
            {}# self.nutrireqdf= xldata.xltodf("static/database/nutrirew.xlsx");
        if self.fooditemfrq.equals(df):
            {}#self.fooditemfrq = xldata.xltodf(r"C:\Users\Harshitha\Desktop\python\diet\database\foodnutri.xlsx");
        if self.dishtype.equals(df):
            {}# self.dishtype = xldata.xltodf(r"C:\Users\Harshitha\Desktop\python\diet\database\currytype.xlsx");
        if self.nutridf.equals(df):
            {}#self.nutridf = xldata.xltodf(r"C:\Users\Harshitha\Desktop\python\diet\database\nutrireq.xlsx");
        if self.foodclassdf.equals(df):
            {}#self.foodclassdf = xldata.xltodf(r"C:\Users\Harshitha\Desktop\python\diet\database\foodclass.xlsx");
        else:
            print("invalid");

        return;

class userdishdta:
    def __init__(self):
        self.usrdishusg= pd.DataFrame();
    def getuserdishdta(self):
        {}#self.foodclassdf = xldata.xltodf(r"C:\Users\Harshitha\Desktop\python\diet\database\raniusg.xlsx");
    def logusrdta(self):
        {}

class glbalusrdta:
    def __init__(self):
        self.glblusrdtadf= pd.DataFrame();
    def getglbalusrdta(self):
        {}
