import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

# Add page options for the overall app.
ui.page_opts(title="PyShiny App with Histogram", fillable=True)

# Add page options for the overall app.
with ui.sidebar():
    ui.input_slider("selected_number_of_bins", "Number of Bins", 0, 100, 20)


@render.plot(alt="A histogram")
def histogram():
    count_of_points: int = 437
    np.random.seed(19680801)
    num_points = input.selected_number_of_bins()
    random_data_array = 100 + 15 * np.random.randn(count_of_points)
    plt.title("Histogram Plot with {} Points".format(num_points))
    plt.hist(random_data_array, input.selected_number_of_bins(), density=True)

@render.plot("scatterplot", alt="A scatter plot")
def scatterplot():
    np.random.seed(42)  # Ensure reproducibility
    num_points = input.selected_number_of_bins()  
    x = np.random.rand(num_points)
    y = np.random.rand(num_points)
    plt.scatter(x, y)
    plt.title("Random Scatter Plot with {} Points".format(num_points))
    plt.xlabel("X axis")
    plt.ylabel("Y axis")




