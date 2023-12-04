import time

alarm = []
format = 0

def set_alarm(alarm_time):
    global alarm
    global format
    alarm=list(alarm_time)

def format_heure():
    global format
    format = int(input("Choisissez un format d'affichage 12 ou 24 :"))

def afficher_heure(hours):
    hours=list(hours)
    global alarm
    global format
    while True:

        hours[2] += 1

        if  hours[0] > 23:
            hours[0]=0

        if  hours[1] > 59:
            hours[1]=0
            hours[0]+=1

        if  hours[2] > 59:
            hours[2]=0
            hours[1]+=1

        time.sleep(1)

        if hours[0] == alarm[0] and hours[1] == alarm[1] and hours[2] == alarm[2]:
            print(hours[0],":",hours[1],":",hours[2], "L'alarme sonne")

        if int(hours[0]) < 12 :
             print(f"{hours[0]%format:02d}:{hours[1]:02d}:{hours[2]:02d} AM", end="\r")
        
        else:
            print(f"{(hours[0]%format):02d}:{hours[1]:02d}:{hours[2]:02d} PM,", end="\r")

set_alarm ((16,30,25)) 
format_heure()
afficher_heure((16, 30, 20))































