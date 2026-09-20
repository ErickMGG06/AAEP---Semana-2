Hlabora = float(input("Ingrese la horas laboradas:\n"))
HValor = float(input("Ingrese su sueldo por hora:\n"))
SBruto = Hlabora*HValor
descuento = 0.05 * SBruto
SNeto = SBruto -descuento
print(SBruto,descuento,SNeto)
