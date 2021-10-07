import glob, os

basepath = os.path.dirname(__file__)

def latest_txt_pathfinder(path):
    if(path==""):
        path=basepath
    files = glob.glob(path+"/output*.txt") # * means all if need specific format then *.csv
    paths = [os.path.join(path, basename) for basename in files]
    return max(paths, key=os.path.getmtime)
