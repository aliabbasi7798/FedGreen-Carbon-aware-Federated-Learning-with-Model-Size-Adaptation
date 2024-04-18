import csv
import matplotlib
import matplotlib.pyplot as plt
if __name__ == "__main__":
    x1 = []
    y1 = []
    z1 = []

    with open('BalanceExperiment/Emnist_E=1_alpha=0.01_1cluster(m=1)_200round_feq1_real.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        i=0
        for row in plots:
            if(i > 0):
                x1.append(float(row[2]))
                y1.append(float(row[1]))
                z1.append(float(row[0]))
            i = i+1


    x2 = []
    y2 = []
    z2 = []

    with open('BalanceExperiment/Emnist_E=1_alpha=0.01_1cluster(m=0.6)_200round_feq1_real.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')

        i = 0
        for row in plots:
            if (i > 0):
                x2.append(float(row[2]))
                y2.append(float(row[1]))
                z2.append(float(row[0]))
            i = i + 1

    x3 = []
    y3 = []
    z3 = []

    with open('BalanceExperiment/Emnist_E=1_alpha=0.01_3cluster(m=0.6 , sd=0.32)_200round_feq1_real.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')

        i = 0
        for row in plots:
            if (i > 0):
                x3.append(float(row[2]))
                y3.append(float(row[1]))
                z3.append(float(row[0]))
            i = i + 1

    x4 = []
    y4 = []
    z4 = []

    with open('FedGreenCS/Emnist_E=1_alpha=0.01_feq1_real_m=0.6_sd=0.32_gc=3_kc=30_b=n.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')

        i = 0
        for row in plots:
            if (i > 0):
                x4.append(float(row[2]))
                y4.append(float(row[1]))
                z4.append(float(row[0]))

            i = i + 1

    x5 = []
    y5 = []
    z5 = []

    with open('FedGreenCS/Emnist_E=1_alpha=0.01_feq1_real_m=1_sd=0_gc=1_kc=30_b=n.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')

        i = 0
        for row in plots:
            if (i > 0):
                x5.append(float(row[2]))
                y5.append(float(row[1]))
                z5.append(float(row[0]))

            i = i + 1
    x6 = []
    y6 = []
    z6 = []

    with open('FedGreenCS/Emnist_E=1_alpha=0.01_feq1_real_m=0.6_sd=0_gc=1_kc=30_b=n.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')

        i = 0
        for row in plots:
            if (i > 0):
                x6.append(float(row[2]))
                y6.append(float(row[1]))
                z6.append(float(row[0]))

            i = i + 1
    # Plot a graph

    matplotlib.use('Agg')
    # Plot Loss curve

    plt.figure()
    #plt.title('Non-IID EMNIST(alpha = 0.01)(E=5)_real intensity')
    # Plot Loss curve


    plt.plot(x1[0:23], y1[0:23], color='r', label='1 cluster m= 1, sd=0(FedAvg)' , linewidth=0.7)
    plt.plot(x2[0:65], y2[0:65], color='k', label='1 cluster m= 0.6, sd=0', linewidth=0.7)

    plt.plot(x3[0:161], y3[0:161], color='g', label='3 cluster m= 0.6, sd=0.4', linewidth=0.7)
    plt.plot(x4, y4, color='m', label='FedGreenCS, m=0.6 , sd=0.32, k-mean-cluster=30', linewidth=0.7)

    plt.plot(x5[0:41], y5[0:41], color='b', label='FedGreenCS, m=1 , k-mean-cluster=30', linewidth=0.7)
    plt.plot(x6[0:150], y6[0:150], color='y', label='FedGreenCS, m=0.6 , k-mean-cluster=30', linewidth=0.7)

    plt.legend()
    plt.ylabel('test accuracy')
    plt.xlabel('Carbon Cost')
    plt.savefig('FedGreenCS_plot/alpha=0.01_clientselection_E=1_round_CS_total_3cluster_b_k=30_carbon.svg')