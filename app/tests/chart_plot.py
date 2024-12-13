import matplotlib.pyplot as plt
from ..charts.attribute.cusum_p import AttributeCusumP
from ..types import AttributeDataType, ChartCusumConfig

def create_plot():
    config = ChartCusumConfig(
        sigma_display = {
            "sigma1": False,
            "sigma2": False
        },
        average_calculating = 'sample',
        sigma_calculating = 'custom',
        sigma_constant = 0.03,
        selected_parameter = 'defect',
        alpha = 0.005,
        betta = 0,
        delta = 1
        )
    
    data = AttributeDataType(
        parameters_quantity = 1,
        subgroups_quantity = 6,
        subgroups_size = 100,
        parameters = ['defect'],
        additionalParameters = [],
        table = [
            {'subgroup': 1, 'size': 100, 'defect': 21},
            {'subgroup': 2, 'size': 100, 'defect': 5},
            {'subgroup': 3, 'size': 100, 'defect': 16},
            {'subgroup': 4, 'size': 100, 'defect': 12},
            {'subgroup': 5, 'size': 100, 'defect': 15},
            {'subgroup': 6, 'size': 100, 'defect': 5}
        ]
    )
    
    chart = AttributeCusumP(config, data)
    
    print(f'Corner:\n{chart.get_corner_parameters()}\n')
    print(f'Values:\n{chart.values_for_plot()}\n')
    print(f'Avg: {chart.get_average()}')
    print(f'Sigma: {chart.get_sigma()}')