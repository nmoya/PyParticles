import math

'''
##################
#                #
#   COMANDOS     #
#                #
##################
P			=> Pause
Q			=> Normal
G			=> Gravidade no clique do mouse
C			=> ON/OFF Colisao entre particulas

'''

##################
#                #
#   PYGAME       #
#                #
##################
RES_X                       = 0		    #Posicao de X na tupla da resolucao
RES_Y                       = 1	            #Posicao de Y na tupla da resolucao
RESOLUTION                  = (640, 480)    #Tamanho da tela
BACKGROUND_COLOR            = (0,0,0)       #Cor de fundo
TEXT_COLOR                  = (255,0,0)	    #Cor do texto desenhado

##################
#                #
#CTEs. VARIAVEIS #
#   NAO MEXER    #
##################
R 						= 0
G 						= 1
B 						= 2
MOUSEX, MOUSEY 		    = 600,400  					#Posicao X e Y do Mouse.
EFFECT 			    	= ""						#Nome do efeito sendo aplicado.
EFFECT_INDEX 		    = 0							#Indice para a funcao de movimentacao das particulas. 0 = default

##################
#                #
#   PARTICULA    #
#                #
##################
CONSTANT_COLOR 		    = False			#Para cada particula. True: Mesma cor. False: Cores de acordo com a massa. Apenas para Verde
PARTICLE_COLOR          = (0, 255, 0)	#Cor da particula.
PARTICLE_COLLISION	    = False			#Colisao entre particulas. (Baixo desempenho O(n2), Max 200)
PARTICLE_FILL           = False			#Particulas preenchidas. False = Sim. True = Nao.
##################
#                #
#   FISICA       #
#                #
##################
ENERGY_LOSS_COLLISION 	    = 1 			   #Energia perdida ao colidir com outras particulas. [0,1]
COLLISION_WITH_MASS	   		= False	       	   #Se a colisao leva em consideracao a massa.
SIZE_PROPORTIONAL           = False            #Energia perdida ao se movimentar proporcional ao tamanho?
