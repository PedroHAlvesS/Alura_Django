def campo_eh_vazio(campo: str):
    """
    Função para verificar se campo é vazio
    :param campo: o campo, sendo do tipo string
    :return: retorna o campo e faz uso do if do python (caso seja vazio, o if vai da False)
    """
    return not campo.strip()


def senhas_sao_diferentes(senha1: str, senha2: str):
    """
    
    :param senha1:
    :param senha2:
    :return:
    """
    return senha1 != senha2