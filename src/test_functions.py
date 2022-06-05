
import pytest
import numpy
import pandas

from project_functions import *

def test_project_documentation(expected_type=str):
    """Test the type of documentation for this project. Expect string as the documentation type"""
    
    doc_type = type(project_documentation())
    
    assert doc_type == expected_type, "***The documentation type is not string"
    
def test_import_file(expected_type = numpy.ndarray, expected_columns = 4):
    """Test the output type of import_file function, with four columns of the output file"""
    
    import os
    import glob
    
    #Test folder directory
    os.chdir(r"/Users/dzakyirfan/Documents/Test dataset")

    #Iterates through all dat file in the test directory
    files_test = [i for i in glob.glob("*.dat")]
    
    array_from_import = import_file(files_test)
    
    assert type(array_from_import) == expected_type, "***The function returns different data type"
    assert array_from_import.shape[1] == expected_columns, "***The function returns unexpected number of columns of array"


def test_parameter_list(expected_type=tuple, expected_total_lists=3):
    """Test the output type of parameter_list function, with total of three lists"""
    
    #Create simple artifical dataset for testing
    import numpy as np

    x = np.linspace(0, 10, 20)
    y = np.linspace(0, 10, 20)
    z = np.linspace(0, 10, 20)
    xi, yi, zi = np.meshgrid(x, y, z)
    val = np.random.rand(20, 20, 20)

    test_array = np.stack((xi.flatten(), 
                           yi.flatten(), 
                           zi.flatten(), 
                           val.flatten()), 
                          axis=1)
    
    test_unique_val = parameter_list(test_array)
    
    assert type(test_unique_val) == expected_type, "***The function returns different data type"
    assert len(test_unique_val) == expected_total_lists, "***The function returns different number of output"
    
def test_basin_scatterplot():
    """Assert whether the function could successfully produce a figure"""
    
    #Create simple artifical dataset for testing
    import numpy as np
    import matplotlib.pyplot as plt

    x = np.linspace(0, 10, 20)
    y = np.linspace(0, 10, 20)
    z = np.linspace(0, 10, 20)
    xi, yi, zi = np.meshgrid(x, y, z)
    val = np.random.rand(20, 20, 20)

    test_array = np.stack((xi.flatten(), 
                           yi.flatten(), 
                           zi.flatten(), 
                           val.flatten()), 
                          axis=1)
    
    #Insert the artificial data to the tested function
    plt.close()
    mpl_basin = basin_scatterplot(test_array)
    assert plt.gcf().number == 1, "***The function cannot display the 3D plot"
    
def test_plotly_friendly_dataframe(expected_type=pandas.core.frame.DataFrame, expected_columns=4):
    """Test the output type of import_file function, with expected four columns of the output dataframe"""
    
    #Create simple artifical dataset for testing
    import numpy as np

    x = np.linspace(0, 10, 50)
    y = np.linspace(0, 10, 50)
    z = np.linspace(0, 10, 50)
    xi, yi, zi = np.meshgrid(x, y, z)
    val = np.random.rand(50, 50, 50)

    test_array = np.stack((xi.flatten(), 
                           yi.flatten(), 
                           zi.flatten(), 
                           val.flatten()), 
                          axis=1)
    
    test_dataframe = plotly_friendly_dataframe(test_array)
    
    assert type(test_dataframe) == expected_type, "***The function is not producing DataFrame"
    assert test_dataframe.shape[1] == expected_columns, "***The function is unable to return four columns"
    
def test_northeast_southwest_slice(expected_type=pandas.core.frame.DataFrame, expected_columns=4):
    """Test the output type of import_file function, with expected four columns of the output dataframe and assert if the depth range of output dataframe is the same as the depth range of input dataframe"""
    
    #Create simple artifical dataset for testing
    import numpy as np

    x = np.linspace(0, 20, 40)
    y = np.linspace(0, 20, 30)
    z = np.linspace(0, 20, 20)
    xi, yi, zi = np.meshgrid(x, y, z)
    val = np.random.rand(40, 30, 20)

    test_array = np.stack((xi.flatten(), 
                           yi.flatten(), 
                           zi.flatten(), 
                           val.flatten()), 
                          axis=1)
    
    #Create DataFrame through plotly_friendly_dataframe()
    test_dataframe = plotly_friendly_dataframe(test_array)
    test_nesw_database = northeast_southwest_slice(test_array, test_dataframe)
    
    assert type(test_nesw_database) == expected_type, "***The function is not producing DataFrame"
    assert test_nesw_database.shape[1] == expected_columns, "***The function is unable to return four columns"
    assert test_dataframe['Depth'].any() == test_nesw_database['Depth'].any(), "***The function could not produce cross-sectional dataframe that reach all depth"
    
def test_northwest_southeast_slice(expected_type=pandas.core.frame.DataFrame, expected_columns=4):
    """Test the output type of import_file function, with expected four columns of the output dataframe and assert if the depth range of output dataframe is the same as the depth range of input dataframe"""
    
    #Create simple artifical dataset for testing
    import numpy as np

    x = np.linspace(0, 10, 20)
    y = np.linspace(0, 10, 10)
    z = np.linspace(0, 10, 15)
    xi, yi, zi = np.meshgrid(x, y, z)
    val = np.random.rand(20, 10, 15)

    test_array = np.stack((xi.flatten(), 
                           yi.flatten(), 
                           zi.flatten(), 
                           val.flatten()), 
                          axis=1)
    
    #Create DataFrame through plotly_friendly_dataframe()
    test_dataframe = plotly_friendly_dataframe(test_array)
    test_nwse_database = northwest_southeast_slice(test_array, test_dataframe)
    
    assert type(test_nwse_database) == expected_type, "***The function is not producing DataFrame"
    assert test_nwse_database.shape[1] == expected_columns, "***The function is unable to return four columns"
    assert test_dataframe['Depth'].any() == test_nwse_database['Depth'].any(), "***The function could not produce cross-sectional dataframe that reach all depth"
    
def test_east_west_slice(expected_type=pandas.core.frame.DataFrame, expected_columns=4):
    """Test the output type of import_file function, with expected four columns of the output dataframe, assert if the depth range of output dataframe is the same as the depth range of input dataframe, and assert that the latitude value is the same in the output dataframe"""
    
    #Create simple artifical dataset for testing
    import numpy as np
    import pandas as pd

    x = np.linspace(0, 10, 20)
    y = np.linspace(0, 10, 10)
    z = np.linspace(0, 10, 15)
    xi, yi, zi = np.meshgrid(x, y, z)
    val = np.random.rand(20, 10, 15)

    test_array = np.stack((xi.flatten(), 
                           yi.flatten(), 
                           zi.flatten(), 
                           val.flatten()), 
                          axis=1)
    
    #Create DataFrame through plotly_friendly_dataframe()
    test_dataframe = plotly_friendly_dataframe(test_array)
    test_ew_database = east_west_slice(test_dataframe, np.unique(x)[5])
    
    assert type(test_ew_database) == expected_type, "***The function is not producing DataFrame"
    assert test_ew_database.shape[1] == expected_columns, "***The function is unable to return four columns"
    assert len(pd.unique(test_dataframe['Depth'])) == len(pd.unique(test_ew_database['Depth'])), "***The function returns slice dataframe that reach all depth"
    assert len(test_ew_database['Latitude'].unique()) == 1, "***The returned DataFrame has no constant latitude value"

def test_north_south_slice(expected_type=pandas.core.frame.DataFrame, expected_columns=4):
    """Test the output type of import_file function, with expected four columns of the output dataframe, assert if the depth range of output dataframe is the same as the depth range of input dataframe, and assert that the longitude value is the same in the output dataframe"""
    
    #Create simple artifical dataset for testing
    import numpy as np
    import pandas as pd

    x = np.linspace(0, 10, 20)
    y = np.linspace(0, 10, 10)
    z = np.linspace(0, 10, 15)
    xi, yi, zi = np.meshgrid(x, y, z)
    val = np.random.rand(20, 10, 15)

    test_array = np.stack((xi.flatten(), 
                           yi.flatten(), 
                           zi.flatten(), 
                           val.flatten()), 
                          axis=1)
    
    #Create DataFrame through plotly_friendly_dataframe()
    test_dataframe = plotly_friendly_dataframe(test_array)
    test_ns_database = north_south_slice(test_dataframe, np.unique(y)[5])
    
    assert type(test_ns_database) == expected_type, "***The function is not producing DataFrame"
    assert test_ns_database.shape[1] == expected_columns, "***The function is unable to return four columns"
    assert len(pd.unique(test_dataframe['Depth'])) == len(pd.unique(test_ns_database['Depth'])), "***The function returns slice dataframe that reach all depth"
    assert len(test_ns_database['Longitude'].unique()) == 1, "***The returned DataFrame has no constant latitude value"

def test_slice_scatterplot():
    """Assert whether the function could successfully produce a figure"""
    
    #Create simple artifical dataset for testing
    import numpy as np
    import matplotlib.pyplot as plt

    x = np.linspace(0, 15, 30)
    y = np.linspace(0, 15, 30)
    z = np.linspace(0, 15, 30)
    xi, yi, zi = np.meshgrid(x, y, z)
    val = np.random.rand(30, 30, 30)

    test_array = np.stack((xi.flatten(), 
                           yi.flatten(), 
                           zi.flatten(), 
                           val.flatten()), 
                          axis=1)
    
    #Create slice dataframe first
    test_dataframe = plotly_friendly_dataframe(test_array)
    test_nesw_slice = northeast_southwest_slice(test_array, test_dataframe)
    
    #Test the visualization function
    plt.close()
    mpl_sliceplot = slice_scatterplot(test_nesw_slice)
    assert plt.gcf().number == 1, "***the function cannot display the scatterplot"
    
def test_northeast_southwest_contourplot():
    """Assert whether the function could successfully produce a figure"""
    
    #Create simple artifical dataset for testing
    import numpy as np
    import matplotlib.pyplot as plt

    x = np.linspace(0, 20, 10)
    y = np.linspace(0, 10, 10)
    z = np.linspace(0, 5, 10)
    xi, yi, zi = np.meshgrid(x, y, z)
    val = np.random.rand(10, 10, 10)

    test_array = np.stack((xi.flatten(), 
                           yi.flatten(), 
                           zi.flatten(), 
                           val.flatten()), 
                          axis=1)
    
    #Create slice dataframe first
    test_dataframe = plotly_friendly_dataframe(test_array)
    test_nesw_slice = northeast_southwest_slice(test_array, test_dataframe)
    
    #Test the visualization function
    plt.close()
    nesw_sliceplot = northeast_southwest_contourplot(test_nesw_slice)
    assert plt.gcf().number == 1, "***the function cannot display the scatterplot"
    
def test_northwest_southeast_contourplot():
    """Assert whether the function could successfully produce a figure"""
    
    #Create simple artifical dataset for testing
    import numpy as np
    import matplotlib.pyplot as plt

    x = np.linspace(0, 20, 10)
    y = np.linspace(0, 10, 10)
    z = np.linspace(0, 5, 10)
    xi, yi, zi = np.meshgrid(x, y, z)
    val = np.random.rand(10, 10, 10)

    test_array = np.stack((xi.flatten(), 
                           yi.flatten(), 
                           zi.flatten(), 
                           val.flatten()), 
                          axis=1)
    
    #Create slice dataframe first
    test_dataframe = plotly_friendly_dataframe(test_array)
    test_nwse_slice = northwest_southeast_slice(test_array, test_dataframe)
    
    #Test the visualization function
    plt.close()
    nwse_sliceplot = northwest_southeast_contourplot(test_nwse_slice)
    assert plt.gcf().number == 1, "***the function cannot display the scatterplot"
    
def test_latitudinal_longitudinal_contourplot():
    """Assert whether the function could successfully produce a figure"""
    
    #Create simple artifical dataset for testing
    import numpy as np
    import matplotlib.pyplot as plt

    x = np.linspace(0, 20, 20)
    y = np.linspace(0, 10, 20)
    z = np.linspace(0, 5, 20)
    xi, yi, zi = np.meshgrid(x, y, z)
    val = np.random.rand(20, 20, 20)

    test_array = np.stack((xi.flatten(), 
                           yi.flatten(), 
                           zi.flatten(), 
                           val.flatten()), 
                          axis=1)
    
    #Create slice dataframe first
    test_dataframe = plotly_friendly_dataframe(test_array)
    test_slice = east_west_slice(test_dataframe, np.unique(x)[5])
    
    #Test the visualization function
    plt.close()
    test_contourplot = latitudinal_longitudinal_contourplot(test_slice, 'Longitude')
    assert plt.gcf().number == 1, "***the function cannot display the scatterplot"
    
def test_isovelocity(expected_type = numpy.ndarray, expected_columns=3):
    """Test the output type of import_file function, with four columns of the output file"""
    
    import os
    import glob
    
    #Test folder directory
    os.chdir(r"/Users/dzakyirfan/Documents/Test dataset")

    #Iterates through all dat file in the test directory
    files_test = [i for i in glob.glob("*.dat")]
    
    isovel_array = isovelocity(files_test, 1.0)
    
    assert type(isovel_array) == expected_type, "***The function returns different data type"
    assert isovel_array.shape[1] == expected_columns, "***The function returns unexpected number of columns of array"
    
def test_isovelocity_map():
    """Assert whether the function could successfully produce a figure"""
    
    import os
    import glob
    import matplotlib.pyplot as plt
    
    #Test folder directory
    os.chdir(r"/Users/dzakyirfan/Documents/Test dataset")

    #Iterates through all dat file in the test directory
    files_test = [i for i in glob.glob("*.dat")]
    
    isovel_array = isovelocity(files_test, 1.0)
    
    #test visualization
    plt.close()
    isovel_map = isovelocity_map(isovel_array, 1.0)
    assert plt.gcf().number == 1, "***the function cannot display the map"
    
    
    

    
    
    
    
    
    
    
        
    
    