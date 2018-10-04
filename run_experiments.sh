for i in 1 2 3 4 5
do
    for j in datasets/synth1/synth1-test.csv datasets/synth2/synth2-test.csv datasets/concrete/concrete-test.csv
    do
        python main.py --data_file $j --config_file experiments/mutation/no_mutation.txt
        python main.py --data_file $j --config_file experiments/mutation/0_1_mutation.txt
        python main.py --data_file $j --config_file experiments/mutation/0_2_mutation.txt
        python main.py --data_file $j --config_file experiments/mutation/0_3_mutation.txt
        python main.py --data_file $j --config_file experiments/mutation/0_4_mutation.txt
        python main.py --data_file $j --config_file experiments/mutation/0_5_mutation.txt
        python main.py --data_file $j --config_file experiments/mutation/0_6_mutation.txt
        python main.py --data_file $j --config_file experiments/mutation/only_mutation.txt
    done
done

for i in 1 2 3 4 5
do
    for j in datasets/synth1/synth1-test.csv datasets/synth2/synth2-test.csv datasets/concrete/concrete-test.csv
    do
        python main.py --data_file $j --config_file experiments/tournament_size/2_tournament_size.txt
        python main.py --data_file $j --config_file experiments/tournament_size/3_tournament_size.txt
        python main.py --data_file $j --config_file experiments/tournament_size/4_tournament_size.txt
        python main.py --data_file $j --config_file experiments/tournament_size/5_tournament_size.txt
        python main.py --data_file $j --config_file experiments/tournament_size/6_tournament_size.txt
        python main.py --data_file $j --config_file experiments/tournament_size/7_tournament_size.txt
        python main.py --data_file $j --config_file experiments/tournament_size/8_tournament_size.txt
        python main.py --data_file $j --config_file experiments/tournament_size/9_tournament_size.txt
        python main.py --data_file $j --config_file experiments/tournament_size/10_tournament_size.txt
    done
done

for i in 1 2 3 4 5
do
    for j in datasets/synth1/synth1-test.csv datasets/synth2/synth2-test.csv datasets/concrete/concrete-test.csv
    do
        python main.py --data_file $j --config_file experiments/population_size/10_population_size.txt
        python main.py --data_file $j --config_file experiments/population_size/50_population_size.txt
        python main.py --data_file $j --config_file experiments/population_size/100_population_size.txt
        python main.py --data_file $j --config_file experiments/population_size/250_population_size.txt
        python main.py --data_file $j --config_file experiments/population_size/500_population_size.txt
        python main.py --data_file $j --config_file experiments/population_size/1000_population_size.txt
    done
done
