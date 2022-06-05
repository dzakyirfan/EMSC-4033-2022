

# Velocity Structure of Jakarta Basin

## Executive summary

Dataset Preparation and 3D visualizations of shear-wave velocity (Vs) model from Jakarta Basin. Velocity properties of a basin are influenced by depth, geometries, and lithology of the basin. This makes the shear-waves velocities of a basin can be highly heterogeneous. The visualizations help analysing shear-wave velocity of a basin to reveal the properties pattern and distribution easier. After the 3D model was created, we can extract 2D cross-sections in multiple orientation for more apparent image of subsurface shear velocity. Furthermore, depth of constant velocity can be extracted and mapped as a proxy of basin depth or certain geological parameters. Hopefully, the workflow and functions that I have built could be applied for any velocity data in other regions, especially for geological and geophysical purposes

## Goals

- Create a function to import hundreds of raw txt file into a single, structured numpy array that is ready for data analysis
- Create functions to prepare a visualization-friendly dataset
- Create functions that enable cross-section of 3D shear-velocity model in multiple orientations: north-south, east-west, and diagonal
- Create a function to build constant-velocity depth dataset

## Background and Innovation  

A sedimentary basin consists of different geological characteristics from rocks around the basin. The difference leads to the contrasting properties and may have an implication in natural hazards, where sedimentary basin could amplify and extend the propagating seismic waves. What makes it more challenging is that there are variation of properties inside the basin. This 8033 project is the precursor of my research project, to visualize the shear-wave velocity properties of a basin in which the different values have different response toward the propagating earthquake. This project can be done using Python, specifically with pacakges such as Numpy, Pandas, Matplotlib, and Plotly. While Numpy and Matplotlib are relatively basic module for number analysis, storing, and visualizations, those modules can be utilized and crafted to subset dataset in a desired line out of 3D volume. On the other hand, Plotly offer delicate visualization with more features than Matplotlib.

## Resources & Timeline

I could be able to start this project thanks to:
- The shear-wave velocity data from Rexha Verdhona Ry as part of his research project that I will continue later on
- The suggestion and approval of Phil Cummins as my research supervisor

To build this project, I will do the following steps:
  - I will be using os, glob, and Numpy to build a function for exporting and arranging hundreds of raw data into one structured Numpy array that is ready for visualization
  - I will use the scatterplot feature of Matplotlib to build a data visualization function of subsurface velocity with respect to the coordinates and depth.
  - I will also use Plotly to visualize interactive basin model
  - The 3D model that I have visualized is then used for making the 2D cross-sections using Matplotlib. I will make functions to create dataset in desired cross-sectional area from north-south, east-west, and diagonal line by indexing, subsetting, and/or filtering Pandas DataFrame
  - The dataset of sliced lines can be an input for 2D visualization using Matplotlib triagulation contour, using matplotlib.axes.tricontourf()
  - The imported files can be further interpolated to obtain constant-velocity depth data in a built function

### Timeline
All these activities were taken in local host before being pushed and uploaded to this repository

2 May 2022 - 8 May 2022:
- Build repository for this project
- Start writing the project plan

9 May 2022 - 15 May 2022:
- Create first draft of project notebook
- Determine the dependencies
- Create raw code for importing files
- Updating the project plan

16 May 2022 - 22 May 2022:
- Create raw code for data visualizations
- Test some Python visualization package (trial and error)

23 May 2022 - 30 May 2022:
- Create raw code for slicing dataset and slice visualizations
- Create raw code to produce isovelocity array and map
- Build functions for all raw codes
- Build testing functions
- Finalize the project notebook
- Write project report

31 May 2022 - 5 June 2022:
- Upload and push files to this repository
- Create `LICENSE.md`
- Update `README.md`

## Testing, validation, documentation

### Testing and Validation
Project functions are tested and validated depends on their function type:
- Functions for data importing, such as **import_file()** and **isovelocity()** are tested using the smaller-size basin files, in which some of the files has been partially removed and some remains for the testing
- Functions for other functions (can be viewed in `ProjectReport.md`) are tested using test dataset that was built independently inside the testing function for direct input to the function itself. 

Testing methods for importing file and other purposes are designed to display the scalability of functions, as well as show the ability of the same functions to handle small-scale dataset. Testing purposes are listed as below:
- Testing for data import will be created to assert the correct type of input and number of data columns in terms of parameters
- Testing for visualization to assert that functions can produce the figure
- Testing for cross-section or data slice to assert the correct data type using DataFrame, and correct number of columns
- Testing for isovelocity data import with exact number of array columns
More information about testing functions can be seen in `test_functions.py` under `src` folder. The testing execution should be undertaken in `RunTests.ipynb` under `notebook` folder.

### Documentation, Code Review
While this section will talk about the general review and documentation for the project functions, detailed information about each of the project functions can be seen in [`project_functions.py`](https://github.com/dzakyirfan/EMSC-4033-2022/blob/b819f8c0d8fac44c97b8d468992f3c2b0d4736dd/src/project_functions.py).

Generally, all functions can run successfully under several circumstances. First, the imported file should follow certain format. The individual file format has structure like [here](https://github.com/dzakyirfan/EMSC-4033-2022/blob/b37f364cc58185ea1b594e7c034fdf3bd91d1606/notebook/sample_input_file.png)

The top most column contains single longitude and latitude value, while depth and velocity data can be found in subsequent columns. This individual file should be imported using **np.genfromtxt()** and arranged with **np.stack()** so that each depth has information regarding latitude, longitude, and velocity in the same column. The arranged output will be 2D numpy array of row and column, with rows representing data for each point, and columns representing data parameters. It does not stop there, but the arranged array for each locations should be merged using **np.concatenate** and make use of empty array to form unified dataset in the same array.

The unified dataset can be readily plotted in `Matplotlib.pyplot` using **matplotlib.pyplot.scatterplot()**. However, the matplotlib package can only produce static image of 3D volume. Therefore, additional visualization package named `Plotly` will be imported to visualize more interactive interface of basin volume. In order to plot using `Plotly`, the dataset should be re-arranged to follow the grid structure. It can be done using `Pandas`, through several useful functions such as **pandas.DataFrame.drop_duplicates()**, **pandas.DataFrame.sort_values()**, and **pandas.DataFrame.replace()** to create new dataset that expand to rectangular form, hence becoming `Plotly` -friendly.

While `Plotly` offer clearer basin display not only on the outside but within the volume itself, data slicing functions were created so the 2D cross-sections in a constant latitude (east-west), a constant longitude (north-south), and diagonal cross sections can be displayed. First, special dataset for slice data were arranged using `Pandas`, particularly through subsetting of a big basin dataframe. Second, the special slice dataset are visualized in the form of contour map, using **matplotlib.tricontourf()**. 

Besides volume and slicing data, other map of constant-velocity map are created as a proxy to boundary between geological/geophysical unit. The imported file have random velocity value due to the measurement, so the desired velocity that we want to map can be interpolated using **np.interp()** to estimate the depth of that velocity in each point. The certain-velocity depth, along with its coordinates will then be merged to create a single dataset in the form of `numpy` array. Next, the array can be an input for map visualization using **matplotlib.tri.Triangulation()** to produce interpolation in required 2D array for **matplotlib.contourf** plotting function.
