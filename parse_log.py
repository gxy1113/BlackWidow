import os
import sys
import json
form_url = []
form_html_url = []
url_log = "data/url_log.txt"
html_url_log = "data/html_url_log.txt"
event_edge = "event_edge.txt"
appname = sys.argv[1]

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
                line_str = line_str.replace("\'", "\"")
                line_dict = json.loads(line_str)
                log.append(line_dict)
        f.close()
    return log


form_url = read_log(url_log)
form_html_url = read_log(html_url_log)
success_forms = {"html": form_html_url, "url": form_url}
event_dict = read_and_convert("data/" + event_edge)
json_object = json.dumps(success_forms, indent=4)
write_file("data/", "event_edge.json", event_dict)
with open("data/" + appname + ".json", "w") as outfile:
    outfile.write(json_object)