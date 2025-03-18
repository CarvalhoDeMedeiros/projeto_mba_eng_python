import pandas as pd
import sqlite3
from sqlalchemy import create_engine, inspect
from src.tools.tools import create_db

class SalvarBancoSQLite:   
    def __init__(self):
        """
        Inicializa a classe SalvarBancoSQLite que é responsável por
        salvar os dados tratados no banco de dados SQLite.
        """
        super().__init__()

    def salvar_no_banco(self, df_tratada):
        """
        Função para salvar os dados já tratados no banco de dados SQLite.
        
        Args:
            df_tratada (pd.DataFrame): DataFrame contendo os dados tratados.
        """
        # Conexão com banco de dados SQLite
        db_path = "projeto_python.db"
        engine = create_engine(f"sqlite:///{db_path}")
        
        # Cria a tabela se não existir
        if not inspect(engine).has_table("flights"):
            create_db(engine)
        
        # Verifica se os dados já existem no banco
        with engine.connect() as connection:
            existing_columns = pd.read_sql("PRAGMA table_info(flights)", connection)["name"].tolist()
            if set(df_tratada.columns).issubset(set(existing_columns)):
                existing_data = pd.read_sql("SELECT * FROM flights", connection)
                df_tratada = df_tratada[~df_tratada.apply(tuple, 1).isin(existing_data.apply(tuple, 1))]
                
                if not df_tratada.empty:
                    df_tratada.to_sql(name='flights', con=connection, index=False, if_exists='append')
        
        # Exibir os primeiros registros inseridos
        with sqlite3.connect(db_path) as con:
            cur = con.cursor()
            cur.execute('SELECT * FROM flights LIMIT 10')
            result = cur.fetchall()
            print("Primeiros registros inseridos no banco de dados:")
            for row in result:
                print(row)
