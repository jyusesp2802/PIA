
salario_base = 1000


int(porcentaje) = input(f"Escribe el porcentaje para bajarle su salario base ")
if porcentaje <= 0.0 :
    salario_base = salario_base + salario_base * porcentaje
else:
    salario_base = (salario_base - salario_base * porcentaje) * - 1
