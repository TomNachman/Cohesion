import random
from Cohesion.relatedFunctions import extract_topics_labels, calculate_nmi_score, calculate_cohesion_score
from Cohesion.utils import read_data_from_csv, random_division
from tqdm import tqdm
from tabulate import tabulate

correlation_dict = {}
error_precentage = []
total_for_print, nmi_score_list, coherence_score_list, cohesion_score_list = {}, {}, {}, {}
passed, failed = 0, 0

if __name__ == '__main__':
    use_tqdm = True
    ground_truth_df_all, ground_truth_list, ground_truth_label_list, ground_truth_df = read_data_from_csv(
        path_to_csv='')
    print('----------- Starting main pipeline -------------')
    print('There are {} docs in path_to_csvthe dataset'.format(len(ground_truth_label_list)))
    models_run_over = None
    for i in tqdm(range(0, 100, 5)) if use_tqdm else range(0, 101, 5):  # create new devision using random 0%-100%
        error_precentage = str(i) + '%'
        coherence_score = random.random()
        cohesion_score = 0
        # try:
        # create new devision
        new_division_labels, topics, topics_synonyms, topics_glove = random_division(ground_truth_df, random_percent=i)
        models_run_over = [topics, topics_synonyms]  # , topics_glove]
        for index, topics in enumerate(models_run_over):
            if index not in total_for_print.keys():
                total_for_print[index], nmi_score_list[index], coherence_score_list[index], cohesion_score_list[
                    index] = [], [], [], []
            topics_names = extract_topics_labels(topics.values())

            # calculate scores
            nmi_score = calculate_nmi_score(ground_truth_label=ground_truth_label_list,
                                            new_division_labels=new_division_labels)
            # coherence_score = calculate_coherence_score(ground_truth_list=ground_truth_list, topics_names=topics_names)
            cohesion_score = calculate_cohesion_score(ground_truth_list=ground_truth_list, topics=new_division_labels,
                                                      topics_names=topics_names)
            passed += 1
            # except:
            #     failed+=1

            # save data
            # cohesion_score = 1
            total_for_print[index].append([error_precentage, nmi_score, coherence_score, cohesion_score])
            nmi_score_list[index].append(nmi_score)
            coherence_score_list[index].append(coherence_score)
            cohesion_score_list[index].append(cohesion_score)
    # TODO check about models_run_over with Asi
    for i in range(len(models_run_over)):
        # present results
        print('\nThe test finished with {:.3f}% of accuracy!'.format(passed / (passed + failed)))
        print('\n---------------------- Results {} -------------------------'.format(i))
        print(tabulate(total_for_print[i], headers=['error %', 'nmi', 'coherence', 'cohesion'], tablefmt='orgtbl'))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
