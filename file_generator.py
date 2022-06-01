from string import Template
import os 

total_week_count = 22
eval_next_to_week_list = [6, 12, 22]
gsoc_year = "2022"
project_name = "Design Challenge 1"
project_tag = "designChallenge1"
author_name = "Utkarsh Tiwari"
base_dir = "./posts/"

os.mkdir(base_dir)

def create_week_file(field_values):
    week_file_name = "{count:02d}_week{week_count}.md"
    week_header_temaplate = """---
layout: page
title: Week $week_count
author: '$author_name'
tags: ["week","gsoc","gsoc$gsoc_year","$project_tag","week#$week_count","eval#$eval_count"]
---

## Week Summary

Week Work summary goes here 

## Daily Work Update

|\#|Day|Date|A short description of the work done|  
|---	|---	|---	|---	|  
|1   	| Monday 	|   2022/01/01	|  |  
|2   	| Tuesday  	|   2022/01/01	| 	|  
|3   	| Wednesday |  2022/01/01 	|  |  
|4   	| Thursday  |   2022/01/01	|  |  
|5   	| Friday  	|   2022/01/01	|  |  
|6   	| Saturday  |  2022/01/01	|  |  
|7   	| Sunday  	|   2022/01/01	|  |  
"""
    file_content = Template(week_header_temaplate).substitute(field_values)
    file_name = week_file_name.format_map(field_values)
    with open(os.path.join(base_dir,file_name),"w") as f:
        f.write(file_content)
    # print(file_name)
    # print(file_content)
    
def create_eval_file(field_values):
    eval_file_name = "{count:02d}_eval{eval_count}.md"
    eval_header_temaplate = """---
layout: page
title: Eval $eval_count
author: "$author_name"
tags: ["eval","gsoc","gsoc$gsoc_year","$project_tag","eval#$eval_count"]
---

## Summary
Evaluation Summary goes here  

## Objectives and Deliverables
| \# | Objectives                    | Associated Deliverables         |
| --- | ----------------------------- | ---------------------------------------------- |
| 1 | helo world  | hello world |
| 2 | helo world  | hello world |
| 3 | helo world  | hello world |
| 4 | helo world  | hello world |

## Learning and Success
Learning and Success goes here.

## Difficulties
Difficulty goes here.

## Plan update
Plan Update goes here.

"""
    file_content = Template(eval_header_temaplate).substitute(field_values)
    file_name = eval_file_name.format_map(field_values)
    with open(os.path.join(base_dir,file_name),"w") as f:
        f.write(file_content)
    # print(file_name)
    # print(file_content)

eval_index = 0
count = 0
for index in range(total_week_count+1):
    if(eval_index < len(eval_next_to_week_list) and index > eval_next_to_week_list[eval_index]):
        field_values = {
            "project_name": project_name,
            "author_name": author_name,
            "gsoc_year": gsoc_year,
            "project_tag": project_tag,
            "week_count": week_count,
            "eval_count": eval_count,
            "count": count
        }
        create_eval_file(field_values)
        count += 1
        eval_index += 1

    week_count = index
    eval_count = eval_index+1
    field_values = {
        "project_name": project_name,
        "author_name": author_name,
        "gsoc_year": gsoc_year,
        "project_tag": project_tag,
        "week_count": week_count,
        "eval_count": eval_count,
        "count": count
    }
    create_week_file(field_values)
    count += 1

if(eval_index < len(eval_next_to_week_list)):
    field_values = {
        "project_name": project_name,
        "author_name": author_name,
        "gsoc_year": gsoc_year,
        "project_tag": project_tag,
        "week_count": week_count,
        "eval_count": eval_count,
        "count": count
    }
    create_eval_file(field_values)
    count += 1
    eval_index += 1
