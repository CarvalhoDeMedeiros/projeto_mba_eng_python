from clean_data import CleanData
from transforme_data import TransformData

class Main:
    def orquestrador(self):
        ''' funcao responsavel por executar o fluxo do projeto
            Args:
                None
            Returns:
                None
        '''

        df_limpo = CleanData().exeute()

        # df_tranformado = TransformData().execute(df_limpo)

if __name__ == "__main__":
    Main().orquestrador()