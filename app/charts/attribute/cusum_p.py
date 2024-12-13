from typing import Sequence
import math 
from ...types import ChartCusumConfig, AttributeDataType, CornerParameters
from ..general import AttributeCusumAbstract

class AttributeCusumP(AttributeCusumAbstract):
    def __init__(self, config: ChartCusumConfig, data: AttributeDataType):
        self.config = config
        self.data = data
        self.config.delta = self.config.delta*self.get_sigma()
    
    def get_average(self) -> float:
        match self.config.average_calculating:
            case 'custom':
                return self.config.average_constant
            case 'grand':
                return sum([n[self.config.selected_parameter] for n in self.data.table])/len([n.size for n in self.data.table])
            case 'sample':
                return sum([n[self.config.selected_parameter]/n['size'] for n in self.data.table])/len(self.data.table)
        
    def get_sigma(self) -> float:
        match self.config.sigma_calculating:
            case 'custom':
                return self.config.sigma_constant
            case 'calculate':
                avg = self.get_average()
                return (sum([(n[self.config.selected_parameter]/n['size'])**2 for n in self.data.table])/len(self.data.table) - avg**2)**0.5
    
    def values_for_plot(self) -> Sequence[float]:
        avg = self.get_average()
        return [sum([(self.data.table[j][self.config.selected_parameter]/self.data.table[j]['size'] - avg) for j in range(i+1)]) for i in range(len(self.data.table))]
    
    def get_corner_parameters(self) -> CornerParameters:
        summary_sigma = self.get_sigma()

        delta = self.config.delta/summary_sigma
        d = 2*(math.log(1 - self.config.betta) - math.log(self.config.alpha if self.config.alpha else 1e-10))/delta
        return {
            'delta': delta,
            'd': d,
            'tetta': math.atan(delta/4),
            'h': d*self.config.delta/2,
            'f': self.config.delta/2
        }