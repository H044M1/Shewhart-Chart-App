from dataclasses import dataclass
from typing import TypedDict, Sequence, Literal

class AttributeTableElement(TypedDict):
    subgroup: int
    disabled: bool = False
    size: int
    
@dataclass 
class AttributeDataType:
    parameters_quantity: int
    subgroups_quantity: int
    subgroups_size: int
    parameters: Sequence[str]
    additionalParameters: Sequence[str]
    table: Sequence[AttributeTableElement]
    
class VariableTableElement(TypedDict):
    number: int
    subgroup: int
    disabled: bool
    
@dataclass 
class VariableDataType:
    parameters_quantity: int
    subgroups_quantity: int
    subgroups_size: int
    parameters: Sequence[str]
    additionalParameters: Sequence[str]
    table: Sequence[VariableTableElement]

class SigmaDisplay(TypedDict):
    sigma1: bool
    sigma2: bool

@dataclass 
class ChartConfig:
    limits_type: Literal['sigma', 'custom']
    sigma_display: SigmaDisplay
    average_calculating: Literal['sample', 'grand', 'custom']
    sigma_calculating: Literal['calculate', 'custom']
    selected_parameter: str
    limits_constant: tuple[float, float] = (-3, 3)
    average_constant: float = 0
    sigma_constant: float = 0

@dataclass 
class ChartCusumConfig:
    sigma_display: SigmaDisplay
    average_calculating: Literal['sample', 'grand', 'custom']
    sigma_calculating: Literal['calculate', 'custom']
    selected_parameter: str
    average_constant: float = 0
    sigma_constant: float = 0
    alpha: float = 0
    betta: float = 0
    delta: float = 1
    
class CornerParameters(TypedDict):
    delta: float
    d: float
    tetta: float
    h: float
    f: float