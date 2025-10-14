import matplotlib.pyplot as plt

from graphics import Graphics, SimulationConfig

plt.ion()  # Enable interactive mode for real-time updates

config = SimulationConfig()  # Initialize simulation configuration

# Initialize muscle and neuron states
muscle1, muscle2 = config.initial_muscle1, config.initial_muscle2
sensory_neuron = excitatory_neuron = inhibitory_neuron = 0.0

graphics = Graphics(config)  # Initialize graphics with the given configuration

with graphics:
    for t in range(config.num_steps):
        # Determine if an event occurs at the current time step
        event = -1 + config.num_steps // 4 <= t <= 2 + config.num_steps // 4
        if t == config.num_steps // 4:
            muscle1 += 0.08  # Apply stimulus to muscle1

        # Update neuron and muscle states based on differential equations
        sensory_neuron += config.time_step * (
            -sensory_neuron + max(0.0, muscle1 - config.initial_muscle1)
        )
        excitatory_neuron += config.time_step * (
            -excitatory_neuron + sensory_neuron
        )
        inhibitory_neuron += config.time_step * (
            -inhibitory_neuron + sensory_neuron
        )
        muscle1 += config.time_step * (
            -muscle1 + config.initial_muscle1 - 0.8 * excitatory_neuron
        )
        muscle2 += config.time_step * (
            -muscle2 + (1 - muscle1) + 0.2 * inhibitory_neuron
        )

        # Store simulation data for analysis
        config.simulation_data[t, :] = [
            sensory_neuron,
            excitatory_neuron,
            inhibitory_neuron,
            muscle1,
            muscle2,
        ]
        print(t, end=" ")  # Print current time step
        # Update graphics for the current state
        graphics.step(
            muscle1,
            muscle2,
            sensory_neuron,
            excitatory_neuron,
            inhibitory_neuron,
            event,
        )
        print(" ----")
        plt.pause(0.01)  # Pause to allow for real-time visualization updates
