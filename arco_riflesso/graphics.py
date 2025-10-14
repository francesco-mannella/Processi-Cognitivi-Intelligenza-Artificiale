import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import PathPatch
from matplotlib.path import Path
from matplotlib.transforms import Affine2D

from mkvideo import vidManager


class SimulationConfig:
    """Configuration for the simulation.

    Attributes:
        num_steps (int): Number of steps in the simulation.
        time_step (float): Time interval between each step.
        simulation_data (np.ndarray): Array to store simulation data.
        initial_muscle1 (float): Initial state of muscle 1.
        initial_muscle2 (float): Initial state of muscle 2.
    """

    def __init__(self, num_steps=70, time_step=0.2, muscle1=0.52):
        self.num_steps = num_steps
        self.time_step = time_step
        self.simulation_data = np.zeros([num_steps, 5])
        self.initial_muscle1 = muscle1
        self.initial_muscle2 = 1 - muscle1


class Graphics:
    """Handles the graphical representation of the simulation.

    Attributes:
        config (SimulationConfig): Configuration for the simulation.
        t (int): Current time step in the simulation.
        fig (matplotlib.figure.Figure): Figure for plotting.
        axis (matplotlib.axes.Axes): Axis for the main plot.
        neuron_axis (matplotlib.axes.Axes): Axis for neuron activity plot.
        bar_axis (matplotlib.axes.Axes): Axis for bar plot.
        neuron_lines (list): Lines representing neuron activities.
    """

    def __init__(self, config):
        self.config = config
        self.t = 0
        self.init_graphics()

    def __enter__(self):
        self.vm = vidManager(fig=self.fig, name="arch", duration=500)
        print("enter")
        return self

    def __exit__(self, type, value, tb):
        self.vm.close()

    def make_bezier(
        self,
        verts,
        codes,
        color,
        lw=4,
        fill=False,
        scatter=None,
        annotate=None,
    ):
        """Create a bezier curve with optional scatter and annotations.

        Args:
            verts (list): Vertices of the bezier curve.
            codes (list): Path codes for the bezier curve.
            color (str): Color of the bezier curve.
            lw (int, optional): Line width of the curve. Defaults to 4.
            fill (bool, optional): Whether to fill the curve. Defaults to False.
            scatter (dict, optional): Scatter plot parameters. Defaults to None.
            annotate (list, optional): Annotation parameters. Defaults to None.

        Returns:
            PathPatch: The created bezier curve patch.
        """
        patch = PathPatch(
            Path(verts, codes), edgecolor=color, lw=lw, fill=fill
        )
        if scatter:
            self.axis.scatter(
                *scatter["xy"], c=[color], s=scatter.get("s", 30)
            )
        if annotate:
            for ann in annotate:
                self.axis.annotate(
                    "",
                    xy=ann["xy"],
                    xytext=ann["xytext"],
                    arrowprops=dict(
                        arrowstyle="->", color=color, lw=ann.get("lw", 4)
                    ),
                )
        return patch

    def make_inhibitor_bezier(self, color):
        """Create a bezier curve for the inhibitor neuron.

        Args:
            color (str): Color of the bezier curve.

        Returns:
            PathPatch: The created bezier curve patch.
        """
        verts = [
            (0.0, 0.48),
            (0.1, 0.40),
            (0.15, 0.40),
            (0.25, 0.40),
            (0.3, 0.48),
        ]
        codes = [Path.MOVETO] + [Path.CURVE3] * 4
        color = np.array(plt.cm.gray(color)) * [0, 0, 1, 1]
        return self.make_bezier(
            verts, codes, color, scatter={"xy": (0.3, 0.48)}
        )

    def make_flexor_bezier(self, color):
        """Create a bezier curve for the flexor neuron.

        Args:
            color (str): Color of the bezier curve.

        Returns:
            PathPatch: The created bezier curve patch.
        """
        verts = [
            (-0.1, 0.8),
            (0.2, 0.8),
            (0.25, 0.8),
            (0.3, 0.8),
            (0.4, 0.75),
            (0.4, 0.6),
            (0.4, 0.58),
        ]
        codes = [Path.MOVETO, Path.LINETO] + [Path.CURVE3] * 4 + [Path.LINETO]
        color = plt.cm.hot(color)
        ann = [{"xy": (-0.1, 0.8), "xytext": (0.2, 0.8)}]
        return self.make_bezier(verts, codes, color, annotate=ann)

    def make_extensor_bezier(self, color):
        """Create a bezier curve for the extensor neuron.

        Args:
            color (str): Color of the bezier curve.

        Returns:
            PathPatch: The created bezier curve patch.
        """
        verts = [
            (0.0, 0.6),
            (0.1, 0.68),
            (0.15, 0.68),
            (0.25, 0.68),
            (0.3, 0.6),
        ]
        codes = [Path.MOVETO] + [Path.CURVE3] * 4
        color = plt.cm.hot(color)
        ann = [{"xy": (0.34, 0.56), "xytext": (0.28, 0.62)}]
        return self.make_bezier(verts, codes, color, annotate=ann)

    def make_bezier_patch(self, color):
        """Create a bezier patch for the graphical representation.

        Args:
            color (str): Color of the bezier patch.

        Returns:
            PathPatch: The created bezier patch.
        """
        verts = [
            (-0.1, 0.8),
            (-0.1, 0.7),
            (-0.1, 0.54),
            (0.0, 0.60),
            (-0.1, 0.54),
            (0.0, 0.48),
        ]
        codes = [
            Path.MOVETO,
            Path.CURVE3,
            Path.CURVE3,
            Path.LINETO,
            Path.MOVETO,
            Path.LINETO,
        ]
        color = plt.cm.hot(color)
        ann = [
            {"xy": (0.0, 0.60), "xytext": (-0.1, 0.54), "lw": 2},
            {"xy": (0.0, 0.48), "xytext": (-0.1, 0.54), "lw": 2},
        ]
        return self.make_bezier(verts, codes, color, annotate=ann)

    def draw(self, m1, m2, f, e, inh, event=False):
        """Draw the current state of the simulation.

        Args:
            m1 (float): State of muscle 1.
            m2 (float): State of muscle 2.
            f (float): Flexor neuron activity.
            e (float): Extensor neuron activity.
            inh (float): Inhibitor neuron activity.
            event (bool, optional): Whether an event occurred. Defaults to False.
        """
        neurons = self.neuron_lines
        self.axis.clear()
        upper_len = np.mean(
            [self.config.initial_muscle1, self.config.initial_muscle2]
        )
        upper_bone = plt.Rectangle((0.1, 0.53), upper_len, 0.02, color="black")
        kneecap = plt.Circle(
            (self.config.initial_muscle1 + 0.07, 0.54), 0.03, color="black"
        )
        hammer = plt.Rectangle(
            (0.6, 0.6 - 0.04 * event), 0.05, 0.1, color="black"
        )
        joint = (0.07 + self.config.initial_muscle1, 0.54)
        angle = -np.pi * 0.25 - 8 * (m1 - m2)
        transform = Affine2D().rotate_around(joint[0], joint[1], angle)
        lower_len = upper_len * 0.7
        lower_bone = plt.Rectangle(
            (0.1 + self.config.initial_muscle1, 0.53),
            lower_len,
            0.02,
            color="black",
        )
        lower_bone.set_transform(transform + self.axis.transData)
        muscle1_patch = plt.Rectangle((0.1, 0.55), m1, 0.03, color="red")
        muscle2_patch = plt.Rectangle((0.1, 0.5), m2, 0.03, color="red")
        n_flexor = plt.Circle((-0.1, 0.8), 0.03, color=plt.cm.hot(20 * f))
        n_extensor = plt.Circle((0.0, 0.6), 0.03, color=plt.cm.hot(20 * e))
        n_inhibitor = plt.Circle(
            (0.0, 0.48),
            0.03,
            color=np.array(plt.cm.gray(140.0 * inh)) * [0, 0, 1, 1],
        )
        patches = [
            upper_bone,
            lower_bone,
            kneecap,
            hammer,
            muscle1_patch,
            muscle2_patch,
            self.make_bezier_patch(20 * f),
            self.make_inhibitor_bezier(140 * inh),
            self.make_extensor_bezier(20 * e),
            self.make_flexor_bezier(10 * (m1 - self.config.initial_muscle1)),
            n_flexor,
            n_extensor,
            n_inhibitor,
        ]
        for patch in patches:
            self.axis.add_patch(patch)

        self.axis.text(0.6, 0.9, f"time: {self.t: 4d}")

        self.axis.set_xticks([])
        self.axis.set_yticks([])
        self.axis.set_xlim(-0.4, 1)
        self.axis.set_ylim(0.0, 1)
        for neuron_data, neuron_line in zip(
            self.config.simulation_data[:, :3].T, neurons
        ):
            neuron_line.set_data(np.arange(self.t), neuron_data[: self.t])

        self.bar_axis.clear()
        self.bar_axis.set_ylim(-0.01, 0.05)
        self.bar_axis.bar(
            ["sensory\nneuron", "excitatory\nneuron", "inhibitory\nneuron"],
            [f, e, inh],
            color=["#ff5555", "#ff5555", "#5555ff"],
        )

    def step(self, m1, m2, f, e, inh, event=False):
        """Advance the simulation by one step.

        Args:
            m1 (float): State of muscle 1.
            m2 (float): State of muscle 2.
            f (float): Flexor neuron activity.
            e (float): Extensor neuron activity.
            inh (float): Inhibitor neuron activity.
            event (bool, optional): Whether an event occurred. Defaults to False.
        """
        self.draw(m1, m2, f, e, inh, event)
        if hasattr(self, "vm"):
            self.vm.save_frame()
        if self.t < self.config.num_steps:
            self.t += 1

    def init_graphics(self):
        """Initialize the graphical components."""
        self.fig, (self.axis, self.neuron_axis, self.bar_axis) = plt.subplots(
            1, 3, figsize=(10, 3)
        )
        self.axis.set_aspect("equal")
        self.neuron_lines = self.neuron_axis.plot(
            np.zeros([3, self.config.num_steps]).T
        )
        for lw, n in zip([1, 6, 2], self.neuron_lines):
            n.set_linewidth(lw)
        self.neuron_axis.legend(
            handles=self.neuron_lines,
            labels=[
                "sensory\nneuron",
                "excitatory\nneuron",
                "inhibitory\nneuron",
            ],
        )
        self.neuron_axis.set_ylim(-0.01, 0.05)
        self.neuron_axis.set_xlabel("Time")
        self.neuron_axis.set_xlim(0, self.config.num_steps)

        self.draw(
            self.config.initial_muscle1,
            self.config.initial_muscle2,
            0.0,
            0.0,
            0.0,
        )
        self.fig.tight_layout()
