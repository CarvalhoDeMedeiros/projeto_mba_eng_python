import pandas as pd

class TransformData:
    def __init__(self):
        super().__init__()

    def execute(self, df):
        """
        Função responsável por transformar os dados.
        
        Args:
            df (pd.DataFrame): DataFrame limpo.
        
        Returns:
            pd.DataFrame: DataFrame transformado.
        """
        df_transformed = df.copy()
        
        # Criar coluna de tempo de voo em minutos
        df_transformed["tempo_voo_minutos"] = df_transformed["tempo_voo"].apply(self.calc_horas)
        
        # Criar coluna de classificação de turno
        df_transformed["turno"] = df_transformed["data_hora"].apply(self.classifica_turno)

        # Mostrar Dataframe
        print(df_transformed.head())
        
        return df_transformed
    
    def calc_horas(self, coluna_tempo_voo):
        """
        Converte a coluna de tempo de voo de horas para minutos.
        
        Args:
            coluna_tempo_voo (float): Tempo de voo em horas.
        
        Returns:
            int: Tempo de voo em minutos.
        """
        return int(coluna_tempo_voo * 60) if not pd.isna(coluna_tempo_voo) else None
    
    def classifica_turno(self, coluna_data_hora):
        """
        Classifica o turno do voo com base no horário.
        
        Args:
            coluna_data_hora (pd.Timestamp): Data e hora do voo.
        
        Returns:
            str: Turno do voo.
        """
        if pd.isna(coluna_data_hora):
            return None
        
        hora = coluna_data_hora.hour
        if 6 <= hora < 12:
            return "MANHÃ"
        elif 12 <= hora < 18:
            return "TARDE"
        elif 18 <= hora < 24:
            return "NOITE"
        else:
            return "MADRUGADA"