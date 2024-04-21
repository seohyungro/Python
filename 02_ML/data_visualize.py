import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler, PowerTransformer


class data_:
    
    def read_file(self , filepath):
        print(filepath)
        if str(filepath)=='':
            return ""
        else:
            return pd.read_csv(str(filepath) , index_col=False )
            

    def get_column_list(self , df):
        # print(list(df.columns))
        # columnname_list=[]
        # for i in df.columns:
        #     columnname_list.append(i)
        return list(df.columns)
    
    def get_cat(self, df):
        if(len(df)==0):
            pass
        else:
            cat_col=[x for x in df.columns if df[x].dtype=='object']
            # cat_col=[]
            # for i in df.columns:
            #     if (df[i].dtype=='object'):
            #         cat_col.append(i)
            return cat_col

    def convert_category(self, df ,column_name):
        print(df[column_name].isna().sum())
        le = LabelEncoder()
        df[column_name]= le.fit_transform(df[column_name])
        return df[column_name]
    
    def drop_columns(self , df , column_name):
        return df.drop(column_name, axis=1)
    
    def get_empty_list(self , df):
        if(len(df)==0):
            pass
        else:
            empty_list=[x for x in df.columns if df[x].isnull().values.any()]    
            return empty_list
    
    def fillmean(self, df , column_name):
        
        df[column_name].fillna(df[column_name].mean(), inplace=True)
        return df[column_name]
    
    def fillnan(self , df , column_name):
        df[column_name].fillna("Unknown", inplace=True)
        return df[column_name]
        
    def StandardScaler(self, df, target_name):
        sc = StandardScaler()
        x = df.drop(target_name, axis = 1)
        scaled_features = sc.fit_transform(x)
        scaled_features_df = pd.DataFrame(scaled_features, index=x.index, columns=x.columns)
        scaled_features_df[target_name] = df[target_name]
        return scaled_features_df
    
    def MinMaxScaler(self, df, target_name):
        mc = MinMaxScaler()
        x = df.drop(target_name, axis = 1)
        scaled_features = mc.fit_transform(x)
        scaled_features_df = pd.DataFrame(scaled_features, index=x.index, columns=x.columns)
        scaled_features_df[target_name] = df[target_name]
        return scaled_features_df
    
    def PowerScaler(self, df, target_name):
        pc = PowerTransformer()
        x = df.drop(target_name, axis = 1)
        scaled_features = pc.fit_transform(x)
        scaled_features_df = pd.DataFrame(scaled_features, index=x.index, columns=x.columns)
        scaled_features_df[target_name] = df[target_name]
        return scaled_features_df
    def 