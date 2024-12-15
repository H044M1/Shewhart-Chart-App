import abc
from typing import Sequence

from ..types import ChartConfig, AttributeDataType, ChartCusumConfig, CornerParameters

class AttributeAbstract(abc.ABC):
    def __init__(self, config: ChartConfig, data: AttributeDataType):
        self.config = config
        data.table = list(filter(lambda item: not item['disabled'], data.table))
        self.data = data
    
    def get_lcl_ucl(self) -> tuple[Sequence[float], Sequence[float]]:
        match self.config.limits_type:
            case "custom":
                lcl = [self.config.limits_constant[0] for i in range(len(self.data.table))]
                ucl = [self.config.limits_constant[1] for i in range(len(self.data.table))]
                return (lcl, ucl)
            case "sigma":
                return self.get_sigma_lcl_ucl()
    
    def get_average(self) -> float:
        match self.config.average_calculating:
            case 'custom':
                return self.config.average_constant
            case 'grand':
                return self.get_grand_average()
            case 'sample':
                return self.get_sample_average()
            
    def get_sigma(self, item: int) -> float:
        match self.config.sigma_calculating:
            case 'custom':
                return self.config.sigma_constant
            case 'calculate':
                return self.get_calculate_sigma(item)
            
    def get_all_sigmas(self) -> Sequence[float]:
        return [self.get_sigma(i) for i in range(len(self.data.table))]
    
    @abc.abstractmethod
    def get_sigma_lcl_ucl(self) -> tuple[Sequence[float], Sequence[float]]: pass
    
    @abc.abstractmethod
    def get_grand_average(self) -> float: pass
    
    @abc.abstractmethod
    def get_sample_average(self) -> float: pass
    
    @abc.abstractmethod
    def get_calculate_sigma(self, item: int) -> float: pass
    
    @abc.abstractmethod
    def get_cl(self) -> float: pass
    
    @abc.abstractmethod
    def values_for_plot(self) -> Sequence[float]: pass
    

class AttributeCusumAbstract(abc.ABC):
    def __init__(self, config: ChartCusumConfig, data: AttributeDataType):
        self.config = config
        self.data = data
    
    @abc.abstractmethod
    def get_average(self) -> float:
        pass
    
    @abc.abstractmethod
    def get_sigma(self) -> float:
        pass
    
    @abc.abstractmethod
    def values_for_plot(self) -> Sequence[float]:
        pass
    
    @abc.abstractmethod
    def get_corner_parameters(self) -> CornerParameters:
        pass