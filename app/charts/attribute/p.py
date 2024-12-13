from typing import Sequence

from ...types import ChartConfig, AttributeDataType
from ..general import AttributeAbstract

class AttributeP(AttributeAbstract):
    def __init__(self, config: ChartConfig, data: AttributeDataType):
        self.config = config
        self.data = data
    
    def get_lcl_ucl(self) -> tuple[list[float], list[float]]:
        match self.config.limits_type:
            case "custom":
                lcl = [self.config.limits_constant[0] for i in range(len(self.data.table))]
                ucl = [self.config.limits_constant[1] for i in range(len(self.data.table))]
                return (lcl, ucl)
            case "sigma":
                avg = self.get_average()
                lcl = [avg - self.config.limits_constant[0]*self.get_sigma(i) for i in range(len(self.data.table))]
                ucl = [avg + self.config.limits_constant[1]*self.get_sigma(i)  for i in range(len(self.data.table))]
                return (lcl, ucl)
        
    def get_average(self) -> float:
        match self.config.average_calculating:
            case 'custom':
                return self.config.average_constant
            case 'grand':
                return sum([n[self.config.selected_parameter] for n in self.data.table])/len([n.size for n in self.data.table])
            case 'sample':
                return sum([n[self.config.selected_parameter]/n['size'] for n in self.data.table])/len(self.data.table)
        
    def get_sigma(self, item: int) -> float:
        match self.config.sigma_calculating:
            case 'custom':
                return self.config.sigma_constant
            case 'calculate':
                return (self.get_average()*(1 - self.get_average())/self.data.table[item]['size'])**0.5
        
    def get_cl(self) -> float:
        return self.get_average()
    
    def values_for_plot(self) -> Sequence[float]:
        return [item[self.config.selected_parameter]/item['size'] for item in self.data.table]