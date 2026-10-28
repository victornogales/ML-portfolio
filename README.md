# ML Portfolio

Classic machine learning algorithms implemented from scratch, mostly in Python with NumPy.

| Folder | What it covers | Language |
|---|---|---|
| [Linear-Regression](Linear-Regression) | Linear regression with gradient descent | C++ |
| [Logistic-Regression](Logistic-Regression) | Logistic regression for classification | Python |
| [Binary-Classification](Binary-Classification) | A small neural network for binary classification | Python |
| [Decision-Trees](Decision-Trees) | Decision trees using entropy and information gain | Python |
| [K-Means](K-Means) | K-means clustering | Python |
| [Gaussian-Model](Gaussian-Model) | Anomaly detection with a Gaussian model | Python |
| [Collaborative-Filtering](Collaborative-Filtering) | Movie recommendations with collaborative filtering | Python |

## Other projects

| Folder | What it covers | Language |
|---|---|---|
| [Decode-Message](Decode-Message) | Reads an encoded message from a text file and decodes it | C++ |
| [KCC.com](KCC.com) | A small static website | HTML |

Each folder was originally its own repository and keeps its commit history.

## Running

Python projects: from inside a project's folder, run its main script, for example:

```
cd K-Means
python k-means.py
```

They mainly use `numpy` and `matplotlib`. Some also need `pandas`, `scikit-learn`, `tensorflow`, `networkx` or `pillow`.

Linear-Regression is built with CMake:

```
cd Linear-Regression
cmake -B build
cmake --build build
```
