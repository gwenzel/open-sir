# open-sir

Open-SIR is an Open Source Python project for modeling pandemics and infectious diseases using Compartmental Models, such as the widely used [Susceptible-Infected-Removed (SIR) model](http://rocs.hu-berlin.de/corona/docs/forecast/model/#classic-sir-dynamics). 

The current stage of the software is *Alpha*.

## Features
- Model the behavior of infectious diseases
- Parameter fitting
- Calculation of confidence intervals
- CLI for interfacing with non Python environments (Bash, Node.JS, Matlab, etc).

So far, Open-SIR provides an implementation of the SIR model and the recently new SIR based model SIR-X, developed by the [Robert Koch Institut](http://rocs.hu-berlin.de/corona/docs/forecast/model/#sir-x-dynamics-outbreaks-with-temporally-increasing-interventions).

## Getting Started

Open-SIR uses [Pipenv](https://pipenv.pypa.io/en/latest/) to automatically create a virtual environment and manage python packages. The python packages required by Open-SIR are listed in the [Pipfile](Pipfile).

### Prerequisites

Python 3.7 and Pipenv are required. 

```
Pipenv
Python 3.7
```

And the python packages
```
numpy
matplotlib
scipy
jupyter
sklearn
```

### Installing

After cloning the repository, change the current directory to the repository by `cd open-sir` and automatically install the environment from the Pipfile using Pipenv:

```
pipenv install
```

Next, activate the Pypenv shell:
```
pipenv shell
```

Check that the installation was succesful using:

```

```

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Jose Alamos** - [RIOT](https://github.com/RIOT-OS)
* **Felipe Huerta** - [PhD Student](https://www.imperial.ac.uk/people/f.huerta-perez17) at [Imperial College London](https://github.com/ImperialCollegeLondon)
* **Sebastián Salata** - Software Engineer - Full Stack

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
