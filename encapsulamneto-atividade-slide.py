# class maquiagem:
#     def __init__ (self,batom,sombra):
#         self.batom=batom
#         self.sombra=sombra
    
    # def get_batom(self):
    #     return self.batom
    # def get_sombra(self):
    #     return self.sombra

    # def set_batom(self,batom):
    #     self.batom=batom
    # def set_sombra(self,sombra):
    #     self.sombra=sombra

#     @property
#     def batom (self):
#         return self.__batom
#     @batom.setter
#     def batom (self,batom):
#         self.__batom=batom
    
#     @property
#     def sombra(self):
#         return self.__sombra
#     @sombra.setter
#     def sombra(self,sombra):
#         self.__sombra=sombra


# cor_batom= str(input('Qual a cor do batom?'))
# cor_sombra= str (input('Qual a cor da sombra?'))
# produção = maquiagem (cor_batom,cor_sombra)
# print(produção.batom)
# mudar_batom= str(input('Mude a cor do batom:'))
# produção.batom=mudar_batom
# print(produção.batom)


#sobrescrita

class Integrante_IFRN:
    def __init__(self,nome,idade):
        self.nome=nome
        self.idade=idade
    
    def exibirMensagem(self):
        print('Seja bem vindo(a) ao IFRN!!')

class professor(Integrante_IFRN):
    def __init__(self,nome,idade,disciplina):
        super().__init__(nome,idade)
        self.disciplina=disciplina

    def exibirMensagem (self):
        print('Meus alunos são os melhores!!')

class aluno(Integrante_IFRN):
    def __init__(self,nome,idade,turma):
        super().__init__(nome,idade)
        self.turma=turma
    
    def exibirMensagem (self):
        print('Vou estudar para tirar 100 em POO')



alunoo = aluno ('Clara',16,'INFO2M')
prof = professor ('Priscilla',20,'POO')


print(prof.nome)
prof.exibirMensagem()