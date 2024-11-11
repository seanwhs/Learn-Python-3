# Standard libraries
from typing import List
# Third party libraries
import matplotlib.pyplot as plt
import pandas as pd
# Custom libraries


class Plotter:
    _bar_colour = 'red'

    def __init__(self) -> None:
        self.label_text_size = 14
        self.fig_size = (3 * 6.4, 4.8)
        self.dpi = 350

    def bar_plot_matplotlib(
            self, x_data: List, y_data: List, x_label: str = None, y_label: str = None, title: str = None) -> plt.Figure:
        fig, ax = plt.subplots(layout="constrained", figsize=self.fig_size)
        ax.bar(x_data, y_data, color=self._bar_colour)
        ax.tick_params(axis='both', labelsize=self.label_text_size)
        if x_label is not None:
            ax.set_xlabel(x_label)
        if y_label is not None:
            ax.set_ylabel(y_label)
        if title is not None:
            ax.set_title(title)

        return fig

    def bar_plot_pandas(
            self, data_frame: pd.DataFrame, x_data: str, y_data: str, title: str = None) -> plt.Figure:
        plt.rcParams['figure.constrained_layout.use'] = True
        ax = data_frame.sort_values(y_data, ascending=False).plot.bar(
            x=x_data, y=y_data, rot=90, color=self._bar_colour, figsize=self.fig_size
        )
        ax.set_ylabel(y_data)
        if title is not None:
            ax.set_title(title)

        fig = ax.get_figure()

        return fig

    @staticmethod
    def store_picture(figure_to_store: plt.figure, path: str, dpi: int = 350) -> None:
        figure_to_store.savefig(path, dpi=dpi)

    @property
    def bar_colour(self):
        return self._bar_colour

    @bar_colour.setter
    def bar_colour(self, new_bar_colour: str):
        self._bar_colour = new_bar_colour

    @classmethod
    def get_bar_colour(cls):
        return cls._bar_colour
