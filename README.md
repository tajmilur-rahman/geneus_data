# GeneUS_data_repo

## Introduction
This repository contains the data for the experiments we did for the paper: "Take Loads Off Your Developers : Automated
User Story Generation Using Large Language Model", which will be published in the proceedings of the 2024 40th ICSME conference.

## Data
The data is organized in the following way:
$ `requirement_doc` folder contains all the requirement documents used in the experiments and their corresponding output
in json.
- `input_and_ground_truth` folder contains the input for each LLM interaction in the experiment and the corresponding
  human provided ground truth. This data in extracted in a Python file that can be imported directly in a Python code
  in case you want to replicated the experiment with our online tool demo.
