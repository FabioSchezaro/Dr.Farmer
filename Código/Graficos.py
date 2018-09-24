#mainProgram

def iniciaGrafico (batimentoCardiaco):
    splitedArray = [float(s) for s in
    arduinoString.split(',')]
    temp = splitedArray[0]
    hum1 = splitedArray[1]
    temp2 = splitedArray[2]
    hum2 = splitedArray[3]
    moisture = splitedArray[4]
    lumen = splitedArray[5]
    tempF.append(temp)
    tempF2.append(temp2)
    humF1.append(hum1)
    humF2.append(hum2)
    moist.append(moisture)
    lum.append(lumen)
    drawnow(makeFig)
    plt.pause(.000005)
    cnt=cnt+1
    if(cnt>50):
        tempF.pop(0)
        tempF2.pop(0)
        humF1.pop(0)
        humF2.pop(0)
        moist.pop(0)
        lum.pop(0)
    #"The best way to learn is to
    # teach" (Openhimmer)