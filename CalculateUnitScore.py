# The score for UNIT is calculated as average score for all SECTIONS in the
# UNIT
# The score for SECTION is calculated as sum of score of all QUESTIONS in
# that SECTION.
# The score for QUESTION is calculated as weight of selected choice divided
# by sum of weights of all choices for that QUESTION.

import json

data = json.load(open('data.json'))

total_section = len(data["UNIT"])
avg_score_for_unit = 0;
total_score_for_unit = 0;
for section in data["UNIT"]:
	score_for_section = 0
	for question in section["QUESTIONS"]:
		score_for_question = 0
		selected = question["SELECTED"]
		weight = 0
		total_weight = 0
		for choices in question["CHOICES"]:
			total_weight = total_weight + choices["WEIGHT"]
			if choices["VAL"]==selected:
				weight = choices["WEIGHT"]
		score_for_question = weight/total_weight
		score_for_section = score_for_section + score_for_question
	total_score_for_unit = total_score_for_unit + score_for_section
avg_score_for_unit = total_score_for_unit / total_section
print("Score for unit is : " + str(avg_score_for_unit))


