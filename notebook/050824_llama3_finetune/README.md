# Fine Tune LLAMA3
This folder contain all the result and notebook we used for fine tune llama3 as Otto

## Note
1. When using 4 bit q model and with batch size of 8. It is using about 20GB VRAM
2. Saving checkpoint seems to be an really slow process in training
3. 

## Run 1
Comment: Initial baseline setting
Dataset: TC14/050724_random200gs_llama3_instruct
Base Model: meta-llama/Meta-Llama-3-8B-Instruct
Checkpoint to choise : 200

## Run 2
Comment: Same Lora adapter as Run 1
Dataset: TC14/050724_raw_llama3_instruct
Base Model: meta-llama/Meta-Llama-3-8B-Instruct

## Run 3
Comment: Change lora adapter parameter, r 8->64 alpha 8->64
Dataset: TC14/050724_random200gs_llama3_instruct
Base Model: meta-llama/Meta-Llama-3-8B-Instruct
Checkpoint to choise : 300

## Run 4
Comment: Change lora adapter parameter, r 8->64 alpha 8->64
Dataset: TC14/050724_raw_llama3_instruct
Base Model: meta-llama/Meta-Llama-3-8B-Instruct
Checkpoint to choise : 600

## Run 5
Comment: Change lora adapter parameter, r 64->256 alpha 64->256
Dataset: TC14/050724_random200gs_llama3_instruct
Base Model: meta-llama/Meta-Llama-3-8B-Instruct
Checkpoint to choise : 300

## Run 6
Comment: Change lora adapter parameter, r 64->256 alpha 64->256
Dataset: TC14/050724_raw_llama3_instruct
Base Model: meta-llama/Meta-Llama-3-8B-Instruct
Checkpoint to choise : 600
