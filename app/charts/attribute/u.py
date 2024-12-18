from typing import Sequence

from ..general import AttributeAbstract

class AttributeU(AttributeAbstract):
    def get_sigma_lcl_ucl(self) -> tuple[list[float], list[float]]:
        avg = self.get_average()
        lcl = [avg + self.config.limits_constant[0]*self.get_sigma(i) for i in range(len(self.data.table))]
        ucl = [avg + self.config.limits_constant[1]*self.get_sigma(i)  for i in range(len(self.data.table))]
        return (lcl, ucl)
    
    def get_grand_average(self) -> float:
        u = self.get_values()
        return sum([n['parameter']*n['size'] for n in u])/sum([n['size'] for n in u])
    
    def get_sample_average(self) -> float:
        u = self.get_values()
        return sum([n['parameter'] for n in u])/len(u)
    
    def get_values(self) -> Sequence[dict]:
        return [{
            'parameter': n[self.config.selected_parameter]/n['size'],
            'size': n['size']
        } for n in self.data.table]
    
    def get_calculate_sigma(self, item: int) -> float:
        return (self.get_average()/self.data.table[item]['size'])**0.5
        
    def get_cl(self) -> float:
        return self.get_average()
    
    def values_for_plot(self) -> Sequence[float]:
        return [item['parameter'] for item in self.get_values()]