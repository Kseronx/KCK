import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def load_data(path):
    data = []
    datax = []
    datay = []
    with open(path) as f:
        for line in f.readlines()[1:]:
            data.append(line.split(',')[1:])
    for i in data:
        if len(i) > 0:
            datax.append(float(i[0]) / 1000.0)
    for y in data:
        sum = 0
        for z in y[1:]:
            sum += float(z)
        count = len(y) - 1
        average = sum / count * 100.0
        datay.append(average)
    return data, datax, datay

def load2(path):
    data = []
    datay = []
    with open(path) as f:
        for line in f.readlines()[1:]:
            data.append(line.split(',')[1:])
        for i in data[-1][1:]:
            datay.append(float(i) * 100)
        average = sum(datay)/len(datay)
    return average, datay

def main():
    data_2cel, data_2celx, data_2cely = load_data('2cel.csv')
    data_2cel_rs, data_2cel_rsx, data_2cel_rsy = load_data('2cel-rs.csv')
    data_cel, data_celx, data_cely = load_data('cel.csv')
    data_cel_rs, data_cel_rsx, data_cel_rsy = load_data('cel-rs.csv')
    data_rsel,data_rselx, data_rsely = load_data('rsel.csv')


    plt.rcParams["font.family"] = "Times New Roman"
    mpl.rcParams.update({'font.size': 14})
    #print(data_2cely)
    font = {'fontname': 'Times New Roman'}
    plots = plt.figure(figsize=(10, 7))
    p_1 = plots.add_subplot(121)
    p_1.plot(data_rselx, data_rsely, label="1-Evol-RS", color='blue', marker='o', markersize=6,markeredgecolor = 'black', markeredgewidth= 0.5, markevery=25)
    p_1.plot( data_cel_rsx,  data_cel_rsy, label="1-Coev-RS", color='green', marker='v', markersize=6,markeredgecolor = 'black', markeredgewidth= 0.5, markevery=25)
    p_1.plot(data_2cel_rsx, data_2cel_rsy, label="2-Coev-RS", color='red', marker='D', markersize=6, markeredgecolor = 'black', markeredgewidth= 0.5, markevery=25)
    p_1.plot(data_celx, data_cely, label="1-Coev", color='black', marker='s', markersize=6, markeredgecolor = 'black', markeredgewidth= 0.5, markevery=25)
    p_1.plot(data_2celx, data_2cely, label="2-Coev", color='magenta', marker='d', markersize=6, markeredgecolor = 'black', markeredgewidth= 0.5, markevery=25)


    p_1.set_xlabel("Rozegranych gier (x1000)", **font)
    p_1.set_ylabel("Odsetek wygranych gier [%]", **font)
    p_1.set_xlim(0, 500)
    p_1.set_ylim(60, 100)
    p_1.legend(loc=4,numpoints=2, )
    p_1.grid(linestyle = 'dotted', dashes=(1,4,1,4))
    p_1.tick_params(direction='in')
    p_12 = plt.twiny()
    p_12.set_xlabel("Pokolenie", **font)
    p_12.set_xlim(0, 200)
    p_12.set_xticks([0, 100, 200, 300, 400, 500])
    p_12.set_xticklabels(["0", "40", "80", "120", "160", "200"])
    p_12.tick_params(direction='in')

    p_2 = plots.add_subplot(122)
    danex = ["1-Evol-RS", "1-Coev-RS", "2-Coev-RS", "1-Coev", "2-Coev"]
    p_2.set_xticklabels(danex, rotation=20)
    p_2.set_ylim(60, 100)
    p_2.yaxis.set_label_position("right")
    p_2.yaxis.tick_right()


    box_data=[]
    srednie=[]

    A2cel, p2data_2cel = load2('2cel.csv')
    srednie.append(A2cel)
    A2celrs, p2data_2celrs = load2('2cel-rs.csv')
    srednie.append(A2celrs)
    Acel, p2data_cel = load2('cel.csv')
    srednie.append(Acel)
    Acelrs, p2data_celrs = load2('cel-rs.csv')
    srednie.append(Acelrs)
    Arsel, p2data_rsel = load2('rsel.csv')
    srednie.append(Arsel)

    box_data.append(p2data_rsel)
    box_data.append(p2data_celrs)
    box_data.append(p2data_2celrs)
    box_data.append(p2data_cel)
    box_data.append(p2data_2cel)
    print(box_data)
    v = np.array(box_data)
    print(v)

    whiskerprops = dict(linestyle = '-',dashes=(0,5,6,1),color='blue',linewidth=1.5)
    capprops = dict(color='black',linewidth=1.5)
    boxprops = dict( linewidth=1.5, color='blue')
    flierprops = dict(marker='+', markerfacecolor='blue', markersize=8,markeredgecolor='blue')
    dot=dict( marker='o', markerfacecolor='blue',markeredgecolor='black')
    p_2.boxplot(v.T, labels=danex,boxprops=boxprops,flierprops=flierprops, notch=True, showmeans=True, meanprops=dot,capprops=capprops,whiskerprops=whiskerprops)
    p_2.grid(linestyle = 'dotted', dashes=(1,4,1,4))
    p_2.tick_params(direction='in')
    plt.savefig('myplot.pdf')
    plt.show()
    plt.close()
if __name__ == '__main__':
    main()