## Training

Run on one dataset, with a specific choice of federated learning method.  
Specify the name of the dataset (experiment), the used method, and configure all other  
hyper-parameters (see all hyper-parameter values in the appendix of the paper).

Fjord on EMNIST dataset experiment
module load conda/2021.11-python3.9

python3 run_experiment.py emnist Fjord
--n_learners 1
--n_rounds 200
--bz 16
--lr 0.1
--lr_scheduler multi_step
--log_freq 1
--device cuda
--optimizer sgd
--seed 45231
--logs_root ./logs_emnist
--verbose 1
--k 5
--sampling_rate 0.1

css
Copy code

FedAvg experiment
```train
python3 run_experiment.py emnist FedAvg \
    --n_learners 1 \
    --n_rounds 50 \
    --bz 128 \
    --lr 0.01 \
    --lr_scheduler multi_step \
    --log_freq 2 \
    --device cpu \
    --optimizer sgd \
    --seed 1234 \
    --logs_root ./logs \
    --verbose 1
FedGreen experiment

train
Copy code
python3 run_experiment.py emnist Fjord-green \
    --n_learners 1 \
    --n_rounds 100 \
    --bz 64 \
    --lr 0.05 \
    --lr_scheduler multi_step \
    --log_freq 1 \
    --device cuda \
    --optimizer sgd \
    --seed 9876 \
    --logs_root ./logs_fedgreen \
    --verbose 1



The test and training accuracy and loss will be saved in the specified log path.

We provide example scripts to run paper and thesis experiments under the scripts/ directory.

References
Horváth et al., “FjORD: Fair and Accurate Federated Learning under Heterogeneous Targets with Ordered Dropout,” NeurIPS 2021.

McMahan et al., “Communication-Efficient Learning of Deep Networks from Decentralized Data (FedAvg),” AISTATS 2017.

Abbasi et al., “FedGreen: Carbon-Aware Federated Learning with Model Size Adaptation,” 2024.


