import os
import sys
import json
form_url = []
form_html_url = []
url_log = "data/url_log.txt"
html_url_log = "data/html_url_log.txt"
all_form_log = "data/all_forms.txt"
event_edge = "event_edge.txt"
appname = sys.argv[1]
mode = sys.argv[2]

def load_file(folder, name):
    try:
        with open(folder + 'a_' + name, 'r') as f:
            data = json.load(f)
        return data
    except:
        return False
    
def write_file(folder, name, data):
    try:
        with open(folder + 'a_' + name, 'w') as f:
            json.dump(data, f, indent=4)
    except:
        print("failed to write to file")
        return False

def read_log(path=""):
    log = []
    if os.path.exists(path):
        with open(path) as f:
            for line in f:
                line_str = line.strip()
                if "xss" in line_str:
                    continue
                if "jaekpot" in line_str:
                    continue
                line_str = parse_url(line_str)
                result = 0
                for item in log:
                    if item == line_str:
                        result = 1
                        break
                if result == 0:
                    log.append(line_str)
        f.close()
    return log

def read_and_convert(path=""):
    log = []
    if os.path.exists(path):
        with open(path) as f:
            for line in f:
                line_str = line.strip()
                line_str = line_str.replace("\"", "\\\"")
                line_str = line_str.replace("\'", "\"")
                try:
                    line_dict = json.loads(line_str)
                    log.append(line_dict)
                except Exception as e:
                    print(e)
                    print(line_str)
        f.close()
    return log

def remove_milisecond(start_time=""):
    start_time = start_time.split('.')[0]
    return int(start_time)

def parse_edge(event_edge = {}):
    event_edge["start_time"] = remove_milisecond(event_edge["start_time"])
    event_edge["end_time"] = remove_milisecond(event_edge["end_time"])
    event_edge['interval'] = event_edge["end_time"] - event_edge["start_time"]
    event_edge["new_eles"] = int(event_edge["new_eles"])
    return event_edge

def collect_data(event_list = list()):
    cnt = 0
    cumulated_time = 0
    for event_edge in event_list:
        if event_edge["new_eles"] == 0:
            cnt = cnt + 1
            cumulated_time = cumulated_time + event_edge["interval"]
    return[len(event_list), cnt, cumulated_time / 60]

def parse_url(url=""):
    url = url.replace("http://", "")
    url_components = url.split("/")
    for component in url_components:
        if component.isnumeric():
            component = "1"
    url = "http://" + '/'.join(url_components)
    return url


if __name__ == '__main__':
    form_url = read_log(url_log)
    form_html_url = read_log(html_url_log)
    all_form = read_log(all_form_log)
    success_forms = {"html": form_html_url, "url": form_url}
    event_dict = read_and_convert("data/" + event_edge)
    event_list = list()
    for event_edge in event_dict:
        event_edge = parse_edge(event_edge)
    json_object = json.dumps(success_forms, indent=4)
    result = collect_data(event_dict)
    print(result)
    write_file("data/", "event_edge.json", event_dict)
    write_file("data/", "all_form.json", all_form)
    success_forms = success_forms[mode]
    failed_forms = list()
    for url in all_form:
        if url in success_forms:
            continue
        failed_forms.append(url)
    classified_forms = {"success": success_forms, "failed": failed_forms}
    write_file("data/", "classified_form.json", classified_forms)
    with open("data/" + appname + ".json", "w") as outfile:
        outfile.write(json_object)
    