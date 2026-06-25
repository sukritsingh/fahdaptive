import mdtraj as md
import os
from glob import glob
import multiprocessing
from tqdm import tqdm
import numpy as np
from time import gmtime, strftime, sleep
from matplotlib import pyplot as plt
from seaborn import palplot, color_palette


n_procs = 12
working_dir = "seeds_pdb"
# working_dir = "old-min-count-seeds_pdb"
output_dir = "/home/sukrit/lilac/data/sampling-test/fast-fah/seed-process/interactive-test/tracking-seed-dfg"

def compute_seed_dfg_dist(strucs):
    struc_d1 = []              
    struc_d2 = []                                                              
    for i,s in enumerate(strucs):                                               
        struc_d1.append(md.compute_distances(s, [[2464, 947]]))                                                                                            
        struc_d2.append(md.compute_distances(s, [[2464, 641]]))                                                                                            
    struc_d1 = np.concatenate(struc_d1)                                        
    struc_d2 = np.concatenate(struc_d2)                                        
    struc_d1 = np.concatenate(struc_d1)                                        
    struc_d2 = np.concatenate(struc_d2)

    return struc_d1, struc_d2

def save_dfg_dist_plot(d1, d2, output_dir):
    plt.clf()
    t = np.arange(len(d1))
    cmap_name = color_palette("magma", as_cmap=True)
    plt.scatter(d1, d2, c=t, s=10, cmap="jet")
    plt.colorbar(label="seed order")
    plt.xlabel("DFG d1 (nm)", fontsize=15)
    plt.ylabel("DFG d2 (nm)", fontsize=15)
    plt.xlim(0.3, 2.0)
    plt.ylim(0.3, 2.0)
    current_time = strftime("%Y-%m-%d-%H:%M:%S", gmtime())
    plt.savefig("%s/dfg-scatter-%s.png" % (output_dir,current_time), dpi=300)


def main(seed_dir, output_dir):
    print("It's time to plot")
    fns = sorted(glob("%s/*.pdb" % working_dir), key=os.path.getmtime)
    # struc = [md.load(i) for i in fns]
    # struc = pool.map(load_single_struc, fns)
    struc = list(tqdm(pool.imap(md.load, fns), total=len(fns)))
    d1, d2 = compute_seed_dfg_dist(struc)
    print("computed distances")
    save_dfg_dist_plot(d1, d2, output_dir)
    print("Plot made")
    all_seeds = md.join(struc)
    stripped_seeds = all_seeds.remove_solvent()
    current_time = strftime("%Y-%m-%d-%H:%M:%S", gmtime())
    stripped_seeds[0].save_pdb("%s/seed-start-noSolv.pdb" % output_dir)
    stripped_seeds.save_xtc("%s/all-seeds-noSolv-%s.xtc" % (output_dir, current_time))
    print("Done")
    print("Now I sleep")
    sleep(3600)

if __name__ == "__main__":
    pool = multiprocessing.Pool(n_procs)
    while True:
        main(working_dir, output_dir)
