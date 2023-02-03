import os

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)


MEMBERS = ['601','602','603','604','605','606','607','608','609','610','611','612','613','614','615','616','617','618','619','620','621','622','623','624','625','627','628','629','630','631','632','633','634','635','636','637','638','639','641','643','644','645','650','651','652','653']

for member in MEMBERS:

    dirFATH = './KNIH_Total_Data/' + member

    createFolder(dirFATH)
