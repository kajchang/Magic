from st4ck.graphing import graph_sankey, graph_line, graph_pie, graph_bar
from st4ck.analysis import analyze
import sys
import argparse
import json


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser()

    parser.add_argument('-f', help='file', required=True)
    parser.add_argument('-sankey', help='graph a sankey chart', required=False, action='store_true')
    parser.add_argument('-line', help='graph a line chart', required=False, action='store_true')
    parser.add_argument('-pie', help='graph a pie chart', required=False, action='store_true')
    parser.add_argument('-bar', help='graph a bar chart', required=False, action='store_true')
    parser.add_argument('-n', help='number of accounts', type=int, default=1)
    parser.add_argument('-id', help='name/id of account to start on', required=False)
    parser.add_argument('-v', help='verbosity', required=False, action='store_true')

    args = parser.parse_args(args)

    file_name = args.f if args.f.endswith('.json') else '{}.json'.format(args.f)

    if not args.sankey and not args.line and not args.pie and not args.bar:
        try:
            with open(file_name) as file_:
                file_data = json.load(file_) # Try loading data already in file_

        except OSError:
            with open(file_name, "w") as file_:  # Create file_ if doesn't exist
                file_data = []
                file_.write(json.dumps(file_data))

        if args.id:
            if args.v:
                file_data.append(analyze(id_=args.id, verbose=True))

            else:
                file_data.append(analyze(id_=args.id))

        else:
            for x in range(args.n):
                if args.v:
                    file_data.append(analyze(verbose=True))

                else:
                    file_data.append(analyze())

        with open(file_name, "w") as file_:
            file_.write(json.dumps(file_data))

    elif args.sankey:
        with open(file_name) as file_:
            graph_sankey(json.load(file_))

    elif args.line:        
        with open(file_name) as file_:
            graph_line(json.load(file_))

    elif args.pie:        
        with open(file_name) as file_:
            graph_pie(json.load(file_))
    elif args.bar:
        with open(file_name) as file_:
            graph_bar(json.load(file_))


if __name__ == '__main__':
    main()
