from kernel.models.pricing_engines.abstract_pricing_engine import AbstractPricingEngine
from kernel.market_data.market import Market
from utils.pricing_settings import PricingSettings
from utils.pricing_results import PricingResults
from kernel.products.taux.abstract_produits_taux import AbstractRateProduct
from kernel.models.stochastic_processes import StochasticProcess


class RatePricingEngine(AbstractPricingEngine):
    """
    Moteur de pricing pour les produits de taux.

    Ce moteur exploite la logique de valorisation propre aux instruments de taux en
    appelant la méthode 'price_product' sur le produit. Cela permet d'uniformiser l'interface
    de valorisation par rapport à celle utilisée pour les options.
    
    Les paramètres de valorisation (notamment la date de valuation) sont définis
    dans l'objet PricingSettings.
    """

    def __init__(self, market: Market, settings: PricingSettings):
        super().__init__(market)
        self.settings = settings
        self.valuation_date = settings.valuation_date

    def get_results(self, derivative: AbstractRateProduct) -> PricingResults:
        """
        Calcule le prix du produit de taux et retourne les résultats encapsulés dans un objet PricingResults.

        Parameters:
            rate_product (AbstractRateProduct): Le produit de taux à valoriser.

        Returns:
            PricingResults: Objet contenant, entre autres, le prix du produit.
        """
        # On met à jour le produit avec la date de valorisation issue des settings.
        # La méthode price_product doit recalculer le prix (et d'autres propriétés si besoin)
        # à partir de la nouvelle valuation_date.
        priced_product = derivative.price_product()
        
        return priced_product
    
    def _get_price(self, derivative: AbstractRateProduct, process : StochasticProcess) -> float:
        return derivative.price
