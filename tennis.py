class Tennis:
    cont1 = 0
    cont2 = 0
    puntos1 = ""
    puntos2 = ""
    
    def imprimir_puntuaje(self):
        if(self.cont1 > 3 or self.cont2 > 3):
            if(self.cont1 - self.cont2 == 0):
                self.puntos1 = "deuce"
                self.puntos2 = "deuce"
                    
            elif(self.cont1 - self.cont2 == -1):
                self.puntos1 = ""
                self.puntos2 = "Advantage"
                    
            elif(self.cont1 - self.cont2 == 1):
                self.puntos1 = "Advantage"
                self.puntos2 = ""
                    
            elif(self.cont1 - self.cont2 < -1):
                self.puntos1 = ""
                self.puntos2 = "GANO"
                    
            elif(self.cont1 - self.cont2 > 1):
               self.puntos1 = "GANO"
               self.puntos2 = ""
                
        else:
            
            if(self.cont1 == 0):
                self.puntos1 = "0"
                
            elif(self.cont1 == 1):
                self.puntos1 = "15"
                    
            elif(self.cont1 == 2):
                self.puntos1 = "30"
                   
            elif(self.cont1 == 3):
                self.puntos1 = "40"
                    
                
            if(self.cont2 == 0):
                self.puntos2 = "0"
                
            elif(self.cont2 == 1):
                self.puntos2 = "15"
                    
            elif(self.cont2 == 2):
                self.puntos2 = "30"
                   
            elif(self.cont2 == 3):
                self.puntos2 = "40"
                
        print("\nPUNTOS:\n\tJugador1\tJugador2\n\t%s\t\t%s" %(self.puntos1, self.puntos2))
            

    def main(self):
        

        salir = 0
        entrada = ''
        
        while(salir == 0):
            self.imprimir_puntuaje()
	            
		
            if(self.puntos1 == "GANO" or self.puntos2 == "GANO"):
                salir = 1
            
            else:
                print("\nEscriba el numero del jugador que anoto [1 o 2] o escriba \"salir\".")
                entrada = input()
                if(entrada == 'salir'):
                    salir = 1
                
                elif(entrada is '1'):
                    self.cont1 += 1
                    
                elif(entrada is '2'):
                    self.cont2 += 1
                    
                else:
                    print("!ENTRADA NO VALIDA!")
                    

if __name__ == '__main__':
	
	tennis1 = Tennis()
	tennis1.main()
