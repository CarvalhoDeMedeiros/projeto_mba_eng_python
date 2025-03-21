from src.manipulacao_dados.pipeline_sqlite import SalvarBancoSQLite
from src.manipulacao_dados.clean_data import CleanData
from src.manipulacao_dados.transforme_data import TransformData

class Main:
    def orquestrador(self):
        ''' funcao responsavel por executar o fluxo do projeto
            Args:
                None
            Returns:
                None
        '''

        df_limpo = CleanData().exeute()

        df_tranformado = TransformData().execute(df_limpo)

        # Salvar no banco de dados
        SalvarBancoSQLite().salvar_no_banco(df_tranformado)

if __name__ == "__main__":
    Main().orquestrador()