'''
Atributos:
Ano, modelo, marca, cor, potencia, combustível, portas, placa, odometro, ligado
funcoes:
- mostrar nivel tanque
- apresentar carro
- mostrar odometro
- andar
- ligar
'''


class Veiculo:
    def __init__(self, ano, modelo, marca, cor, potencia, volume_no_tanque, portas, placa):
        self.ano = ano
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.potencia = potencia
        self.volume_no_tanque = volume_no_tanque
        self.portas = portas
        self.placa = placa
        self.odometro = 0
        self.ligado = False

    def mostrar_nivel_tanque(self):
        print(self.volume_no_tanque)

    def mostrar_odometro(self):
        print(self.odometro)

    def apresentar_carro(self):
        print(f'''Marca / Modelo: {self.marca}/{self.modelo}
        Ano: {self.ano}
        Quilometragem: {self.odometro}''')

    def ligar(self):
        if self.volume_no_tanque > 0:
            self.ligado = True
        else:
            print('Carro não tem gasolina')

    def desligar(self):
        self.ligado = False

    def andar(self, distancia, consumo):
        if self.ligado:
            if self.volume_no_tanque >= distancia / consumo:
                print(f'Andou {distancia}km')
                self.odometro += distancia
                self.volume_no_tanque -= distancia/consumo
            else:
                print(f'Abasteça, pois você só pode rodar atualmente {self.volume_no_tanque / consumo}')
        else:
            print('Ligue o carro primeiro')

    def abastecer(self, quantidade):
         self.volume_no_tanque += quantidade


v1 = Veiculo(2012, 'Tucson 2.0', 'Hyundai', 'Prata', 150, 60, 4, 'AAA-1564')

