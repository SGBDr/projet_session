import argparse
import datetime
import requests

def main():
   args = analyser_commande()


def analyser_commande():
    parser = argparse.ArgumentParser(description="Extraction de valeurs historiques pour un ou plusieurs symboles boursiers.")
    
    # Positional arguments
    parser.add_argument("symbole", nargs="+", help="Nom d'un symbole boursier")
    
    # Optional arguments
    parser.add_argument("-d", "--début", dest="date_debut", type=str, help="Date recherchée la plus ancienne (format: AAAA-MM-JJ)")
    parser.add_argument("-f", "--fin", dest="date_fin", type=str, default=str(datetime.date.today()), help="Date recherchée la plus récente (format: AAAA-MM-JJ)")
    parser.add_argument("-v", "--valeur", dest="valeur", choices=["fermeture", "ouverture", "min", "max", "volume"], default="fermeture", help="La valeur désirée (par défaut: fermeture)")

    args = parser.parse_args()

    # Default value of date_debut
    args.date_debut = args.date_debut if args.date_debut is not None else args.date_fin

    return parser.parse_args()

def format_date(date):
    date_block = date.split("-")
    return f"datetime.date({date_block[0]}, {date_block[1]}, {date_block[2]})"


def produire_historique(symbole, date_debut, date_fin, valeur_desiree):
    # first line
    print(f"titre={symbole}: valeur={valeur_desiree}, début={format_date(date_debut)}, fin={format_date(date_fin)}")
    


if __name__ == "__main__":
    main()