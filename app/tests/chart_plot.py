import matplotlib.pyplot as plt
from ..charts.attribute.p import AttributeP
from ..types import AttributeDataType, ChartConfig

def create_plot():
    config = ChartConfig(
        limits_type = "sigma",
        sigma_display = {
            "sigma1": False,
            "sigma2": False
        },
        average_calculating = 'sample',
        sigma_calculating = 'calculate',
        selected_parameter = 'defect'
    )
    
    data = AttributeDataType(
        parameters_quantity = 1,
        subgroups_quantity = 6,
        subgroups_size = 100,
        parameters = ['defect'],
        additional_parameters = [],
        table = [
            {'subgroup': 1, 'size': 100, 'defect': 21},
            {'subgroup': 2, 'size': 10, 'defect': 5},
            {'subgroup': 3, 'size': 100, 'defect': 16},
            {'subgroup': 4, 'size': 100, 'defect': 12},
            {'subgroup': 5, 'size': 100, 'defect': 15},
            {'subgroup': 6, 'size': 100, 'defect': 5}
        ]
    )
    
    chart = AttributeP(config, data)
    
    print({
        'type': 'p',
        'mean': chart.get_average(),
        'lcl': chart.get_lcl_ucl()[0],
        'cl': chart.get_cl(),
        'ucl': chart.get_lcl_ucl()[1],
        'sigmas': chart.get_all_sigmas(),
        'values': chart.values_for_plot()
    })