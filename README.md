
## Training

Run on one dataset, with a specific  choice of federated learning method.
Specify the name of the dataset (experiment), the used method, and configure all other
hyper-parameters (see all hyper-parameters values in the appendix of the paper)

Fjord on emnist dataset experiment
``` 

 module load conda/2021.11-python3.9 

 python3 run_experiment.py emnist Fjord \
    --n_learners 1 \
    --n_rounds 200 \
    --bz 16\
    --lr 0.1 \
    --lr_scheduler multi_step \
    --log_freq 1 \
    --device cuda \
    --optimizer sgd \
    --seed 45231 \
    --logs_root ./logs_emnist \
    --verbose 1\
    --k 5\
    --sampling_rate 0.1
```

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
```

The test and training accuracy and loss will be saved in the specified log path.

We provide example scripts to run paper experiments under `scripts/` directory.

