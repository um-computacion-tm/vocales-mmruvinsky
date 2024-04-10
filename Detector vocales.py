import unittest

def detector(palabra):
    contadores = {"a":0, "e":0, "i":0, "o":0, "u":0}
    for letra in palabra.lower():
        if letra == "a":
            contadores["a"] += 1
        elif letra == "e":
            contadores["e"] += 1
        elif letra == "i":
            contadores["i"] += 1
        elif letra == "o":
            contadores["o"] += 1
        elif letra == "u":
            contadores["u"] += 1
        else: print("No contiene vocales")
    return (contadores)


class TestVocales(unittest.TestCase):

    def test_caso_1(self):
        esperado = {'a': 5, 'e': 1, "i": 0, "o": 0,'u': 1,}
        resultado = detector("aca hay una frase")
        self.assertDictEqual(resultado, esperado)
        
    def test_caso_2(self):
        esperado = {"a": 1, "e" : 1, "i" : 1, "o" : 1, "u" : 1}  
        resultado = detector("reticulado")
        self.assertDictEqual(resultado, esperado)
        
    def test_caso_3(self):
        esperado = {"a": 3, "e" : 0, "i" : 1, "o" : 1, "u" : 0}
        resultado = detector("ANASTASIO")
        self.assertDictEqual(resultado, esperado)
        
    def test_caso_4(self):
        esperado = {"a": 1, "e" : 1, "i" : 1, "o" : 1, "u" : 1} 
        resultado = detector("HumANoidE")
        self.assertDictEqual(resultado, esperado)
        
    def test_caso_5(self):
        esperado = {"a": 2, "e" : 2, "i" : 1, "o" : 3, "u" : 1} 
        resultado = detector("funciona con frases creo")
        self.assertDictEqual(resultado, esperado)
        

if __name__ == '__main__':
    unittest.main()