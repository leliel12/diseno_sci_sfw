import attr

import numpy as np

import matplotlib.pyplot as plt


@attr.s(repr=False)
class ParticlePlotter:
    particle = attr.ib()
    
    def __repr__(self):
        return f"ParticlePlotter(particle={hex(id(self.particle))})"
    
    def __call__(self, kind="scatter_hist", **kwargs):
        method = getattr(self, kind)
        return method(**kwargs)
    
    def scatter_hexbin(self, ax=None, hexbin_kws=None, scatter_kws=None):
        
        p = self.particle
        
        ax = plt.gca() if ax is None else ax

        hexbin_kws = {} if hexbin_kws is None else hexbin_kws
        scatter_kws = {} if scatter_kws is None else scatter_kws

        hexbin_kws.setdefault("cmap", "Greys")

        ax.hexbin(p.x, p.y, **hexbin_kws)
        ax.scatter(p.x, p.y, **scatter_kws)

        return ax
    
    def scatter_hist(self, ax=None, hist_kws=None, scatter_kws=None):
        p = self.particle
        ax = plt.gca() if ax is None else ax
        hist_kws = {} if hist_kws is None else hist_kws
        scatter_kws = {} if scatter_kws is None else scatter_kws
        hist_kws.setdefault("cmap", "Greys")
        ax.hist2d(p.x, p.y, **hist_kws)
        ax.scatter(p.x, p.y, **scatter_kws)
        ax.set_title("Scatter Hist")
        
        return ax
    
@attr.s
class ParticleOOPAcc:
    x = attr.ib(converter=np.asarray)
    y = attr.ib(converter=np.asarray)
    z = attr.ib(converter=np.asarray)
    m = attr.ib(converter=np.asarray)
    
    @property
    def plot(self):
        return ParticlePlotter(self)
    
# TESTING
    
from matplotlib.testing.decorators import check_figures_equal

@check_figures_equal()
def test_ParticleOOP_scatterhist(fig_test, fig_ref):
    p = ParticleOOPAcc(
        x = np.random.normal(size=100), 
        y = np.random.normal(size=100),
        z = np.random.normal(size=100),
        m = np.random.uniform(size=100)
    )
    
    # test
    test_ax = fig_test.subplots()
    p.plot.scatter_hist(ax=test_ax)
    
    #expected
    exp_ax = fig_ref.subplots()
  
    exp_ax.hist2d(p.x, p.y, cmap="viridis")
    exp_ax.scatter(p.x, p.y)    
    
    exp_ax.set_title("Scatter Hist")
