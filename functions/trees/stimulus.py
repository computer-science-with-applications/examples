import sys
import os.path
from tree import Tree


def insert_levels(t, levels, v):
    if len(levels) == 1:
        t.add_child( Tree(levels[0], v) )
    else:
        level = levels[0]
        newlevels = levels[1:]

        st = [c for c in t.children if c.key == level]

        assert len(st) in (0,1)

        if len(st) == 0:
            st = Tree(level, 0)
            t.add_child(st)
        else:
            st = st[0]

        insert_levels(st, newlevels, v)


def aggregate_stimulus_values(t):
    if t.num_children == 0:
        # We've reached a leaf node. The value of the
        # node will be the cost of a project
        return t.value

    total_cost = 0
    for st in t.children:
        total_cost += aggregate_stimulus_values(st)

    t.value = total_cost

    return total_cost

    
def print_stimulus_tree(t, maxdepth = None):
    t.print(vformat="${:,}", maxdepth = maxdepth)


def read_stimulus_line(line):
    fields = line.split(";")
    city = fields[0]
    state = fields[1]
    description = fields[2]
    jobs = int(fields[3])
    cost = int(fields[4])
    program = fields[5]

    return city, state, description, jobs, cost, program


def read_stimulus_file(fname):
    if not os.path.exists(fname):
        return None

    t = Tree("US", 0)

    with open(fname, encoding='latin-1') as f:
        for line in f:
            city, state, description, jobs, cost, program = read_stimulus_line(line)
    
            levels = (state, city, program, description)
    
            insert_levels(t, levels, cost)

    return t
    

if __name__ == "__main__":
    if(len(sys.argv) != 2):
        print("Usage: python stimulus.py STIMULUS_FILE")
        sys.exit(1)

    sfile = sys.argv[1]

    if not os.path.exists(sfile):
        print("Error: %s does not exist")
        sys.exit(1)    

    t = read_stimulus_file(sfile)

    aggregate_stimulus_values(t)

    print_stimulus_tree(t)


