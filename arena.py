import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import threading
import random

RUN = True

class Run:
    def __init__(self):
        self.run = True
    def stop(self):
        self.run = False
    def start(self):
        self.run = True

def generate_report(bf1, bf2, num, name=None, win_loss_color=False):
    """generates a report saved to name for num batles between bf1 and bf2"""
    dfs, a = multiple_fights(bf1, bf2, num)
    render_report(dfs, a, win_loss_color=win_loss_color, save_name=name)
    
def run_battles(bfs, batch=1, num_threads=1, total=None):
    """continuously runs battles randomly between BFs in bfs, each BF facing off random in batch size battles"""
    global RUN
    RUN = True
    bfs_in_use = list(map(lambda x: 0, bfs))
    # run = [True]
    threads = []
    lock = threading.Lock()
    for _ in range(num_threads):
        t = threading.Thread(target=run_battle_thread, args=(bfs, bfs_in_use, batch, lock))
        threads.append(t)
    threads.append(threading.Thread(target=stopping_thread))
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    
def run_battle_thread(bfs, bfs_in_use, batch, lock):
    """continuously runs battles, updating which bfs are in use and freeing them"""
    while RUN:
        lock.acquire()
        bf1, bf2, i, j = find_unused_bfs_and_use(bfs, bfs_in_use)
        lock.release()
        for _ in range(batch):
            fight_battleflies(bf1, bf2, False)
        return_bfs(bfs_in_use, i, j)
        
def stopping_thread():
    """input to stop threads"""
    global RUN
    input("Press enter to stop battles")
    RUN = False
    
def find_unused_bfs_and_use(bfs, bfs_in_use):
    l = len(bfs_in_use)-1
    i, j = random.randint(0, l), random.randint(0, l)
    while i == j or bfs_in_use[i] == 1 or bfs_in_use[j] == 1:
        i, j = random.randint(0, l), random.randint(0, l)
    bfs_in_use[i] = 1
    bfs_in_use[j] = 1
    return bfs[i], bfs[j], i, j
    
def return_bfs(bfs_in_use, i, j):
    bfs_in_use[i] = 0
    bfs_in_use[j] = 0
    
    
    
def fight_battleflies(bf1, bf2, detailed=False):
    status={"shield1":[bf1.shield], 
            "hull1":[bf1.hull], 
            "shield2":[bf2.shield], 
            "hull2":[bf2.hull], 
            "time":[0]}
    about = {"bf1":bf1.get_name(), "bf2":bf2.get_name()}
    bf1.aim_at_enemy(bf2)
    bf2.aim_at_enemy(bf1)
    while bf1.hull>0 and bf2.hull>0:
        
        wait = min(bf1.reloading_for(), bf2.reloading_for())
        bf1.fast_forward_utilities(wait)
        bf2.fast_forward_utilities(wait)
        bf1.fast_forward_weapons(wait)
        bf2.fast_forward_weapons(wait)
        if detailed:
            status["shield1"].append(bf1.shield)
            status["hull1"].append(bf1.hull)
            status["shield2"].append(bf2.shield)
            status["hull2"].append(bf2.hull)
            status["time"].append(status["time"][-1]+wait)
    if bf1.hull > 0:
        bf1.won_battle()
        bf2.lost_battle()
    else:
        bf2.won_battle()
        bf1.lost_battle()
    bf1.reset_stats()
    bf2.reset_stats()
    if detailed: return status, about

def multiple_fights(bf1, bf2, num):
    report = []
    for _ in range(num):
        s, a = fight_battleflies(bf1, bf2, True)
        report.append(s)
        
    report = list(map(lambda x: turn_report_into_df(x), report))
    return report, a

def turn_report_into_df(s):
    df = pd.DataFrame(s)
    df = df/1e3
    df = df.set_index(["time"])

    df[df < 0] = None
    df = df.fillna(value=0, limit=1)
    df.shield1 += df.hull1.iloc[0]
    df.shield2 += df.hull2.iloc[0]
    return df


def render_report(dfs, a, win_loss_color=False, save_name=None):
    fig, ax = plt.subplots(figsize=(10, 6), nrows=2)
    fig.tight_layout()

    ax[0].set_title(a["bf1"])
    ax[0].set_ylabel("shield + hull")
    for df in dfs:
        if win_loss_color:
            ax[0].plot(df.shield1, c="#ff7154" if df.hull1.iloc[-1]==0 else "#54ff62", alpha=1/(len(dfs)**0.5))
            ax[0].plot(df.hull1, c="#ff7154" if df.hull1.iloc[-1]==0 else "#54ff62", alpha=1/(len(dfs)**0.5))
        else:
            ax[0].plot(df.shield1, c="#54c3ff", alpha=1/(len(dfs)**0.5))
            ax[0].plot(df.hull1, c="#ffbb54", alpha=1/(len(dfs)**0.5))

    ax[0].axes.get_xaxis().set_visible(False)

    ax[1].set_title(a["bf2"])
    ax[1].set_ylabel("shield + hull")
    for df in dfs:

        if win_loss_color:
            ax[1].plot(df.shield2, c="#54ff62" if df.hull1.iloc[-1]==0 else "#ff7154", alpha=1/(len(dfs)**0.5))
            ax[1].plot(df.hull2, c="#54ff62" if df.hull1.iloc[-1]==0 else "#ff7154", alpha=1/(len(dfs)**0.5))
        else:
            ax[1].plot(df.shield2, c="#54c3ff", alpha=1/(len(dfs)**0.5))
            ax[1].plot(df.hull2, c="#ffbb54", alpha=1/(len(dfs)**0.5))
    ax[1].set_xlabel("seconds")

    ax[0].set_ylim(bottom=0)
    ax[1].set_ylim(bottom=0)

    if save_name: fig.savefig(f"{save_name}.png")