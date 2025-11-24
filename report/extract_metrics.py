import os
import numpy as np

# Paths to results and test_results folders
folders = [
    os.path.join('..', 'new_results'),
    os.path.join('..', 'new_test_results')
]

for folder in folders:
    if not os.path.exists(folder):
        continue
    for subdir in os.listdir(folder):
        subpath = os.path.join(folder, subdir)
        metrics_path = os.path.join(subpath, 'metrics.npy')
        if ('ETTm1' in metrics_path): continue
        if os.path.isfile(metrics_path):
            metrics = np.load(metrics_path)
            print(f"{metrics_path}:")
            print(f"  MAE:   {metrics[0]:.4f}")
            print(f"  MSE:   {metrics[1]:.4f}")
