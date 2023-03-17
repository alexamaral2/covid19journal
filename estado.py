from noticia import Noticia

class Estado:
    def __init__(self,idEstado,nome,sigla,noticia,imgEstado):
        self.__idEstado = idEstado
        self.__nome = nome
        self.__sigla = sigla
        self.__noticia = noticia
        self.__imgEstado = imgEstado
      
    def get_idEstado(self):
        return self.__idEstado 
    def get_nome(self):
        return self.__nome
    def get_noticia(self):
        return self.__noticia
    def get_sigla(self):
        return self.__sigla
    def get_imgEstado(self):
        return self.__imgEstado
  

#Testando se a Classe irá retornar as Noticias por "Estado" usando um id de Teste. 
#Ex.: Se o indice do Estado RJ for id: 2, logo o if deverá retornar somente as noticias desse estado

#test_id = 2
#for estados in lista_estados:
#        for noticiaEstado in estados.get_noticia():
#           if noticiaEstado.get_id() == test_id:    
#               print(noticiaEstado.get_titulo())
#               print(estados.get_nome())