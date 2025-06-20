"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """

    import re
    import pandas as pd

    with open("files/input/clusters_report.txt", "r") as f:
        content = f.readlines()

    init = 0
    for idx, linea in enumerate(content):
        if "----------" in linea:
            init = idx + 1
            break

    cl, cant, porc, keys = [], [], [], []

    i = init
    
    while i < len(content):
        
        if content[i].strip():
        
            m = re.match(r"\s*(\d+)\s+(\d+)\s+([\d,\.]+)\s*%\s*(.*)", content[i].strip())
        
            if m:
                a, b, c, txt = m.groups()
               
                cl.append(int(a))
               
                cant.append(int(b))
               
                porc.append(float(c.replace(",", ".")))
               
                des = txt.strip()
               
                j = i + 1
               
                while j < len(content) and not re.match(r"\s*\d+\s+\d+", content[j]) and content[j].strip():
                    des += " " + content[j].strip()
                    j += 1
               
                des = re.sub(r"\s+", " ", des)
               
                des = re.sub(r"\s*,\s*", ", ", des)
               
                if des.endswith("."):
                    des = des[:-1]
               
                keys.append(des)
               
                i = j
           
            else:
                i += 1
        
        else:
            i += 1

    return pd.DataFrame({
        "cluster": cl,
        "cantidad_de_palabras_clave": cant,
        "porcentaje_de_palabras_clave": porc,
        "principales_palabras_clave": keys
    })