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

    with open('FedGreenCS/Emnist_E=1_alpha=0.01_feq1_real_m=1_sd=0_gc=1_kc=30_b=n.csv', 'r') as csvfile:
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

    with open('FedGreenCS/Emnist_E=1_alpha=0.01_feq1_real_m=1.csv', 'r') as csvfile:
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

    with open('FedGreenCS/Emnist_E=1_alpha=0.01_feq1_real_m=1_sd=0_gc=1_kc=5_b=n_new.csv', 'r') as csvfile:
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

    with open('FedGreenCS/Emnist_E=1_alpha=0.01_feq1_real_m=1_sd=0_gc=1_kc=10_b=n_newn.csv', 'r') as csvfile:
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


    #plt.plot(z1, y1, color='r', label='1 cluster m= 1, sd=0(FedAvg)' , linewidth=0.7)
    #plt.plot(z2, y2, color='k', label='1 cluster m= 0.6, sd=0', linewidth=0.7)

    plt.plot(z3, y3, color='g', label='FedGreenCS, m=1, k-mean-cluster=30', linewidth=0.7)
    plt.plot(z4, y4, color='m', label='FedGreenCS, m=1, k-mean-cluster=20', linewidth=0.7)

    plt.plot(z5, y5, color='b', label='FedGreenCS, m=1 , k-mean-cluster=5', linewidth=0.7)
    plt.plot(z6, y6, color='y', label='FedGreenCS, m=1 , k-mean-cluster=10', linewidth=0.7)

    plt.legend()
    plt.ylabel('test accuracy')
    plt.xlabel('Communication Round')
    plt.savefig('FedGreenCS_plot/alpha=0.01_clientselection_E=1_round_CS_total_3cluster_b_k=v.pdf')