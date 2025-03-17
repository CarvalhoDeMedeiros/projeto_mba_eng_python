import pandas as pd
import re
from src.tools.tools import padroniza_str


class CleanData:
    '''
    Classe responsavel por limpar os dados
        Args:
            None
        Returns:
            dataframe: dataframe limpo
    '''
    def __init__(self):
        super().__init__()
    def exeute(self):
        '''
        Função responsavel por executar o fluxo do projeto
        para efetivar a limpeza dos dados
            Args:
                None
            Returns:
                dataframe: dataframe limpo
        '''
        df = self.load_data()

        df_work = self.clean_data(df)

        return df_work

    def load_data(self):
        df = pd.read_csv("https://raw.githubusercontent.com/JackyP/testing/master/datasets/nycflights.csv", index_col=0)
        df["data"] = pd.to_datetime(df[['year', 'month', 'day']]) 
        print(df.head())

        return df
    
    def clean_data(self, df):
        # Colunas desejadas
        usecols=["year", "month",  "day", "hour", "minute","arr_delay","carrier","flight","air_time","distance", "origin", "dest"]

        # Filtrar dados
        df_raw = df.loc[
            (~df["carrier"].isna()) \
            & (~df["flight"].isna()) \
            & (~df["year"].isna()) \
            & (~df["hour"].isna()) \
            & (~df["minute"].isna()) \
            & (~df["month"].isna()) \
            & (~df["day"].isna()) \
            & (df["air_time"] > 0)
        ].loc[:, usecols]

        # Remover duplicados
        df_raw.drop_duplicates(inplace=True)

        # Verificar se a quantidade de linhas é a mesma
        tmp = df.loc[:, usecols].copy() 

        # Remover linhas com air_time = 0
        tmp = tmp[tmp["air_time"]>0]
        for col in ["carrier","flight", "year", "month", "day" ,"hour", "minute"]:
            tmp_df = tmp.loc[~df[col].isna()]
            tmp = tmp_df.copy()

        # Remover duplicados
        tmp.drop_duplicates(inplace=True)

        # Verificar se a quantidade de linhas é a mesma
        tmp.shape[0] == df_raw.shape[0]

        # Criar coluna de data
        df_raw["date_time"] =  pd.to_datetime(df_raw[["year", "month", "day", "hour", "minute"]],  dayfirst=True)
        df_raw["date_time"]

        # Remover colunas que não serão utilizadas
        usecols2 =["date_time", "arr_delay","carrier","flight","air_time","distance", "origin", "dest" ]

        new_columns = ["data_hora", "atraso_chegada", "companhia", "id_voo","tempo_voo", "distancia", "origem", "destino"]
        columns_map = {usecols2[i]: new_columns[i] for i in range(len(usecols2))}
        columns_map

        df_work = df_raw.loc[:, usecols2].copy()
        df_work.rename(columns=columns_map, inplace=True)
        print(df_work.head())

        # Definir tipos de variaveis
        df_work["distancia"] = df_work.loc[:,"distancia"].astype(float)
        df_work["companhia"] = df_work.loc[:,"companhia"].astype(str)
        df_work["id_voo"] = df_work.loc[:,"id_voo"].astype(str)
        df_work["atraso_chegada"] = df_work.loc[:,"atraso_chegada"].astype(str)
        df_work["origem"] = df_work.loc[:,"origem"].astype(str)
        df_work["destino"] = df_work.loc[:,"destino"].astype(str)

        # Tratamento das strings
        df_work["companhia"] = df_work.loc[:,"companhia"].apply(lambda x: padroniza_str(x))
        df_work["id_voo"] = df_work.loc[:,"id_voo"].apply(lambda x: padroniza_str(x))
        df_work["origem"] = df_work.loc[:,"origem"].apply(lambda x: padroniza_str(x))
        df_work["destino"] = df_work.loc[:,"destino"].apply(lambda x: padroniza_str(x))

        print(df_work.head())

        return df_work