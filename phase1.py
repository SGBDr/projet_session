import argparse
import datetime

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



if __name__ == "__main__":
    main()