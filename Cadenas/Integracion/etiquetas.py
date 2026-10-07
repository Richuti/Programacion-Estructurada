entrada = input("Ingrese las etiquetas separadas por comas: ")
etiquetas = []
for etiqueta in entrada.split(","):
    etiqueta_limpia = etiqueta.strip().lower()
    if etiqueta_limpia != "":
        etiquetas.append(etiqueta_limpia)
etiquetas_unicas = set(etiquetas)
etiquetas_ordenadas = sorted(etiquetas_unicas)
resumen = " | ".join(etiquetas_ordenadas)
print(etiquetas)
print(etiquetas_ordenadas)
print(resumen)
