# open-sir

Open-SIR is an Open Source Python project for modelling pandemics and infectious diseases using Compartmental Models, such as the widely used [Susceptible-Infected-Removed (SIR) model](http://rocs.hu-berlin.de/corona/docs/forecast/model/#classic-sir-dynamics). 

The current stage of the software is *Alpha*.

## Features
- Model the dynamics of infectious diseases
- Parameter fitting
- Calculation of confidence intervals
- CLI for interfacing with non Python environments (Bash, Node.JS, Matlab, etc).

So far, Open-SIR provides an implementation of the SIR model and the recently new SIR based model SIR-X, developed by the [Robert Koch Institut](http://rocs.hu-berlin.de/corona/docs/forecast/model/#sir-x-dynamics-outbreaks-with-temporally-increasing-interventions).

## Getting Started

Open-SIR uses [Pipenv](https://pipenv.pypa.io/en/latest/) to automatically create a virtual environment and manage python packages. The python packages required by Open-SIR are listed in the [Pipfile](Pipfile).

### Dependencies
* Python 3.7
* Pipenv
* NumPy
* SciPy
* Jupyter
* Matplotlib

### Installing (for developers now)

After cloning the repository, change the current directory to the repository by `cd open-sir` and automatically install the environment from the Pipfile using Pipenv:

```
pipenv install
```

Next, activate the Pipenv shell:
```
pipenv shell
```
## Usage example

In the Pipenv shell, check that the installation was successful calling the CLI open-sir.py

```
python open-sir.py -p '[0.95,0.38]' -i '[341555,445,0]' -t 6 
```

Alternatively, instead of activating the shell, you can run the same command through Pipenv outside the open-sir Pipenv environment:

```
pipenv run python open-sir.py -p '[0.95,0.38]' -i '[341555,445,0]' -t 6 
```

The output of open-sir.py is a table with a 6 day prediction of the number of susceptible (S), infected (I) and removed (R) population. The initial conditions -i represent Ealing data as of 04/04/2020. The parameters provide a prediction in the hypothetical case that no lockdown is taking place.

The last line of the output should be
```
6.000000000000000000e+00,3.213056091837603017e+05,1.233370563811089232e+04,8.360685178128811458e+03
```

Open and run the Jupyter Notebook [SIR-X.ipynb](SIR-X.ipynb) to:
* Get an overview of the SIR model
* Explore case studies

And learn how to use the API to:

* Build compartmental models
* Fit parameters to existing data 
* Predict susceptible, infected and removed population
* Calculate confidence intervals of the predictions


## Running the tests

Test the correct implementation of the SIR model using

```
pipenv run test
```

### Coding style

Coding analysis is automatically reviewed using [Pylint](https://www.pylint.org/) and [Black 19.10b0](https://black.readthedocs.io/en/stable/) with the non-default parameters available in [.pylintrc](pylintrc)

## Authors

* **José Álamos** - [RIOT](https://github.com/RIOT-OS)
* **Felipe Huerta** - [PhD Student](https://www.imperial.ac.uk/people/f.huerta-perez17) at [Imperial College London](https://github.com/ImperialCollegeLondon)
* **Sebastián Salata** - Software Engineer - Full Stack

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgements

* [Robert Koch Institut](https://www.rki.de/EN/Home/homepage_node.html) for the clear explanation of SIR and SIR-X models.
