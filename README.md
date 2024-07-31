# ModellingCollectiveAntBehavior
# Ant Behavior Simulation: From ODE to Agent-Based Model

## Introduction

The goal of the project was to convert an Ordinary Differential Equation (ODE) model into an Agent-Based Model (ABM) to study the collective behavior of ants, specifically their decision-making and resource allocation during foraging.

## Project Overview

### Original ODE Model

The original ODE model describes the dynamics of ants choosing between two feeders based on:
- **Discovery Rates (α):** The rate at which uncommitted ants find feeders independently.
- **Recruitment Rates (β):** The rate at which committed ants recruit uncommitted ants to a feeder.
- **Attrition Rates (λ):** The rate at which committed ants abandon a feeder and return to being uncommitted.

The ODEs are given by:
dXA/dt = α(N − XA − XB) + βAXA(N − XA − XB) − λAXA
dXB/dt = α(N − XA − XB) + βBXB(N − XA − XB) − λBXB
where `XA` and `XB` are the numbers of ants committed to feeders A and B, respectively, and `N` is the total number of ants.

### Agent-Based Model (ABM)

In the ABM, each ant is modeled as an individual agent operating within a grid environment. This approach captures more nuanced interactions between ants and their environment. The main features include:
- **Movement:** Ants move randomly within the grid.
- **State Transitions:** Ants transition between uncommitted, committed to feeder A, and committed to feeder B states based on probabilistic rules derived from the ODE parameters.
- **Recruitment:** Committed ants can recruit uncommitted ants to their feeder through tandem running.

## Implementation

The model was implemented in Python using the following libraries:
- **NumPy:** For numerical computations.
- **Matplotlib:** For visualizing the simulation results.

### Files and Directories
- `main.py`: The main script to run the simulation.
- `ant.py`: Contains the `Ant` class defining the behavior and state transitions of ants.
- `environment.py`: Defines the grid environment and contains functions for initializing and updating the state of the simulation.
- `requirements.txt`: Lists the required Python libraries.
- `README.md`: This documentation file.

### Running the Simulation

1. **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```
2. **Run the main script:**
    ```bash
    python main.py
    ```

### Visualization

The simulation results can be visualized using Matplotlib. The ants' movements and state transitions are plotted over time, showing how the colony's foraging behavior evolves.

## Impact and Further Research

This project laid the foundation for my ongoing research on the spread of infectious diseases using agent-based models. By simulating interactions, movements, and disease transmission among agents, I aim to provide insights into effective intervention strategies and public health policies. This work has significant potential to enhance our understanding and control of disease outbreaks, ultimately contributing to better healthcare outcomes.

## Future Work

- **Integrate additional environmental factors:** Include more complex environmental variables to make the model more realistic.
- **Expand to other species:** Adapt the model to study the behavior of other social insects or animals.
- **Apply to epidemiology:** Extend the model to simulate disease spread in human populations.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or suggestions.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For any questions or inquiries, please contact amachira@asu.edu


