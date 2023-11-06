# -*- coding: utf-8 -*-
"""
Phase 1 du projet de session
"""

import argparse
import datetime
from tools import request_information_in_json_format, format_date


def main():
    """
    Starting poin of our program, main fonction
    """
    args = analyser_commande()
    produire_historique(args.symbole, args.date_debut, args.date_fin, args.valeur)


def analyser_commande():
    """
    Analyse the command line, config all args and return this appropriation value tu the caller
    """
    parser = argparse.ArgumentParser(
        description="Extraction de valeurs historiques pour un ou plusieurs symboles boursiers.")
    # Positional arguments
    parser.add_argument("symbole", nargs="+", help="Nom d'un symbole boursier")
    # Optional arguments

    parser.add_argument("-d", "--début", dest="date_debut", type=str, default=None,
                        help="Date recherchée la plus ancienne (format: AAAA-MM-JJ)")
    parser.add_argument("-f", "--fin", dest="date_fin", type=str,
                        default=str(datetime.date.today()),
                        help="Date recherchée la plus récente (format: AAAA-MM-JJ)")
    parser.add_argument("-v", "--valeur", dest="valeur",
                        choices=["fermeture", "ouverture", "min", "max", "volume"],
                        default="fermeture", help="La valeur désirée (par défaut: fermeture)")
    args = parser.parse_args()
    # Default value of date_debut
    args.date_debut = args.date_debut if args.date_debut is not None else args.date_fin

    return args


def produire_historique(symboles, date_debut, date_fin, valeur):
    """
    Get information from th server(by using tools function) and parse it
    to the require format
    """
    # For each symbole
    for symbole in symboles:
        # creation of the request
        url = f'https://pax.ulaval.ca/action/{symbole}/historique/'
        params = {'début': date_debut, 'fin': date_fin}

        # getting data in json format
        data = request_information_in_json_format(url=url, params=params)

        # process on data
        final_data = []
        for date in data["historique"].keys():
            final_data.append((format_date(date), data["historique"][date][valeur]))
        # displaying informations
        print(
            f"titre={symbole}: valeur={valeur}, début={format_date(date_debut)}" +
            f", fin={format_date(date_fin)}"
        )
        print(final_data)


if __name__ == "__main__":
    main()
