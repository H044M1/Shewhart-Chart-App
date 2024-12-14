from ..types import ChartConfig, ChartCusumConfig, AttributeDataType

def parse_config(config: dict) -> ChartConfig|ChartCusumConfig:
    if config['chart'] in ('cusum_p', 'cusum_c'):
        return ChartCusumConfig(
            sigma_display = config['sigmaDisplay'],
            average_calculating = config['mean'].lower(),
            sigma_calculating = config['sigma'].lower(),
            selected_parameter = config['characteristic'],
            average_constant = config['meanCustom'],
            sigma_constant = config['sigmaCustom'],
            alpha = config['alpha'],
            betta = config['betta'],
            delta = config['delta']
        )
    else:
        return ChartConfig(
            limits_type = config['limits'].lower(),
            sigma_display = config['sigmaDisplay'],
            average_calculating = config['mean'].lower(),
            sigma_calculating = config['sigma'].lower(),
            selected_parameter = config['characteristic'],
            ma_span = config['ma_span'],
            limits_constant = config["limitsValue"],
            average_constant = config['meanCustom'],
            sigma_constant = config['sigmaCustom'],
        )
        
def parse_data(data: dict) -> AttributeDataType:
    return AttributeDataType(
        parameters_quantity = data['parameters_quantity'],
        subgroups_quantity = data['subgroups_quantity'],
        subgroups_size = data['subgroups_size'],
        parameters = data['parameters'],
        additional_parameters = data['additional_parameters'],
        table = data['table'],
    ) 