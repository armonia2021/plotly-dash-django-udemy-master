# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 11:21:43 2021

@author: Cattolica
"""


def calcola_nutrienti(prova,pasto):
    acqua = []
    acqua_riv = []
    calorie_riv = []
    calorie = []
    proteine = []
    proteine_riv = []
    grassi=[]
    grassi_riv = []
    carboidrati = []
    carboidrati_riv = []
    fibre = []
    fibre_riv=[]
    ferro = []
    ferro_riv = []
    sodio = []
    sodio_riv = []
    zuccheri = []
    zuccheri_riv = []
    colesterolo = []
    colesterolo_riv = []
    calcio = []
    calcio_riv = []
    potassio = []
    potassio_riv = []
    zinco = []
    zinco_riv = []
    k = []
    k_riv = []
    folico = []
    folico_riv = []
    d = []
    d_riv = []
    saturi = []
    saturi_riv = []
    ind = []
    count = 0
    quantita = []
    nome = []
    if(pasto in prova.keys()):
        #print('Calcolo i nutrienti in',pasto.lower())
        for indice in prova[pasto].keys():
            
            if('Ingredienti' in prova[pasto][indice].keys()):
                #print('Sto vedendo una ricetta')
                print(prova[pasto][indice]['Nome'])
                nome.append(prova[pasto][indice]['Nome'])
                if('Quantita' in prova[pasto][indice].keys()):
                    risultato = calcola_nutrienti_ricetta_calorie(prova[pasto][indice]['Ingredienti'],prova[pasto][indice]['Quantita'])
                    acqua.append(risultato[0])
                    calorie.append(risultato[1])
                    proteine.append(risultato[2])
                    grassi.append(risultato[3])
                    carboidrati.append(risultato[4])
                    fibre.append(risultato[5])
                    ferro.append(risultato[6])
                    sodio.append(risultato[7])
                    zuccheri.append(risultato[8])
                    colesterolo.append(risultato[9])
                    potassio.append(risultato[10])
                    calcio.append(risultato[11])
                    zinco.append(risultato[12])
                    k.append(risultato[13])
                    folico.append(risultato[14])
                    d.append(risultato[15])
                    saturi.append(risultato[16])
                    
                    acqua_riv.append(risultato[0])
                    calorie_riv.append(risultato[1])
                    proteine_riv.append(risultato[2])
                    grassi_riv.append(risultato[3])
                    carboidrati_riv.append(risultato[4])
                    fibre_riv.append(risultato[5])
                    ferro_riv.append(risultato[6])
                    sodio_riv.append(risultato[7])
                    zuccheri_riv.append(risultato[8])
                    colesterolo_riv.append(risultato[9])
                    potassio_riv.append(risultato[10])
                    calcio_riv.append(risultato[11])
                    zinco_riv.append(risultato[12])
                    k_riv.append(risultato[13])
                    folico_riv.append(risultato[14])
                    d_riv.append(risultato[15])
                    saturi_riv.append(risultato[16])
                    ind.append(count)
                    count = count + 1
                    quantita.append(0)
                    print('Count', count)
                else:
                    risultato = calcola_nutrienti_ricetta(prova[pasto][indice]['Ingredienti'])
                    acqua.append(risultato[0])
                    calorie.append(risultato[1])
                    proteine.append(risultato[2])
                    grassi.append(risultato[3])
                    carboidrati.append(risultato[4])
                    fibre.append(risultato[5])
                    ferro.append(risultato[6])
                    sodio.append(risultato[7])
                    zuccheri.append(risultato[8])
                    colesterolo.append(risultato[9])
                    potassio.append(risultato[10])
                    calcio.append(risultato[11])
                    zinco.append(risultato[12])
                    k.append(risultato[13])
                    folico.append(risultato[14])
                    d.append(risultato[15])
                    saturi.append(risultato[16])
                    
                    acqua_riv.append(risultato[0])
                    calorie_riv.append(risultato[1])
                    proteine_riv.append(risultato[2])
                    grassi_riv.append(risultato[3])
                    carboidrati_riv.append(risultato[4])
                    fibre_riv.append(risultato[5])
                    ferro_riv.append(risultato[6])
                    sodio_riv.append(risultato[7])
                    zuccheri_riv.append(risultato[8])
                    colesterolo_riv.append(risultato[9])
                    potassio_riv.append(risultato[10])
                    calcio_riv.append(risultato[11])
                    zinco_riv.append(risultato[12])
                    k_riv.append(risultato[13])
                    folico_riv.append(risultato[14])
                    d_riv.append(risultato[15])
                    saturi_riv.append(risultato[16])
                    ind.append(count)
                    count = count + 1
                    quantita.append(0)
                    print('Count', count)
            else:       
                if('Nutrienti principali' in prova[pasto][indice].keys()):
                    nome.append(prova[pasto][indice]['Nome'])
                    #print('Entro in dietabit')
                    acq = False
                    cal = False
                    pro = False
                    gra = False
                    car = False
                    fib = False
                    fer = False
                    sod = False
                    zuc = False
                    col = False
                    calc = False
                    pot = False
                    zin = False
                    kvi = False
                    fol = False
                    dvi = False
                    sat = False
                    for nutri in prova[pasto][indice]['Nutrienti principali'].keys():
                        if('Acqua' in nutri):
                            acqua.append(prova[pasto][indice]['Nutrienti principali'][nutri])
                            acq = True
                        if('Calorie' in nutri):
                            calorie.append(prova[pasto][indice]['Nutrienti principali'][nutri])
                            cal = True
                        if('Proteine' in nutri):
                            proteine.append(prova[pasto][indice]['Nutrienti principali'][nutri])
                            pro = True
                        if('Grassi' in nutri):
                            #print(prova[pasto][indice]['Nutrienti principali'][nutri])
                            grassi.append(prova[pasto][indice]['Nutrienti principali'][nutri])
                            #print(type(grassi[count]))
                            gra = True
                        if('Carboidrati' in nutri):
                            carboidrati.append(prova[pasto][indice]['Nutrienti principali'][nutri])
                            car = True
                        if('Fibre' in nutri):
                            fibre.append(prova[pasto][indice]['Nutrienti principali'][nutri])
                            fib = True
                    if(prova[pasto][indice]['Minerali']!='ND'):
                        for minerali in prova[pasto][indice]['Minerali'].keys():
                            if('Ferro' in minerali):
                                ferro.append(prova[pasto][indice]['Minerali'][minerali])
                                fer = True
                            if('Sodio' in minerali):
                                sodio.append(prova[pasto][indice]['Minerali'][minerali])
                                sod = True
                                print('Sodio',sodio)
                            if('Calcio' in minerali):
                                calcio.append(prova[pasto][indice]['Minerali'][minerali])
                                calc = True
                            if('Potassio' in minerali):
                                potassio.append(prova[pasto][indice]['Minerali'][minerali])
                                pot = True
                            if('Zinco' in minerali):
                                zinco.append(prova[pasto][indice]['Minerali'][minerali])
                                zin = True
                    if(prova[pasto][indice]['Carboidrati']!='ND'):
                        for carbo in prova[pasto][indice]['Carboidrati'].keys():
                            if('Zuccheri' in carbo):
                                zuccheri.append(prova[pasto][indice]['Carboidrati'][carbo])
                                zuc = True
                    if(prova[pasto][indice]['Lipidi']!='ND'):
                        for grass in prova[pasto][indice]['Lipidi'].keys():
                            #print(grassi)
                            
                            if('Colesterolo' in grass):
                                #print(type(prova[pasto][indice]['Lipidi'][grass]))
                                colesterolo.append(prova[pasto][indice]['Lipidi'][grass])
                                #print(colesterolo[count])
                                col = True
                            if('Grassi saturi' in grass):
                                #print(type(prova[pasto][indice]['Lipidi'][grass]))
                                saturi.append(prova[pasto][indice]['Lipidi'][grass])
                                #print(saturi[count])
                                sat = True
                    if(prova[pasto][indice]['Vitamine']!='ND'):
                        for vit in prova[pasto][indice]['Vitamine'].keys():
                            #print(grassi)
                            
                            if('Vitamina K' in vit):
                                #print(type(prova[pasto][indice]['Vitamine'][vit]))
                                k.append(prova[pasto][indice]['Vitamine'][vit]/1000)
                                #print(k[count])
                                kvi = True
                            if('Acido folico' in vit):
                                #print(type(prova[pasto][indice]['Vitamine'][vit]))
                                #print((prova[pasto][indice]['Vitamine'][vit]))
                                if(prova[pasto][indice]['Vitamine'][vit]=='tr'):
                                    folico.append(0.01)
                                else:
                                    folico.append(prova[pasto][indice]['Vitamine'][vit]/1000)
                                #print(folico[count])
                                fol = True
                            if('Vitamina D (' in vit and dvi==False):
                                #print(type(prova[pasto][indice]['Vitamine'][vit]))
                                d.append(prova[pasto][indice]['Vitamine'][vit]/1000)
                                #print(folico[count])
                                dvi = True
                elif('Nutrienti' in prova[pasto][indice].keys() and 'Descrizione' in prova[pasto][indice].keys()):
                    #print('Entro in crea')
                    nome.append(prova[pasto][indice]['Nome'])
                    acq = False
                    cal = False
                    pro = False
                    gra = False
                    car = False
                    fib = False
                    fer = False
                    sod = False
                    zuc = False
                    col = False
                    calc = False
                    pot = False
                    zin = False
                    kvi = False
                    fol = False
                    dvi = False
                    sat = False
                    #print(fib)
                    for nutri in prova[pasto][indice]['Nutrienti'].keys():
                        if('Acqua' in nutri):
                            acqua.append(prova[pasto][indice]['Nutrienti'][nutri])
                            acq = True
                        if('Energia (kcal)' in nutri):
                            calorie.append(prova[pasto][indice]['Nutrienti'][nutri])
                            cal = True
                        if('Proteine' in nutri):
                            proteine.append(prova[pasto][indice]['Nutrienti'][nutri])
                            pro = True
                        if('Lipidi' in nutri):
                            #print(prova[pasto][indice]['Nutrienti'][nutri])
                            grassi.append(prova[pasto][indice]['Nutrienti'][nutri])
                            gra = True
                        if('Carboidrati' in nutri):
                            if(prova[pasto][indice]['Nutrienti'][nutri] == 'tr'):
                                carboidrati.append(0.01)
                            else:
                                carboidrati.append(prova[pasto][indice]['Nutrienti'][nutri])
                            car = True
                        if('Fibra' in nutri):
                            fibre.append(prova[pasto][indice]['Nutrienti'][nutri])
                            fib = True
                            #print(fib,nutri)
                        if('Zuccheri' in nutri):
                            if(prova[pasto][indice]['Nutrienti'][nutri] == 'tr'):
                                zuccheri.append(0.01)
                            else:
                                zuccheri.append(prova[pasto][indice]['Nutrienti'][nutri])
                            zuc = True
                            #print(zuc,nutri)
                        if('Colesterolo' in nutri):
                            if(prova[pasto][indice]['Nutrienti'][nutri] == 'tr'):
                                colesterolo.append(0.01)
                            else:
                                colesterolo.append(prova[pasto][indice]['Nutrienti'][nutri])
                            col = True
                            #print(col,nutri)
                    if(prova[pasto][indice]['Minerali']!='ND'):
                        for minerali in prova[pasto][indice]['Minerali'].keys():
                            if('Ferro' in minerali):
                                ferro.append(prova[pasto][indice]['Minerali'][minerali])
                                fer = True
                            if('Sodio' in minerali):
                                sodio.append(prova[pasto][indice]['Minerali'][minerali])
                                sod = True
                                print(sodio)
                            if('Calcio' in minerali):
                                calcio.append(prova[pasto][indice]['Minerali'][minerali])
                                calc = True
                            if('Potassio' in minerali):
                                potassio.append(prova[pasto][indice]['Minerali'][minerali])
                                pot = True
                            if('Zinco' in minerali):
                                zinco.append(prova[pasto][indice]['Minerali'][minerali])
                                zin = True
                    if(prova[pasto][indice]['Vitamine']!='ND'):
                        for vit in prova[pasto][indice]['Vitamine'].keys():
                            #print(grassi)
                            
                            if('Vitamina K' in vit):
                                #print(type(prova[pasto][indice]['Vitamine'][vit]))
                                k.append(prova[pasto][indice]['Vitamine'][vit]/1000)
                                #print(k[count])
                                kvi = True
                            if('Acido folico' in vit):
                                #print(type(prova[pasto][indice]['Vitamine'][vit]))
                                #print(prova[pasto][indice]['Vitamine'][vit])
                                if(prova[pasto][indice]['Vitamine'][vit]=='tr'):
                                    folico.append(0.01)
                                else:
                                    folico.append(float(prova[pasto][indice]['Vitamine'][vit])/1000)
                                #print(folico[count])
                                fol = True
                            if('Vitamina D (' in vit and dvi==False):
                                #print(type(prova[pasto][indice]['Vitamine'][vit]))
                                d.append(prova[pasto][indice]['Vitamine'][vit]/1000)
                                #print(folico[count])
                                dvi = True
                    if('Grassi' in prova[pasto][indice].keys()):
                        if(prova[pasto][indice]['Grassi']!='ND'):
                            for grass in prova[pasto][indice]['Grassi'].keys():
                                #print(grassi)
                                
                                if('Acidi grassi Saturi' in grass):
                                    #print(type(prova[pasto][indice]['Grassi'][grass]))
                                    saturi.append(prova[pasto][indice]['Grassi'][grass]*grassi[count]/100)
                                    #print(saturi[count])
                                    sat = True
                # BDA
                elif('Nutrienti' in prova[pasto][indice].keys() and 'Zuccheri' in prova[pasto][indice].keys()):
                    #print('Entro in crea')
                    nome.append(prova[pasto][indice]['Nome'])
                    acq = False
                    cal = False
                    pro = False
                    gra = False
                    car = False
                    fib = False
                    fer = False
                    sod = False
                    zuc = False
                    col = False
                    calc = False
                    pot = False
                    zin = False
                    kvi = False
                    fol = False
                    dvi = False
                    sat = False
                    #print(fib)
                    for nutri in prova[pasto][indice]['Nutrienti'].keys():
                        if('Acqua' in nutri):
                            acqua.append(prova[pasto][indice]['Nutrienti'][nutri])
                            acq = True
                        if('Energia, ricalcolata, kcal' in nutri):
                            calorie.append(prova[pasto][indice]['Nutrienti'][nutri])
                            cal = True
                        if('Proteine totali' in nutri):
                            proteine.append(prova[pasto][indice]['Nutrienti'][nutri])
                            pro = True
                        if('Lipidi totali' in nutri):
                            #print(prova[pasto][indice]['Nutrienti'][nutri])
                            grassi.append(prova[pasto][indice]['Nutrienti'][nutri])
                            gra = True
                        if('Carboidrati disponibili' in nutri):
                            if(prova[pasto][indice]['Nutrienti'][nutri] == 'tr'):
                                carboidrati.append(0.01)
                            else:
                                carboidrati.append(prova[pasto][indice]['Nutrienti'][nutri])
                            car = True
                        if('Fibra' in nutri):
                            fibre.append(prova[pasto][indice]['Nutrienti'][nutri])
                            fib = True
                            #print(fib,nutri)
                        
                        if('Colesterolo' in nutri):
                            if(prova[pasto][indice]['Nutrienti'][nutri] == 'tr'):
                                colesterolo.append(0.01)
                            else:
                                colesterolo.append(prova[pasto][indice]['Nutrienti'][nutri])
                            col = True
                            #print(col,nutri)
                    if(prova[pasto][indice]['Minerali']!='ND'):
                        for minerali in prova[pasto][indice]['Minerali'].keys():
                            if('Ferro' in minerali):
                                ferro.append(prova[pasto][indice]['Minerali'][minerali])
                                fer = True
                            if('Sodio' in minerali):
                                sodio.append(prova[pasto][indice]['Minerali'][minerali])
                                sod = True
                                print(sodio)
                            if('Calcio' in minerali):
                                calcio.append(prova[pasto][indice]['Minerali'][minerali])
                                calc = True
                            if('Potassio' in minerali):
                                potassio.append(prova[pasto][indice]['Minerali'][minerali])
                                pot = True
                            if('Zinco' in minerali):
                                zinco.append(prova[pasto][indice]['Minerali'][minerali])
                                zin = True
                    if(prova[pasto][indice]['Vitamine']!='ND'):
                        for vit in prova[pasto][indice]['Vitamine'].keys():
                            #print(grassi)
                            
                            if('Vitamina K' in vit):
                                #print(type(prova[pasto][indice]['Vitamine'][vit]))
                                k.append(prova[pasto][indice]['Vitamine'][vit]/1000)
                                #print(k[count])
                                kvi = True
                            if('Folati' in vit):
                                #print(type(prova[pasto][indice]['Vitamine'][vit]))
                                #print(prova[pasto][indice]['Vitamine'][vit])
                                if(prova[pasto][indice]['Vitamine'][vit]=='tr'):
                                    folico.append(0.01)
                                else:
                                    folico.append(float(prova[pasto][indice]['Vitamine'][vit])/1000)
                                #print(folico[count])
                                fol = True
                            if('Vitamina D, ' in vit and dvi==False):
                                #print(type(prova[pasto][indice]['Vitamine'][vit]))
                                d.append(prova[pasto][indice]['Vitamine'][vit]/1000)
                                #print(folico[count])
                                dvi = True
                    if('Acidi Grassi' in prova[pasto][indice].keys()):
                        if(prova[pasto][indice]['Acidi Grassi']!='ND'):
                            for grass in prova[pasto][indice]['Acidi Grassi'].keys():
                                #print(grassi)
                                
                                if('Acidi grassi saturi' in grass):
                                    #print(type(prova[pasto][indice]['Grassi'][grass]))
                                    saturi.append(prova[pasto][indice]['Acidi Grassi'][grass]*grassi[count]/100)
                                    #print(saturi[count])
                                    sat = True
                elif('Nutrienti' in prova[pasto][indice].keys() and 'Name' in prova[pasto][indice].keys()):
                    #print('Entro in crea')
                    nome.append(prova[pasto][indice]['Name'])
                    acq = False
                    cal = False
                    pro = False
                    gra = False
                    car = False
                    fib = False
                    fer = False
                    sod = False
                    zuc = False
                    col = False
                    calc = False
                    pot = False
                    zin = False
                    kvi = False
                    fol = False
                    dvi = False
                    sat = False
                    #print(fib)
                    for nutri in prova[pasto][indice]['Nutrienti'].keys():
                        
                        if('Energia (kcal)' in nutri):
                            calorie.append(float(prova[pasto][indice]['Nutrienti'][nutri]))
                            cal = True
                        if('Proteine' in nutri):
                            proteine.append(float(prova[pasto][indice]['Nutrienti'][nutri]))
                            pro = True
                        
                        if('Carboidrati' in nutri):
                            if(prova[pasto][indice]['Nutrienti'][nutri] == 'tr'):
                                carboidrati.append(0.01)
                            else:
                                carboidrati.append(float(prova[pasto][indice]['Nutrienti'][nutri]))
                            car = True
                        if('Fibre' in nutri):
                            fibre.append(float(prova[pasto][indice]['Nutrienti'][nutri]))
                            fib = True
                            #print(fib,nutri)
                        if('Zuccheri' in nutri):
                            if(prova[pasto][indice]['Nutrienti'][nutri] == 'tr'):
                                zuccheri.append(0.01)
                            else:
                                zuccheri.append(float(prova[pasto][indice]['Nutrienti'][nutri]))
                            zuc = True
                            #print(zuc,nutri)
                        if('Colesterolo' in nutri):
                            if(prova[pasto][indice]['Nutrienti'][nutri] == 'tr'):
                                colesterolo.append(0.01)
                            else:
                                colesterolo.append(float(prova[pasto][indice]['Nutrienti'][nutri].replace(',','.').replace('g',''))*1000) # riporto in mg
                            col = True
                            #print(col,nutri)
                    if(prova[pasto][indice]['Minerali']!='ND'):
                        for minerali in prova[pasto][indice]['Minerali'].keys():
                            if('Ferro' in minerali):
                                ferro.append(float(prova[pasto][indice]['Minerali'][minerali]))
                                fer = True
                            if('Sodio' in minerali):
                                sodio.append(float(prova[pasto][indice]['Minerali'][minerali]))
                                sod = True
                                print(sodio)
                            if('Calcio' in minerali):
                                calcio.append(float(prova[pasto][indice]['Minerali'][minerali]))
                                calc = True
                            if('Potassio' in minerali):
                                potassio.append(float(prova[pasto][indice]['Minerali'][minerali]))
                                pot = True
                            if('Zinco' in minerali):
                                zinco.append(float(prova[pasto][indice]['Minerali'][minerali]))
                                zin = True
                    
                    if('Grassi' in prova[pasto][indice].keys()):
                        if(prova[pasto][indice]['Grassi']!='ND'):
                            for grass in prova[pasto][indice]['Grassi'].keys():
                                #print(grassi)
                                gras = 0
                                if('Grassi Saturi' in grass):
                                    #print(type(prova[pasto][indice]['Grassi'][grass]))
                                    saturi.append(float(prova[pasto][indice]['Grassi'][grass]))#*grassi[count]/100)
                                    #print(saturi[count])
                                    sat = True
                                    gras = gras + float(prova[pasto][indice]['Grassi'][grass])
                                    gra = True
                                if('Grassi Insaturi' in grass):
                                    
                                    gras = gras + float(prova[pasto][indice]['Grassi'][grass])
                                    gra = True
                                if('Grassi Monoinsaturi' in grass):
                                    
                                    gras = gras + float(prova[pasto][indice]['Grassi'][grass])
                                    gra = True
                                if(gra):
                                    grassi.append(gras)
                else:
                    #print('Entro in open')
                    if('product_name' in prova[pasto][indice].keys()):
                        nome.append(prova[pasto][indice]['product_name'])
                    elif('product_name_en' in prova[pasto][indice].keys()):
                        nome.append(prova[pasto][indice]['product_name_en'])
                    else:
                        nome.append('Not found')
                    acq = False
                    cal = False
                    pro = False
                    gra = False
                    car = False
                    fib = False
                    fer = False
                    sod = False
                    zuc = False
                    col = False
                    calc = False
                    pot = False
                    zin = False
                    kvi = False
                    fol = False
                    dvi = False
                    sat = False
                    #print(fib)
                    if('Acqua' in prova[pasto][indice].keys()):
                        print('Acqua',prova[pasto][indice]['Acqua'])
                        print('Quantita',prova[pasto][indice]['Quantita'])
                        acqu = prova[pasto][indice]['Acqua'] #* prova[pasto][indice]['Quantit�']/100 # acqua contenuta nella bevanda
                        print(acqu)
                        acq = True
                        acqua.append(acqu)
                        print(acqua)
# =============================================================================
#                     if('ingredients' in prova[pasto][indice].keys()):
#                         #print(prova[pasto][indice]['ingredients'])
#                         acqu = 0
#                         for j in range(0,len(prova[pasto][indice]['ingredients'])):
#                             for key in prova[pasto][indice]['ingredients'][j].keys():
#                                 if('water' in key):
#                                     #print(key)
#                                     acqu = acqu + prova[pasto][indice]['ingredients'][j][key]
#                                     #acqua.append(prova[pasto][indice]['ingredients'][j][key])
#                                     acq = True
#                         acqua.append(acqu)
#                         acq = True
# =============================================================================
                    if('nutriments' in prova[pasto][indice].keys()):
                        for key in prova[pasto][indice]['nutriments'].keys():
                            if(key == 'energy-kcal'):
                                calorie.append(prova[pasto][indice]['nutriments'][key])
                                cal = True
                            if(key == 'proteins'):
                                proteine.append(prova[pasto][indice]['nutriments'][key])
                                pro = True
                            if(key == 'fat'):
                                grassi.append(prova[pasto][indice]['nutriments'][key])
                                gra = True
                            if(key == 'carbohydrates'):
                                #print(key)
                                
                                #print(prova[pasto][indice]['nutriments'][key])
                                carboidrati.append(prova[pasto][indice]['nutriments'][key])
                                car = True
                            if(key == 'fiber'):
                                fibre.append(prova[pasto][indice]['nutriments'][key])
                                fib = True
                                #print(fib)
                            if(key == 'iron'):
                                #print(prova[pasto][indice]['nutriments']['iron_unit'])
                                if(prova[pasto][indice]['nutriments']['iron_unit']=='mg'):
                                    ferro.append(prova[pasto][indice]['nutriments'][key])
                                elif(prova[pasto][indice]['nutriments']['iron_unit']=='g'):
                                    ferro.append(prova[pasto][indice]['nutriments'][key]*1000)
                                else:
                                    ferro.append(prova[pasto][indice]['nutriments'][key]/1000)
                                fer = True
                            if(key == 'sodium'):
                                sodio.append(prova[pasto][indice]['nutriments'][key]*1000)
                                sod = True
                                print(sodio)
                                #print(sod)
                            if(key == 'sugar'):
                                zuccheri.append(prova[pasto][indice]['nutriments'][key])
                                zuc = True
                                #print(zuc)
                            if(key == 'cholesterol'):
                                #print(prova[pasto][indice]['nutriments']['cholesterol_unit'])
                                if(prova[pasto][indice]['nutriments']['cholesterol_unit']=='mg'):
                                    ferro.append(prova[pasto][indice]['nutriments'][key])
                                elif(prova[pasto][indice]['nutriments']['cholesterol_unit']=='g'):
                                    ferro.append(prova[pasto][indice]['nutriments'][key]*1000)
                                else:
                                    ferro.append(prova[pasto][indice]['nutriments'][key]/1000)
                                col = True
                            if(key == 'calcium'):
                                #print(prova[pasto][indice]['nutriments']['calcium_unit'])
                                if(prova[pasto][indice]['nutriments']['calcium_unit']=='mg'):
                                    calcio.append(prova[pasto][indice]['nutriments'][key])
                                elif(prova[pasto][indice]['nutriments']['calcium_unit']=='g'):
                                    calcio.append(prova[pasto][indice]['nutriments'][key]*1000)
                                else:
                                    calcio.append(prova[pasto][indice]['nutriments'][key]/1000)
                                calc = True
                            if(key == 'potassium'):
                                #print(prova[pasto][indice]['nutriments']['potassium_unit'])
                                if(prova[pasto][indice]['nutriments']['potassium_unit']=='mg'):
                                    potassio.append(prova[pasto][indice]['nutriments'][key])
                                elif(prova[pasto][indice]['nutriments']['potassium_unit']=='g'):
                                    potassio.append(prova[pasto][indice]['nutriments'][key]*1000)
                                else:
                                    potassio.append(prova[pasto][indice]['nutriments'][key]/1000)
                                pot = True
                            if(key == 'zinc'):
                                #print(prova[pasto][indice]['nutriments']['zinc_unit'])
                                if(prova[pasto][indice]['nutriments']['zinc_unit']=='mg'):
                                    zinco.append(prova[pasto][indice]['nutriments'][key])
                                elif(prova[pasto][indice]['nutriments']['zinc_unit']=='g'):
                                    zinco.append(prova[pasto][indice]['nutriments'][key]*1000)
                                else:
                                    zinco.append(prova[pasto][indice]['nutriments'][key]/1000)
                                zin = True
                            if(key == 'vitamin-k'):
                                #print(prova[pasto][indice]['nutriments']['vitamin-k_unit'])
                                if(prova[pasto][indice]['nutriments']['vitamin-k_unit']=='mg'):
                                    k.append(prova[pasto][indice]['nutriments'][key])
                                elif(prova[pasto][indice]['nutriments']['vitamin-k_unit']=='g'):
                                    k.append(prova[pasto][indice]['nutriments'][key]*1000)
                                else:
                                    k.append(prova[pasto][indice]['nutriments'][key]/1000)
                                kvi = True
                            if(key == 'folic-acid'):
                                #print(prova[pasto][indice]['nutriments']['folic-acid_unit'])
                                if(prova[pasto][indice]['nutriments']['folic-acid_unit']=='mg'):
                                    folico.append(prova[pasto][indice]['nutriments'][key])
                                elif(prova[pasto][indice]['nutriments']['folic-acid_unit']=='g'):
                                    folico.append(prova[pasto][indice]['nutriments'][key]*1000)
                                else:
                                    folico.append(prova[pasto][indice]['nutriments'][key]/1000)
                                fol = True
                            if(key == 'vitamin-d'):
                                #print(prova[pasto][indice]['nutriments']['vitamin-d_unit'])
                                if(prova[pasto][indice]['nutriments']['vitamin-d_unit']=='mg'):
                                    d.append(prova[pasto][indice]['nutriments'][key])
                                elif(prova[pasto][indice]['nutriments']['vitamin-d_unit']=='g'):
                                    d.append(prova[pasto][indice]['nutriments'][key]*1000)
                                else:
                                    d.append(prova[pasto][indice]['nutriments'][key]/1000)
                                dvi = True
                            if(key == 'satured-fat'):
                                saturi.append(prova[pasto][indice]['nutriments'][key])
                                sat = True

#print(prova[pasto][indice].keys())
                print(prova[pasto][indice]['Quantita'])
                quantita.append(prova[pasto][indice]['Quantita'])
                print(quantita)
                if(cal):
                    if(type(calorie[count]) == str):
                        calorie[count] = float(calorie[count])
                    calorie_riv.append(calorie[count]*float(quantita[count])/100)
                else:
                    calorie_riv.append(0)
                    calorie.append(0)
                if(acq):
                    print(acqua[count])
                    if(acqua[count]=='tr'):
                        acqua[count]=0.1
                    print('Count',count)
                    print(float(quantita[count]))
                    acqua_riv.append(acqua[count]*float(quantita[count])/100)
                else:
                    acqua_riv.append(0)
                    acqua.append(0)
                if(pro):
                    if(proteine[count] == 'tr'):
                        proteine[count] = 0.01
                    if(type(proteine[count]) == str):
                        proteine[count] = float(proteine[count])
                    proteine_riv.append(proteine[count]*float(quantita[count])/100)
                else:
                    proteine_riv.append(0)
                    proteine.append(0)
                if(gra):
                    #print('Grassi:')
                    #print(grassi)
                    if('tr' in str(grassi[count])):
                        grassi[count]=0.01
                    grassi_riv.append(grassi[count]*float(quantita[count])/100)
                else:
                    grassi_riv.append(0)
                    grassi.append(0)
                if(car):
                    if(type(carboidrati[count]) == str):
                        carboidrati[count] = float(carboidrati[count])
                    carboidrati_riv.append(carboidrati[count]*float(quantita[count])/100)
                else:
                    carboidrati_riv.append(0)
                    carboidrati.append(0)
                if(fib):
                    print(fibre[count])
                    if('tr' in str(fibre[count])):
                        fibre[count]=0.01
                    fibre_riv.append(float(fibre[count])*float(quantita[count])/100)
                else:
                    fibre_riv.append(0)
                    fibre.append(0)
                if(fer):
                    if(ferro[count] == 'tr'):
                        ferro[count] = 0.01
                    ferro_riv.append(ferro[count]*float(quantita[count])/100)
                else:
                    ferro_riv.append(0)
                    ferro.append(0)
                if(sod):
                    print(sodio)
                    if(sodio[count] == 'tr'):
                        sodio[count] = 0.01
                    print('Count',count)
                    print(float(quantita[count]))
                    sodio_riv.append(sodio[count]*float(quantita[count])/100)
                else:
                    sodio_riv.append(0)
                    sodio.append(0)
                if(zuc):
                    zuccheri_riv.append(zuccheri[count]*float(quantita[count])/100)
                else:
                    zuccheri_riv.append(0)
                    zuccheri.append(0)
                if(col):
                    colesterolo_riv.append(colesterolo[count]*float(quantita[count])/100)
                else:
                    colesterolo_riv.append(0)
                    colesterolo.append(0)
                if(calc):
                    calcio_riv.append(calcio[count]*float(quantita[count])/100)
                else:
                    calcio_riv.append(0)
                    calcio.append(0)
                if(pot):
                    if(potassio[count] == 'tr'):
                        potassio[count]=0.01
                    potassio_riv.append(potassio[count]*float(quantita[count])/100)
                else:
                    potassio_riv.append(0)
                    potassio.append(0)
                if(zin):
                    if(zinco[count] == 'tr'):
                        zinco[count]=0.01
                    zinco_riv.append(zinco[count]*float(quantita[count])/100)
                else:
                    zinco_riv.append(0)
                    zinco.append(0)
                if(kvi):
                    k_riv.append(k[count]*float(quantita[count])/100)
                else:
                    k_riv.append(0)
                    #print(k)
                    k.append(0)
                if(fol):
                    folico_riv.append(folico[count]*float(quantita[count])/100)
                else:
                    folico_riv.append(0)
                    folico.append(0)
                if(dvi):
                    d_riv.append(d[count]*float(quantita[count])/100)
                else:
                    d_riv.append(0)
                    d.append(0)
                if(sat):
                    saturi_riv.append(saturi[count]*float(quantita[count])/100)
                else:
                    saturi_riv.append(0)
                    saturi.append(0)
                ind.append(count)
                count = count + 1
                print('Count',count)
    risultato = [acqua_riv, calorie_riv,proteine_riv, grassi_riv,saturi_riv,carboidrati_riv,fibre_riv,ferro_riv, sodio_riv, zuccheri_riv,colesterolo_riv,calcio_riv,potassio_riv,zinco_riv,k_riv,
                 folico_riv, d_riv, nome]
    return risultato

def calcola_nutrienti_ricetta(ricetta):
    acqua = []
    acqua_riv = []
    calorie_riv = []
    calorie = []
    proteine = []
    proteine_riv = []
    grassi=[]
    grassi_riv = []
    carboidrati = []
    carboidrati_riv = []
    fibre = []
    fibre_riv=[]
    ferro = []
    ferro_riv = []
    sodio = []
    sodio_riv = []
    zuccheri = []
    zuccheri_riv = []
    colesterolo = []
    colesterolo_riv = []
    calcio = []
    calcio_riv = []
    potassio = []
    potassio_riv = []
    zinco = []
    zinco_riv = []
    k = []
    k_riv = []
    folico = []
    folico_riv = []
    d= []
    d_riv = []
    saturi = []
    saturi_riv = []
    ind = []
    count = 0
    quantita = []
    nome = []
    for indice in ricetta.keys():
        nome.append(ricetta[indice]['Nome'])
        print(ricetta[indice]['Nome'])
        if('Nutrienti principali' in ricetta[indice].keys()):
            #print('Entro in nutrienti')
            acq = False
            cal = False
            pro = False
            gra = False
            car = False
            fib = False
            fer = False
            sod = False
            zuc = False
            col = False
            calc = False
            pot = False
            zin = False
            kvi = False
            fol = False
            dvi = False
            sat = False
            for nutri in ricetta[indice]['Nutrienti principali'].keys():
                #print(nutri)
                if('Acqua' in nutri):
                    #print('Acqua',ricetta[indice]['Nutrienti principali'][nutri])
                    acqua.append(ricetta[indice]['Nutrienti principali'][nutri])
                    acq = True
                if('Calorie' in nutri):
                    calorie.append(ricetta[indice]['Nutrienti principali'][nutri])
                    cal = True
                if('Proteine' in nutri):
                    proteine.append(ricetta[indice]['Nutrienti principali'][nutri])
                    pro = True
                if('Grassi' in nutri):
                    grassi.append(ricetta[indice]['Nutrienti principali'][nutri])
                    gra = True
                if('Carboidrati' in nutri):
                    carboidrati.append(ricetta[indice]['Nutrienti principali'][nutri])
                    car = True
                if('Fibre' in nutri):
                    fibre.append(ricetta[indice]['Nutrienti principali'][nutri])
                    fib = True
            for minerali in ricetta[indice]['Minerali'].keys():
                if('Ferro' in minerali):
                    ferro.append(ricetta[indice]['Minerali'][minerali])
                    fer = True
                if('Sodio' in minerali):
                    sodio.append(ricetta[indice]['Minerali'][minerali])
                    sod = True
                if('Calcio' in minerali):
                    calcio.append(ricetta[indice]['Minerali'][minerali])
                    calc = True
                if('Potassio' in minerali):
                    potassio.append(ricetta[indice]['Minerali'][minerali])
                    pot = True
                if('Zinco' in minerali):
                    zinco.append(ricetta[indice]['Minerali'][minerali])
                    zin = True
            for carbo in ricetta[indice]['Carboidrati'].keys():
                if('Zuccheri' in carbo):
                    zuccheri.append(ricetta[indice]['Carboidrati'][carbo])
                    zuc = True
            if(ricetta[indice]['Lipidi'] !='ND'):
                for grass in ricetta[indice]['Lipidi'].keys():
                    if('Colesterolo' in grass):
                        colesterolo.append(ricetta[indice]['Lipidi'][grass])
                        col = True
                    if('Grassi saturi' in grass):
                        saturi.append(ricetta[indice]['Lipidi'][grass])
                        sat = True
            if(ricetta[indice]['Vitamine'] !='ND'):
                for vitamine in ricetta[indice]['Vitamine'].keys():
                    if('Vitamina K' in vitamine):
                        k.append(float(ricetta[indice]['Vitamine'][vitamine])/1000)
                        kvi = True
                    if('Acido folico' in vitamine):
                        folico.append(float(ricetta[indice]['Vitamine'][vitamine])/1000)
                        fol = True
                    if('Vitamina D (' in vitamine and dvi==False):
                        d.append(float(ricetta[indice]['Vitamine'][vitamine])/1000)
                        dvi = True
        elif('Nutrienti' in ricetta[indice].keys() and 'Descrizione' in ricetta[indice].keys()):
            #print('Entro in nutrienti')
            acq = False
            cal = False
            pro = False
            gra = False
            car = False
            fib = False
            fer = False
            sod = False
            zuc = False
            col = False
            calc = False
            pot = False
            zin = False
            kvi = False
            fol = False
            dvi = False
            sat = False
            #print(fib)
            for nutri in ricetta[indice]['Nutrienti'].keys():
                #print(nutri)
                if('Acqua' in nutri):
                    if(ricetta[indice]['Nutrienti'][nutri] == 'tr'):
                        ricetta[indice]['Nutrienti'][nutri] = 0.1
                    acqua.append(ricetta[indice]['Nutrienti'][nutri])
                    acq = True
                if('Energia (kcal)' in nutri):
                    calorie.append(ricetta[indice]['Nutrienti'][nutri])
                    cal = True
                if('Proteine' in nutri):
                    proteine.append(ricetta[indice]['Nutrienti'][nutri])
                    pro = True
                if('Lipidi' in nutri):
                    grassi.append(ricetta[indice]['Nutrienti'][nutri])
                    gra = True
                if('Carboidrati' in nutri):
                    if(ricetta[indice]['Nutrienti'][nutri] == 'tr'):
                        carboidrati.append(0.01)
                    else:
                        carboidrati.append(ricetta[indice]['Nutrienti'][nutri])
                    car = True
                if('Fibra' in nutri):
                    fibre.append(ricetta[indice]['Nutrienti'][nutri])
                    fib = True
                    #print(fib,nutri)
                if('Zuccheri' in nutri):
                    if(ricetta[indice]['Nutrienti'][nutri] == 'tr'):
                        zuccheri.append(0.01)
                    else:
                        zuccheri.append(ricetta[indice]['Nutrienti'][nutri])
                    zuc = True
                if('Colesterolo' in nutri):
                    colesterolo.append(ricetta[indice]['Nutrienti'][nutri])
                    col = True
                    #print(fib,nutri)
            if(ricetta[indice]['Minerali']!='ND'):
                for minerali in ricetta[indice]['Minerali'].keys():
                    if('Ferro' in minerali):
                        ferro.append(ricetta[indice]['Minerali'][minerali])
                        fer = True
                    if('Sodio' in minerali):
                        if(ricetta[indice]['Minerali'][minerali] == 'tr'):
                            ricetta[indice]['Minerali'][minerali] = 0.01
                        sodio.append(ricetta[indice]['Minerali'][minerali])
                        sod = True
                    if('Calcio' in minerali):
                        calcio.append(ricetta[indice]['Minerali'][minerali])
                        calc = True
                    if('Potassio' in minerali):
                        if(ricetta[indice]['Minerali'][minerali] == 'tr'):
                            ricetta[indice]['Minerali'][minerali] = 0.01
                        potassio.append(ricetta[indice]['Minerali'][minerali])
                        pot = True
                    if('Zinco' in minerali):
                        if(ricetta[indice]['Minerali'][minerali] == 'tr'):
                            ricetta[indice]['Minerali'][minerali] = 0.01
                        zinco.append(ricetta[indice]['Minerali'][minerali])
                        zin = True
            if(ricetta[indice]['Vitamine'] !='ND'):
                for vitamine in ricetta[indice]['Vitamine'].keys():
                    if('Vitamina K' in vitamine):
                        k.append(ricetta[indice]['Vitamine'][vitamine])
                        kvi = True
                    if('Acido folico' in vitamine):
                        folico.append(float(ricetta[indice]['Vitamine'][vitamine])/1000)
                        fol = True
                    if('Vitamina D (' in vitamine and dvi==False):
                        d.append(float(ricetta[indice]['Vitamine'][vitamine])/1000)
                        dvi = True
            if('Grassi' in ricetta[indice].keys()):
                if(ricetta[indice]['Grassi'] !='ND'):
                    for grass in ricetta[indice]['Grassi'].keys():
                        if('Acidi grassi Saturi' in grass):
                            saturi.append(float(ricetta[indice]['Grassi'][grass]*grassi[count])/100)
                            sat = True
        elif('Nutrienti' in ricetta[indice].keys() and 'Zuccheri' in ricetta[indice].keys()):
            #print('Entro in nutrienti')
            acq = False
            cal = False
            pro = False
            gra = False
            car = False
            fib = False
            fer = False
            sod = False
            zuc = False
            col = False
            calc = False
            pot = False
            zin = False
            kvi = False
            fol = False
            dvi = False
            sat = False
            #print(fib)
            for nutri in ricetta[indice]['Nutrienti'].keys():
                #print(nutri)
                if('Acqua' in nutri):
                    if(ricetta[indice]['Nutrienti'][nutri] == 'tr'):
                        ricetta[indice]['Nutrienti'][nutri] = 0.1
                    acqua.append(ricetta[indice]['Nutrienti'][nutri])
                    acq = True
                if('Energia, ricalcolata, kcal' in nutri):
                    calorie.append(ricetta[indice]['Nutrienti'][nutri])
                    cal = True
                if('Proteine totali' in nutri):
                    proteine.append(ricetta[indice]['Nutrienti'][nutri])
                    pro = True
                if('Lipidi totali' in nutri):
                    grassi.append(ricetta[indice]['Nutrienti'][nutri])
                    gra = True
                if('Carboidrati disponibili' in nutri):
                    if(ricetta[indice]['Nutrienti'][nutri] == 'tr'):
                        carboidrati.append(0.01)
                    else:
                        carboidrati.append(ricetta[indice]['Nutrienti'][nutri])
                    car = True
                if('Fibra' in nutri):
                    fibre.append(ricetta[indice]['Nutrienti'][nutri])
                    fib = True
                    #print(fib,nutri)
                
                if('Colesterolo' in nutri):
                    colesterolo.append(ricetta[indice]['Nutrienti'][nutri])
                    col = True
                    #print(fib,nutri)
            if(ricetta[indice]['Minerali']!='ND'):
                for minerali in ricetta[indice]['Minerali'].keys():
                    if('Ferro' in minerali):
                        ferro.append(ricetta[indice]['Minerali'][minerali])
                        fer = True
                    if('Sodio' in minerali):
                        if(ricetta[indice]['Minerali'][minerali] == 'tr'):
                            ricetta[indice]['Minerali'][minerali] = 0.01
                        sodio.append(ricetta[indice]['Minerali'][minerali])
                        sod = True
                    if('Calcio' in minerali):
                        calcio.append(ricetta[indice]['Minerali'][minerali])
                        calc = True
                    if('Potassio' in minerali):
                        if(ricetta[indice]['Minerali'][minerali] == 'tr'):
                            ricetta[indice]['Minerali'][minerali] = 0.01
                        potassio.append(ricetta[indice]['Minerali'][minerali])
                        pot = True
                    if('Zinco' in minerali):
                        if(ricetta[indice]['Minerali'][minerali] == 'tr'):
                            ricetta[indice]['Minerali'][minerali] = 0.01
                        zinco.append(ricetta[indice]['Minerali'][minerali])
                        zin = True
            if(ricetta[indice]['Vitamine'] !='ND'):
                for vitamine in ricetta[indice]['Vitamine'].keys():
                    if('Vitamina K' in vitamine):
                        k.append(ricetta[indice]['Vitamine'][vitamine])
                        kvi = True
                    if('Folati totali' in vitamine):
                        folico.append(float(ricetta[indice]['Vitamine'][vitamine])/1000)
                        fol = True
                    if('Vitamina D, ' in vitamine and dvi==False):
                        d.append(float(ricetta[indice]['Vitamine'][vitamine])/1000)
                        dvi = True
            if('Acidi Grassi' in ricetta[indice].keys()):
                if(ricetta[indice]['Acidi Grassi'] !='ND'):
                    for grass in ricetta[indice]['Acidi Grassi'].keys():
                        if('Acidi grassi saturi' in grass):
                            saturi.append(float(ricetta[indice]['Acidi Grassi'][grass]*grassi[count])/100)
                            sat = True
        #print(acq,cal,pro,gra,car,fib)   
        quantita.append(ricetta[indice]['Quantita'])
        if(cal):
            calorie_riv.append(float(calorie[count])*float(quantita[count])/100)
        else:
            calorie_riv.append(0)
            calorie.append(0)
        if(acq):
            acqua_riv.append(float(acqua[count])*float(quantita[count])/100)
        else:
            acqua_riv.append(0)
            acqua.append(0)
        if(pro):
            proteine_riv.append(float(proteine[count])*float(quantita[count])/100)
        else:
            proteine_riv.append(0)
            proteine.append(0)
        if(gra):
            grassi_riv.append(float(grassi[count])*float(quantita[count])/100)
        else:
            grassi_riv.append(0)
            grassi.append(0)
        if(car):
            carboidrati_riv.append(float(carboidrati[count])*float(quantita[count])/100)
        else:
            carboidrati_riv.append(0)
            carboidrati.append(0)
        if(fib):
            fibre_riv.append(float(fibre[count])*float(quantita[count])/100)
        else:
            fibre_riv.append(0)
            fibre.append(0)
        if(fer):
            ferro_riv.append(float(ferro[count])*float(quantita[count])/100)
        else:
            ferro_riv.append(0)
            ferro.append(0)
        if(sod):
            sodio_riv.append(float(sodio[count])*float(quantita[count])/100)
        else:
            sodio_riv.append(0)
            sodio.append(0)
        if(zuc):
            zuccheri_riv.append(float(zuccheri[count])*float(quantita[count])/100)
        else:
            zuccheri_riv.append(0)
            zuccheri.append(0)
        if(col):
            colesterolo_riv.append(float(colesterolo[count])*float(quantita[count])/100)
        else:
            colesterolo_riv.append(0)
            colesterolo.append(0)
        if(calc):
            calcio_riv.append(float(calcio[count])*float(quantita[count])/100)
        else:
            calcio_riv.append(0)
            calcio.append(0)
        if(pot):
            potassio_riv.append(float(potassio[count])*float(quantita[count])/100)
        else:
            potassio_riv.append(0)
            potassio.append(0)
        if(zin):
            zinco_riv.append(float(zinco[count])*float(quantita[count])/100)
        else:
            zinco_riv.append(0)
            zinco.append(0)
        if(kvi):
            k_riv.append(float(k[count])*float(quantita[count])/100)
        else:
            k_riv.append(0)
            k.append(0)
        if(fol):
            folico_riv.append(float(folico[count])*float(quantita[count])/100)
        else:
            folico_riv.append(0)
            folico.append(0)
        if(dvi):
            d_riv.append(float(d[count])*float(quantita[count])/100)
        else:
            d_riv.append(0)
            d.append(0)
        if(sat):
            saturi_riv.append(float(saturi[count])*float(quantita[count])/100)
        else:
            saturi_riv.append(0)
            saturi.append(0)
        ind.append(count)
        count = count + 1
    #print(acqua_riv)
    risultato = [sum(acqua_riv), sum(calorie_riv),sum(proteine_riv), sum(grassi_riv),sum(carboidrati_riv),sum(fibre_riv),sum(ferro_riv),sum(sodio_riv),sum(zuccheri_riv),sum(colesterolo_riv),sum(potassio_riv),
                 sum(calcio_riv),sum(zinco_riv),sum(k_riv),sum(folico_riv), sum(d_riv),sum(saturi_riv)]
    #print(risultato)
    return risultato
    
    
def calcola_nutrienti_ricetta_calorie(ricetta, qty):
    acqua = []
    acqua_riv = []
    calorie_riv = []
    calorie = []
    proteine = []
    proteine_riv = []
    grassi=[]
    grassi_riv = []
    carboidrati = []
    carboidrati_riv = []
    fibre = []
    fibre_riv=[]
    ferro = []
    ferro_riv = []
    sodio = []
    sodio_riv = []
    zuccheri = []
    zuccheri_riv = []
    colesterolo = []
    colesterolo_riv = []
    calcio = []
    calcio_riv = []
    potassio = []
    potassio_riv = []
    zinco = []
    zinco_riv = []
    k = []
    k_riv = []
    folico = []
    folico_riv = []
    d= []
    d_riv = []
    saturi = []
    saturi_riv = []
    calcio = []
    calcio_riv = []
    ind = []
    count = 0
    quantita = []
    nome = []
    for indice in ricetta.keys():
        nome.append(ricetta[indice]['Nome'])
        if('Nutrienti principali' in ricetta[indice].keys()):
            #print('Entro in nutrienti')
            acq = False
            cal = False
            pro = False
            gra = False
            car = False
            fib = False
            fer = False
            sod = False
            zuc = False
            col = False
            calc = False
            pot = False
            zin = False
            kvi = False
            fol = False
            dvi = False
            sat = False
            for nutri in ricetta[indice]['Nutrienti principali'].keys():
                #print(nutri)
                if('Acqua' in nutri):
                    #print('Acqua',ricetta[indice]['Nutrienti principali'][nutri])
                    acqua.append(ricetta[indice]['Nutrienti principali'][nutri])
                    acq = True
                if('Calorie' in nutri):
                    calorie.append(ricetta[indice]['Nutrienti principali'][nutri])
                    cal = True
                if('Proteine' in nutri):
                    proteine.append(ricetta[indice]['Nutrienti principali'][nutri])
                    pro = True
                if('Grassi' in nutri):
                    grassi.append(ricetta[indice]['Nutrienti principali'][nutri])
                    gra = True
                if('Carboidrati' in nutri):
                    carboidrati.append(ricetta[indice]['Nutrienti principali'][nutri])
                    car = True
                if('Fibre' in nutri):
                    fibre.append(ricetta[indice]['Nutrienti principali'][nutri])
                    fib = True
            for minerali in ricetta[indice]['Minerali'].keys():
                if('Ferro' in minerali):
                    ferro.append(ricetta[indice]['Minerali'][minerali])
                    fer = True
                if('Sodio' in minerali):
                    sodio.append(ricetta[indice]['Minerali'][minerali])
                    sod = True
                if('Calcio' in minerali):
                    calcio.append(ricetta[indice]['Minerali'][minerali])
                    calc = True
                if('Potassio' in minerali):
                    potassio.append(ricetta[indice]['Minerali'][minerali])
                    pot = True
                if('Zinco' in minerali):
                    zinco.append(ricetta[indice]['Minerali'][minerali])
                    zin = True
            for carbo in ricetta[indice]['Carboidrati'].keys():
                if('Zuccheri' in carbo):
                    zuccheri.append(ricetta[indice]['Carboidrati'][carbo])
                    zuc = True
            if(ricetta[indice]['Lipidi'] !='ND'):
                for grass in ricetta[indice]['Lipidi'].keys():
                    if('Colesterolo' in grass):
                        colesterolo.append(ricetta[indice]['Lipidi'][grass])
                        col = True
                    if('Grassi saturi' in grass):
                        saturi.append(ricetta[indice]['Lipidi'][grass])
                        sat = True
            if(ricetta[indice]['Vitamine'] !='ND'):
                for vitamine in ricetta[indice]['Vitamine'].keys():
                    if('Vitamina K' in vitamine):
                        k.append(float(ricetta[indice]['Vitamine'][vitamine])/1000)
                        kvi = True
                    if('Acido folico' in vitamine):
                        folico.append(float(ricetta[indice]['Vitamine'][vitamine])/1000)
                        fol = True
                    if('Vitamina D (' in vitamine and dvi==False):
                        d.append(float(ricetta[indice]['Vitamine'][vitamine])/1000)
                        dvi = True
        elif('Nutrienti' in ricetta[indice].keys() and 'Descrizione' in ricetta[indice].keys()):
            #print('Entro in nutrienti')
            acq = False
            cal = False
            pro = False
            gra = False
            car = False
            fib = False
            sod = False
            zuc = False
            col = False
            calc = False
            pot = False
            zin = False
            kvi = False
            fol = False
            dvi = False
            sat = False
            fer = False
            #print(fib)
            for nutri in ricetta[indice]['Nutrienti'].keys():
                #print(nutri)
                if('Acqua' in nutri):
                    if(ricetta[indice]['Nutrienti'][nutri] == 'tr'):
                        ricetta[indice]['Nutrienti'][nutri] = 0.1
                    acqua.append(ricetta[indice]['Nutrienti'][nutri])
                    acq = True
                if('Energia (kcal)' in nutri):
                    calorie.append(ricetta[indice]['Nutrienti'][nutri])
                    cal = True
                if('Proteine' in nutri):
                    proteine.append(ricetta[indice]['Nutrienti'][nutri])
                    pro = True
                if('Lipidi' in nutri):
                    grassi.append(ricetta[indice]['Nutrienti'][nutri])
                    gra = True
                if('Carboidrati' in nutri):
                    if(ricetta[indice]['Nutrienti'][nutri] == 'tr'):
                        carboidrati.append(0.01)
                    else:
                        carboidrati.append(ricetta[indice]['Nutrienti'][nutri])
                    car = True
                if('Fibra' in nutri):
                    fibre.append(ricetta[indice]['Nutrienti'][nutri])
                    fib = True
                    #print(fib,nutri)
                if('Zuccheri' in nutri):
                    if(ricetta[indice]['Nutrienti'][nutri] == 'tr'):
                        zuccheri.append(0.01)
                    else:
                        zuccheri.append(ricetta[indice]['Nutrienti'][nutri])
                    zuc = True
                if('Colesterolo' in nutri):
                    colesterolo.append(ricetta[indice]['Nutrienti'][nutri])
                    col = True
                    #print(fib,nutri)
            if(ricetta[indice]['Minerali']!='ND'):
                for minerali in ricetta[indice]['Minerali'].keys():
                    if('Ferro' in minerali):
                        ferro.append(ricetta[indice]['Minerali'][minerali])
                        fer = True
                    if('Sodio' in minerali):
                        if(ricetta[indice]['Minerali'][minerali] == 'tr'):
                            ricetta[indice]['Minerali'][minerali] = 0.01
                        sodio.append(ricetta[indice]['Minerali'][minerali])
                        sod = True
                    if('Calcio' in minerali):
                        calcio.append(ricetta[indice]['Minerali'][minerali])
                        calc = True
                    if('Potassio' in minerali):
                        if(ricetta[indice]['Minerali'][minerali] == 'tr'):
                            ricetta[indice]['Minerali'][minerali] = 0.01
                        potassio.append(ricetta[indice]['Minerali'][minerali])
                        pot = True
                    if('Zinco' in minerali):
                        if(ricetta[indice]['Minerali'][minerali] == 'tr'):
                            ricetta[indice]['Minerali'][minerali] = 0.01
                        zinco.append(ricetta[indice]['Minerali'][minerali])
                        zin = True
            if(ricetta[indice]['Vitamine'] !='ND'):
                for vitamine in ricetta[indice]['Vitamine'].keys():
                    if('Vitamina K' in vitamine):
                        k.append(ricetta[indice]['Vitamine'][vitamine])
                        kvi = True
                    if('Acido folico' in vitamine):
                        folico.append(float(ricetta[indice]['Vitamine'][vitamine])/1000)
                        fol = True
                    if('Vitamina D (' in vitamine and dvi==False):
                        d.append(float(ricetta[indice]['Vitamine'][vitamine])/1000)
                        dvi = True
            if(ricetta[indice]['Grassi'] !='ND'):
                for grass in ricetta[indice]['Grassi'].keys():
                    if('Acidi grassi Saturi' in grass):
                        saturi.append(float(ricetta[indice]['Grassi'][grass]*grassi[count])/100)
                        sat = True
        elif('Nutrienti' in ricetta[indice].keys() and 'Zuccheri' in ricetta[indice].keys()):
            #print('Entro in nutrienti')
            acq = False
            cal = False
            pro = False
            gra = False
            car = False
            fib = False
            sod = False
            zuc = False
            col = False
            calc = False
            pot = False
            zin = False
            kvi = False
            fol = False
            dvi = False
            sat = False
            fer = False
            #print(fib)
            for nutri in ricetta[indice]['Nutrienti'].keys():
                #print(nutri)
                if('Acqua' in nutri):
                    if(ricetta[indice]['Nutrienti'][nutri] == 'tr'):
                        ricetta[indice]['Nutrienti'][nutri] = 0.1
                    acqua.append(ricetta[indice]['Nutrienti'][nutri])
                    acq = True
                if('Energia, ricalcolata, kcal' in nutri):
                    calorie.append(ricetta[indice]['Nutrienti'][nutri])
                    cal = True
                if('Proteine totali' in nutri):
                    proteine.append(ricetta[indice]['Nutrienti'][nutri])
                    pro = True
                if('Lipidi totali' in nutri):
                    grassi.append(ricetta[indice]['Nutrienti'][nutri])
                    gra = True
                if('Carboidrati disponibili' in nutri):
                    if(ricetta[indice]['Nutrienti'][nutri] == 'tr'):
                        carboidrati.append(0.01)
                    else:
                        carboidrati.append(ricetta[indice]['Nutrienti'][nutri])
                    car = True
                if('Fibra' in nutri):
                    fibre.append(ricetta[indice]['Nutrienti'][nutri])
                    fib = True
                    #print(fib,nutri)
                
                if('Colesterolo' in nutri):
                    colesterolo.append(ricetta[indice]['Nutrienti'][nutri])
                    col = True
                    #print(fib,nutri)
            if(ricetta[indice]['Minerali']!='ND'):
                for minerali in ricetta[indice]['Minerali'].keys():
                    if('Ferro' in minerali):
                        ferro.append(ricetta[indice]['Minerali'][minerali])
                        fer = True
                    if('Sodio' in minerali):
                        if(ricetta[indice]['Minerali'][minerali] == 'tr'):
                            ricetta[indice]['Minerali'][minerali] = 0.01
                        sodio.append(ricetta[indice]['Minerali'][minerali])
                        sod = True
                    if('Calcio' in minerali):
                        calcio.append(ricetta[indice]['Minerali'][minerali])
                        calc = True
                    if('Potassio' in minerali):
                        if(ricetta[indice]['Minerali'][minerali] == 'tr'):
                            ricetta[indice]['Minerali'][minerali] = 0.01
                        potassio.append(ricetta[indice]['Minerali'][minerali])
                        pot = True
                    if('Zinco' in minerali):
                        if(ricetta[indice]['Minerali'][minerali] == 'tr'):
                            ricetta[indice]['Minerali'][minerali] = 0.01
                        zinco.append(ricetta[indice]['Minerali'][minerali])
                        zin = True
            if(ricetta[indice]['Vitamine'] !='ND'):
                for vitamine in ricetta[indice]['Vitamine'].keys():
                    if('Vitamina K' in vitamine):
                        k.append(ricetta[indice]['Vitamine'][vitamine])
                        kvi = True
                    if('Folati totali' in vitamine):
                        folico.append(float(ricetta[indice]['Vitamine'][vitamine])/1000)
                        fol = True
                    if('Vitamina D, ' in vitamine and dvi==False):
                        d.append(float(ricetta[indice]['Vitamine'][vitamine])/1000)
                        dvi = True
            if(ricetta[indice]['Acidi Grassi'] !='ND'):
                for grass in ricetta[indice]['Acidi Grassi'].keys():
                    if('Acidi grassi saturi' in grass):
                        saturi.append(float(ricetta[indice]['Grassi'][grass]*grassi[count])/100)
                        sat = True
        else:
            #print('Entro in nutrienti')
            acq = False
            cal = False
            pro = False
            gra = False
            car = False
            fib = False
            sod = False
            zuc = False
            col = False
            calc = False
            pot = False
            zin = False
            kvi = False
            fol = False
            dvi = False
            sat = False
            fer = False
            #print(fib)
            for nutri in ricetta[indice]['Nutrienti'].keys():
                #print(nutri)
                if('Acqua' in nutri):
                    if(ricetta[indice]['Nutrienti'][nutri] == 'tr'):
                        ricetta[indice]['Nutrienti'][nutri] = 0.1
                    acqua.append(ricetta[indice]['Nutrienti'][nutri])
                    acq = True
                if('Calorie (kcal)' in nutri):
                    calorie.append(ricetta[indice]['Nutrienti'][nutri])
                    cal = True
                if('Proteine' in nutri):
                    proteine.append(ricetta[indice]['Nutrienti'][nutri])
                    pro = True
                if('Grassi' in nutri):
                    grassi.append(ricetta[indice]['Nutrienti'][nutri])
                    gra = True
                if('Carboidrati' in nutri):
                    if(ricetta[indice]['Nutrienti'][nutri] == 'tr'):
                        carboidrati.append(0.01)
                    else:
                        carboidrati.append(ricetta[indice]['Nutrienti'][nutri])
                    car = True
                
        #print(acq,cal,pro,gra,car,fib)   
        quantita.append(ricetta[indice]['Quantita']*qty/100)
        if(cal):
            calorie_riv.append(float(calorie[count])*float(quantita[count])/100)
        else:
            calorie_riv.append(0)
            calorie.append(0)
        if(acq):
            acqua_riv.append(float(acqua[count])*float(quantita[count])/100)
        else:
            acqua_riv.append(0)
            acqua.append(0)
        if(pro):
            proteine_riv.append(float(proteine[count])*float(quantita[count])/100)
        else:
            proteine_riv.append(0)
            proteine.append(0)
        if(gra):
            grassi_riv.append(float(grassi[count])*float(quantita[count])/100)
        else:
            grassi_riv.append(0)
            grassi.append(0)
        if(car):
            carboidrati_riv.append(float(carboidrati[count])*float(quantita[count])/100)
        else:
            carboidrati_riv.append(0)
            carboidrati.append(0)
        if(fib):
            fibre_riv.append(float(fibre[count])*float(quantita[count])/100)
        else:
            fibre_riv.append(0)
            fibre.append(0)
        if(fer):
            ferro_riv.append(float(ferro[count])*float(quantita[count])/100)
        else:
            ferro_riv.append(0)
            ferro.append(0)
        if(sod):
            sodio_riv.append(float(sodio[count])*float(quantita[count])/100)
        else:
            sodio_riv.append(0)
            sodio.append(0)
        if(zuc):
            zuccheri_riv.append(float(zuccheri[count])*float(quantita[count])/100)
        else:
            zuccheri_riv.append(0)
            zuccheri.append(0)
        if(col):
            colesterolo_riv.append(float(colesterolo[count])*float(quantita[count])/100)
        else:
            colesterolo_riv.append(0)
            colesterolo.append(0)
        if(calc):
            calcio_riv.append(float(calcio[count])*float(quantita[count])/100)
        else:
            calcio_riv.append(0)
            calcio.append(0)
        if(pot):
            potassio_riv.append(float(potassio[count])*float(quantita[count])/100)
        else:
            potassio_riv.append(0)
            potassio.append(0)
        if(zin):
            zinco_riv.append(float(zinco[count])*float(quantita[count])/100)
        else:
            zinco_riv.append(0)
            zinco.append(0)
        if(kvi):
            k_riv.append(float(k[count])*float(quantita[count])/100)
        else:
            k_riv.append(0)
            k.append(0)
        if(fol):
            folico_riv.append(float(folico[count])*float(quantita[count])/100)
        else:
            folico_riv.append(0)
            folico.append(0)
        if(dvi):
            d_riv.append(float(d[count])*float(quantita[count])/100)
        else:
            d_riv.append(0)
            d.append(0)
        if(sat):
            saturi_riv.append(float(saturi[count])*float(quantita[count])/100)
        else:
            saturi_riv.append(0)
            saturi.append(0)
        ind.append(count)
        count = count + 1
    #print(acqua_riv)
    risultato = [sum(acqua_riv), sum(calorie_riv),sum(proteine_riv), sum(grassi_riv),sum(carboidrati_riv),sum(fibre_riv),sum(ferro_riv),sum(sodio_riv),sum(zuccheri_riv),sum(colesterolo_riv),sum(potassio_riv),
                 sum(calcio_riv),sum(zinco_riv),sum(k_riv),sum(folico_riv), sum(d_riv),sum(saturi_riv)]
    #print(risultato)
    return risultato   
    
    
    
#def dataframe_nutrimenti(colazione,pranzo,cena,merenda,data):
#    import pandas as pd
#    dati = []
#    titolo = ['Acqua','Calorie','Proteine','Grassi','Grassi Saturi', 'Carboidrati', 'Fibre','Ferro (mg)','Sodio (mg)','Zuccheri','Colesterolo (mg)','Calcio (mg)','Potassio (mg)','Zinco (mg)',
#              'Vitamina K (mg)','Acido folico (mg)','Vitamina D (mg)']
#    for i in range(0,len(colazione)-1):
#        print(i)
#        dati.append(sum(colazione[i])+sum(pranzo[i])+sum(cena[i])+sum(merenda[i]))
#    dataf = pd.DataFrame([titolo,dati],columns=titolo)
#    dataf = dataf.drop(0)
#    dataf = dataf.rename({1: data}, axis='index')
#    return dataf

def dataframe_nutrimenti(colazione,pranzo,cena,merenda,data):
    print('Dataframe')
    import pandas as pd
    dati = []
    cola = [] 
    pra = [] 
    cen = []
    mere = []
    titolo = ['Acqua','Calorie','Proteine','Grassi','Grassi Saturi', 'Carboidrati', 'Fibre','Ferro (mg)','Sodio (mg)','Zuccheri','Colesterolo (mg)','Calcio (mg)','Potassio (mg)','Zinco (mg)',
              'Vitamina K (mg)','Acido folico (mg)','Vitamina D (mg)']
    for i in range(0,len(colazione)-1):
        print(i)
        print(sum(colazione[i]))
        cola.append(sum(colazione[i]))
        pra.append(sum(pranzo[i]))
        cen.append(sum(cena[i]))
        mere.append(sum(merenda[i]))
        dati.append(sum(colazione[i])+sum(pranzo[i])+sum(cena[i])+sum(merenda[i]))
    dataf = pd.DataFrame([titolo,dati],columns=titolo)
    dataf = dataf.drop(0)
    dataf = dataf.rename({1: data}, axis='index')
    print(cola)
    print(titolo)
    print(len(cola))
    print(len(titolo))
    datacolazione = pd.DataFrame([titolo,cola],columns=titolo)
    print(datacolazione)
    datacolazione = datacolazione.drop(0)
    print(datacolazione)
    datacolazione = datacolazione.rename({1: data}, axis='index')
    print(datacolazione)
    print(datacolazione.keys())
    #pranzo
    datapranzo = pd.DataFrame([titolo,pra],columns=titolo)
    datapranzo = datapranzo.drop(0)
    datapranzo = datapranzo.rename({1: data}, axis='index')
    #cena
    datacena = pd.DataFrame([titolo,cen],columns=titolo)
    datacena = datacena.drop(0)
    datacena = datacena.rename({1: data}, axis='index')
    #merenda
    datamerenda = pd.DataFrame([titolo,mere],columns=titolo)
    datamerenda = datamerenda.drop(0)
    datamerenda = datamerenda.rename({1: data}, axis='index')
    return dataf, datacolazione, datapranzo, datacena, datamerenda

def grafico():
    import pymongo
    from pymongo import MongoClient
    import ssl
    import datetime
    import pandas as pd

    # Sistemare tutto
    client = pymongo.MongoClient(
        "mongodb+srv://armonia_amministrazione:uanrimcoantitao2l0i2c1a@clusterarmonia.ukpoq.mongodb.net/local?retryWrites=true&w=majority",
        ssl_cert_reqs=ssl.CERT_NONE)
    # db = client.test
    db = client['ArmoniaBot']
    col = db['AlimentiDB']

    prove = col.find({'Nome': 'AlessioNone'})
    data = pd.DataFrame()
    for prova in prove:
        date = prova['Data']
        colazione = calcola_nutrienti(prova, 'Colazione')
        pranzo = calcola_nutrienti(prova, 'Pranzo')
        cena = calcola_nutrienti(prova, 'Cena')
        merenda = calcola_nutrienti(prova, 'Merenda')
        dff, cola, pra, cen, mere = dataframe_nutrimenti(colazione, pranzo, cena, merenda, date)
        data = data.append(dff)
    data['Data'] = data.index
    data["Data"] = pd.to_datetime(data["Data"], format="%Y-%m-%d")
    data.sort_values("Data", inplace=True)
    x1 = data['Data']
    y1 = data['Calorie']
    x2 = data['Data']
    y2 = data['Acqua']

    return x1, y1, x2, y2


def cibo_mangiato(pasto, nome, data):
    import pymongo
    from pymongo import MongoClient
    import ssl
    import datetime
    import pandas as pd
    # Sistemare tutto
    client = pymongo.MongoClient(
        "mongodb+srv://armonia_amministrazione:uanrimcoantitao2l0i2c1a@clusterarmonia.ukpoq.mongodb.net/local?retryWrites=true&w=majority",
        ssl_cert_reqs=ssl.CERT_NONE)
    # db = client.test
    db = client['ArmoniaBot']
    col = db['AlimentiDB']
    prova = col.find_one({'Nome': nome, 'Data': data})
    colazione_cibo_mess = 'A colazione hai mangiato:\n'
    col_cibo = []
    qty = []
    if(prova!=None and pasto in prova.keys()):
        for i in range(0, len(prova[pasto])):
            # print(i)
            if ('Quantita' in prova[pasto][str(i + 1)].keys()):
                qty.append(prova[pasto][str(i + 1)]['Quantita'])
            else:
                qty.append('-')

            if ('Nome' in prova[pasto][str(i + 1)].keys()):
                col_cibo.append(prova[pasto][str(i + 1)]['Nome'])
                colazione_cibo_mess = colazione_cibo_mess + prova[pasto][str(i + 1)]['Nome'] + '\n'
            elif ('Name' in prova[pasto][str(i + 1)].keys()):
                col_cibo.append(prova[pasto][str(i + 1)]['Name'])
                colazione_cibo_mess = colazione_cibo_mess + prova[pasto][str(i + 1)]['Name'] + '\n'
            elif ('product_name' in prova[pasto][str(i + 1)].keys()):
                col_cibo.append(prova[pasto][str(i + 1)]['product_name'])
                colazione_cibo_mess = colazione_cibo_mess + prova[pasto][str(i + 1)]['product_name'] + '\n'
            elif ('product_name_en' in prova[pasto][str(i + 1)].keys()):
                col_cibo.append(prova[pasto][str(i + 1)]['product_name_en'])
                colazione_cibo_mess = colazione_cibo_mess + prova[pasto][str(i + 1)]['product_name_en'] + '\n'
            elif ('product_name_fr' in prova[pasto][str(i + 1)].keys()):
                col_cibo.append(prova[pasto][str(i + 1)]['product_name_fr'])
                colazione_cibo_mess = colazione_cibo_mess + prova[pasto][str(i + 1)]['product_name_fr'] + '\n'
            elif ('product_name_it' in prova[pasto][str(i + 1)].keys()):
                col_cibo.append(prova[pasto][str(i + 1)]['product_name_it'])
                colazione_cibo_mess = colazione_cibo_mess + prova[pasto][str(i + 1)]['product_name_it'] + '\n'
            elif ('brand' in prova[pasto][str(i + 1)].keys()):
                col_cibo.append(prova[pasto][str(i + 1)]['brand'])
                colazione_cibo_mess = colazione_cibo_mess + prova[pasto][str(i + 1)]['brand'] + '\n'
        df = pd.DataFrame({'Alimento': col_cibo, 'Quantita': qty})
    else:
        df = pd.DataFrame()
    return df

def identifica(email):
    import pymongo
    from pymongo import MongoClient
    import ssl
    import datetime
    import pandas as pd
    # Sistemare tutto
    client = pymongo.MongoClient(
        "mongodb+srv://armonia_amministrazione:uanrimcoantitao2l0i2c1a@clusterarmonia.ukpoq.mongodb.net/local?retryWrites=true&w=majority",
        ssl_cert_reqs=ssl.CERT_NONE)
    # db = client.test
    db = client['ArmoniaBot']
    col = db['DatabaseAnagraficoTelegram']
    utente = col.find_one({'email': email})
    if (utente == None):
        user = ''
    else:
        user = utente['Nome'] + utente['Cognome']
    return user