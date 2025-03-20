from .abstract_interpolator import Interpolator
import numpy as np
from scipy.optimize import curve_fit

class NelsonSiegelInterpolator(Interpolator):
    """
    Implements the Nelson-Siegel yield curve model for yield curve fitting and interpolation.

    This model provides a parsimonious representation of the yield curve using four parameters.
    It is widely used in fixed income markets to fit and interpolate interest rates across different maturities.
    """

    def __init__(self, maturities: np.ndarray[float], rates: np.ndarray[float]):
        """
        Initializes the interpolator with observed market rates and calibrates the Nelson-Siegel model.

        Parameters:
            maturities (np.ndarray[float]): A list or array of maturities (in years).
            rates (np.ndarray[float]): A list or array of observed yield rates corresponding to the maturities.
        """
        super().__init__(maturities, rates)

        self.params = self._calibrate()

    @staticmethod
    def _nelson_siegel(t, beta0: float, beta1: float, beta2: float, tau: float ) -> float:
        """
        Computes the yield at a given maturity using the Nelson-Siegel model formula.

        Parameters:
            t (float): Maturity in years.
            beta0, beta1, beta2, tau (floats): Model parameters 

        Returns:
            float: Yield rate for the given maturity.
        """
        return beta0 + beta1 * (1 - np.exp(-t / tau)) / (t / tau) + beta2 * (
            (1 - np.exp(-t / tau)) / (t / tau) - np.exp(-t / tau))

    def _calibrate(self) -> np.ndarray[float]:
        """
        Calibrates the Nelson-Siegel parameters by fitting the model to observed yield data.

        Returns:
            np.ndarray[float]: Estimated parameters [beta0, beta1, beta2, tau].
        """
        p0 = [0.02, -0.02, 0.02, 1.0]  # Initial parameter guess
        params, _ = curve_fit(self._nelson_siegel, self.maturities, self.rates, p0=p0,
                              bounds=([0, -np.inf, -np.inf, 0.01], [np.inf, np.inf, np.inf, np.inf]))
        return np.array(params)

    def interpolate(self, t: float) -> float:
        """
        Interpolates the yield for a given maturity using the calibrated Nelson-Siegel model.

        Parameters:
            t (float): Maturity at which to estimate the yield.

        Returns:
            float: Estimated yield rate for the given maturity.
        """
        return self._nelson_siegel(t, *self.params)
