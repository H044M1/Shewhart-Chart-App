from typing import Sequence

from ..general import AttributeAbstract

class AttributeNP(AttributeAbstract):
    def get_sigma_lcl_ucl(self) -> tuple[list[float], list[float]]:
        avg = self.get_average()
        lcl = [avg + self.config.limits_constant[0]*self.get_sigma(i) for i in range(len(self.data.table))]
        ucl = [avg + self.config.limits_constant[1]*self.get_sigma(i)  for i in range(len(self.data.table))]
        return (lcl, ucl)
    
    def get_grand_average(self) -> float:
        return sum([n[self.config.selected_parameter]/n['size'] for n in self.data.table])*sum([n['size'] for n in self.data.table])/(len(self.data.table))**2
    
    def get_sample_average(self) -> float:
        return sum([n[self.config.selected_parameter] for n in self.data.table])/len(self.data.table)
    
    def get_calculate_sigma(self, item: int) -> float:
        item_object = self.data.table[item]
        return (self.get_average()*abs(1 - self.get_average()/item_object['size']))**0.5
        
    def get_cl(self) -> float:
        return self.get_average()
    
    def values_for_plot(self) -> Sequence[float]:
        avg = self.get_average()
        return [item[self.config.selected_parameter] for item in self.data.table]