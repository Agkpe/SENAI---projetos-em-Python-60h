from colorama import Fore, Back, Style # Bibliotecas sempre são importadas em cima no código - biblioteca de cor para o terminal do código


# verificar a valor_hora
def verificar_valor_hora(carga, salario):
    return salario / carga


# verificar quantidade de horas extras
def quant_extra(valor_extra, valor_hora):
    return valor_extra * valor_hora


# calculo do valor da hora extra
def hora_extra_receber(quant_hora, hora_extra):
    return quant_hora * hora_extra


# somar com o salario
def salario_bruto(salario, hora_extra_receber):
    return salario + hora_extra_receber


# verificar os descontos  vt, vr
def desconto(salario_bruto, vt, vr):
    return salario_bruto - (vt+vr)


# liquido e o bruto
def salario_liquido(salario_recebeder):
    return salario_recebeder



def sistema_rh():
    while True:
        print(Back.RED +'CALCULE SALARIO:')
        salario = float(input("Salario R$: "))
        carga = 220
        print('Verifique o Salário a receber: ')
        valor_hora = verificar_valor_hora(carga, salario)
        print('Valor hora R$: ', round(valor_hora))
        print()
        extra_50 = quant_extra(1.5,  round(valor_hora))
        extra_100 = quant_extra(2,  round(valor_hora))
        print ('Extra 50%', round(extra_50))
        print ('Extra 100%', round( extra_100))
        print()
        quantidade_50 = float(input('Quantidade de extra realizada, 50%: '))
        quantidade_100 = float(input('Quantidade de extra realizada, 100%: '))


        hora_receber_50 = hora_extra_receber(quantidade_50, extra_50)
        hora_receber_100 = hora_extra_receber(quantidade_100, extra_100)
        print(f'''

                hora extra 50% - R$ {hora_receber_50}
                hora receber 100% - R$ {hora_receber_100}

              ''')
        print()
        hora_extra_total =hora_receber_50 + hora_receber_100
        salario_b = salario_bruto(salario, hora_extra_total)
        print('Salário bruto: R$:', salario_b)

        print()
        print('DESCONTOS: ')

        salari_liqu = desconto(salario_b, 250.0, 250.0)
        print(F'Salario a receber - r${salari_liqu:.2F}')


sistema_rh()

