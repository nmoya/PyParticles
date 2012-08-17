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
RESOLUTION                  = (480, 320)    #Tamanho da tela
BACKGROUND_COLOR            = (0,0,0)       #Cor de fundo
TEXT_COLOR                  = (255,0,0)	    #Cor do texto desenhado

##################
#                #
#CTEs. VARIAVEIS #
#   NAO MEXER    #
##################
MOUSEX, MOUSEY 		    = 0,0  						#Posicao X e Y do Mouse.
EFFECT 			    = ""						#Nome do efeito sendo aplicado.
EFFECT_INDEX 		    = 0							#Indice para a funcao de movimentacao das particulas. 0 = default

			   
##################
#                #
#   PARTICULA    #
#                #
##################
CONSTANT_SPEED              = True 		#Para cada particula. True: Mesma velocidade. False: Velocidade Randomica.
CONSTANT_MASS               = False		#Para cada particula. True: Mesma massa. False: Massa randomica.
CONSTANT_COLOR 		    = False		#Para cada particula. True: Mesma cor. False: Cores de acordo com a massa
CONSTANT_ANGLE		    = False		#Para cada particula. True: Mesmo angulo de movimentacao (Ex. math.pi). False: Angulos randomicos.
CONSTANT_Y		    = False		#Particulas comecando na mesma linha.  [0, RESOLUTION[RES_Y]]
CONSTANT_X		    = False		#Particulas comecando na mesma coluna. [0, RESOLUTION[RES_X]]
PARTICLE_NUMBER             = 100		#Numero de particulas.
PARTICLE_SIZE               = 8			#Tamanho da particula.
PARTICLE_COLOR              = (0, 255, 0)	#Cor da particula.
PARTICLE_SPEED              = 2.4		#Velocidade da particula.
PARTICLE_MASS		    = 200		#Massa default para a particula
PARTICLE_ANGLE              = math.pi		#Angulacao de movimento.
PARTICLE_FILL               = False		#Particulas preenchidas. False = Sim. True = Nao.
PARTICLE_COLLISION	    = False		#Colisao entre particulas. (Baixo desempenho O(n2), Max 200)
##################
#                #
#   FISICA       #
#                #
##################
GRAVITY                     = (math.pi, 0.000) #Direcao(rad) e velocidade
AIR_MASS 		    = 0		       #Massa do ar. Constante para a resistencia do ar. 0 = OFF. 'Energia gasta para se movimentar.'
ELASTICITY                  = 0	               #Energia perdida ao colidir com laterais [0,1[. Leva em consideracao a Massa. (0.003 e interessante)
ENERGY_LOSS_COLLISION 	    = 1 	       #Energia perdida ao colidir com outras particulas. [0,1]
COLLISION_WITH_MASS	    = False	       #Se a colisao leva em consideracao a massa.
SIZE_PROPORTIONAL           = False            #Energia perdida ao se movimentar proporcional ao tamanho?
