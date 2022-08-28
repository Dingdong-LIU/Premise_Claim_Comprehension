import os, json

## Calculate and count in big Json file


def percentage_and_count(base_dir):
    stance_proportion_path = os.path.join(base_dir, 'stance_proportion.json')
    with open(stance_proportion_path, 'r') as f:
        stance_proportion = json.load(f)
    output = {
        "percentage": {},
        "count": stance_proportion,
    }
    claims_count = sum(stance_proportion.values())
    output["percentage"] = {
        k: "{:.0%}".format(v/claims_count) for k, v in stance_proportion.items()
    }
    return output


def create_claim_center_dict(base_dir):
    stance_count_path = os.path.join(base_dir, 'stance_count.json')
    supportiveness_path = os.path.join(base_dir, 'supportiveness.json')

    with open(stance_count_path, 'r') as f:
        stance_count = json.load(f)
    cs_to_st = {j: k for k, v in stance_count.items() for j in v}
    with open(supportiveness_path, 'r') as f:
        supportiveness = json.load(f)

    output = {"positive": [], "neutral": [], "negative": []}
    for t in supportiveness:
        st = cs_to_st[t['text']]
        output[st].append(t)
    return output

def related_questions(base_dir, task_name):
    data_file_path = os.path.join(base_dir, f"{task_name}-upvotes.json")
    with open(data_file_path, 'r') as f:
        data_file = json.load(f)
    rq = data_file["relatedQuestions"]
    return rq

def get_answers(base_dir, task_name):
    answer_data_path = os.path.join(base_dir, f"{task_name}-aligned.json")
    with open(answer_data_path, 'r') as f:
        answer_data = json.load(f)['answers']
    original_urlEncode = [x['content'] for x in answer_data]

    upvotes_data_path = os.path.join("../upvotes", f"{task_name}-upvotes.json")
    with open(upvotes_data_path, 'r') as f:
        upvotes_data = json.load(f)['answers']
        upvotes_data = [x for x in upvotes_data if x is not None]
    upvotes_urlEncode = [x['content'] for x in upvotes_data]

    for i, ec in enumerate(original_urlEncode):
        up_i = upvotes_urlEncode.index(ec)
        upvotes = upvotes_data[up_i]["upvotes"]
        answer_data[i]["upvotes"] = upvotes
    
    return answer_data
