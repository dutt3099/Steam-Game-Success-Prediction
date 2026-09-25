# Steam Game Success Prediction

This project studies whether Steam game metadata and text information can be used to predict game success.

The main experimental notebook is:

`stm_research_questions.ipynb`

## Research Questions

**RQ1 — Can pre-launch metadata predict commercial success?**

**RQ2 — Does BERT text improve over metadata-only baselines?**

**RQ3 — Which features are most predictive? Do they differ by genre?**

## Dataset

The dataset is not included in this repository because of its size.
Download it from Kaggle:

[Game Recommendations on Steam — Kaggle](https://www.kaggle.com/datasets/antonkozyriev/game-recommendations-on-steam/data)

After downloading, place the required dataset files in the `Dataset/` folder.

## Project Structure

```text
stm/
├── Dataset/                  # Dataset files
├── model/                    # Saved models and embeddings
├── opt/                      # Results, tables and plots
├── README.md                 # Project documentation
├── setup_steam_env.py        # Creates/checks the project environment
├── steam_env/                # Project virtual environment
└── stm_research_questions.ipynb
```

## First Step: Set Up the Environment

Run this before starting the notebook or pipeline.

Open a terminal in the main `stm` folder and run:

```bash
python setup_steam_env.py
```

The script checks whether `steam_env` exists.

- If it exists, it is used.
- If it is missing, the script creates it.

Activate the environment after it has been created.

### macOS / Linux

```bash
source steam_env/bin/activate
```

### Windows

```bat
steam_env\Scripts\activate
```

## Run the Notebook

From the main `stm` folder, start Jupyter:

```bash
jupyter notebook
```

Then open:

`stm_research_questions.ipynb`

Run the notebook cells in order, starting with **00). Dependencies Check**.

> Run the notebook from the main `stm` folder so that the `Dataset`, `model`, and `opt` paths are found correctly.

## What the Notebook Does

The notebook follows this workflow:

1. Check dependencies and the Python environment.
2. Load and inspect the Steam data.
3. Create the features used for prediction.
4. Split the data into training, validation and test sets.
5. Train metadata-only baseline models.
6. Train a tabular neural-network model.
7. Train BERT-based text models using descriptions and tags.
8. Combine metadata and text in a fusion model.
9. Analyse feature importance and genre-specific results.
10. Run an ablation study and evaluate the final models.

## Success Definition and Evaluation

A game is classified as **successful** when its positive-review ratio is **70% or higher**.

The data is split into:

- **70%** training
- **15%** validation
- **15%** test

A fixed random seed of **42** is used.

The main evaluation metric is **Macro-F1**.

## Models Used

The notebook includes:

- Logistic Regression
- Random Forest
- LightGBM
- XGBoost
- Tabular MLP
- BERT-only models
- Fusion Model combining tabular features and DistilBERT text representations

The text model uses **`distilbert-base-uncased`**.

## Main Outputs

The project stores generated files in:

`model/` — trained models, embeddings and saved model data

`opt/` — feature-importance plots, genre results and result summaries

## Computational Environment

The notebook uses Python and Jupyter together with libraries including NumPy, Pandas, scikit-learn, LightGBM, XGBoost, PyTorch, Transformers, Matplotlib, Seaborn, SHAP, tqdm and Joblib.

On Apple Silicon Macs, PyTorch uses **MPS** when it is available; otherwise the notebook uses CPU.

## Reproducibility

Keep the project structure unchanged and run the notebook from the main `stm` folder. The configuration used by the notebook contains the data paths, success threshold, split sizes, random seed, model settings and training parameters.

Right now it is optimised to run on Apple MacBook Pro M2 with 8Gb of RAM, which means it checks for MPS (Metal Performance Shaders, Apple’s framework for GPU-accelerated computing on MacBooks with Apple Silicon (M1, M2, M3)). Running it on Windows/ Linux may require extra setup to run it properly.
