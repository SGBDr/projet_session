# -*- coding: utf-8 -*-
"""
Bourse implamentaion : phase 2
"""

import datetime

from exceptions import ErreurDate
from tools import request_historique_in_json_format, get_date_from_string

class Bourse:
    """
    Bourse implementation
    """

    def prix(self, symbole, date):
        """
        Return the close price of action with symbole according to the date and configuration
        """
        # Get current date
        date_aujourdhui = datetime.date.today()

        if date > date_aujourdhui:
            raise ErreurDate("La date spécifiée est postérieure à la date du jour.")

        # Get historique list
        historique = request_historique_in_json_format(symbole=symbole)
        

        # Search the first close value before the specify date
        for string_date in historique.keys():
            temp_date = get_date_from_string(string_date)
            if temp_date <= date:
                return historique[string_date]['fermeture']

        # If not date had been found, return the must recent close value
        if historique:
            return historique[historique.keys()[0]]['fermeture']

        # If historique is empty
        return 0.0
    