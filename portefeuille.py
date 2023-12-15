# -*- coding: utf-8 -*-
"""
Portefeuille implamentaion : phase 2
"""

import json
import datetime
from exceptions import ErreurDate, LiquiditeInsuffisante, ErreurQuantite
from tools import format_date, get_date_from_format


class Portefeuille:
    """
        PorteFeuille Class, allow portefeuille gestion
    """

    def __init__(self, bourse, nom_portefeuille):
        """
        Initialization
        """
        self.bourse = bourse
        self.liquidite = 0
        self.deposits = []
        self.positions = []
        self.nom_portefeuille = nom_portefeuille

        # Load existing data from JSON file
        self.lire_json()

    def __del__(self):
        """
        Destructor: called when the instance is about to be destroyed
        """
        self.écrire_json()

    def lire_json(self):
        """
        Load the current state to a JSON file
        """
        try:
            with open(f"portefeuilles/{self.nom_portefeuille}.json", 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.liquidite = data.get('liquidite', 0)
                self.deposits = data.get('deposits', [])
                self.positions = data.get('positions', [])
        except FileNotFoundError:
            # File doesn't exist, use default values
            self.écrire_json()

    def écrire_json(self):
        """
        Save the current state to a JSON file
        """
        data = {
            'liquidite': self.liquidite,
            'deposits': self.deposits,
            'positions': self.positions
        }

        with open(f"portefeuilles/{self.nom_portefeuille}.json", 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2)

    def déposer(self, amount, date = datetime.date.today()):
        """
        Do some deposit
        """
        # verify the date
        if date > datetime.date.today():
            raise ErreurDate()

        # update the liquidite and the deposit
        self.liquidite += amount
        self.deposits.append({'date': format_date(str(date)), 'amount': amount})

    def solde(self, date = datetime.date.today()):
        """
        Get sold at some date
        """
        # verify condition for admisible date
        if date > datetime.date.today():
            raise ErreurDate()

        amount = 0
        for deposite in self.deposits:
            amount += deposite["amount"] if get_date_from_format(deposite["date"]) <= date else 0

        return amount

    def acheter(self, symbole, quantite, date_achat = datetime.date.today()):
        """
        Buy stocks
        """
        # Verify the date
        if date_achat > datetime.date.today():
            raise ErreurDate()

        # Get the stock price at the purchase date
        prix_achat = self.bourse.prix(symbole, date_achat)
        cout_total = quantite * prix_achat

        # Verify if the portfolio has enough liquidity for the purchase
        if cout_total > self.solde(date_achat):
            raise LiquiditeInsuffisante()
        self.liquidite -= cout_total

        # Add the purchase to the portfolio
        self.positions.append({
                'symbole': symbole, 
                'quantite': quantite, 
                'prix': prix_achat, 
                'date': format_date(str(date_achat))
            })
        self.deposits.append({'date': format_date(str(date_achat)), 'amount': -cout_total})

    def vendre(self, symbole, quantite, date_vente = datetime.date.today()):
        """
        Sell stocks
        """
        # Verify the date
        if date_vente > datetime.date.today():
            raise ErreurDate()

        # Verify if the portfolio has enough quantity of the specified stock
        # for the sale
        quantite_disponible = 0
        for position in self.positions:
            if position['symbole'] == symbole and get_date_from_format(position["date"]) <= date_vente:
                quantite_disponible += position['quantite']

        if quantite > quantite_disponible:
            raise ErreurQuantite()

        # Get the stock price at the sale date
        prix_vente = self.bourse.prix(symbole, date_vente)

        # Calculate the total revenue from the sale
        recette_totale = quantite * prix_vente

        # Add the revenue to the liquidity
        self.liquidite += recette_totale

        self.positions.append({
                'symbole': symbole, 
                'quantite': quantite, 
                'prix': prix_vente, 
                'date': format_date(str(date_vente))
            })
        self.deposits.append({'date': format_date(str(date_vente)), 'amount': recette_totale})

    def valeur_totale(self, date = datetime.date.today()):
        """
        Get the total value of the portfolio at a specific date
        """
        # Verify the condition for an admissible date
        if date > datetime.date.today():
            raise ErreurDate()
        total_value = 0
        for position in self.positions:
            prix_actuel = self.bourse.prix(position['symbole'], date)
            total_value += position['quantite'] * prix_actuel

        return total_value

    def valeur_des_titres(self, symboles, date = datetime.date.today()):
        """
        Get the total value of specified stocks at a specific date
        """
        # Verify the condition for an admissible date
        if date > datetime.date.today():
            raise ErreurDate()
        prix_actuel = 0
        for symbole in symboles:
            prix_actuel += self.bourse.prix(symbole, date)
        return prix_actuel

    def titres(self, date = datetime.date.today()):
        """
        Get the dictionary of symbols and quantities of all stocks 
        in the portfolio at a specific date
        """
        # Verify the condition for an admissible date
        if date > datetime.date.today():
            raise ErreurDate()

        titres_dict = {}

        for position in self.positions:
            symbole = position['symbole']
            quantite = position['quantite']
            

            if symbole in titres_dict:
                titres_dict[symbole] += quantite
            else:
                titres_dict[symbole] = quantite

        # Remove symbols with quantities of 0 or less
        temp_titre = []
        for symbole, quantite in titres_dict.items():
            if quantite > 0:
                temp_titre.append({"symbole" : symbole, "quantite" : quantite})

        return titres_dict

    def valeur_projetee(self, date, rendement):
        """
        Get the projected value of the portfolio at a future date with specified annual returns
        """
        # Verify the condition for an admissible date
        if date < datetime.date.today():
            raise ErreurDate()

        # Initialize the projected value with the current total value of the portfolio
        projected_value = self.valeur_totale()

        # Calculate the projected value based on the specified annual returns
        for position in self.titres(date = datetime.date.today()):
            symbole = position['symbole']
            quantite = position['quantite']

            if isinstance(rendement, float):
                # If a single annual return is specified, apply it to all positions
                rendement_symbole = rendement
            elif symbole in rendement:
                # If individual annual returns are specified, use the one for the current position
                rendement_symbole = rendement[symbole]
            else:
                # If no specific annual return is provided for the current position, assume it's 0%
                rendement_symbole = 0.0

            # Get the stock price at the projection date
            prix = self.bourse.prix(symbole, datetime.date.today())

            year_n = int((date - datetime.date.today()).days / 365)
            day_m = (date - datetime.date.today()).days % 365

            # Calculate the projected value for the position
            projected_value += (quantite * prix * (1 + rendement_symbole / 100) ** year_n)
            projected_value += day_m * quantite * prix * rendement_symbole / 36500

        return projected_value
