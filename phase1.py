import argparse
import datetime

def main():
    parser = argparse.ArgumentParser(description="Extraction de valeurs historiques pour un ou plusieurs symboles boursiers.")
    
    # Positional arguments
    parser.add_argument("symbole", nargs="+", help="Nom d'un symbole boursier")
    
    # Optional arguments
    parser.add_argument("-d", "--début", dest="date_debut", type=str, help="Date recherchée la plus ancienne (format: AAAA-MM-JJ)")
    parser.add_argument("-f", "--fin", dest="date_fin", type=str, default=str(datetime.date.today()), help="Date recherchée la plus récente (format: AAAA-MM-JJ)")
    parser.add_argument("-v", "--valeur", dest="valeur", choices=["fermeture", "ouverture", "min", "max", "volume"], default="fermeture", help="La valeur désirée (par défaut: fermeture)")

    args = parser.parse_args()

    # Programme logic with params
    symboles = args.symbole
    date_debut = args.date_debut if args.date_debut is not None else args.date_fin
    date_fin = args.date_fin
    valeur = args.valeur

    # debuging code
    print("Symboles boursiers :", symboles)
    print("Date de début :", date_debut)
    print("Date de fin :", date_fin)
    print("Valeur désirée :", valeur)

if __name__ == "__main__":
    main()
