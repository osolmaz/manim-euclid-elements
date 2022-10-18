import os
import json
import argparse
import traceback
from manim import *
from proposition import generate_scene

LOW_QUALITY_DIR = "media/videos/480p15/"
HIGH_QUALITY_DIR = "media/videos/1080p60/"

parser = argparse.ArgumentParser(description="Process some integers.")
parser.add_argument(
    "propositions",
    metavar="N",
    type=str,
    nargs="*",
    help="Proposition ids, format: bookNo.propositionNo, e.g. 1.47",
)
parser.add_argument(
    "-l",
    "--low-quality",
    action="store_true",
    help="Render low quality",
)
parser.add_argument(
    "-s",
    "--skip-existing",
    action="store_true",
    help="Skip existing propositions",
)
parser.add_argument(
    "-i",
    "--ignore-errors",
    action="store_true",
    help="Ignore errors",
)
parser.add_argument(
    "-p",
    "--preview",
    action="store_true",
    help="Preview the scenes",
)
args = parser.parse_args()


config["disable_caching"] = True
if args.low_quality:
    config["quality"] = "low_quality"

books = [
    "elements-data/data/book-01.json",
    "elements-data/data/book-02.json",
    "elements-data/data/book-03.json",
    "elements-data/data/book-04.json",
    "elements-data/data/book-05.json",
    "elements-data/data/book-06.json",
    "elements-data/data/book-07.json",
    "elements-data/data/book-08.json",
    "elements-data/data/book-09.json",
    "elements-data/data/book-10.json",
    "elements-data/data/book-11.json",
    "elements-data/data/book-12.json",
    "elements-data/data/book-13.json",
]

# skipped_ids = ["3.25", "3.33", "3.35", "3.36"]
skipped_ids = []
all_propositions = {}

for path in books:
    book_dict = json.loads(open(path).read())
    basename = os.path.basename(path).split(".")[0]
    for prop_dict in book_dict:
        title = prop_dict["title"]
        prop_id = prop_dict["id"]
        if "Proposition" not in title or prop_id in skipped_ids:
            continue
        book_id = prop_id.split(".")[0]
        wildcard = book_id + ".*"
        if (
            args.propositions == []
            or prop_id in args.propositions
            or wildcard in args.propositions
        ):
            all_propositions[prop_id] = prop_dict

logfile = open("render.log", "a")
for id, prop_dict in all_propositions.items():
    title = prop_dict["title"]
    book_id, prop_id = [int(i) for i in prop_dict["id"].split(".")]
    name = "%02d-%03d" % (book_id, prop_id)
    print(">> Rendering %s into %s" % (id, name))

    scene = generate_scene(
        prop_dict,
        name=name,
    )

    if config["quality"] == "low_quality":
        path = LOW_QUALITY_DIR + name + ".mp4"
    else:
        path = HIGH_QUALITY_DIR + name + ".mp4"

    if not os.path.exists(path) or not args.skip_existing:
        if args.ignore_errors:
            try:
                s = scene()
                s.render(preview=args.preview)
            except KeyboardInterrupt:
                quit()
            except:
                logfile.write("#### Failed " + name + "\n")
                traceback.print_exc(file=logfile)
                traceback.print_exc()
                logfile.write("\n\n")
                logfile.flush()
        else:
            s = scene()
            s.render(preview=args.preview)
    else:
        print(">> Skipping render")
    config["output_file"] = None

