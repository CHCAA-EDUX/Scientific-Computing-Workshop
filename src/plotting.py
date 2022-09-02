import os
import argparse
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def save_plot(inpath, outpath):
    # load data
    dataframe = pd.read_csv(inpath)
    # get x,y
    x = dataframe["Height"]
    y = dataframe["Weight"]
    # linear regression using scipy
    stats = linregress(x, y)
    # get slope and intercept
    m = stats.slope
    b = stats.intercept
    # scatter plot
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    # add regression line
    ax.plot(x, m * x + b, color="red")   # I've added a color argument here
    # Save figure
    fig.savefig(outpath)

    return None

def load_args():
    # Create the parser
    parser = argparse.ArgumentParser()# Add an argument
    # input and output arguments
    parser.add_argument('--inpath', "-i", type=str, required=True)
    parser.add_argument('--outpath', "-o", type=str, required=True)
    # Parse the argument
    args = parser.parse_args()

    return args

def main():
    # load args
    args = load_args()
    # get inpath
    inpath = os.path.join("data", args.inpath)
    # get outpath
    outpath = os.path.join(args.outpath)
    # save plot
    save_plot(inpath, outpath)
    
    return None

if __name__ == "__main__":
    main()