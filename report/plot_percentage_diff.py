import matplotlib.pyplot as plt
import numpy as np

# Original results from screenshot (benchmark: {pred_len: (MSE, MAE)})
original_results = {
    'ECL_96_96':    (0.201, 0.317),
    'ECL_96_192':   (0.222, 0.334),
    'ECL_96_336':   (0.231, 0.338),
    'ECL_96_720':   (0.254, 0.361),
    'ETTm2_96_96':  (0.255, 0.339),
    'ETTm2_96_192': (0.281, 0.340),
    'ETTm2_96_336': (0.339, 0.372),
    'ETTm2_96_720': (0.422, 0.419),
    'Exchange_96_96':  (0.197, 0.323),
    'Exchange_96_192': (0.300, 0.369),
    'Exchange_96_336': (0.509, 0.524),
    'Exchange_96_720': (1.447, 0.941),
    'traffic_96_96':   (0.613, 0.388),
    'traffic_96_192':  (0.616, 0.382),
    'traffic_96_336':  (0.622, 0.337),
    'traffic_96_720':  (0.660, 0.408),
    'weather_96_96':   (0.266, 0.336),
    'weather_96_192':  (0.307, 0.367),
    'weather_96_336':  (0.359, 0.395),
    'weather_96_720':  (0.419, 0.428),
    'ili_36_24':   (3.483, 1.287),
    'ili_36_36':   (3.103, 1.148),
    'ili_36_48':   (2.669, 1.085),
    'ili_36_60':   (2.770, 1.125),
}

# Reproduced results (benchmark: (MSE, MAE))
reproduced_results = {
    'ECL_96_96':    (0.2002, 0.3141),
    'ECL_96_192':   (0.2155, 0.3285),
    'ECL_96_336':   (0.2593, 0.3590),
    'ECL_96_720':   (0.2563, 0.3597),
    'ETTm2_96_96':  (0.2534, 0.3264),
    'ETTm2_96_192': (0.2853, 0.3397),
    'ETTm2_96_336': (0.3307, 0.3670),
    'ETTm2_96_720': (0.4158, 0.4132),
    'Exchange_96_96':  (0.1429, 0.2785),
    'Exchange_96_192': (0.2801, 0.3888),
    'Exchange_96_336': (0.4682, 0.5075),
    'Exchange_96_720': (1.3707, 0.8907),
    'traffic_96_96':   (0.6301, 0.4003),
    'traffic_96_192':  (0.6672, 0.4181),
    'traffic_96_336':  (0.6048, 0.3733),
    'traffic_96_720':  (0.6632, 0.4101),
    'weather_96_96':   (0.2694, 0.3345),
    'weather_96_192':  (0.3340, 0.3923),
    'weather_96_336':  (0.3850, 0.4138),
    'weather_96_720':  (0.4252, 0.4312),
    'ili_36_24':   (3.2578, 1.2717),
    'ili_36_36':   (3.2316, 1.2217),
    'ili_36_48':   (3.4828, 1.2873),
    'ili_36_60':   (2.8600, 1.1286),
}

# Sort keys for consistent plotting
benchmarks = list(original_results.keys())

mae_perc_diff = []
mse_perc_diff = []
labels = []

for bench in benchmarks:
    orig_mse, orig_mae = original_results[bench]
    rep_mse, rep_mae = reproduced_results[bench]
    # Percentage diff: (reproduced - original) / original * 100
    mae_diff = (rep_mae - orig_mae) / orig_mae * 100
    mse_diff = (rep_mse - orig_mse) / orig_mse * 100
    mae_perc_diff.append(mae_diff)
    mse_perc_diff.append(mse_diff)
    # Label: e.g. ECL 96_96
    # if bench.startswith('ili'):
    #     label = 'ILI ' + bench.split('_')[2]
    # else:
    ds, pred = bench.split('_', 1)
    label = ds + ' ' + pred
    labels.append(label)

x = np.arange(len(labels))  # label locations
width = 0.35  # width of the bars

fig, ax = plt.subplots(figsize=(10, 4.5))  # Wider figure
rects1 = ax.bar(x - width/2, mae_perc_diff, width, label='MAE (%diff)')
rects2 = ax.bar(x + width/2, mse_perc_diff, width, label='MSE (%diff)')

# Add labels, title, legend
ax.set_ylabel('Percentage Difference (%)')
ax.set_xlabel('Benchmark')
ax.set_title('Percentage Difference between Original and Reproduced Results')
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=60, ha='right')
ax.legend()
ax.margins(x=0.01)
ax.tick_params(axis='x', labelsize=10)
ax.set_ylim(-50, 50)

# Annotate bars using bar_label for automatic placement, vertical and outside
ax.bar_label(rects1, fmt='%.1f%%', padding=1, fontsize=7, rotation=90, label_type='edge')
ax.bar_label(rects2, fmt='%.1f%%', padding=1, fontsize=7, rotation=90, label_type='edge')

fig.tight_layout()
plt.show()
