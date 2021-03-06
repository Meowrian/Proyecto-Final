# -*- coding: utf-8 -*-
"""DM combat helper.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nq6kiZjygxXfvZa0v3NS52okKqtuUg95
"""

import random
from operator import itemgetter

print('La idea del programa es hacer el cálculo de daño y rolls para los combates de manera más fácil')
print('Los únicos stats que se llevan es de los enemigos, este programa es para uso del dm, cada jugador llevará la cuenta de sus hitpoints y ataques')
print('El programa está inspirado a que empecé a jugar D&D hace poco más de un mes y soy DM, nadie en el grupo (me incluyo) tenía mucha experiencia previa')
print('Los enemigos que se pueden crear se limitan a los que he manejado hasta ahora, relativamente simples, con ataques melee o ranged')
print('Si quien usa el programa no tiene experiencia con crear enemigos, o no está familiarizado con todos los stats, igualmente podrá rear encuentros con personajes precreados')
print('Sin embargo para poder usar el programa se debe tener conocimientos básicos sobre D&D, lo cual se supone cierto ya que este programa lo usaría el dungeon master')
print(' ')

nplayers=int(input('Ingrese la cantidad de jugadores: '))
if nplayers<=0:
  print('Debe haber al menos un jugador en la party')
else:
  #se hace una lista con cantidad de items igual a cantidad de jugadores y se va agregando el nombre de cada jugador
  players=[]
  print('\nEscoja el nombre de cada personaje:')
  for i in range(1, nplayers+1):
    print('Jugador', i, ':'), 
    p_name=input()
    players.append(p_name)

  #Se añaden los modificadores de cada jugador para sus hojas de personajes
  players_AC=[]
  print('\nAsigne la armor class de cada personaje:')
  for player in players:
    print('AC de', player, ':')
    p_ac=int(input())
    players_AC.append([player, p_ac])

#Función para calcular daño, por ejemplo Hit:1d6+2
def onhit(x, d, bonus):
  hit=0
  for i in range(1, x):
    roll=random.randint(1,d)
    hit=hit+roll
  hit=hit+bonus
  return hit

#Función para crear enemigos
Goblin=['Goblin', 15, 7, 30, [8, -1], [14, 2], [10, 0], [10, 0], [8, -1], [8, -1], 9, 'Skills: Stealth +6. Senses: Darkvision 60ft. Languages: Common, Goblin', 50, 'Nimble Escape: The goblin can take the Disengage or Hide action as a bonus action on each of its turns', [['Scimitar', 1, 'melee', 4, 5, 1, 6, 2], ['Shortbow', 1, 'ranged', 4, 80, 320, 1, 6, 2]]]
Bugbear=['Bugbear', 16, 27, 30, [15, 2], [14, 2], [13, 1], [8, -1], [11, 0], [9, -1], 10, 'Skills: Stealth +6, Survival +2. Senses: Darkvision 60ft. Languages: Common, Goblin', 200, 'Brute: When a bugbear hits with a melee weapon attack, the attack deals one extre die of the weapon"s damage to the target. Surprise Attack: If the bugbear surprises a creature and hits it with an attack during the first roung of combat, the target takes an extra 7 (2d6) damage from the attack', [['Morningstar', 1, 'melee', 4, 5, 2, 8, 2], ['Javelin', 1, 'both', 4, 5, 30, 120, 2, 6, 2, 1, 6, 2]]]
enemydata=[Goblin, Bugbear]
enemynames=['Goblin', 'Bugbear']

def create_enemy():
  print('Los modifiers se deben agregar como "-1" o "2". "+2" no será valido')
  name=input('Nombre del enemigo: ')
  ac=int(input('AC: '))
  hitpoints=int(input('Hit points: '))
  speed=int(input('Speed (ft): '))
  stre=[]
  stre1=int(input('Strength: '))
  stre2=int(input('Strength modifier: '))
  stre.extend((stre1, stre2))
  dex=[]
  dex1=int(input('Dexterity: '))
  dex2=int(input('Dexterity modifier: '))
  dex.extend((dex1, dex2))
  con=[]
  con1=int(input('Constitution: '))
  con2=int(input('Constitution modifier: '))
  con.extend((con1, con2))
  inte=[]
  inte1=int(input('Ingelligence: '))
  inte2=int(input('Ingelligence modifier: '))
  inte.extend((inte1, inte2))
  wis=[]
  wis1=int(input('Wisdom: '))
  wis2=int(input('Wisdom modifier: '))
  wis.extend((wis1, wis2))
  cha=[]
  cha1=int(input('Charisma: '))
  cha2=int(input('Charisma modifier: '))
  cha. extend((cha1, cha2))
  passivep=input('Passive Perception: ')
  extrainfo=input('Extra info (skills, senses, languages, resistances, immunities...): ')
  challenge=int(input('Challenge (xp): '))
  special=input('Habilidades especiales: ')
  actions=int(input('Cantidad de Acciones: '))
  act=[]
  for i in range(1, actions+1):
   namea=input('Nombre de la acción: ')
   targets=int(input('Cantidad de objetivos (número): '))
   tipea=input('Tipo de acción (melee, ranged, both y other. Multiattack no entra en esta categoría):')
   tipea=tipea.lower()
   bonushit=int(input('Modificador al hit: '))
   if tipea=='melee':
     reach=int(input('Alcance (ft): '))
     x=int(input('Cantidad de dados: '))
     d=int(input('Dado (4, 6, 8, 10, 12, 20): '))
     bonusatt=int(input('Modificador: '))
     act.append([namea, targets, tipea, bonushit, reach, x, d, bonusatt])
   elif tipea=='ranged':
     reach_min=int(input('Mínimo Alcance (ft): '))
     reach_max=int(input('Máximo Alcance (ft): '))
     x=int(input('Cantidad de dados: '))
     d=int(input('Dado (4, 6, 8, 10, 12, 20): '))
     bonusatt=int(input('Modificador: '))
     act.append([namea, targets, tipea, bonushit, reach_min, reach_max, x, d, bonusatt])
   elif tipea=='both':
     reach=int(input('Alcance melee (ft): '))
     reach_min=int(input('Mínimo Alcance (ft): '))
     reach_max=int(input('Máximo Alcance (ft): '))
     x1=int(input('Cantidad de dados (melee): '))
     d1=int(input('Dado (4, 6, 8, 10, 12, 20) (melee): '))
     bonusatt1=int(input('Modificador (melee): '))
     x2=int(input('Cantidad de dados (ranged): '))
     d2=int(input('Dado (4, 6, 8, 10, 12, 20) (ranged): '))
     bonusatt2=int(input('Modificador (ranged): '))
     act.append([namea, targets, tipea, bonushit, reach, reach_min, reach_max, x1, d1, bonusatt1, x2, d2, bonusatt2])
  new=[]
  new.extend((name, ac, hitpoints, speed, stre, dex, con , inte, wis, cha, passivep, extrainfo, challenge, special, act))
  enemynames.append(name)
  enemydata.append(new)

def addnew(crear):
  while crear=='yes':
    create_enemy()
    print('\nLos enemigos existentes son:')
    for i in enemynames:
      print(i)
    crear=input('\n¿Crear otro nuevo enemigo? yes/no: ')

def attack(chosenaction):
  print('¿A quién vamos a atacar? (escoger número)')
  playernum=1
  for player in players:
    print(playernum, '-', player)
    playernum=playernum+1
  targetint=int(input())
  for player in players:
    if players.index(player)==(targetint-1):
      target=player
  for acs in players_AC:
    if acs[0]==player:
      targetAC=acs[1]               ####################
  if chosenaction[2]=='melee':
    rollhit=random.randint(1,20)+chosenaction[3]
    if rollhit>=targetAC:
      print('\nEl ataque pega')
      hit=True
    else:
      print('\nEl ataque no pega')
      hit=False
    if hit==True:
      sumrolls=0
      for rolls in (0, chosenaction[-3]):
        rollatt=random.randint(1, chosenaction[-2])
        sumrolls=sumrolls+rollatt
      totalatt=sumrolls+chosenaction[-1]
    print('El daño inflingido es', totalatt)
  elif chosenaction[2]=='ranged':
    distance=int(input('\nDistancia al objetivo (ft): '))
    if distance < chosenaction[4] or distance > chosenaction[5]:
      print('Tendrás desventaja en este ataque')
      roll1=random.randint(1,20)
      roll2=random.randint(1,20)
      rollhit=min([roll1, roll2])+chosenaction[3]
      if rollhit>=targetAC:
        print('\nEl ataque pega')
      hit=True
    else:
      print('\nEl ataque no pega')
      hit=False
    if hit==True:
      sumrolls=0
      for rolls in (0, chosenaction[-3]):
        rollatt=random.randint(1, chosenaction[-2])
        sumrolls=sumrolls+rollatt
      totalatk=sumrolls+chosenaction[-1]
    print('El daño inflingido es', totalatk)
  elif chosenaction[2]=='both':
    print('\nEl ataque puede ser melee o ranged. Recuerda que melee alcanza', chosenaction[4], 'ft, y ranged alcanza de', chosenaction[5], 'hasta', chosenaction[6], 'ft')
    subtype=input('¿Será melee o ranged?: ')
    if subtype=='melee':
      rollhit=random.randint(1,20)+chosenaction[3]
      if rollhit>=targetAC:
        print('\nEl ataque pega')
        hit=True
      else:
        print('\nEl ataque no pega')
        hit=False
      if hit==True:
        sumrolls=0
        for rolls in (0, chosenaction[-3]):
          rollatt=random.randint(1, chosenaction[-2])
          sumrolls=sumrolls+rollatt
        totalatt=sumrolls+chosenaction[-1]
      print('El daño inflingido es', totalatt)

def turns(order, orderdm, gogogo):
  while gogogo==True:
    for i in range(0, len(order)): #Uno por uno imprimo a quién le toca el turno
      print('\nTurno de', order[i][0])
      if orderdm[i][0] in enemynames:  #si el turno le toca a un enemigo
        if orderdm[i][2]<=0:
          print(order[i][0], 'está muerto')
        else:
          for item in enemydata: 
            if item[0]==orderdm[i][0]:  #para encontrar el enemigo en enemydata
              print('\nAtaques disponibles:')
              count=1
              for a in item[-1]:  #item[-1] indica la lista de acciones del enemigo, luego imprimo tipo 1 - Scimitar y en la línea de abajo "Scimitar ataca a 1 objetivos a melee. Alcanza hasta 5 pies."
                print(count, '-', a[0])
                if a[2]=='melee':
                  print(a[0], 'ataca a', a[1], 'objetivos a melee. Alcanza hasta', a[4], 'pies.')
                elif a[2]=='ranged':
                  print(a[0], 'ataca a', a[1], 'objetivos a rango. Alcanza desde', a[4], 'hasta', a[5], 'pies.')
                elif a[2]=='both':
                  print(a[0], 'ataca a', a[1], 'objetivos a melee (hasta', a[4], 'pies) o a rango (de', a[5], 'hasta', a[6], 'pies).')
                count=count+1
              wantattack=input('\n¿Atacas este turno? yes/no: ')
              if wantattack=='yes':
                atk=int(input('Número del ataque a usar: '))
                chosenattack=atk-1
                #chosenaction=item[-1][chosenattack]
                attack(item[-1][chosenattack])
      else:
        wantattack=input('\n¿Ataca este turno? yes/no: ')
        if wantattack=='yes':
          wanttarget=input('Objetivo (como aparece en el orden, ej Goblin 3): ') #[[meow, 26], [jeipi, 17], .....]
          for cooldude in order:
            if cooldude[0]==wanttarget:
              enemyplace=order.index(cooldude)
          for boi in orderdm: #reviso las posiciones de todos en orderdm para luego tener el nombre Goblin en vez de Goblin 3
            if orderdm.index(boi)==enemyplace:  #encuentro la posición
              for badboi in enemydata: #para cada enemigo en enemy data...
                if badboi[0]==boi[0]:  #si el nombre del enemigo es el mismo nombre en orderdm
                  targetboi=enemydata[enemydata.index(badboi)]  #targetboi manda al enemigo en enemydata
                  dmgdealt=int(input('Daño inflingido: '))
                  boi[2]=boi[2]-dmgdealt
    whatnow=input('¿Iniciar nueva ronda? yes/no: ')  
    if whatnow=='yes':
      gogogo=True
    elif whatnow=='no':
      print('Final del encuentro')
      gogogo=False

def encounter(add):
  order=[]
  orderdm=[]
  for player in players:
    print('\nIniciativa de', player)
    roll=int(input())
    order.append([player, roll])
    orderdm.append([player, roll])
  print('\nAñade los enemigos')
  print('\nLos enemigos existentes son:')
  for i in enemynames:
    print(i)
  print(' ')
  while add == True:
    type_e=input('Tipo de enemigo: ')
    if type_e in enemynames:
      num_e=int(input('Cantidad:'))
      indice=1
      for i in range(1, num_e+1):
        for baddude in enemydata:
          if baddude[0]==type_e:
            i_mod=baddude[5][1]
            roll=random.randint(1,20)+i_mod
            dude = ' '.join([str(elem) for elem in [type_e, i]]) 
            order.append([dude, roll])
            orderdm.append([type_e, roll, baddude[2]])
        indice=indice+1
      addyn=input('\n¿Añadir otro tipo de enemigo? yes/no: ')
      if addyn=='yes':
        add=True
      elif addyn=='no':
        add=False
    else:
      print('El enemigo no se encuentra registrado')
      crear=input('¿Crear un nuevo enemigo? yes/no: ')
      addnew(crear)
      print('\nAñade los enemigos')
      print('\nLos enemigos existentes son:')
      for i in enemynames:
        print(i)
      print(' ')
      add=True
  order=list(reversed(sorted(order, key=itemgetter(1))))
  orderdm=list(reversed(sorted(orderdm, key=itemgetter(1))))
  print('\nEl orden para jugadores y enemigos será')
  for i in order:
    print(i[0])
  gogogo=True
  turns(order, orderdm, gogogo)

#[['Scimitar', 1, 'melee', 4, 5, 1, 6, 2], ['Shortbow', 1, 'ranged', 4, 80, 320, 1, 6, 2]]
#[namea, targets, tipea, bonushit, reach, x, d, bonusatt], [namea, targets, tipea, bonushit, reach_min, reach_max, x, d, bonusatt], [namea, targets, tipea, bonushit, reach, reach_min, reach_max, x1, d1, bonusatt1, x2, d2, bonusatt2]
#(name, ac, hitpoints, speed, stre, dex, con , inte, wis, cha, passivep, extrainfo, challenge, special, act)
  
print('\nEn este momento hay dos enemigos precreados (Goblin y Bugbear)\n')
 
crear=input('¿Crear un nuevo enemigo? yes/no: ')
if crear=='yes':
  addnew(crear)

start=True

while start==True:
  funkyvariable=input('\nEscriba start si quiere iniciar un encuentro: ')
  if funkyvariable=='start':
    print('\n*Inicio de encuentro*')
    print('Lanzen iniciativa!')
    add=True
    encounter(add)
  else:
    print('Hasta la próxima!')
    start=False