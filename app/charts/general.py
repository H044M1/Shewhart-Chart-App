import abc
from typing import Sequence

from ..types import ChartConfig, AttributeDataType, ChartCusumConfig, CornerParameters

class AttributeAbstract(abc.ABC):
    def __init__(self, config: ChartConfig, data: AttributeDataType):
        self.config = config
        self.data = data
    
    @abc.abstractmethod
    def get_lcl_ucl(self) -> tuple[list[float], list[float]]:
        pass
    
    @abc.abstractmethod
    def get_average(self) -> float:
        pass
    
    @abc.abstractmethod
    def get_sigma(self, item: int) -> float:
        pass
    
    @abc.abstractmethod
    def get_cl(self) -> float:
        pass
    
    @abc.abstractmethod
    def values_for_plot(self) -> Sequence[float]:
        pass

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