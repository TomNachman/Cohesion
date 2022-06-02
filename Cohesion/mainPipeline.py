import random
from Cohesion.relatedFunctions import extract_topics_labels, calculate_nmi_score, calculate_cohesion_score
from Cohesion.utils import read_data_from_csv, random_division, create_topic_names_using_tf_idf
from tqdm import tqdm
from tabulate import tabulate
import os

correlation_dict = {}
error_precentage = []
total_for_print, nmi_score_list, coherence_score_list, cohesion_score_list = {}, {}, {}, {}
passed, failed = 0, 0

if __name__ == '__main__':
    use_tqdm = True
    path = "C:\\Users\\nachm\\Documents\\University\\Year4\\CohesionPack\\event2012.tsv"
    ground_truth_list, ground_truth_label_list = read_data_from_csv(path_to_csv=path)
    print('----------- Starting main pipeline -------------')
    print('There are {} docs in path_to_csv the dataset'.format(len(ground_truth_label_list)))
    topics, _, _ = create_topic_names_using_tf_idf(ground_truth_list, ground_truth_label_list)
    topics_names = extract_topics_labels(topics.values())
    cohesion_score = calculate_cohesion_score(ground_truth_list=ground_truth_list, topics=ground_truth_label_list,
                                              topics_names=topics_names)
    print(cohesion_score)
    print(topics_names)
