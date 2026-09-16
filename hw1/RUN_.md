# HW1 experiment reproduction


## Part 1.3: behavioral cloning

### Ant-v2

```text
python rob831/scripts/run_hw1.py --expert_policy_file rob831/policies/experts/Ant.pkl --env_name Ant-v2 --exp_name question_1_3_ant_bc --expert_data rob831/expert_data/expert_data_Ant-v2.pkl --n_iter 1 --n_layers 2 --size 64 --learning_rate 0.005 --num_agent_train_steps_per_iter 1000 --train_batch_size 100 --batch_size 1000 --eval_batch_size 5000 --ep_len 1000 --seed 1 --scalar_log_freq 1 --video_log_freq -1 --which_gpu 0
```

Original run: `./data/q1_question_1_3_ant_bc_Ant-v2_16-09-2026_15-37-59`.

### Humanoid-v2

```text
python rob831/scripts/run_hw1.py --expert_policy_file rob831/policies/experts/Humanoid.pkl --env_name Humanoid-v2 --exp_name question_1_3_humanoid_bc --expert_data rob831/expert_data/expert_data_Humanoid-v2.pkl --n_iter 1 --n_layers 2 --size 64 --learning_rate 0.005 --num_agent_train_steps_per_iter 1000 --train_batch_size 100 --batch_size 1000 --eval_batch_size 5000 --ep_len 1000 --seed 1 --scalar_log_freq 1 --video_log_freq -1 --which_gpu 0
```

Original run: `./data/q1_question_1_3_humanoid_bc_Humanoid-v2_16-09-2026_15-34-05`.


## Part 1.4: Humanoid learning-rate sweep

Only the learning rate changes. Each command starts a separate BC run.

### Learning rate 1e-5

```text
python rob831/scripts/run_hw1.py --expert_policy_file rob831/policies/experts/Humanoid.pkl --env_name Humanoid-v2 --exp_name question_1_4_humanoid_lr_1e-5 --expert_data rob831/expert_data/expert_data_Humanoid-v2.pkl --n_iter 1 --n_layers 2 --size 64 --learning_rate 1e-5 --num_agent_train_steps_per_iter 1000 --train_batch_size 100 --batch_size 1000 --eval_batch_size 5000 --ep_len 1000 --seed 1 --scalar_log_freq 1 --video_log_freq -1 --which_gpu 0 --save_params
```

Original run: `./data/q1_question_1_4_humanoid_lr_1e-5_Humanoid-v2_16-09-2026_15-54-17`.

### Learning rate 1e-4

```text
python rob831/scripts/run_hw1.py --expert_policy_file rob831/policies/experts/Humanoid.pkl --env_name Humanoid-v2 --exp_name question_1_4_humanoid_lr_1e-4 --expert_data rob831/expert_data/expert_data_Humanoid-v2.pkl --n_iter 1 --n_layers 2 --size 64 --learning_rate 1e-4 --num_agent_train_steps_per_iter 1000 --train_batch_size 100 --batch_size 1000 --eval_batch_size 5000 --ep_len 1000 --seed 1 --scalar_log_freq 1 --video_log_freq -1 --which_gpu 0 --save_params
```

Original run: `./data/q1_question_1_4_humanoid_lr_1e-4_Humanoid-v2_16-09-2026_15-56-13`.

### Learning rate 1e-3

```text
python rob831/scripts/run_hw1.py --expert_policy_file rob831/policies/experts/Humanoid.pkl --env_name Humanoid-v2 --exp_name question_1_4_humanoid_lr_1e-3 --expert_data rob831/expert_data/expert_data_Humanoid-v2.pkl --n_iter 1 --n_layers 2 --size 64 --learning_rate 1e-3 --num_agent_train_steps_per_iter 1000 --train_batch_size 100 --batch_size 1000 --eval_batch_size 5000 --ep_len 1000 --seed 1 --scalar_log_freq 1 --video_log_freq -1 --which_gpu 0 --save_params
```

Original run: `./data/q1_question_1_4_humanoid_lr_1e-3_Humanoid-v2_16-09-2026_15-57-00`.

### Learning rate 5e-3

```text
python rob831/scripts/run_hw1.py --expert_policy_file rob831/policies/experts/Humanoid.pkl --env_name Humanoid-v2 --exp_name question_1_4_humanoid_lr_5e-3 --expert_data rob831/expert_data/expert_data_Humanoid-v2.pkl --n_iter 1 --n_layers 2 --size 64 --learning_rate 5e-3 --num_agent_train_steps_per_iter 1000 --train_batch_size 100 --batch_size 1000 --eval_batch_size 5000 --ep_len 1000 --seed 1 --scalar_log_freq 1 --video_log_freq -1 --which_gpu 0 --save_params
```

Original run: `./data/q1_question_1_4_humanoid_lr_5e-3_Humanoid-v2_16-09-2026_15-57-42`.

### Learning rate 1e-2

```text
python rob831/scripts/run_hw1.py --expert_policy_file rob831/policies/experts/Humanoid.pkl --env_name Humanoid-v2 --exp_name question_1_4_humanoid_lr_1e-2 --expert_data rob831/expert_data/expert_data_Humanoid-v2.pkl --n_iter 1 --n_layers 2 --size 64 --learning_rate 1e-2 --num_agent_train_steps_per_iter 1000 --train_batch_size 100 --batch_size 1000 --eval_batch_size 5000 --ep_len 1000 --seed 1 --scalar_log_freq 1 --video_log_freq -1 --which_gpu 0 --save_params
```

Original run: `./data/q1_question_1_4_humanoid_lr_1e-2_Humanoid-v2_16-09-2026_15-58-33`.

### Learning rate 5e-2

```text
python rob831/scripts/run_hw1.py --expert_policy_file rob831/policies/experts/Humanoid.pkl --env_name Humanoid-v2 --exp_name question_1_4_humanoid_lr_5e-2 --expert_data rob831/expert_data/expert_data_Humanoid-v2.pkl --n_iter 1 --n_layers 2 --size 64 --learning_rate 5e-2 --num_agent_train_steps_per_iter 1000 --train_batch_size 100 --batch_size 1000 --eval_batch_size 5000 --ep_len 1000 --seed 1 --scalar_log_freq 1 --video_log_freq -1 --which_gpu 0 --save_params
```

Original run: `./data/q1_question_1_4_humanoid_lr_5e-2_Humanoid-v2_16-09-2026_16-00-40`.

## Part 2.2: DAgger

### Ant-v2

```text
python rob831/scripts/run_hw1.py --expert_policy_file rob831/policies/experts/Ant.pkl --env_name Ant-v2 --exp_name question_2_ant_dagger --expert_data rob831/expert_data/expert_data_Ant-v2.pkl --n_iter 10 --do_dagger --n_layers 2 --size 64 --learning_rate 0.005 --num_agent_train_steps_per_iter 1000 --train_batch_size 100 --batch_size 1000 --eval_batch_size 5000 --ep_len 1000 --seed 1 --scalar_log_freq 1 --video_log_freq 5 --which_gpu 0 --save_params
```



### Humanoid-v2

```text
python rob831/scripts/run_hw1.py --expert_policy_file rob831/policies/experts/Humanoid.pkl --env_name Humanoid-v2 --exp_name question_2_humanoid_dagger --expert_data rob831/expert_data/expert_data_Humanoid-v2.pkl --n_iter 10 --do_dagger --n_layers 2 --size 64 --learning_rate 0.005 --num_agent_train_steps_per_iter 1000 --train_batch_size 100 --batch_size 1000 --eval_batch_size 5000 --ep_len 1000 --seed 1 --scalar_log_freq 1 --video_log_freq 5 --which_gpu 0 --save_params
```

Original run: `./data/q2_question_2_humanoid_dagger_Humanoid-v2_16-09-2026_16-03-18`.

