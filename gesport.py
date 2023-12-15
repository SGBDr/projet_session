# -*- coding: utf-8 -*-
"""
Phase 3 du projet de session
"""

import argparse
import datetime
from phase1 import analyser_commande
from portefeuille import Portefeuille
from bourse import Bourse


def analyser_commande():
    """
    Analyse the command line, config all args and return this appropriation value tu the caller
    """
    parser = argparse.ArgumentParser(description="Gestionnaire de portefeuille d'actions")

    parser.add_argument('action', dest="action",
                        choices=['deposer', 'acheter', 'vendre', 'lister', 'projeter'],
                        help='Action à effectuer')
    parser.add_argument('-d',
                        '--date', dest="date",
                        default=str(datetime.date.today()),
                        help='Date effective (par défaut, date du jour)')
    parser.add_argument('-q',
                        '--quantité', dest="quantite",
                        type=int, default=1,
                        help='Quantité désirée (par défaut: 1)')
    parser.add_argument('-t',
                        '--titres', dest="titres",
                        nargs='+',
                        default=[],
                        help='Le ou les titres à considérer')
    parser.add_argument('-r',
                        '--rendement', dest="rendement",
                        type=float,
                        default=0,
                        help='Rendement annuel global (par défaut, 0)')
    parser.add_argument('-v',
                        '--volatilité', dest="volatilite",
                        type=float, default=0,
                        help='Indice de volatilité global sur le rendement annuel (par défaut, 0)')
    parser.add_argument('-g', '--graphique', dest="graphique",
                        type=bool, default=False,
                        help='Affichage graphique (par défaut, pas d\'affichage graphique)')
    parser.add_argument('-p', '--portefeuille',
                        default='folio', dest="portefeuille",
                        help='Nom de portefeuille (par défaut, utiliser folio)')

    args = parser.parse_args()
    return args


def main():
    """
        main
    """
    args = analyser_commande()

    # Initialize Bourse and Portefeuille instances
    portefeuille = Portefeuille(nom_portefeuille=args.portefeuille, bourse=Bourse())

    # Perform the specified action
    if args.action == 'deposer':
        # Implement the logic for deposer action
        portefeuille.déposer(amount=args.quantite, date=args.date)
        print(f'solde = {portefeuille.solde()}')
    elif args.action == 'acheter':
        # Implement the logic for acheter action
        for symbole in args.titres:
            portefeuille.acheter(symbole=symbole, date_achat=args.date, quantite=args.quantite)
        print(f'solde = {portefeuille.solde()}')
    elif args.action == 'vendre':
        # Implement the logic for vendre action
        for symbole in args.titres:
            portefeuille.vendre(symbole=symbole, date_vente=args.date, quantite=args.quantite)
        print(f'solde = {portefeuille.solde()}')
    elif args.action == 'lister':
        # Implement the logic for lister action
        all_titres = portefeuille.titres(date=args.date)
        titres = []
        for element in args.titres:
            if element in all_titres:
                titres.append(element)

        for symbole in titres:
            quantite = all_titres[symbole]
            prix_actuel = portefeuille.valeur_des_titres(symboles=[symbole], date=args.date)

            print(f'{symbole} = {quantite} x {prix_actuel} = {quantite * prix_actuel}')
    elif args.action == 'projeter':
        # Implement the logic for projeter action

        print(f'valeur projetée = {0}')
