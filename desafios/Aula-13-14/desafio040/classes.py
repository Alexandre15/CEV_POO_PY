import json


class Usuario:
    def __init__(self, nome, email) -> None:
        self.nome = nome
        self.email = email


class Aluno:
    def __init__(self, nome: str, curso: str, serie: str) -> None:
        self.nome = nome
        self.curso = curso
        self.serie =serie


class XML:
    def exportar(self, listaobj):
        import xml.etree.ElementTree as ET
        
        elemento = ET.Element("xml")

        for obj in listaobj:
            aluno = ET.SubElement(elemento, obj.__class__.__name__.lower())

            for att, valor in vars(obj).items():
                ET.SubElement(aluno, att).text = str(valor)

        ET.indent(elemento, space="\t")
        return ET.tostring(elemento, encoding="unicode", xml_declaration=True)


class JSON:
    def exportar(self, listaobj):
        return json.dumps(listaobj, default=vars, indent=4, ensure_ascii=False)


def exportar_dados(formato: XML | JSON, lista):
    print(formato.exportar(lista))