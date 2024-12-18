from typing import Sequence
import math 
from ...types import ChartCusumConfig, AttributeDataType, CornerParameters
from ..general import AttributeCusumAbstract

class AttributeCusumC(AttributeCusumAbstract):
    def __init__(self, config: ChartCusumConfig, data: AttributeDataType):
        self.config = config
        self.data = data
    
    def get_average(self) -> float:
        match self.config.average_calculating:
            case 'custom':
                return self.config.average_constant
            case 'sample':
                return sum([n[self.config.selected_parameter] for n in self.data.table])/len(self.data.table)
        
    def get_sigma(self) -> float:
        match self.config.sigma_calculating:
            case 'custom':
                print(self.config)
                return self.config.sigma_constant
            case 'calculate':
                average = self.get_average()
                sigmas = [average**0.5 for i in range(len(self.data.table))]
                return sum(sigmas[i]*self.data.table[i]['size'] for i in range(len(sigmas)))/sum([item['size'] for item in self.data.table])
    
    def values_for_plot(self) -> Sequence[float]:
        avg = self.get_average()
        return [sum([(self.data.table[j][self.config.selected_parameter] - avg) for j in range(i+1)]) for i in range(len(self.data.table))]
    
    def get_corner_parameters(self) -> CornerParameters:
        summary_sigma = self.get_sigma()
        
        delta = self.config.delta*summary_sigma
        d = 2*(math.log(1 - self.config.betta) - math.log(self.config.alpha if self.config.alpha else 1e-10))/self.config.delta
        return {
            'delta': delta,
            'd': d,
            'tetta': math.atan(self.config.delta/1.5),
            'h': d*delta/2,
            'f': delta/2
        }