import matplotlib.pyplot as plt
import numpy as np


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


def render_report(win_loss_color=False, save_name=None):
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