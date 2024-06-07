import matplotlib.pyplot as plt

from colors import ColorGenerator, ColorCycles


class Figure():
    
    def __init__(self, rows=1, columns=1, figsize=(5, 5), dpi=100):
        self.colorpalette = ColorGenerator()
        self.m = rows
        self.n = columns
        self.figsize = figsize
        self.fig = plt.figure(figsize=self.figsize)
        self.axes = self.fig.add_subplot(1,1,1)
        self.default_palette = ColorCycles.cycles["matlab"]
        
        self.axcount = [0] # [[ax0_n_plots], [ax1_n_plots], [ax2_plot0, ax2_plot1]]
        
    def plot(self, x, y):
        self.axes.plot(x, y)
        plt.show()
        
    def scatter(self, x, y, palette : str = 'default', color : str = 'default'):
        colors = self.colorpalette.harmony(seed = self.default_palette[self.axcount[0]], mode="monochromatic", monochrome="full", n=8)
        for i in range(len(x)):
            self.axes.scatter(x[i], y[i], color=colors[i], s=400)
        plt.draw()
        self.axcount[0] += 1
    
    def semilogx(self):
        pass
    
    def semilogy(self):
        pass
    
if __name__ == "__main__":
    f = Figure()
    f.scatter([1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8])
    f.scatter([3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8])
    f.scatter([5, 6, 7, 8, 9, 10, 11, 12], [1, 2, 3, 4, 5, 6, 7, 8])
    f.scatter([7, 8, 9, 10, 11, 12, 13, 14], [1, 2, 3, 4, 5, 6, 7, 8])
    f.scatter([9, 10, 11, 12, 13, 14, 15, 16], [1, 2, 3, 4, 5, 6, 7, 8])
    plt.show()