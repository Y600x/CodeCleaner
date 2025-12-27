import json
from ui.console import info

def generate_report(path, stats):
    data={
        "files":stats.files,
        "comments":stats.comments,
        "blanks":stats.blank
    }
    if path.endswith(".json"):
        with open(path,"w") as f: json.dump(data,f,indent=2)
    else:
        with open(path,"w") as f:
            for k,v in data.items(): f.write(f"{k}:{v}\n")
    info("Report generated")
