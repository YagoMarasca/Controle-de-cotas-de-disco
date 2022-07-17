class Usuarios:
    __contador = 0;
    __espacoOcupado = 0;
    __media = 0;

    def __init__(self, usuario, tamanho):
        self._usuario = usuario;
        self._tamanho = tamanho / (1024**2);
        self.espaco_total(self._tamanho)
       

    def __str__(self):
        if len(self._usuario)> 6:
            return "{}\t {}\t {:0.2f} MB \t\t {}\n".format(Usuarios.Contador(), self._usuario, self._tamanho, self.porcentagem())
        else:
            return "{}\t {}\t\t {:0.2f} MB \t\t {}\n".format(Usuarios.Contador(), self._usuario, self._tamanho, self.porcentagem())
    
    @classmethod
    def espaco_total(cls, tamanho):
        cls.__espacoOcupado += tamanho;
        return cls.__espacoOcupado
    
    def porcentagem(self):
        porcentagem = self._tamanho /  self.__espacoOcupado * 100
        return "{:.2f}%".format(porcentagem)

    @classmethod
    def Contador(cls):
        cls.__contador += 1;
        return cls.__contador;

    @classmethod
    def espaco_medio(cls):
        cls.__media = cls.__espacoOcupado / cls.__contador;
        return cls.__media

    @property
    def espaco_Ocupado(self):
        return "{:.2f}".format(__class__.__espacoOcupado)

    
    