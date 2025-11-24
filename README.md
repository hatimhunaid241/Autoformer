# Autoformer (NeurIPS 2021)

Autoformer: Decomposition Transformers with Auto-Correlation for Long-Term Series Forecasting

Time series forecasting is a critical demand for real applications. Enlighted by the classic time series analysis and stochastic process theory, we propose the Autoformer as a general series forecasting model [[paper](https://arxiv.org/abs/2106.13008)]. **Autoformer goes beyond the Transformer family and achieves the series-wise connection for the first time.**

In long-term forecasting, Autoformer achieves SOTA, with a **38% relative improvement** on six benchmarks, covering five practical applications: **energy, traffic, economics, weather and disease**.

:triangular_flag_on_post:**News** (2023.08) Autoformer has been included in [Hugging Face](https://huggingface.co/models?search=autoformer). See [blog](https://huggingface.co/blog/autoformer).

:triangular_flag_on_post:**News** (2023.06) The extension version of Autoformer ([Interpretable weather forecasting for worldwide stations with a unified deep model](https://www.nature.com/articles/s42256-023-00667-9)) has been published in Nature Machine Intelligence as the [Cover Article](https://www.nature.com/natmachintell/volumes/5/issues/6).

:triangular_flag_on_post:**News** (2023.02) Autoformer has been included in our [[Time-Series-Library]](https://github.com/thuml/Time-Series-Library), which covers long- and short-term forecasting, imputation, anomaly detection, and classification.

:triangular_flag_on_post:**News** (2022.02-2022.03) Autoformer has been deployed in [2022 Winter Olympics](https://en.wikipedia.org/wiki/2022_Winter_Olympics) to provide weather forecasting for competition venues, including wind speed and temperature.

## Autoformer vs. Transformers

**1. Deep decomposition architecture**

We renovate the Transformer as a deep decomposition architecture, which can progressively decompose the trend and seasonal components during the forecasting process.

<p align="center">
<img src=".\pic\Autoformer.png" height = "250" alt="" align=center />
<br><br>
<b>Figure 1.</b> Overall architecture of Autoformer.
</p>

**2. Series-wise Auto-Correlation mechanism**

Inspired by the stochastic process theory, we design the Auto-Correlation mechanism, which can discover period-based dependencies and aggregate the information at the series level. This empowers the model with inherent log-linear complexity. This series-wise connection contrasts clearly from the previous self-attention family.

<p align="center">
<img src=".\pic\Auto-Correlation.png" height = "250" alt="" align=center />
<br><br>
<b>Figure 2.</b> Auto-Correlation mechansim.
</p>


## Project Context & Reproducibility

**This repository is a fork of the official Autoformer codebase.** Our work focuses on reproducing the main results and figures from the NeurIPS 2021 paper, with an emphasis on clear reproducibility, documentation, and critical analysis for the COMP3314 course project.

### What We Did
- Reproduced key experiments and results from the paper using the provided scripts and datasets.
- Added/modified scripts for easier experiment management and reproducibility (see `scripts/` and `utils/`).
- Documented the setup, training, and evaluation process in detail.
- Analyzed discrepancies between our results and those reported in the paper.
- Provided critical insights and suggestions for further improvement.

### Setup Instructions
1. **Clone the repository**
2. **Install dependencies**
  - Using Conda: `conda env create -f environment.yml && conda activate autoformer`
  - Or using pip: `pip install -r requirements.txt`
3. **Download datasets**
  - Run: `make get_dataset` or use the provided scripts in `utils/`.
4. **Run Experiments**
  - Example: `bash scripts/ETT_script/Autoformer_ETTm1.sh`
  - See `scripts/` for all available experiment scripts.
  - You can also run all experiments using `bash script_all.sh`.

### Results
- We successfully reproduced the main results for [list datasets/benchmarks].
- See the `results/` and `test_results/` folders for output files, metrics, and plots.
- When starting from scratch, you will have to run the scripts to generate the results.
- For a detailed comparison with the original paper, see the report in `report/`.

### Troubleshooting
- If you encounter CUDA or dependency issues, check your PyTorch and CUDA versions.
- For dataset download issues, verify your internet connection or use the direct Google Drive links in the README.

### Contributions
- [List your team members and their contributions.]
- [Highlight any new scripts, bug fixes, or improvements you made.]

### License
This project inherits the license of the original Autoformer repository.

---
For more details, see the full report in the `report/` folder.

## Main Results

We experiment on six benchmarks, covering five main-stream applications. We compare our model with ten baselines, including Informer, N-BEATS, etc. Generally, for the long-term forecasting setting, Autoformer achieves SOTA, with a **38% relative improvement** over previous baselines.

<p align="center">
<img src=".\pic\results.png" height = "550" alt="" align=center />
</p>

## Baselines

We will keep adding series forecasting models to expand this repo:

- [x] Autoformer
- [x] Informer
- [x] Transformer
- [x] Reformer
- [ ] LogTrans
- [ ] N-BEATS

## Citation

If you find this repo useful, please cite our paper. 

```
@inproceedings{wu2021autoformer,
  title={Autoformer: Decomposition Transformers with {Auto-Correlation} for Long-Term Series Forecasting},
  author={Haixu Wu and Jiehui Xu and Jianmin Wang and Mingsheng Long},
  booktitle={Advances in Neural Information Processing Systems},
  year={2021}
}
```

## Contact

If you have any questions or want to use the code, please contact wuhx23@mails.tsinghua.edu.cn.

## Acknowledgement

We appreciate the following github repos a lot for their valuable code base or datasets:

https://github.com/zhouhaoyi/Informer2020

https://github.com/zhouhaoyi/ETDataset

https://github.com/laiguokun/multivariate-time-series-data

