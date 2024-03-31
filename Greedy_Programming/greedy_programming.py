class Voraz:


    def __init__(self, finca):
        self.finca = finca
        self.n = len(finca)

    def tiempoRegadoTablones(self,ts):
        """
        Calculates the total time required to water each plank in a given permutation.
        Args:
            ts (list): A list of tuples representing the time required to water each plank.
        Returns:
            list: A list of integers representing the cumulative time required to water each plank in the given permutation.
        """
        tp = list(range(len(ts))) # lista de tiempo de regado
        for t in range(len(ts)): # tablon de la permutacion
            if t == 0 or len(tp)==1:
                tp[t] = 0

        else:
            tr=ts[t-1][1] # tiempo de regado del tablon
            tp[t]=tp[t-1] + tr
        return tp


    def costo(self,ts, ti,tr, pi):
        """
        Calculate the cost based on the given parameters.

        Parameters:
        ts (int): Survival time.
        ti (int): Start Time.
        tr (int): Watering time.
        pi (int): The penalty factor.

        Returns:
        int: The calculated cost.

        """
        if (ts- tr) >= ti:
            return ts-(ti+tr)
        else:
            return pi*((ti+tr)-ts)



    def costoFinca(self,p):
        """
        Calculates the total cost of maintaining a farm.

        Args:
            p (list): A list of tuples representing the properties of each plot in the farm. Each tuple contains the following elements:
                - Element 0: Survival time.
                - Element 1: The time required to water the plot.
                - Element 2: The cost of watering the plot.

        Returns:
            float: The total cost of maintaining the farm.

        """
        c = 0
        ti = self.tiempoRegadoTablones(p)
        for t in range(len(p)):
            c += self.costo(p[t][0],ti[t],p[t][1],p[t][2])
        return c


    def heuristica(tablon):
        """
        Calculates the heuristic value for a given tablon.

        The heuristic value is calculated as the difference between the survival time of the tablon and the time for watering the tablon, divided by the priority of the tablon.

        Parameters:
        tablon (list): A list containing the survival time, the time for watering the tablon, and the priority of the tablon.

        Returns:
        float: The calculated heuristic value.

        """
        return round((tablon[0]-tablon[1])/tablon[2],2)

    def roV(self,finca):
        n = self.n
        memo = [(1000,[])]*n
        if n == 1:
            return self.costoFinca(finca)
        else:
            for i in range(n):
                memo[i] = self.heuristica(finca[i]),[finca[i]]

            memo.sort(key=lambda x: x[0])
        return memo,self.costoFinca(finca)